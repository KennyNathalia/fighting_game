import pygame

class Fighter():
    #constructor
    def __init__(self, x, y):
        #creates rectangle object
        self.rect = pygame.Rect((x, y, 80, 180))
        self.vel_y = 0
        self.jump = False
        self.attacking = False
        self.attackType = 0
        self.health = 100

    def move(self, screen_width, screen_height, surface, target):
        SPEED = 10
        GRAVITY = 2
        #dx and dy are the changes in the x and y coordinates
        dx = 0
        dy = 0

        #get keypresses
        key =   pygame.key.get_pressed()

        #can only perform other actions if not currently attacking
        if self.attacking == False:
            #movement
            if key[pygame.K_a]:
                dx = -SPEED

            if key[pygame.K_d]:
                dx = SPEED 

            #jump. You can only jump if your not currently jumping
            if key[pygame.K_w] and self.jump == False:
                self.vel_y = -30
                self.jump = True

            #attack
            if key[pygame.K_r] or key[pygame.K_t]:
                self.attack(surface, target)

                #determine which attack was used
                if key[pygame.K_r]:
                    self.attackType = 1
                    #print('attack 1!')
                if key[pygame.K_t]:
                    self.attackType = 2
                    #print('attack 2!')

        #apply gravity
        self.vel_y += GRAVITY
        dy += self.vel_y

        #makes sure player stays on screen
        #for example, it can't go lower than zero, otherwise it will go off the screen
        if self.rect.left + dx < 0:
            dx = 0 - self.rect.left 

        #same thing for the right side
        #if it goes higher than the screen_width, it stops
        if self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right

        #bottom
        if self.rect.bottom + dy > screen_height - 110:
            self.vel_y = 0
            self.jump = False
            dy = screen_height - 110 - self.rect.bottom
            
        #update player position
        self.rect.x += dx
        self.rect.y += dy


    def attack(self, surface, target):
        self.attacking = True
        attacking_rect = pygame.Rect(self.rect.centerx, self.rect.y, 2 * self.rect.width, self.rect.height)

        #check collision
        if attacking_rect.colliderect(target.rect):
            print("hit!")
            target.health -= 10

        pygame.draw.rect(surface, (0, 150, 0), attacking_rect)

    #draws the fighter
    def draw(self, surface): 
        #gives the rectangle a color
        pygame.draw.rect(surface, (255, 0, 0), self.rect)