import pygame
from fighter import Fighter

#initialize all imported pygame modules
pygame.init()

#create game window
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

#makes the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fighterz")

#set framerate so that fighters move normally
clock = pygame.time.Clock()
FPS = 60

#define colors
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

#load background image
bg_image = pygame.image.load("D:/laravel/fighting_game/assets/images/background/background.gif").convert_alpha()

#function for drawing the background
#blitting is drawing
def draw_bg():
    #scale resizes the images to the given screen width and height
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0, 0))

#function for drawing the fighters health bars
#if for example health is 50, the ratio will be 0.5
#the health bar width changes depending on the ratio
def draw_health_bar(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, WHITE, (x - 2, y - 2, 404, 34))
    pygame.draw.rect(screen, RED, (x, y, 400, 30))
    pygame.draw.rect(screen, YELLOW, (x, y, 400 * ratio, 30))


#create two fighter instances
fighter_1 = Fighter(200, 310)
fighter_2 = Fighter(700, 310)

#game loop so that the game window doesn't shut off
run = True
while run:

    #runs at 60 fps otherwise it will move too fastd
    clock.tick(FPS)

    #draw background
    draw_bg()

    #show stats
    draw_health_bar(fighter_1.health, 20, 20)
    draw_health_bar(fighter_2.health, 580, 20)

    #move fighters
    fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2)
    #fighter_2.move()

    #draw fighters
    fighter_1.draw(screen)
    fighter_2.draw(screen)

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #updates display
    pygame.display.update()

#exit pygame
pygame.quit()