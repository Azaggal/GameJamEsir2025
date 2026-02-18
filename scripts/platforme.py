import pygame
from math import exp

class Platforme(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.liste = []

    def update(self):
        for el in self.liste :
            el.update()

    def draw(self,screen,scroll):
        for el in self.liste :
            el.draw(screen,scroll)
            
        
class Deplacement(pygame.sprite.Sprite):

    def __init__(self,x_depart,y_depart,x_arrivee,y_arrivee,nb_frame,color,numero):
        super().__init__()

        self.x_chemin = (x_arrivee - x_depart)/nb_frame
        self.y_chemin = (y_arrivee - y_depart)/nb_frame


        self.x_chemin = int(self.x_chemin)
        self.y_chemin = int(self.y_chemin)
        self.y_arrivee = y_arrivee
        self.x_arrivee = x_arrivee 
        self.y_depart = y_depart
        self.x_depart = x_depart

        self.numero = numero
        
        self.color = color

        self.aller = True
        self.nombre_frame = nb_frame


        self.image = pygame.image.load("assets/prises/prise2_violet.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (16, 16))
        self.rect = pygame.Rect(x_depart,y_depart,16,16)

    def update(self):
        
        if self.aller:
                self.rect.x += self.x_chemin
                self.rect.y += self.y_chemin
                if self.numero == 1:
                    if self.rect.x > self.x_arrivee and self.y_arrivee > self.rect.y :
                        self.aller = False
                elif self.x_arrivee == self.x_depart :
                    if 10 > abs(self.rect.y - self.y_arrivee):
                        self.aller = False
                elif self.y_arrivee == self.y_depart :
                    if 10 > abs(self.rect.x - self.x_arrivee):
                        self.aller = False
                elif 20 > abs(self.rect.x - self.x_arrivee) and 20 > abs(self.rect.y - self.y_arrivee) :
                    self.aller = False
        else : 
                self.rect.x -= self.x_chemin
                self.rect.y -= self.y_chemin
                if self.numero == 1:
                    if self.x_depart > self.rect.x and self.rect.y > self.y_depart :
                        self.aller = True
                elif self.x_arrivee == self.x_depart :
                    if 10 > abs(self.rect.y - self.y_depart):
                        self.aller = True
                elif self.y_arrivee == self.y_depart :
                    if 10 > abs(self.rect.x - self.x_depart):
                        self.aller = True
                elif 10 > abs(self.rect.x - self.x_depart) and 10 > abs(self.rect.y - self.y_depart) :
                    self.aller = True
            

    def draw(self, screen, scroll):
        screen.blit(self.image, (self.rect.x-scroll[0], self.rect.y-scroll[1]))

class VitesseHorizontale(pygame.sprite.Sprite) :
    def __init__(self,x_depart,y_depart,color):
        super().__init__()

        self.image = pygame.image.load("assets/prises/prise2_bleu.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (16, 16))
        self.rect = pygame.Rect(x_depart,y_depart,16,16)

        self.color = color


    def draw(self, screen, scroll):
        screen.blit(self.image, (self.rect.x-scroll[0], self.rect.y-scroll[1]))


class VitesseVerticale(pygame.sprite.Sprite) :
    def __init__(self,x_depart,y_depart,color):
        super().__init__()

        self.image = pygame.image.load("assets/prises/prise2_vert.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (16, 16))
        self.rect = pygame.Rect(x_depart,y_depart,16,16)
        
        self.color = color


    def draw(self, screen, scroll):
        screen.blit(self.image, (self.rect.x-scroll[0], self.rect.y-scroll[1]))
        

class PetitePrise(pygame.sprite.Sprite) :
    def __init__(self,x_depart,y_depart,color):
        super().__init__()

        self.image = pygame.image.load("assets/prises/prise2_rouge.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (16, 16))
        self.rect = pygame.Rect(x_depart,y_depart,16,16)

        self.color = color


    def draw(self, screen, scroll):
        screen.blit(self.image, (self.rect.x-scroll[0], self.rect.y-scroll[1]))



class Catapulte(pygame.sprite.Sprite) :
    def __init__(self,x_depart,y_depart,x_arrivee,y_arrivee,nb_frame,velocite_x,velocite_y,color):
        super().__init__()

        self.velocite_x=velocite_x
        self.velocite_y=velocite_y

        self.color = color
    

        self.x_chemin = (x_arrivee - x_depart)/nb_frame
        self.y_chemin = (y_arrivee - y_depart)/nb_frame
        self.x_chemin = int(self.x_chemin)
        self.y_chemin = int(self.y_chemin)
        self.y_arrivee = y_arrivee
        self.x_arrivee = x_arrivee 
        self.y_depart = y_depart
        self.x_depart = x_depart

        self.aller = True
        self.revenir = False
        self.nombre_frame = nb_frame
        self.active = False


        self.image = pygame.image.load("assets/prises/prise2_jaune.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (16, 16))
        self.rect = pygame.Rect(x_depart,y_depart,16,16)

    def update(self):
        if self.active == True :
            if self.aller:
                self.rect.x += self.x_chemin
                self.rect.y += self.y_chemin
                if self.x_arrivee == self.x_depart :
                    if 10 > abs(self.rect.y - self.y_arrivee):
                        self.aller = False
                elif self.y_arrivee == self.y_depart :
                    if 10 > abs(self.rect.x - self.x_arrivee):
                        self.aller = False
                elif 10 > abs(self.rect.x - self.x_arrivee) and 10 > abs(self.rect.y - self.y_arrivee) :
                    self.aller = False
            else : 
                    self.rect.x -= self.x_chemin
                    self.rect.y -= self.y_chemin
                    if self.x_arrivee == self.x_depart :
                        if 10 > abs(self.rect.y - self.y_depart):
                            self.aller = True
                            if self.revenir == True :
                                self.revenir = False
                                self.active = False
                    elif self.y_arrivee == self.y_depart :
                        if 10 > abs(self.rect.x - self.x_depart):
                            self.aller = True
                            if self.revenir == True :
                                self.revenir = False
                                self.active = False
                    elif 10 > abs(self.rect.x - self.x_depart) and 10 > abs(self.rect.y - self.y_depart) :
                        self.aller = True
                        if self.revenir == True :
                            self.revenir = False
                            self.active = False
                

    def draw(self, screen, scroll):
        screen.blit(self.image, (self.rect.x-scroll[0], self.rect.y-scroll[1]))
