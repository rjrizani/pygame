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
        'image' : pygame.transform.scale(pygame.image.load('simon_say/superman.png'), (50, 100)),
        'sound' : pygame.mixer.Sound('simon_say/superman.wav')
    },
    2 :{
        'image' : pygame.transform.scale(pygame.image.load('simon_say/spiderman.png'), (50, 100)),
        'sound' : pygame.mixer.Sound('simon_say/spiderman.wav')
    },
    3 :{
        'image' : pygame.transform.scale(pygame.image.load('simon_say/ironman.png'), (50, 100)),
        'sound' : pygame.mixer.Sound('simon_say/ironman.wav')
    },
    4 :{
        'image' : pygame.transform.scale(pygame.image.load('simon_say/batman.png'), (50, 100)),
        'sound' : pygame.mixer.Sound('simon_say/batman.wav')
    }
}

"""
SUPERHEROES[4]['sound'].play()          #testing play the sound
pygame.time.delay(2000)
"""

#list to store the sequence
sequence = []

#function to display  message on the screen
def display_message(message, color=(255, 255, 255)):
    font = pygame.font.SysFont(None, 48)
    text = font.render(message, True, color)
    text_rect = text.get_rect(center=(window_width // 2, window_height // 4))
    window.fill((0, 0, 0))  # Fill with black to clear previous message
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
    pygame.time.delay(2000)

    for superhero_num in sequence:
        SUPERHEROES[superhero_num]['sound'].play()
        display_image()
        pygame.time.delay(1000)


#function to play the squence and get player response
def play_sound_and_get_response():
    global sequence
    sequence_length = len(sequence)+1
    play_sequence(sequence_length)

    #wait for player response
    for i, superhero_num in enumerate(sequence):
       waiting_for_input = True
       start_time = pygame.time.get_ticks()  # Start timer for input
       while waiting_for_input:
           for event in pygame.event.get():
               if event.type == pygame.MOUSEBUTTONDOWN:
                   mouse_x,mouse_y = pygame.mouse.get_pos()
                   image_rect = SUPERHEROES[superhero_num]['image'].get_rect(
                       topleft = (((superhero_num)-1)*100+25, 150)
                   )
                   if image_rect.collidepoint(mouse_x, mouse_y):
                       SUPERHEROES[superhero_num]['sound'].play()
                       display_image()
                       pygame.time.delay(500)
                       waiting_for_input = False
                   else:
                       return False   #wrong sequence, game over
               if event.type == pygame.QUIT:
                   pygame.quit()
                   sys.exit()
    return True

pygame.mixer.init()

gameover = False
while not gameover:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True

    #play sound and get player response
    if play_sound_and_get_response():
        display_message("correct sequence", (0, 255, 0))  # Green for correct
        pygame.time.delay(2000)
    else:
        display_message("wrong sequence", (255, 0, 0))  # Red for wrong
        pygame.time.delay(2000)
        gameover = True

pygame.quit()
sys.exit()



