import pygame

class Musique:
    def __init__(self, music_path="assets/audio/bg_music.mp3"):
        pygame.mixer.init()

        self.music = music_path

        # Chargement et lecture de la musique
        pygame.mixer.music.load(self.music)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1) 

    def stop(self):
        pygame.mixer.music.stop()

    def pause(self):
        pygame.mixer.music.pause()

    def resume(self):
        pygame.mixer.music.unpause()

    def volume(self, n):
        pygame.mixer.music.set_volume(n)
