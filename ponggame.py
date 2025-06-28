import pygame
import random

# Initialize Pygame
pygame.init()

# --- Game Constants ---
WIDTH, HEIGHT = 800, 600  # Screen dimensions
FPS = 60                   # Frames per second

# Colors (RGB)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Paddle properties
PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100
PADDLE_SPEED = 7

# Ball properties
BALL_SIZE = 20
BALL_SPEED_X = 7
BALL_SPEED_Y = 7

# Score font
SCORE_FONT = pygame.font.Font(None, 80)
MESSAGE_FONT = pygame.font.Font(None, 60)

# --- Set up the game window ---
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Classic Pong")
clock = pygame.time.Clock()

# --- Game Classes ---

class Paddle:
    def __init__(self, x, y, color):
        """
        Initializes a paddle.

        Args:
            x (int): X-coordinate of the top-left corner.
            y (int): Y-coordinate of the top-left corner.
            color (tuple): RGB color of the paddle.
        """
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.color = color
        self.score = 0

    def draw(self, surface):
        """
        Draws the paddle on the given surface.

        Args:
            surface (pygame.Surface): The surface to draw on (e.g., the screen).
        """
        # Removed border_radius for compatibility with older Pygame versions
        pygame.draw.rect(surface, self.color, self.rect)

    def move(self, dy):
        """
        Moves the paddle vertically, keeping it within screen bounds.

        Args:
            dy (int): The change in Y-coordinate.
        """
        self.rect.y += dy
        # Keep paddle within screen bounds
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

    def ai_move(self, ball):
        """
        Simple AI movement for the opponent paddle.
        Moves the paddle towards the ball's Y-position.

        Args:
            ball (Ball): The ball object.
        """
        if self.rect.centery < ball.rect.centery:
            self.move(PADDLE_SPEED)
        elif self.rect.centery > ball.rect.centery:
            self.move(-PADDLE_SPEED)


class Ball:
    def __init__(self, x, y, color):
        """
        Initializes the ball.

        Args:
            x (int): X-coordinate of the top-left corner.
            y (int): Y-coordinate of the top-left corner.
            color (tuple): RGB color of the ball.
        """
        self.rect = pygame.Rect(x, y, BALL_SIZE, BALL_SIZE)
        self.color = color
        self.dx = BALL_SPEED_X * random.choice([1, -1]) # Random initial direction X
        self.dy = BALL_SPEED_Y * random.choice([1, -1]) # Random initial direction Y

    def draw(self, surface):
        """
        Draws the ball on the given surface.

        Args:
            surface (pygame.Surface): The surface to draw on.
        """
        # Removed border_radius for compatibility with older Pygame versions
        pygame.draw.ellipse(surface, self.color, self.rect)

    def move(self):
        """
        Moves the ball based on its current direction.
        """
        self.rect.x += self.dx
        self.rect.y += self.dy

    def check_collision_wall(self):
        """
        Checks for collision with top/bottom walls and reverses Y-direction if hit.
        """
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.dy *= -1

    def check_collision_paddle(self, paddle):
        """
        Checks for collision with a paddle and reverses X-direction if hit.

        Args:
            paddle (Paddle): The paddle object to check collision with.
        """
        if self.rect.colliderect(paddle.rect):
            self.dx *= -1
            # Add a slight random variation to Y-speed after collision
            self.dy += random.uniform(-1, 1) * 0.5
            # Ensure Y-speed doesn't get too high
            self.dy = max(-BALL_SPEED_Y * 1.5, min(BALL_SPEED_Y * 1.5, self.dy))

    def reset(self):
        """
        Resets the ball to the center of the screen with a random initial direction.
        """
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.dx = BALL_SPEED_X * random.choice([1, -1])
        self.dy = BALL_SPEED_Y * random.choice([1, -1])

# --- Game Initialization ---

def reset_game():
    """Resets all game elements to their initial state."""
    player_paddle = Paddle(50, HEIGHT // 2 - PADDLE_HEIGHT // 2, GREEN)
    ai_paddle = Paddle(WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, BLUE)
    ball = Ball(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, WHITE)
    return player_paddle, ai_paddle, ball

player_paddle, ai_paddle, ball = reset_game()

# --- Game State Variables ---
game_active = False # True when game is being played, False for menu/game over
player_score = 0
ai_score = 0
max_score = 5 # Score needed to win

# --- Game Loop ---
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not game_active: # Start or restart game on spacebar
                    player_score = 0
                    ai_score = 0
                    player_paddle, ai_paddle, ball = reset_game()
                    game_active = True

    # Player paddle movement (held down keys)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_paddle.move(-PADDLE_SPEED)
    if keys[pygame.K_DOWN]:
        player_paddle.move(PADDLE_SPEED)

    # --- Game Logic (only if game is active) ---
    if game_active:
        ball.move()
        ball.check_collision_wall()
        ball.check_collision_paddle(player_paddle)
        ball.check_collision_paddle(ai_paddle)
        ai_paddle.ai_move(ball)

        # Check for scoring
        if ball.rect.left <= 0: # AI scores
            ai_score += 1
            ball.reset()
            game_active = False # Pause game until spacebar is pressed again
        elif ball.rect.right >= WIDTH: # Player scores
            player_score += 1
            ball.reset()
            game_active = False # Pause game until spacebar is pressed again

        # Check for game over
        if player_score >= max_score:
            game_active = False
            # Display "Player Wins!" message
        elif ai_score >= max_score:
            game_active = False
            # Display "AI Wins!" message

    # --- Drawing ---
    screen.fill(BLACK) # Clear the screen

    # Draw paddles and ball
    player_paddle.draw(screen)
    ai_paddle.draw(screen)
    ball.draw(screen)

    # Draw center line (dashed)
    for i in range(0, HEIGHT, 20):
        pygame.draw.rect(screen, WHITE, (WIDTH // 2 - 2, i, 4, 10))

    # Draw scores
    player_text = SCORE_FONT.render(str(player_score), True, WHITE)
    ai_text = SCORE_FONT.render(str(ai_score), True, WHITE)
    screen.blit(player_text, (WIDTH // 4 - player_text.get_width() // 2, 20))
    screen.blit(ai_text, (WIDTH * 3 // 4 - ai_text.get_width() // 2, 20))

    # Display messages
    if not game_active:
        if player_score >= max_score:
            message = MESSAGE_FONT.render("PLAYER WINS!", True, WHITE)
        elif ai_score >= max_score:
            message = MESSAGE_FONT.render("AI WINS!", True, WHITE)
        elif player_score == 0 and ai_score == 0:
            message = MESSAGE_FONT.render("Press SPACE to Start", True, WHITE)
        else: # After a score, before game over
            message = MESSAGE_FONT.render("Press SPACE to Continue", True, WHITE)

        message_rect = message.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
        screen.blit(message, message_rect)

    # Update the display
    pygame.display.flip()

    # Control frame rate
    clock.tick(FPS)

pygame.quit()
