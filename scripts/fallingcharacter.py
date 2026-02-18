import pygame
import random
from scripts.image import Images
from settings import Settings



class FallingCharacter(pygame.sprite.Sprite):
    def __init__(self,position,vitesse,warning_time):
        super().__init__()
        
        #___/Character\___
        self.character_number = random.randint(0,5) 
        self.position = [position[0] - 28, position[1] -28]
   
        
        #Animation
        self.frame = 0
        self.animation_images = Images.extract_animation_line_from_sheet("assets/entities/fallingcharacter/character_sheet.png",self.character_number,4,64,64)
        self.current_image = self.animation_images[self.frame]
        
        #Rect/Collision
        self.rect = pygame.rect.Rect(self.position[0] + 8,self.position[1] + 16,48,32)
        self.rect.center = position
        
        #Mask
        self.mask = pygame.mask.from_surface(self.current_image)
        
        #Variable
        self.vitesse = vitesse
        self.is_falling = False


        #___/Warning\___
        self.warning_time = warning_time

        self.warning_frame = 0
        self.warning_animation_images = Images.extract_animation_line_from_sheet("assets/others/Point_exclamation.png",0,4,32,32)
        self.current_warning_images = self.warning_animation_images[0]

        self.start_time = pygame.time.get_ticks()
        self.current_time = pygame.time.get_ticks() - self.start_time



    def animation_update(self):
        self.warning_frame += 0.2
        if self.warning_frame > 3:
            self.warning_frame = 0
        else:
            self.current_warning_images = self.warning_animation_images[int(self.warning_frame)]

        self.frame += 0.08
        if self.frame > 3:
            self.frame = 0
        else:
            self.current_image = self.animation_images[int(self.frame)]
            self.mask = pygame.mask.from_surface(self.current_image)
        

    def verify_time(self,player_position):
        self.current_time = pygame.time.get_ticks() - self.start_time
        if self.current_time > self.warning_time:
            self.is_falling = True
            self.position = [self.position[0] ,player_position[1]  - Settings.SCREEN_RESOLUTION[1]]
            self.rect.topleft = [self.position[0] + 8 ,player_position[1]  - Settings.SCREEN_RESOLUTION[1] + 16]

    def update(self,player_position):
        self.animation_update()
        if self.is_falling:
            self.position[1] += self.vitesse
            self.rect.y += self.vitesse
        else:
             self.verify_time(player_position)

    
    def draw(self, screen, scroll):
        if self.is_falling:
            screen.blit(self.current_image, (self.position[0] -scroll[0], self.position[1]-scroll[1]))
            #pygame.draw.rect(screen,(255,0,0),(self.rect.x - scroll[0], self.rect.y - scroll[1],48,32))
        else:
            screen.blit(self.current_warning_images, (self.position[0] - scroll[0] + 20, 0))

        

