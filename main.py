import pygame

#initialize all imported pygame modules
pygame.init()

#create game window
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

#makes the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fighter")

#load background image
bg_image = pygame.image.load("D:/laravel/fighting_game/assets/images/background/background.gif").convert_alpha()

#function for drawing the background
#blitting is drawing
def draw_bg():
    #scale resizes the images to the given screen width and height
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0, 0))


#game loop so that the game window doesn't shut off
run = True
while run:

    #draw background
    draw_bg()

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #updates display
    pygame.display.update()

#exit pygame
pygame.quit()