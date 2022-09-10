import pygame

class Fighter():
    #constructor
    def __init__(self, x, y):
        #creates rectangle object
        self.rect = pygame.Rect((x, y, 80, 180))

    def move(self, screen_width):
        SPEED = 10
        #dx and dy are the changes in the x and y coordinates
        dx = 0
        dy = 0

        #get keypresses
        key =   pygame.key.get_pressed()

        #movement
        if key[pygame.K_a]:
            dx = -SPEED

        if key[pygame.K_d]:
            dx = SPEED 

        #makes sure player stays on screen
        #for example, it can't go lower than zero, otherwise it will go off the screen
        if self.rect.left + dx < 0:
            dx = 0 - self.rect.left 

        #same thing for the right side
        #if it goes higher than the screen_width, it stops
        if self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right
            
        #update player position
        self.rect.x += dx
        self.rect.y += dy

    #draws the fighter
    def draw(self, surface): 
        #gives the rectangle a color
        pygame.draw.rect(surface, (255, 0, 0), self.rect)