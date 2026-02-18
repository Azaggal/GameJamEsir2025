import pygame

class MenuConfig:
    BACKGROUND_COLOR = (232,220,202)
    def init():
        

        #___/JOUER\____
        MenuConfig.JOUER_STILL = pygame.image.load("assets/buttons/jeu_buttons/jouer/jouer_still.png").convert_alpha()
        MenuConfig.JOUER_PRESSED = pygame.image.load("assets/buttons/jeu_buttons/jouer/jouer_pressed.png").convert_alpha()

        #___/REPRENDRE\____
        MenuConfig.REPRENDRE_STILL = pygame.image.load("assets/buttons/jeu_buttons/reprendre/reprendre_still.png").convert_alpha()
        MenuConfig.REPRENDRE_PRESSED = pygame.image.load("assets/buttons/jeu_buttons/reprendre/reprendre_pressed.png").convert_alpha()

        #___/QUITTER\____
        MenuConfig.QUITTER_STILL = pygame.image.load("assets/buttons/jeu_buttons/quitter/quitter_still.png").convert_alpha()
        MenuConfig.QUITTER_PRESSED = pygame.image.load("assets/buttons/jeu_buttons/quitter/quitter_pressed.png").convert_alpha()
        
        #___/OPTIONS\____
        MenuConfig.OPTIONS_STILL = pygame.image.load("assets/buttons/jeu_buttons/options/options_still.png").convert_alpha()
        MenuConfig.OPTIONS_PRESSED = pygame.image.load("assets/buttons/jeu_buttons/options/options_pressed.png").convert_alpha()

        #___/MENU PRINCIPAL\____
        MenuConfig.MENU_PRINCIPAL_STILL = pygame.image.load("assets/buttons/jeu_buttons/menu_principal/menu_principal_still.png").convert_alpha()
        MenuConfig.MENU_PRINCIPAL_PRESSED = pygame.image.load("assets/buttons/jeu_buttons/menu_principal/menu_principal_pressed.png").convert_alpha()

        #___/RETOUR\____
        MenuConfig.RETOUR_STILL = pygame.image.load("assets/buttons/jeu_buttons/retour/retour_still.png").convert_alpha()
        MenuConfig.RETOUR_PRESSED = pygame.image.load("assets/buttons/jeu_buttons/retour/retour_pressed.png").convert_alpha()

        #___/CREDIT\____
        MenuConfig.CREDITS_STILL = pygame.image.load("assets/buttons/jeu_buttons/credits/credits_still.png").convert_alpha()
        MenuConfig.CREDITS_PRESSED = pygame.image.load("assets/buttons/jeu_buttons/credits/credits_pressed.png").convert_alpha()
        
        #___/CONTROL\____
        MenuConfig.CONTROL_STILL = pygame.image.load("assets/buttons/jeu_buttons/control/control_still.png").convert_alpha()
        MenuConfig.CONTROL_PRESSED = pygame.image.load("assets/buttons/jeu_buttons/control/control_pressed.png").convert_alpha()

        #___/VOLUME\____
        MenuConfig.VOLUME = pygame.image.load("assets/texts/volume.png").convert_alpha()

        #___/FLECHE\____
        MenuConfig.FLECHE_DROITE_PRESSED = pygame.transform.flip(pygame.image.load("assets/buttons/jeu_buttons/fleche/fleche_pressed.png").convert_alpha(),  True, False)
        MenuConfig.FLECHE_DROITE_STILL = pygame.transform.flip(pygame.image.load("assets/buttons/jeu_buttons/fleche/fleche_still.png").convert_alpha(),  True, False)
        
        MenuConfig.FLECHE_GAUCHE_PRESSED = pygame.image.load("assets/buttons/jeu_buttons/fleche/fleche_pressed.png").convert_alpha()
        MenuConfig.FLECHE_GAUCHE_STILL = pygame.image.load("assets/buttons/jeu_buttons/fleche/fleche_still.png").convert_alpha()
  
        #___/MUSIQUE\___
        MenuConfig.ON_MUSIQUE_PRESSED = pygame.image.load("assets/buttons/jeu_buttons/musique/on_musique_pressed.png").convert_alpha()
        MenuConfig.OFF_MUSIQUE_PRESSED = pygame.image.load("assets/buttons/jeu_buttons/musique/off_musique_pressed.png").convert_alpha()
        MenuConfig.ON_MUSIQUE_STILL = pygame.image.load("assets/buttons/jeu_buttons/musique/on_musique_still.png").convert_alpha()
        MenuConfig.OFF_MUSIQUE_STILL = pygame.image.load("assets/buttons/jeu_buttons/musique/off_musique_still.png").convert_alpha()

        #___/PLEINE ECRAN\___
        MenuConfig.ON_PLEINE_ECRAN_PRESSED = pygame.image.load("assets/buttons/jeu_buttons/pleine_ecran/on_pleine_ecran_pressed.png").convert_alpha()
        MenuConfig.OFF_PLEINE_ECRAN_PRESSED = pygame.image.load("assets/buttons/jeu_buttons/pleine_ecran/off_pleine_ecran_pressed.png").convert_alpha()
        MenuConfig.ON_PLEINE_ECRAN_STILL = pygame.image.load("assets/buttons/jeu_buttons/pleine_ecran/on_pleine_ecran_still.png").convert_alpha()
        MenuConfig.OFF_PLEINE_ECRAN_STILL = pygame.image.load("assets/buttons/jeu_buttons/pleine_ecran/off_pleine_ecran_still.png").convert_alpha()

        #___/XBOX\___
        MenuConfig.XBOX_CONTROLLER = pygame.image.load("assets/others/xbox_controller.png")
        MenuConfig.KEYBOARD_CONTROLLER = pygame.image.load("assets/others/clavier_control.png")

        #___/XBOX\___
        MenuConfig.CREDIT = pygame.image.load("assets/others/credit.png")

        #__/LOGO\____
        MenuConfig.LOGO = pygame.image.load("assets/others/logo.png")
