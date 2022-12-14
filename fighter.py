import pygame

class Fighter():
    #constructor
    def __init__(self, x, y, data, sprite_sheet, animation_steps):
        self.size = data[0]
        self.flip = False
        self.animation_list = self.load_images(sprite_sheet, animation_steps)
        self.action = 0 #0:idle. 1:run. 2: jump. 3:attack. 4:attack2. 5:hit. 6:death.
        self.frame_index = 0
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = pygame.Rect((x, y, 80, 180))
        self.vel_y = 0
        self.jump = False
        self.attacking = False
        self.attackType = 0
        self.health = 100

    def load_images(self, sprite_sheet, animation_steps):
        #extract images from spritesheet
        #the first for loop is goes down and up, the second one goes from left to right
        #enumerate increases the y variable if done with a row and goes to the next row
        animation_list = []
        for y, animation in enumerate(animation_steps):
            temp_img_list = []
            for x in range(animation):
                temp_img = sprite_sheet.subsurface(x * self.size, y * self.size, self.size, self.size)
                temp_img_list.append(temp_img)
            animation_list.append(temp_img_list)
        return animation_list

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

        #makes sure that the players face eachother
        #if the target is on the right hand side of the player, there is no need to flip
        if target.rect.centerx > self.rect.centerx:
            self.flip = False
        else: 
            self.flip = True
            
        #update player position
        self.rect.x += dx
        self.rect.y += dy


    def attack(self, surface, target):
        self.attacking = True
        attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip) , self.rect.y, 2 * self.rect.width, self.rect.height)

        #check collision
        if attacking_rect.colliderect(target.rect):
            print("hit!")
            target.health -= 10

        pygame.draw.rect(surface, (0, 150, 0), attacking_rect)

    #draws the fighter
    #blitting is drawing
    def draw(self, surface): 
        #gives the rectangle a color
        pygame.draw.rect(surface, (255, 0, 0), self.rect)
        surface.blit(self.image, (self.rect.x, self.rect.y))