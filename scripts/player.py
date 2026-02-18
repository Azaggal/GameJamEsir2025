import pygame
import copy
import math
import random

from game_config import GameConfig
from settings import Settings

from scripts.image import Images

from scripts.platforme import VitesseHorizontale, VitesseVerticale,PetitePrise,Catapulte


class Player(pygame.sprite.Sprite):

    def __init__(self,position = [0,0]):
        super().__init__()

        
        #___/Etats\___
        self.position = position
        self.velocity = [0,0]
        self.angle = 0
        self.vitesse_balancement = 0
        self.current_frame = 0
        self.f_b_jump = 0
        
        #___/Etats\___
        self.is_jumping = False
        self.is_moving_down = False
        self.is_moving_up = False
        self.is_moving_right = False
        self.is_moving_left = False
        self.f_b_jump = 0
        self.accroche = False
        self.etat_accrcoche = []
        self.accroche = True
        self.jump_animation = False


        self.boost_x = 1
        self.boost_y = 1

        self.f_b_stun = [0,None]

        self.boom = pygame.image.load("assets/others/BOOM.png") 
        self.boom = pygame.transform.scale(self.boom, (64, 64))
        self.boom_sound = pygame.mixer.Sound("assets/audio/boom.mp3")
        self.ecraser_sound = pygame.mixer.Sound("assets/audio/ecraser.mp3")

        
        #___/Rect et textures\___
        self.image = Images.load_player("assets/entities/player/perso_skin2.png", 256)[self.current_frame]
        self.rect = pygame.Rect(position[0], position[1], 10, 10)
        self.mask = pygame.mask.from_surface(self.image) 
        


    def collision_sprites(self, sprites_group):
        """
        Méthode qui teste les collisions
        """
        collisions = pygame.sprite.spritecollide(self, sprites_group, False)
        return collisions

    def collision_rect(self,list):
        collision = []
        for tile in list:
            if self.rect.colliderect(tile):
                collision.append(tile)
        return collision


    def draw(self, surface, scroll):
        """
        Méthode qui dessine le personnage sur une surface en fonction d'un scroll
        """

        pivot = (300 // 2, 100 // 2)
        image_offset = pygame.math.Vector2(30, 0)

        rotated_offset = image_offset.rotate(-self.angle+90)  # Rotation du vecteur autour du pivot
        rotated_position = (pivot[0] + rotated_offset.x, pivot[1] + rotated_offset.y)
        
        # Faire tourner l'image
        rotated_image = pygame.transform.rotate(self.image, self.angle)  # Pygame tourne dans le sens anti-horaire

        # Obtenir le nouveau rectangle de l'image après rotation
        rect = rotated_image.get_rect(center=rotated_position)

        # Dessiner l'image
        surface.blit(self.tint_red(rotated_image), (self.rect.x + rect.x- scroll[0] - 145,self.rect.y + rect.y - scroll[1] - 50))

        if len(self.etat_accrcoche) != 0 :
            if not isinstance(self.etat_accrcoche[0], PetitePrise):
                if isinstance(self.etat_accrcoche[0], Catapulte):
                    if self.etat_accrcoche[0].aller:
                        surface.blit(self.get_outline(rotated_image,self.etat_accrcoche[0].color),(self.rect.x + rect.x- scroll[0] - 145,self.rect.y + rect.y - scroll[1] - 50))
                else :
                    surface.blit(self.get_outline(rotated_image,self.etat_accrcoche[0].color),(self.rect.x + rect.x- scroll[0] - 145,self.rect.y + rect.y - scroll[1] - 50))

        
        # Pour le debug, on peut dessiner le rectangle (optionnel)
        #pygame.draw.rect(surface, (0, 255, 0), (self.rect.x - scroll[0], self.rect.y - scroll[1], 10, 10))
        #pygame.draw.rect(surface,(0,255,0),(self.rect.x - scroll[0],self.rect.y - scroll[1],10,10))
        if self.f_b_stun[0] != 0:
            self.shake_screen(surface, 3)
            surface.blit(self.boom, (self.f_b_stun[1].rect.x - scroll[0], self.f_b_stun[1].rect.y - scroll[1]))
            if self.f_b_stun[0] == 19 :
                self.boom_sound.play()
        


    def add_momentum(self, direction):
        if self.accroche:
            self.vitesse_balancement += direction * GameConfig.SWING_SPEED
            self.vitesse_balancement = max(min(self.vitesse_balancement, GameConfig.MAX_VELOCITY), -GameConfig.MAX_VELOCITY)

    def play_jump_animation(self):
        self.current_frame += 0.27
        if self.current_frame >= 2.9:
            self.current_frame = 0
            self.jump_animation = False
        self.image = Images.load_player("assets/entities/player/perso_skin2.png", 256)[int(self.current_frame)]

    def tint_red(self,surface):
        if self.f_b_poigne > 0 and 120 > self.f_b_poigne:
            tinted_surface = surface.copy()
            red_overlay = pygame.Surface(surface.get_size(),pygame.SRCALPHA)   
            red_overlay.fill((255, 255-(self.f_b_poigne*255/120), 255-(self.f_b_poigne*255/120)))  # Ajouter de la transparence avec alpha
            tinted_surface.blit(red_overlay, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
            return tinted_surface
        return surface

    def contact(self,liste_prise):
        liste = []
        for prise in liste_prise :
            if self.rect.colliderect(prise.rect):
                liste.append(prise)
        return liste
    

    

    def shake_screen(self,surface, intensity):
        offset_x = random.randint(-intensity, intensity)
        offset_y = random.randint(-intensity, intensity)
        surface.blit(surface, (offset_x, offset_y))
    
    
    def get_outline(self,image,color=(255,0,0)):
        """Returns an outlined image of the same size.  the image argument must
        either be a convert surface with a set colorkey, or a convert_alpha
        surface. color is the color which the outline will be drawn."""
        rect = image.get_rect()
        mask = pygame.mask.from_surface(image)
        outline = mask.outline()
        outline_image = pygame.Surface(rect.size).convert_alpha()
        outline_image.fill((0,0,0,0))
        for point in outline:
            outline_image.set_at(point,color)
        return outline_image
    

    def update(self,screen, collision_dict, fallingcharacter):
        """
        Fonction qui met à jour les états du joueur
        """
        if self.jump_animation == True:
            self.play_jump_animation()

        self.f_b_jump = max(self.f_b_jump-1,0)

        collision = self.collision_sprites(collision_dict["climbing_hole_map"])
        


        if len(collision) != 0 :
            if self.accroche == True:
                if collision[0].name == "tileset_8_7" :
                    self.f_b_poigne += 1

                if self.f_b_poigne >= 120 :
                    self.velocity[1] =  min(self.velocity[1]+GameConfig.GRAVITY_A_Y,8)
                    self.velocity[0] += self.angle/45


                if self.is_jumping and self.velocity[1] == 0:
                    self.jump_animation = True
                if self.current_frame == 1.62:
                    pygame.mixer.Sound("assets/audio/saut.mp3").play()
                    self.velocity[1] = -6 + abs(self.angle/20)
                    self.velocity[0] += self.angle/9
            else :
                pygame.mixer.Sound("assets/audio/reception.wav").play()
                self.f_b_poigne = 0
                self.velocity = [0,0]
                self.accroche = True
                self.rect.x = collision[0].rect.x + 3
                self.rect.y = collision[0].rect.y

        elif len(self.etat_accrcoche) != 0:
            if self.accroche == True:
                if self.f_b_poigne >= 120 :
                        self.velocity[1] = min(self.velocity[1]+GameConfig.GRAVITY_A_Y,8)
                        self.velocity[0] += self.angle/45

                if self.velocity[1] == 0 :
                    if isinstance(self.etat_accrcoche[0],PetitePrise) :
                        self.f_b_poigne += 1
                    elif isinstance(self.etat_accrcoche[0],VitesseHorizontale) :
                        self.boost_x = 2
                    elif isinstance(self.etat_accrcoche[0],VitesseVerticale) :
                        self.boost_y = 1.5
                    elif isinstance(self.etat_accrcoche[0],Catapulte) :
                        self.etat_accrcoche[0].active = True
                    if self.is_jumping : 
                    
                        self.jump_animation = True

                    if self.current_frame == 1.62:
                        pygame.mixer.Sound("assets/audio/saut.mp3").play()
                        if isinstance(self.etat_accrcoche[0],Catapulte) :
                            if self.etat_accrcoche[0].aller :
                                self.velocity[1] = -self.etat_accrcoche[0].velocite_y
                                self.velocity[0] = self.etat_accrcoche[0].velocite_x
                            else : 
                                self.velocity[1] = -6*self.boost_y + abs(self.angle/20)
                                self.velocity[0] += self.angle/9*self.boost_x
                            self.etat_accrcoche[0].revenir = True
                            
                        else :
                            self.velocity[1] = -6*self.boost_y + abs(self.angle/20)
                            self.velocity[0] += self.angle/9*self.boost_x
                    elif self.is_jumping : 
                        self.jump_animation = True
                    else :
                        self.rect.x = self.etat_accrcoche[0].rect.x + 3
                        self.rect.y = self.etat_accrcoche[0].rect.y

                    self.boost_x = 1
                    self.boost_y = 1
            else :
                pygame.mixer.Sound("assets/audio/reception_magie.wav").play()
                self.f_b_poigne = 0
                self.velocity = [0,0]
                self.accroche = True
                self.rect.x = self.etat_accrcoche[0].rect.x + 3
                self.rect.y = self.etat_accrcoche[0].rect.y
        else :
            self.f_b_poigne = 0
            self.accroche = False
            self.vitesse_balancement = 0
            self.velocity[1] =  min(self.velocity[1]+GameConfig.GRAVITY_A_Y,8)


        if self.accroche :
            acceleration = -GameConfig.SPRING_FORCE * self.angle
            self.vitesse_balancement += acceleration

            self.angle += self.vitesse_balancement
            if abs(self.angle) > GameConfig.MAX_ANGLE:
                self.angle = GameConfig.MAX_ANGLE * (self.angle / abs(self.angle))  # Limite l'angle

            # Gestion de l'élan


            # Atténuation naturelle du balancement
            self.vitesse_balancement *= 0.99
        


        if self.accroche == False:
            if self.is_moving_right :
                self.velocity[0] = min(self.velocity[0]+0.05,15)

            if self.is_moving_left :
                self.velocity[0] = max(self.velocity[0]-0.05,-15)

        


        #___/COLLISION AVEC FALLINGCHARACTER\___
        collision_character = self.collision_rect(fallingcharacter)
        if len(collision_character) != 0:
            if len(collision) != 0 :
                if not (collision[0].name == "tileset_5_7" or collision[0].name == "tileset_6_7" or collision[0].name == "tileset_7_7") :
                    self.etat_accrcoche = []
                    self.velocity[1] -= 1
                    self.velocity[0] -= 1
                    # Appliquer l'effet de tremblement
                    self.f_b_stun = [20, collision_character[0]]
                    
                    # Retirer le personnage qui a touché le joueur
                    fallingcharacter.remove(collision_character[0])
            else :
                if len(self.etat_accrcoche) != 0 :
                    self.etat_accrcoche[0].revenir = True
                    self.etat_accrcoche = []
                    self.f_b_poigne = 0
                self.velocity[1] += 15
                self.velocity[0] -= 1
                self.velocity[1] /= 5
                self.velocity[0] /= 5

                # Appliquer l'effet de tremblement
                self.f_b_stun = [20, collision_character[0]]

                
                # Retirer le personnage qui a touché le joueur
                fallingcharacter.remove(collision_character[0])

            
            
        self.f_b_stun[0] = max(self.f_b_stun[0]-1,0)

        self.rect.y += self.velocity[1] 
                   
        self.rect.x += self.velocity[0]

        if self.rect.x > 616 : 
            self.rect.x = 616
            self.velocity[0] = 0        
        elif 16 > self.rect.x : 
            self.rect.x = 16
            self.velocity[0] = 0

        self.position = [self.rect.x, self.rect.y]



