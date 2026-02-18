
from scripts.map import File

class Settings():
    def init():

        #___/Configuration modifiable par le joueur\___
        #La configuration modifiable par le joueur est contenue dans "settings.json"
        settings_data = File.import_json("settings.json")
        for setting,value in settings_data.items():
            if setting == "display_resolution":
                Settings.DISPLAY_RESOLUTION = value
            elif setting == "fullscreen":
                Settings.FULLSCREEN = value
            elif setting == "musique":
                Settings.MUSIQUE = value
            elif setting == "volume":
                Settings.VOLUME = value
    
        #___/Configuration inmodifiable par le joueur\___
        Settings.SCREEN_SCALE = Settings.DISPLAY_RESOLUTION[0] // 400
        Settings.SCREEN_RESOLUTION = [x // Settings.SCREEN_SCALE for x in Settings.DISPLAY_RESOLUTION]
        Settings.TILE_SIZE = 16
        Settings.GAME_FPS = 60
        
    
    def change_full_screen():
        Settings.FULLSCREEN = not Settings.FULLSCREEN
        data = File.import_json("settings.json")
        data["fullscreen"] = Settings.FULLSCREEN
        File.export_json("settings.json",data)

    def change_musique():
        Settings.MUSIQUE = not Settings.MUSIQUE
        data = File.import_json("settings.json")
        data["musique"] = Settings.MUSIQUE
        File.export_json("settings.json",data)

    def lower_musique_volume():
        Settings.VOLUME = max(Settings.VOLUME - 0.1,0.1)
        data = File.import_json("settings.json")
        data["volume"] = Settings.VOLUME
        File.export_json("settings.json",data)

    def higher_musique_volume():
        Settings.VOLUME = min(Settings.VOLUME + 0.1,0.9)
        data = File.import_json("settings.json")
        data["volume"] = Settings.VOLUME
        File.export_json("settings.json",data)
