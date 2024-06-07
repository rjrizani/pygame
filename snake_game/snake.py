import pygame
import time
import random
import math

pygame.init()

WIDTH, HIGHT = 400,300
WINDOW_SIZE = (WIDTH, HIGHT)
WINDOW_TITLE = "Snake Game"

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#create the game window
window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption(WINDOW_TITLE)

#snake class to manage movement and growth
class Snake:
    def __init__(self,speed):
        self.body = [(WIDTH//2-i * 20, HIGHT//2) for i in range(4)]
        #[(200, 150), (180, 150), (160, 150), (140, 150)]
        self.direction = (1,0)  #start moving toward the right
        self.speed =speed

    def move(self):
        dx, dy = self.direction
        new_head = ((self.body[0][0] + dx * 20) % WIDTH, (self.body[0][1] + dy * 20) % HIGHT)
        self.body.pop()
        self.body.insert(0, new_head)

    def grow(self):
        dx, dy = self.direction
        new_tail = ((self.body[-1][0] - dx * 20) % WIDTH, (self.body[-1][1] - dy * 20) % HIGHT)
        self.body.append(new_tail)

    def change_direction(self,dx,dy):
        if (dx, dy) != (-self.direction[0], -self.direction[1]):
            self.direction = (dx, dy)
    def get_head(self):
        return self.body[0]

    def get_body(self):
        return self.body[1:]

    def set_speed(self, speed):
        self.speed = speed

class Food:
    def __init__(self):
        self.position = (random.randint(10, WIDTH-10), random.randint(10, HIGHT-10))

    def respawn(self):
        self.position = (random.randint(10, WIDTH-10), random.randint(10, HIGHT-10))

    def get_position(self):
        return self.position

def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

#show intro screen
def show_intro_screen():
    font_large = pygame.font.Font(None, 50)
    font_small = pygame.font.Font(None, 30)

    game_name = font_large.render("Snake Game", True, BLACK)
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
        window.blit(game_name, (WIDTH // 2 - game_name.get_width() // 2, HIGHT // 4 - game_name.get_height() // 2))

        window.blit(slow_button, (WIDTH // 2 - slow_button.get_width() // 2, HIGHT // 2 - 10))
        window.blit(normal_button, (WIDTH // 2 - normal_button.get_width() // 2, HIGHT // 2 + 40))
        window.blit(fast_button, (WIDTH // 2 - fast_button.get_width() // 2, HIGHT // 2 + 90))
        pygame.display.update()


def main():
    speed_level = show_intro_screen()

    if speed_level == "slow":
        snake_speed = 5
    elif speed_level == "normal":
        snake_speed = 10
    else:
        snake_speed = 15

    snake = Snake(speed_level)
    food = Food()

    score = 0  # Initialize the score to zero
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction(0, -1)
                elif event.key == pygame.K_DOWN:
                    snake.change_direction(0, 1)
                elif event.key == pygame.K_LEFT:
                    snake.change_direction(-1, 0)
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction(1, 0)
        snake.move()

        head = snake.get_head()
        if distance(head, food.get_position()) < 20:
            snake.grow()
            food.respawn()
            score += 1

        #cek kalo snake nyetuh diri sendiri
        if head in snake.get_body():
            #draw gameOver
            font = pygame.font.Font(None, 50)
            text = font.render("Game Over", True, BLACK)
            window.blit(text, (WIDTH // 2 - text.get_width() // 2, HIGHT // 2 - text.get_height() // 2))
            pygame.display.update()
            time.sleep(2)
            pygame.quit()
            return

        window.fill(WHITE)

        #draw snake's body as black rectangles
        for segment in snake.body:
            pygame.draw.rect(window, BLACK, (segment[0], segment[1], 20, 20))

        RED = (255, 0, 0)
        #draw food as a red circle
        pygame.draw.circle(window, RED, food.get_position(), 10)

        #draw score
        font = pygame.font.Font(None, 30)
        text = font.render("Score: " + str(score), True, BLACK)
        window.blit(text, (10, 10))

        pygame.display.update()
        clock.tick(snake_speed)

if __name__ == "__main__":
    main()
