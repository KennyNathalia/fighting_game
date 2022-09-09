import pygame

class Fighter():
    #constructor
    def __init__(self, x, y):
        #creates rectangle object
        self.rect = pygame.Rect((x, y, 80, 180))

    #draws the fighter
    def draw(self, surface): 
        pygame.draw.rect(surface, (255, 0, 0), self.rect)