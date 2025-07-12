import pygame
import random

# Initialize Pygame
pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
WHITE = (255, 255, 255) 
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#PADDEL PROPERTIES
PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100   
PADDLE_SPEED = 7

# BALL PROPERTIES
BALL_SIZE = 20
BALL_SPEED_X = 7
BALL_SPEED_Y = 7

#SCORE FONT
FONT = pygame.font.Font(None, 80)   
MESSAGE_FONT = pygame.font.Font(None, 60)

#SET UP DISPLAY
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")
# Game clock
clock = pygame.time.Clock()

#GAME CLASS

class Paddel:
    def __init__(self,x,y,color):
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.color = color

    def draw(self,surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def move(self, dy):
        self.rect.y += dy
        # Keep the paddle within the screen bounds
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

    def ai_move(self, ball):
        if self.rect.centery < ball.rect.centery:
            self.move(PADDLE_SPEED)
        elif self.rect.centery > ball.rect.centery:
            self.move(-PADDLE_SPEED)

class Ball:
    def __init__(self, x, y,color):
        self.rect = pygame.Rect(x, y, BALL_SIZE, BALL_SIZE)
        self.color = color
        self.dx = BALL_SPEED_X * random.choice((1, -1))  # Randomize initial horizontal direction
        self.dy = BALL_SPEED_Y * random.choice((1, -1))

    def draw(self, surface):
        pygame.draw.ellipse(surface, self.color, self.rect)

    def move(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

    def check_collision_wall(self):
        # Check for collision with top and bottom walls
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.dy *= -1

    def check_collision_paddle(self, paddle):
        # Check for collision with paddle
        if self.rect.colliderect(paddle.rect):
            self.dx *= -1
            
            self.dy += random.uniform(-1,1) *0.5
            self.dy = max(-BALL_SPEED_Y * 1.5, min(BALL_SPEED_Y * 1.5, self.dy))

    def reset(self):
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.dx = BALL_SPEED_X * random.choice((1, -1))
        self.dy = BALL_SPEED_Y * random.choice((1, -1))

def reset_game():
    player_paddle = Paddel(50, HEIGHT // 2 - PADDLE_HEIGHT // 2, GREEN)
    ai_paddle = Paddel(WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, BLUE)
    ball = Ball(WIDTH // 2, HEIGHT // 2, WHITE)
    return player_paddle, ai_paddle, ball

player_paddle, ai_paddle, ball = reset_game()

#game state variables
game_active = False
player_score = 0
ai_score = 0
max_score = 5

#game loop
running = True
while running:
    #event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_active:
                game_active = True
                player_paddle, ai_paddle, ball = reset_game()
                player_score = 0
                ai_score = 0

    #player paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_paddle.move(-PADDLE_SPEED)
    if keys[pygame.K_DOWN]:
        player_paddle.move(PADDLE_SPEED)

    #game logic
    if game_active:
        #move ball
        ball.move()
        ball.check_collision_wall()
        ball.check_collision_paddle(player_paddle)
        ball.check_collision_paddle(ai_paddle)

        #AI paddle movement
        ai_paddle.ai_move(ball)

        #check for scoring
        if ball.rect.left <= 0:
            ai_score += 1
            if ai_score >= max_score:
                game_active = False
            ball.reset()
        elif ball.rect.right >= WIDTH:
            player_score += 1
            if player_score >= max_score:
                game_active = False
            ball.reset()




    #drawing
    screen.fill(BLACK)

    #draw paddles and ball
    player_paddle.draw(screen)
    ai_paddle.draw(screen)
    ball.draw(screen)

    #draw center line(dashed)
    for i in range(0, HEIGHT, 20):
        pygame.draw.rect(screen,WHITE,(WIDTH // 2 - 1, i, 2, 10))

    #draw scores
    SCORE_FONT = pygame.font.Font(None, 74)
    MESSAGE_FONT = pygame.font.Font(None, 60)
    player_text = SCORE_FONT.render(str(player_score), True, WHITE)
    ai_text = SCORE_FONT.render(str(ai_score), True, GREEN)
    screen.blit(player_text, (WIDTH // 4, 20))
    screen.blit(ai_text, (WIDTH * 3 // 4 - ai_text.get_width()//2, 20))

    #draw game message
    if not game_active:
        if player_score >= max_score:
            message = "You Win!"
        elif ai_score >= max_score:
            message = "AI Wins!"
        else:
            message = "Press SPACE to Start"
        message_text = MESSAGE_FONT.render(message, True, WHITE)
        text_rect = message_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(message_text, text_rect)




    #update display
    pygame.display.flip()

    #control frame rate
    clock.tick(FPS)

pygame.quit()