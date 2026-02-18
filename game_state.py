import pygame
import sys

from game_config import GameConfig
from settings import Settings

from scripts.player import Player
from scripts.map import Map
from scripts.platforme import Platforme,Deplacement, VitesseHorizontale, VitesseVerticale, Catapulte, PetitePrise
from scripts.fallingcharacter import FallingCharacter
from scripts.text import Text



class GameState():

    def __init__(self, display,parent):
        
        #___/Initialisation du parent\___
        self.parent = parent


        #___/Initialisation de pygame\___
        self.display = display
        self.screen = pygame.Surface(Settings.SCREEN_RESOLUTION)
        self.clock = pygame.time.Clock()
        self.map = Map()

        self.progression_icon = pygame.image.load("assets/others/barre.png") 
        self.progression_barre = pygame.image.load("assets/others/icon.png") 

        #___/Initialisation des états\___
        self.current_state = "playing"

        #___/Initialisation des sprites\___
        self.player = Player()
        self.liste_platforme = []
        self.falling_character = []

        #___/Initialisation des attributs\___
        self.scroll =  [0,0]
        
        #___/Initialisation du timer\___
        self.finish_time = 0

        self.falling_timer = pygame.time.get_ticks()     

        #___/Initialisation des joysticks\___
        self.joysticks = []
        for i in range(pygame.joystick.get_count()):
            joystick = pygame.joystick.Joystick(i)
            joystick.init()
            self.joysticks.append(joystick)



 
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            # event clavier/souris
            if event.type == pygame.KEYDOWN:
                #Touche  Q, D (Déplacement)
                if event.key == pygame.K_q or event.key == pygame.K_LEFT:
                    self.player.add_momentum(-1)
                    self.player.is_moving_left = True
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    self.player.add_momentum(1)
                    self.player.is_moving_right = True
                
                #Touche ESPACE (Saut)
                if event.key == pygame.K_SPACE:
                    self.player.is_jumping = True

                #Touche ECHAP (Escape)
                if event.key == pygame.K_ESCAPE:
                    self.parent.current_state = "menu"
                    self.player.is_moving_left = False
                    self.player.is_moving_right = False
                    self.player.is_moving_up = False
                    self.player.is_moving_down = False
                    self.player.is_jumping = False

                
            if event.type == pygame.KEYUP:
                #Touche  Q, D (Déplacement)
                if event.key == pygame.K_q or event.key == pygame.K_LEFT:
                    self.player.is_moving_left = False
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    self.player.is_moving_right = False

                #Touche ESPACE (Saut)
                if event.key == pygame.K_SPACE:
                    self.player.is_jumping = False

            # Événements manette
            if event.type == pygame.JOYAXISMOTION:
                # Axe 0 = gauche/droite, Axe 1 = haut/bas
                if event.axis == 0:  # Gauche/Droite
                    if event.value < -0.5:
                        self.player.add_momentum(-1)
                        self.player.is_moving_left = True
                    else:
                        self.player.is_moving_left = False
                    if event.value > 0.5:
                        self.player.add_momentum(1)
                        self.player.is_moving_right = True
                 
                    else :
                        self.player.is_moving_right = False
                        

            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 0: # A sur manette XBOX
                    self.player.is_jumping = True

            if event.type == pygame.JOYBUTTONUP:
                if event.button == 0:
                    self.player.is_jumping = False


    ################################
    ###        INIT PART         ###
    ################################


    def initialize_game(self,map_name):
        """
        Méthode qui permet d'initialiser une partie
        """
        self.load_map(map_name) #On charge la carte
        self.spawn_player() #On fait appaitre le joueur
        self.set_scroll_to_spawn() #On met le scroll au spawn
        self.platformes = Platforme()
        self.platformes.liste = [VitesseVerticale(560,4192,(0,255,0)),VitesseVerticale(576,3952,(0,255,0)),VitesseVerticale(368 ,3712,(0,255,0)),VitesseVerticale(256 ,3664,(0,255,0)),VitesseVerticale(64, 3648,(0,255,0)),VitesseVerticale(80, 3536,(0,255,0))
                                 ,VitesseVerticale(64, 3440,(0,255,0)),VitesseVerticale(80, 3344,(0,255,0)),VitesseVerticale(16, 2400,(0,255,0)),VitesseVerticale(64, 3248,(0,255,0)),

                                 PetitePrise(112, 4688,(255,0,0)),PetitePrise(400, 4656,(255,0,0)),PetitePrise(528, 4608,(255,0,0)),PetitePrise(544, 4560,(255,0,0)),PetitePrise(520, 4512,(255,0,0)),
                                 PetitePrise(400, 4464,(255,0,0)),PetitePrise(208, 4496,(255,0,0)),PetitePrise(160, 4496,(255,0,0)),PetitePrise(112, 4448,(255,0,0)),PetitePrise(64, 4400,(255,0,0)),
                                 PetitePrise(272, 4272,(255,0,0)),PetitePrise(512, 4240,(255,0,0)),
                                 
                                 VitesseHorizontale(496, 2432,(0,0,255)),VitesseHorizontale(176, 2384,(0,0,255)),VitesseHorizontale(112, 2304,(0,0,255)),VitesseHorizontale(416, 2272,(0,0,255)),VitesseHorizontale(512, 2128,(0,0,255)),
                                 VitesseHorizontale(368, 2160,(0,0,255)),VitesseHorizontale(224, 2192,(0,0,255)),
                                 
                                 Deplacement(432, 3070,432, 2860,100,(255,0,255),0),
                                 Deplacement(560, 2752,416,2752,100,(255,0,255),0),
                                 Deplacement(400, 2752,250, 2752,100,(255,0,255),0),
                                 Deplacement(64, 2720,350, 2550,100,(255,0,255),1),
                                 Deplacement(560, 2304,560, 2144,100,(255,0,255),0),
                                                                                                                                                                                                                                           
                                 Catapulte(80, 2176, 80,2016, 100,0,10,(255,255,0)),Catapulte(96, 1904, 96, 1760, 100,0,10,(255,255,0)),Catapulte(80, 1584, 80, 1376, 100,0,10,(255,255,0)),Catapulte(96, 1232, 96, 976, 100,0,10,(255,255,0)),Catapulte(112, 816, 112, 256, 200,0,10,(255,255,0))]

        self.pan_vert = pygame.image.load("assets/others/pan_vert.png") 
        self.pan_vert = pygame.transform.scale(self.pan_vert, (64, 128))

        self.pan_rouge = pygame.image.load("assets/others/pan_rouge.png") 
        self.pan_rouge = pygame.transform.scale(self.pan_rouge, (96, 48))
        
        self.pan_jaune = pygame.image.load("assets/others/pan_jaune.png") 
        self.pan_jaune = pygame.transform.scale(self.pan_jaune, (64, 128))

        self.pan_bleu = pygame.image.load("assets/others/pan_bleu.png") 
        self.pan_bleu = pygame.transform.scale(self.pan_bleu, (64, 128))

        self.pan_violet = pygame.image.load("assets/others/pan_violet.png") 
        self.pan_violet = pygame.transform.scale(self.pan_violet, (128, 64))
    ##################################
    ###        UPDATE PART         ###
    ##################################


    def load_map(self, map_name):
        """
        Méthode qui permet de charger une carte
        """
        self.map.load(map_name)
        


    def spawn_player(self):
        """
        Méthode qui permet de faire spawn le joueur (Créer un nouveau joueur)
        """
        self.player = Player([self.map.spawn[0] * Settings.TILE_SIZE,self.map.spawn[1] * Settings.TILE_SIZE])
        
        


    def set_scroll_to_spawn(self):
        """
        Méthode qui permet de mettre la caméra au point de spawn
        """
        self.scroll = [self.map.spawn[0]* Settings.TILE_SIZE - Settings.SCREEN_RESOLUTION[0]//2, self.map.spawn[1]* Settings.TILE_SIZE- Settings.SCREEN_RESOLUTION[1]//2]


    
    def update_scroll(self,coord_x,coord_y):
        """
        Méthode qui met à jour le scroll de la caméra
        """
        screen_x_center = Settings.SCREEN_RESOLUTION[0]//2
        self.scroll[0] += ((coord_x - screen_x_center - self.scroll[0]) / GameConfig.SCROLLING_SMOOTHNESS) * int(GameConfig.X_SCROLLING)


        screen_y_center = Settings.SCREEN_RESOLUTION[1]//2
        self.scroll[1] += ((coord_y - screen_y_center - self.scroll[1]) / GameConfig.SCROLLING_SMOOTHNESS) * int(GameConfig.Y_SCROLLING)


    #################################
    ###        STATE PART         ###
    #################################


    def score(self):
        hauteur_max = self.map.size["height"]*16
        pos_player = self.player.position[1]
        score = int(round((hauteur_max - pos_player)/hauteur_max *100))
        return score





    ################################
    ###        DRAW PART         ###
    ################################
 


    def draw(self):
        self.screen.fill(GameConfig.BACKGROUND_COLOR)
        self.map.draw_tile(self.screen, self.scroll, player=self.player)

        # self.screen.blit(self.progression_icon, self.avancee_barre, -20)
        # self.screen.blit(self.progression_barre, 100, -20)

        self.platformes.draw(self.screen, self.scroll)
        self.screen.blit(self.pan_bleu, (480 - self.scroll[0], 2464- self.scroll[1]))
        self.screen.blit(self.pan_rouge, (144 - self.scroll[0], 4646- self.scroll[1]))
        self.screen.blit(self.pan_violet, (400 - self.scroll[0], 3070- self.scroll[1]))
        self.screen.blit(self.pan_vert, (560 - self.scroll[0], 4170- self.scroll[1]))
        self.screen.blit(self.pan_jaune, (80 - self.scroll[0], 2144- self.scroll[1]))
        self.player.draw(self.screen, self.scroll)
        self.draw_falling_character()
        Text.draw_text(self.screen, str(self.score())+"%", 15, (Settings.SCREEN_RESOLUTION[0]//2, 10), (0, 0, 0), "assets/fonts/gamebubble/Game Bubble.ttf",True)
        


    def avance_barre(self):
        self.avancee_barre = 100 + (self.player.position[0]/(self.map.size['width']*16))*400
        
    def draw_falling_character(self):
        for character in self.falling_character:
            character.draw(self.screen,self.scroll)

    def spawn_falling_character(self):
        self.current_time = pygame.time.get_ticks() - self.falling_timer

        interval = 12000 - ((self.score() / 100) * 10000)
        if self.current_time > interval:
            self.falling_character.append(FallingCharacter(
                [self.player.position[0], self.player.position[1] - Settings.SCREEN_RESOLUTION[1]],
                2, 
                2000
            ))
            self.falling_timer = pygame.time.get_ticks()

    def update_falling_character(self):
        for character in self.falling_character:
            if character.position[1] < self.map.size["height"] * 16:
                character.update(self.player.position)
            else:
                self.falling_character.remove(character)


    def render(self):
        """
        Méthode qui gère le rendu du display
        """
        self.display.blit(pygame.transform.scale(self.screen, Settings.DISPLAY_RESOLUTION), (0, 0))
        pygame.display.flip()
        self.clock.tick(Settings.GAME_FPS)


    def main_loop(self):
        self.game_loop()


    def game_loop(self):
        self.events()

        #__/Update\__
        self.update_scroll(self.player.position[0],self.player.position[1])
        self.platformes.update()
        self.player.update(self.screen, self.map.collision_dict, self.falling_character)
        self.update_falling_character()
        self.avance_barre()
        
        #__/Prise\___
        prise = self.player.contact(self.platformes.liste)
        self.player.etat_accrcoche = []
        if len(prise) != 0:
            self.player.etat_accrcoche = prise
        self.spawn_falling_character()
                
        self.draw()
        self.render()

