import pygame, sys
from pygame.locals import QUIT, MOUSEBUTTONDOWN

pygame.init()

window_width, window_height = 400,300
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Ping pong")

#colors
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)

#PADDLE
paddle_width = 10
paddle_height = 80

paddle_x = window_width // 2 - paddle_width // 2            #POSISI DITENGAH
paddle_y = window_height - paddle_height - 10                   #POSISI BAWAH

#BALL
ball_x = window_width // 2
ball_y = window_height // 2
ball_radius = 10
ball_x_speed = 3
ball_y_speed = -3

#score
score = 0
font = pygame.font.SysFont(None, 36)

game_over = False


while not game_over:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        #move the paddle
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle_x > 0:
            paddle_x -= 5
        if keys[pygame.K_RIGHT] and paddle_x < window_width - paddle_width:
            paddle_x += 5

        #move the ball
        ball_x += ball_x_speed
        ball_y += ball_y_speed


    #draw everthing
    window.fill(WHITE)
    paddle = pygame.draw.rect(window, BLACK, (paddle_x, paddle_y, paddle_height, paddle_width))
    ball = pygame.draw.circle(window, BLACK, (ball_x, ball_y), ball_radius)

    score_text = font.render("Score: " + str(score), True, BLUE)
    window.blit(score_text, (10, 10))

    pygame.display.update()

    # ball collision with walls
    if ball.left <= 0 or ball.right >= window_width:
        ball_x_speed *= -1
    if ball.top <= 0:
        ball_y_speed *= -1

    #ball collision with paddle
    if pygame.Rect.colliderect(ball, paddle):
        ball_y_speed *= -1
        score += 1


    if ball.bottom >= window_height:
        game_over = True

    pygame.time.delay(30)

window.fill(RED)
score_text = font.render("Score: " + str(score), True, BLUE)
window.blit(score_text, (10, 10))
game_over_text = font.render("Game Over", True, BLUE)
window.blit(game_over_text, (window_width // 2 - game_over_text.get_width() // 2, window_height // 2 - game_over_text.get_height() // 2))
pygame.display.update()

pygame.time.delay(2000)
pygame.quit()
sys.exit()


