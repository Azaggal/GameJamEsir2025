import pygame
import random
import sys

from scripts.button import Button, ToggleButton
from scripts.image import Images
from scripts.tile import Tile

from menu_config import MenuConfig
from settings import Settings


class MenuState():

    def __init__(self, display,parent):
        MenuConfig.init()
        self.parent = parent
        self.display = display
        self.screen = pygame.Surface(Settings.SCREEN_RESOLUTION,pygame.SRCALPHA)
        self.clock = pygame.time.Clock()
        
        
        self.current_menu = "principal"
        self.previous_menu = "principal"

        screen_center_x = Settings.SCREEN_RESOLUTION[0]//2
        #___/Boutons Menu Principal\___
        self.menu_principal_buttons = pygame.sprite.Group()
        self.menu_principal_buttons.add(Button(screen_center_x,75,lambda: self.apply_button_action("jouer_button"),MenuConfig.JOUER_STILL,image_pressed=MenuConfig.JOUER_PRESSED,scale_factor=0.75,center=True,play_sound=True))
        self.menu_principal_buttons.add(Button(screen_center_x,110,lambda: self.apply_button_action("options_button"),MenuConfig.OPTIONS_STILL,image_pressed=MenuConfig.OPTIONS_PRESSED,scale_factor=0.75,center=True,play_sound=True))
        self.menu_principal_buttons.add(Button(screen_center_x,145,lambda: self.apply_button_action("credits_button"),MenuConfig.CREDITS_STILL,image_pressed=MenuConfig.CREDITS_PRESSED,scale_factor=0.75,center=True,play_sound=True))
        self.menu_principal_buttons.add(Button(screen_center_x,180,lambda: self.apply_button_action("control_button"),MenuConfig.CONTROL_STILL,image_pressed=MenuConfig.CONTROL_PRESSED,scale_factor=0.75,center=True,play_sound=True))
        self.menu_principal_buttons.add(Button(screen_center_x,215,lambda: self.apply_button_action("quitter_button"),MenuConfig.QUITTER_STILL,image_pressed=MenuConfig.QUITTER_PRESSED,scale_factor=0.75,center=True,play_sound=True))
        
        
        #___/Boutons Pause\___
        self.pause_buttons = pygame.sprite.Group()
        self.pause_buttons.add(Button(screen_center_x,24,lambda: self.apply_button_action("reprendre_button"),MenuConfig.REPRENDRE_STILL,image_pressed=MenuConfig.REPRENDRE_PRESSED,scale_factor=0.7,center=True,play_sound=True))
        self.pause_buttons.add(Button(screen_center_x,60,lambda: self.apply_button_action("options_button"),MenuConfig.OPTIONS_STILL,image_pressed=MenuConfig.OPTIONS_PRESSED,scale_factor=0.7,center=True,play_sound=True))
        self.pause_buttons.add(Button(screen_center_x,96,lambda: self.apply_button_action("menu_principal_button"),MenuConfig.MENU_PRINCIPAL_STILL,image_pressed=MenuConfig.MENU_PRINCIPAL_PRESSED,scale_factor=0.7,center=True,play_sound=True))

        #___/Boutons Credits\___
        self.credits_buttons = pygame.sprite.Group()
        self.credits_buttons.add(Button(8,8,lambda: self.apply_button_action("retour_button"),MenuConfig.RETOUR_STILL,image_pressed=MenuConfig.RETOUR_PRESSED,scale_factor=0.7,play_sound=True))

        #___/Boutons Options\___
        self.options_buttons = pygame.sprite.Group()
        self.options_buttons.add(Button(8,8,lambda: self.apply_button_action("retour_button"),MenuConfig.RETOUR_STILL,image_pressed=MenuConfig.RETOUR_PRESSED,scale_factor=0.7,play_sound=True))
        self.options_buttons.add(ToggleButton(screen_center_x,65,lambda: self.apply_button_action("musique"), MenuConfig.OFF_MUSIQUE_STILL,MenuConfig.ON_MUSIQUE_STILL,image_clicked_not_pressed=MenuConfig.OFF_MUSIQUE_PRESSED, image_clicked_pressed=MenuConfig.ON_MUSIQUE_PRESSED,scale_factor=0.9,center=True, pressed_by_default=Settings.MUSIQUE,play_sound=True))
        self.options_buttons.add(ToggleButton(screen_center_x,101,lambda: self.apply_button_action("fullscreen"), MenuConfig.OFF_PLEINE_ECRAN_STILL,MenuConfig.ON_PLEINE_ECRAN_STILL,image_clicked_not_pressed=MenuConfig.OFF_PLEINE_ECRAN_PRESSED, image_clicked_pressed=MenuConfig.ON_PLEINE_ECRAN_PRESSED,scale_factor=0.9,center=True, pressed_by_default=Settings.FULLSCREEN,play_sound=True))
        self.options_buttons.add(Button(screen_center_x + 32,173,lambda: self.apply_button_action("volume_plus"),MenuConfig.FLECHE_DROITE_STILL,image_pressed=MenuConfig.FLECHE_DROITE_PRESSED,scale_factor=1.5,center=True,play_sound=True))
        self.options_buttons.add(Button(screen_center_x - 32,173,lambda: self.apply_button_action("volume_moins"),MenuConfig.FLECHE_GAUCHE_STILL,image_pressed=MenuConfig.FLECHE_GAUCHE_PRESSED,scale_factor=1.5,center=True,play_sound=True))
       

        #___/Boutons Options\___
        self.control_buttons = pygame.sprite.Group()
        self.control_buttons.add(Button(8,8,lambda: self.apply_button_action("retour_button"),MenuConfig.RETOUR_STILL,image_pressed=MenuConfig.RETOUR_PRESSED,scale_factor=0.7,play_sound=True))
        


        #___/Initialisation prise\___
        self.prises = self.initialize_prises(10)
        self.falling_character = [Images.extract_animation_line_from_sheet("assets/entities/fallingcharacter/character_sheet.png",0,4,64,64),
                                  Images.extract_animation_line_from_sheet("assets/entities/fallingcharacter/character_sheet.png",1,4,64,64),
                                  Images.extract_animation_line_from_sheet("assets/entities/fallingcharacter/character_sheet.png",2,4,64,64),
                                  Images.extract_animation_line_from_sheet("assets/entities/fallingcharacter/character_sheet.png",3,4,64,64)]
        
        self.falling = {"falling" : False , "position" : [0,0] , "animations" : [], "frame" : 0}

    def events(self):
        """
        Gére les évenements
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                pygame.quit()

                


    def apply_button_action(self,bouton):
        """
        Fonction qui gère les différentes actions des boutons
        """
        if bouton == "jouer_button":
            self.parent.current_state = "game"
            self.current_menu = "pause"
            self.parent.launch_session()
        elif bouton == "reprendre_button":
            self.parent.current_state = "game"
            self.previous_menu = self.current_menu
            self.current_menu = "pause"

        elif bouton == "menu_principal_button":
            self.current_menu = "principal"

        elif bouton == "quitter_button":
            sys.exit()
            pygame.quit()


        elif bouton == "options_button":
            self.previous_menu = self.current_menu
            self.current_menu = "options"

        elif bouton == "control_button":
            self.previous_menu = self.current_menu
            self.current_menu = "control"

        elif bouton == "credits_button":
            self.previous_menu = self.current_menu
            self.current_menu = "credits"

        elif bouton == "retour_button":
            temp = self.current_menu
            self.current_menu = self.previous_menu
            self.previous_menu = temp

        elif bouton == "musique":
            Settings.change_musique()
            if Settings.MUSIQUE:
                self.parent.musique.resume()
            else:
                self.parent.musique.pause()

        elif bouton == "fullscreen":
            Settings.change_full_screen()
            self.parent.display = pygame.display.set_mode(Settings.DISPLAY_RESOLUTION, pygame.FULLSCREEN if Settings.FULLSCREEN else 1)

        elif bouton == "volume_moins":
            Settings.lower_musique_volume()
            self.parent.musique.volume(Settings.VOLUME)

        elif bouton == "volume_plus":
            Settings.higher_musique_volume()
            self.parent.musique.volume(Settings.VOLUME)

    def initialize_prises(self,n):
        prises = []
        tileset = Images.extract_tiles("assets/maps/intro/textures/tiles/tileset.png")
        used_positions = []
        for _ in range(n):
            random_prise = f"tileset_{random.randint(0,4)}_{random.randint(7,9)}"
            position_ok = False
            while not position_ok:
                x = random.randint(0, 6) * 16
                y = random.randint(0, 16) * 16
                if (x, y) not in used_positions:
                    used_positions.append((x, y))
                    position_ok = True
            prises.append(Tile(random_prise, x, y, tileset[random_prise]))
            
            random_prise = f"tileset_{random.randint(0,4)}_{random.randint(7,9)}"
            position_ok = False
            while not position_ok:
                x = random.randint(19, 25) * 16
                y = random.randint(0, 16) * 16
                if (x, y) not in used_positions:
                    used_positions.append((x, y))
                    position_ok = True
            prises.append(Tile(random_prise, x, y, tileset[random_prise]))

            
        return prises

    def random_falling_character(self):
        if random.randint(0,200) == 1 and not self.falling["falling"]:
            print("true")
            self.falling["falling"] = True
            if random.randint(0,1) == 0:
                self.falling["position"] = [random.randint(0,15)*16,-64]
            else:
                self.falling["position"] = [random.randint(20,24)*16,-64]
            self.falling["animation"] = self.falling_character[random.randint(0,3)]
            self.falling["frame"] = 0
        
        elif self.falling["falling"]:
            self.falling["frame"] += 0.08
            if self.falling["frame"] > 3:
                self.falling["frame"] = 0
            self.falling["position"][1] += 3
            self.screen.blit(self.falling["animation"][int(self.falling["frame"])],self.falling["position"])
            if self.falling["position"][1] > Settings.SCREEN_RESOLUTION[1] + 64:
                self.falling = {"falling" : False , "position" : [0,0] , "animations" : [], "frame" : 0}



    def draw_prises(self):
        for prise in self.prises:
            prise.draw(self.screen,[0,0])


    def draw(self):
        #___/Screen\___
        self.screen.fill(MenuConfig.BACKGROUND_COLOR)
        if self.current_menu == "principal":
            self.menu_principal_buttons.draw(self.screen)
            self.draw_prises()
        elif self.current_menu == "pause":
            self.pause_buttons.draw(self.screen)
        elif self.current_menu == "options":
            volume_bouton = pygame.transform.scale(MenuConfig.VOLUME, (int(MenuConfig.VOLUME.get_width() * 0.9), int(MenuConfig.VOLUME.get_height() * 0.9)))
            x_center = Settings.SCREEN_RESOLUTION[0]//2 - volume_bouton.get_width()//2
            self.screen.blit(volume_bouton, (x_center,105 + volume_bouton.get_height()//2))

            numbers = pygame.image.load("assets/texts/chiffres.png")
            rect = pygame.Rect(int(Settings.VOLUME*10-1)*32, 0, 32, 32)
            number = numbers.subsurface(rect)
            x_center = Settings.SCREEN_RESOLUTION[0]//2 - number.get_width()//2
            self.screen.blit(number, (x_center,141 + number.get_height()//2))

            self.options_buttons.draw(self.screen)
        elif self.current_menu == "credits":
            self.credits_buttons.draw(self.screen)
            self.display.blit(MenuConfig.CREDIT,(0,0))


        elif self.current_menu == "control":
            self.screen.blit(pygame.transform.scale(MenuConfig.XBOX_CONTROLLER,(MenuConfig.XBOX_CONTROLLER.get_width()//1.5,MenuConfig.XBOX_CONTROLLER.get_height()//1.5)),(5,110))
            self.screen.blit(pygame.transform.scale(MenuConfig.KEYBOARD_CONTROLLER,(MenuConfig.KEYBOARD_CONTROLLER.get_width()//1.3,MenuConfig.KEYBOARD_CONTROLLER.get_height()//1.3)),(180,35))
            self.control_buttons.draw(self.screen)

        self.random_falling_character()
        self.display.blit(pygame.transform.scale(self.screen, Settings.DISPLAY_RESOLUTION), (0,0))
        
        #___/Dispaly\___
        
        if self.current_menu == "credits":
            self.display.blit(pygame.transform.scale(MenuConfig.CREDIT,(MenuConfig.CREDIT.get_width() *1.7,MenuConfig.CREDIT.get_height() *1.7)),(Settings.DISPLAY_RESOLUTION[0] // 2 - (MenuConfig.CREDIT.get_width() *1.7 )//2,140))
        
        elif self.current_menu == "principal":
            self.display.blit(pygame.transform.scale(MenuConfig.LOGO,(MenuConfig.LOGO.get_width() *1,MenuConfig.LOGO.get_height() *1)),(Settings.DISPLAY_RESOLUTION[0] // 2 - (MenuConfig.LOGO.get_width() *1 )//2,10))
        
        pygame.display.flip()
        self.clock.tick(Settings.GAME_FPS)




        


    def main_loop(self):
        """
        Loop principale qui gère les différents menus
        """
        if self.current_menu == "principal":
            self.menu_principal_loop()
        elif self.current_menu == "pause":
            self.pause_loop()
        elif self.current_menu == "options":
            self.options_loop()
        elif self.current_menu == "credits":
            self.credits_loop()
        elif self.current_menu == "control":
            self.control_loop()

    def control_loop(self):
        self.events()
        self.control_buttons.update()
        self.draw()


    def options_loop(self):
        self.events()
        self.options_buttons.update()
        self.draw()

    
    def credits_loop(self):
        self.events()
        self.credits_buttons.update()
        self.draw()



    def pause_loop(self):
        self.events()
        self.pause_buttons.update()
        self.draw()


    def menu_principal_loop(self):
        self.events()
        
        self.draw()
        self.menu_principal_buttons.update()
        

        