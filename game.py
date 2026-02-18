import subprocess
import sys

try:
    import pygame
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pygame"])
    import pygame


import pygame
import sys

from game_state import GameState
from menu_state import MenuState

from scripts.son import Musique
from settings import Settings



class Game():
    def __init__(self):
        Settings.init()
        self.clock = pygame.time.Clock()
        self.display = pygame.display.set_mode(Settings.DISPLAY_RESOLUTION, pygame.FULLSCREEN if Settings.FULLSCREEN else 1)
        self.current_state = "menu"
        self.menu_state = MenuState(self.display,self)
        self.musique = Musique("assets/audio/bg_music.mp3")
        if not Settings.MUSIQUE:
            self.musique.pause()    

        self.start_time = pygame.time.get_ticks()
        self.current_time =  pygame.time.get_ticks() - self.start_time
    
        #Premier fondu
        self.logo_gamejam = pygame.image.load("assets/others/logo_gamejam.png")
        self.premier_fondu = False
        self.fondu_finished = False
        
    def launch(self):
        # Affichage du logo pendant 2 secondes
        logo_scaled = pygame.transform.scale(self.logo_gamejam, (self.logo_gamejam.get_width() // 5, self.logo_gamejam.get_height() // 5))
        logo_position = (Settings.DISPLAY_RESOLUTION[0] // 2 - logo_scaled.get_width() // 2,Settings.DISPLAY_RESOLUTION[1] // 2 - logo_scaled.get_height() // 2)
        start_time = pygame.time.get_ticks()
        while pygame.time.get_ticks() - start_time < 2000:
            self.display.fill((0, 0, 0))
            self.display.blit(logo_scaled, logo_position)
            self.events()
            self.render()

        fade_duration = 1000
        fade_start = pygame.time.get_ticks()
        while True:
            elapsed = pygame.time.get_ticks() - fade_start
            if elapsed > fade_duration: 
                break
            alpha = int((elapsed / fade_duration) * 255)
            self.display.fill((0, 0, 0))
            self.display.blit(logo_scaled, logo_position)
            fade_surface = pygame.Surface(Settings.DISPLAY_RESOLUTION)
            fade_surface.fill((0, 0, 0))
            fade_surface.set_alpha(alpha)
            self.display.blit(fade_surface, (0, 0))

            self.events()
            self.render()

        # On passe ensuite au jeu
        self.launch_session()

    def launch_session(self):
        """
        Permet de lancer le jeu
        """
        self.game_state = GameState(self.display,self)
        self.game_state.initialize_game("intro")
        self.game_loop()
        

    def game_loop(self):
        """
        Permet de gérer les différentes boucles du jeu
        """
        run = True
        while run:
            if self.current_state == "game":
                self.game_state.main_loop()
            elif self.current_state == "menu":
                self.menu_state.main_loop()
            
    def render(self):
        """
        Méthode qui gère le rendu du display
        """
        pygame.display.flip()
        self.clock.tick(Settings.GAME_FPS)

    def events(self):
        """
        Gére les évenements
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


if __name__ == "__main__":
    pygame.init()
    pygame.joystick.init()
    game = Game()
    game.launch()
    


