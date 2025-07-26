import pygame
import sys
import math 
from pygame.locals import QUIT, MOUSEBUTTONDOWN

pygame.init()

window_width, window_height = 600, 400
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Spinner Game")

#colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)  
BLACK = (0, 0, 0)

background_image = pygame.image.load("background.png").convert()
background_image = pygame.transform.scale(background_image, (window_width, window_height))

spinner_image = [
    pygame.image.load("fidgetspinner1.png").convert_alpha(),
    pygame.image.load("fidgetspinner2.png").convert_alpha(),
    pygame.image.load("fidgetspinner3.png").convert_alpha(),
]

spinner_width, spinner_height = 300, 300
spinner_image = [pygame.transform.scale(image, (spinner_width, spinner_height)) for image in spinner_image]

#posisition and rotation
spinner_x = window_width // 2
spinner_y = window_height // 2
spinner_rotation = 0

#spinner speed and index
spinner_rotation_speed = 5
current_spinner = 0

#font for display speed
font = pygame.font.SysFont(None, 48)

#function to change spinner option
def change_spinner():
    global current_spinner
    current_spinner += 1
    if current_spinner >= len(spinner_image):
        current_spinner = 0


#game over
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            change_spinner()

    window.blit(background_image, (0, 0))

    #rotate the spinner based on mouse move
    mouse_x, mouse_y = pygame.mouse.get_pos()
    angle = math.atan2(mouse_y - spinner_y, mouse_x - spinner_x)
    spinner_rotation_speed = math.degrees(angle)  # Adjusting for the spinner  #radian to degree conversion

    #rotate the spinner image
    spinner_rotation += spinner_rotation_speed
    rotate_spinner = pygame.transform.rotate(spinner_image[current_spinner], -spinner_rotation)
    rotate_rect = rotate_spinner.get_rect(center=(spinner_x, spinner_y))

    window.blit(rotate_spinner, rotate_rect)


    spinner_text = font.render(f"Spinner Speed: {spinner_rotation_speed}", True, BLACK)
    window.blit(spinner_text, (300, 10))
    pygame.display.update()
    pygame.time.delay(30)

pygame.quit()
pygame.exit()