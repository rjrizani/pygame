import pygame
import random
import math
import time  # For delaying before closing the game

pygame.init()

# Constants for the game window
WIDTH, HEIGHT = 400, 300  # Updated window size
WINDOW_SIZE = (WIDTH, HEIGHT)
WINDOW_TITLE = "Hungry Snake Game"

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the game window
window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption(WINDOW_TITLE)


# Snake class to manage the snake's movement and growth
class Snake:
    def __init__(self, speed):
        self.body = [(WIDTH // 2 - i * 20, HEIGHT // 2) for i in range(4)]  # Initial size is 4 segments
        self.direction = (1, 0)  # Start moving towards the right
        self.speed = speed

    def move(self):
        dx, dy = self.direction
        new_head = ((self.body[0][0] + dx * 20) % WIDTH, (self.body[0][1] + dy * 20) % HEIGHT)
        self.body.pop()  # Remove the tail segment
        self.body.insert(0, new_head)  # Insert the new head

    def grow(self):
        dx, dy = self.direction
        new_tail = ((self.body[-1][0] - dx * 20) % WIDTH, (self.body[-1][1] - dy * 20) % HEIGHT)
        self.body.append(new_tail)

    def change_direction(self, dx, dy):
        # Avoid reversing direction (e.g., from right to left) to prevent self-collision
        if (dx, dy) != (-self.direction[0], -self.direction[1]):
            self.direction = (dx, dy)

    def get_head(self):
        return self.body[0]

    def get_body(self):
        return self.body[1:]

    def set_speed(self, speed):
        self.speed = speed


# Food class to manage the position and respawn of food
class Food:
    def __init__(self):
        self.position = (random.randint(10, WIDTH - 10), random.randint(10, HEIGHT - 10))

    def respawn(self):
        self.position = (random.randint(10, WIDTH - 10), random.randint(10, HEIGHT - 10))

    def get_position(self):
        return self.position


# Function to calculate the distance between two points
def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


# Show intro screen
def show_intro_screen():
    font_large = pygame.font.Font(None, 50)
    font_small = pygame.font.Font(None, 30)

    game_name = font_large.render("Hungry Snake Game", True, BLACK)
    slow_button = font_small.render("SLOW", True, BLACK)
    normal_button = font_small.render("NORMAL", True, BLACK)
    fast_button = font_small.render("FAST", True, BLACK)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            # Check for button clicks to set snake's speed
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if 125 <= x <= 275 and 150 <= y <= 200:
                    return "slow"
                elif 125 <= x <= 275 and 200 <= y <= 250:
                    return "normal"
                elif 125 <= x <= 275 and 250 <= y <= 300:
                    return "fast"

        window.fill(WHITE)

        # Align the game name to the middle of the top half
        window.blit(game_name, (WIDTH // 2 - game_name.get_width() // 2, HEIGHT // 4 - game_name.get_height() // 2))

        # Align the buttons horizontally with small text
        window.blit(slow_button, (WIDTH // 2 - slow_button.get_width() // 2, HEIGHT // 2 - 10))
        window.blit(normal_button, (WIDTH // 2 - normal_button.get_width() // 2, HEIGHT // 2 + 40))
        window.blit(fast_button, (WIDTH // 2 - fast_button.get_width() // 2, HEIGHT // 2 + 90))

        pygame.display.update()

# Main game loop
def main():
    speed_level = show_intro_screen()

    if speed_level == "slow":
        snake_speed = 5
    elif speed_level == "normal":
        snake_speed = 10
    else:
        snake_speed = 15

    snake = Snake(snake_speed)
    food = Food()

    clock = pygame.time.Clock()

    score = 0  # Initialize the score to zero

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            # Handle user input to change the snake's direction
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction(0, -1)
                elif event.key == pygame.K_DOWN:
                    snake.change_direction(0, 1)
                elif event.key == pygame.K_LEFT:
                    snake.change_direction(-1, 0)
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction(1, 0)

        # Move the snake
        snake.move()

        # Check for collisions with food
        head = snake.get_head()
        if distance(head, food.get_position()) < 20:
            food.respawn()
            snake.grow()
            score += 1  # Increase the score by one when the snake eats the food

        # Check for self-collision
        if head in snake.get_body():
            # Draw "Game Over" on the screen for 2 seconds
            font = pygame.font.Font(None, 36)
            text = font.render("Game Over", True, BLACK)
            window.blit(text, (WIDTH // 2 - 70, HEIGHT // 2))
            pygame.display.update()
            time.sleep(2)  # Wait for 2 seconds
            pygame.quit()
            return

        # Clear the window with a white background
        window.fill(WHITE)

        # Draw the snake's body as black rectangles
        for segment in snake.body:
            pygame.draw.rect(window, BLACK, (segment[0], segment[1], 20, 20))

        # Draw the snake's head as a black rectangle
        pygame.draw.rect(window, BLACK, (head[0] + 10, head[1] + 10, 10, 10))

        # Draw the food as a black circle
        pygame.draw.circle(window, BLACK, (food.get_position()[0] + 10, food.get_position()[1] + 10), 10)

        # Draw the score on the top left side
        font = pygame.font.Font(None, 30)
        score_text = font.render(f"Score: {score}", True, BLACK)
        window.blit(score_text, (10, 10))

        # Update the display
        pygame.display.update()

        # Set the frame rate
        clock.tick(snake.speed)  # Adjust the game speed according to the snake's speed


if __name__ == "__main__":
    main()
