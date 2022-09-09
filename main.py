import pygame

#initialize all imported pygame modules
pygame.init()

#create game window
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

#makes the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fighter")


#game loop so that the game window doesn't shut off
run = True
while run:

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

#exit pygame
pygame.quit()