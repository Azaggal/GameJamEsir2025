import pygame
from settings import Settings



class Tile(pygame.sprite.Sprite):

    def __init__(self,name,pos_x,pos_y,image): 
        super().__init__()
        self.name = name
        self.position = [pos_x,pos_y]
        self.image = image
        self.rect = self.image.get_rect(topleft=(self.position)) 

        
        self.mask = pygame.mask.from_surface(self.image)


    def draw(self,surface,scroll):
        surface.blit(self.image, (self.position[0] - scroll[0],self.position[1] - scroll[1]))


        
       