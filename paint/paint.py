import pygame
from pygame.locals import QUIT

pygame.init()

window_width, window_height = 400, 300
toolbar_height = 50

white = (255, 255, 255)
black = (0, 0, 0)
gray = (128, 128, 128)
red=(255,0,0)

#create the window
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Paint')

#Variables
drawing = False
brush_size = 2
min_brush_size = 1
max_brush_size = 10
brush_color = black
eraser_mode = False
last_pos = None

#create canvas
canvas = pygame.Surface((window_width, window_height - toolbar_height))
canvas.fill(white)

#create a toolbar
toolbar = pygame.Surface((window_width, toolbar_height))
toolbar.fill(gray)

#main loop of the program
running = True
while running:

    toolbar.fill(gray)
    font = pygame.font.SysFont(None, 25)
    pen_text = font.render('Pen', True, black)
    eraser_text = font.render('Eraser', True, black)
    decrease_brush_text = font.render('-', True, black)
    increase_brush_text = font.render('+', True, black)
    toolbar.blit(pen_text, (40, 20))
    toolbar.blit(eraser_text, (80, 20))
    toolbar.blit(decrease_brush_text, (120, 20))
    toolbar.blit(increase_brush_text, (160, 20))

    #draw color selection buttons
    color_button_width =20
    color_button_hight = 20
    black_color_button = pygame.draw.circle(toolbar,black,(240,25),color_button_width//2)
    red_color_button = pygame.draw.circle(toolbar,red,(280,25),color_button_width//2)

    window.fill(white)

    window.blit(canvas, (0, toolbar_height))
    window.blit(toolbar, (0, 0))

    pygame.display.update()