# Import required modules
import pygame
import random
import sys

# Initialize the Pygame library
pygame.init()

# Set up the game window dimensions
window_width, window_height = 400, 300
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Simon Says')

SUPERHEROES ={
    1 :{
        'image' : pygame.transform.scale(pygame.image.load('superman.png'), (50, 100)),
        'sound' : pygame.mixer.Sound('superman.wav')
    },
    2 :{
        'image' : pygame.transform.scale(pygame.image.load('spiderman.png'), (50, 100)),
        'sound' : pygame.mixer.Sound('spiderman.wav')
    },
    3 :{
        'image' : pygame.transform.scale(pygame.image.load('ironman.png'), (50, 100)),
        'sound' : pygame.mixer.Sound('ironman.wav')
    },
    4 :{
        'image' : pygame.transform.scale(pygame.image.load('batman.png'), (50, 100)),
        'sound' : pygame.mixer.Sound('batman.wav')
    }
}

"""
SUPERHEROES[4]['sound'].play()          #testing play the sound
pygame.time.delay(2000)
"""

#list to store the sequence
sequence = []

#function to display  message on the screen
def display_message(message):
    font = pygame.font.SysFont(None, 48)
    text = font.render(message, True, (255, 255, 255))
    text_rect = text.get_rect(center=(window_width // 2, window_height // 4))
    window.fill((255, 255, 255))
    window.blit(text, text_rect)
    pygame.display.update()


#function to display the superhero image
def display_image():
    for i in range(1,5):
        window.blit(SUPERHEROES[i]['image'], ((i-1)*100+25,150))
    pygame.display.update()

#function to play the sequence of sounds and images
def play_sequence(length):
    global sequence
    sequence = [random.randint(1, 4) for _ in range(length)]
    display_message("listen sequence")

    for superhero_num in sequence:
        SUPERHEROES[superhero_num]['sound'].play()
        display_image()


#function to play the squence and get player response
def play_sound_and_get_response():
    global sequence
    sequence_length = len(sequence)+1
    play_sequence(sequence_length)

    #wait for player response
    for superhero_num in sequence:
       waiting_for_input = True
       while waiting_for_input:
           for event in pygame.event.get():
               if event.type == pygame.MOUSEBUTTONDOWN:
                   mouse_x,mouse_y = pygame.mouse.get_pos()
                   image_rect = SUPERHEROES[superhero_num]['image'].get_rect(
                       topleft = ((superhero_num-1)*100+25, 150)
                   )
                   if image_rect.collidepoint(mouse_x, mouse_y):
                       waiting_for_input = False
                   else:
                       return False   #wrong sequence, game over
    return True

pygame.mixer.init()

gameover = False
while not gameover:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True

    #play sound and get player response
    if play_sound_and_get_response():
        display_message("correct sequence")
        pygame.time.delay(2000)
    else:
        display_message("wrong sequence")
        pygame.time.delay(2000)
        gameover = True

pygame.quit()
sys.exit()



