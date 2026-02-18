import pygame
import os



class Images():
    def extract_tile_from_tileset(tileset_path,tile_size,x,y):
        """
        Fonction qui permet de récuperer une tile d'un tileset en fonction de sa taille et de son emplacement dans le tileset
        """
        if os.path.exists(tileset_path):
            tileset_image = pygame.image.load(tileset_path).convert_alpha()
            rect = pygame.Rect(x*tile_size, y*tile_size, tile_size, tile_size)
            return tileset_image.subsurface(rect)
        else:
            print(f"Fichier non trouvé lors du chargement des textures : {tileset_path} ")


    def extract_animation_line_from_sheet(sheet_path,animation_level,frame_number, width,height):
        if os.path.exists(sheet_path):
            res = []
            tileset_image = pygame.image.load(sheet_path).convert_alpha()
            for x in range(frame_number):
                rect = pygame.Rect(x * width, animation_level * height, width, height)
                frame = tileset_image.subsurface(rect)

                res.append(frame)
            return res
        else:
            print(f"Fichier non trouvé : {sheet_path}")
            return []


    
    def load_player(path, size):
        image = pygame.image.load(path).convert_alpha()
        l=[]
        for i in range(0, 3):
            frame = image.subsurface(pygame.Rect(i*size, 0, size, size))
            l.append(pygame.transform.scale(frame, (size/4, size/4)))
        return l

    def is_tile_empty(tile):
        """
        Vérifie si tous les pixels du tile sont transparents
        """
        for x in range(tile.get_width()):
            for y in range(tile.get_height()):
                if tile.get_at((x, y))[3] != 0:  # Vérifie si le pixel a une opacité non nulle
                    return False
        return True



    def extract_tiles(tileset_path):
        """
        Permet d'extraire les tiles d'un tileset dans un dictionnaire, en ignorant les tiles vides.
        """
        
        tileset = pygame.image.load(tileset_path)
        
        # Dimensions du tileset
        tileset_width, tileset_height = tileset.get_size()

        # Dictionnaire pour stocker les tiles valides
        tiles = {}

        # Parcours du tileset
        for y in range(0, tileset_height, 16):
            for x in range(0, tileset_width, 16):
                # Extraire une sous-surface
                tile = tileset.subsurface((x, y, 16, 16))

                # Vérifier si le tile n'est pas complètement vide
                if not Images.is_tile_empty(tile):
                    key = f"tileset_{x//16}_{y//16}"
                    tiles[key] = tile

        return tiles
    
    

if __name__ == "__main__":
    
    
    print(Images.extract_tiles("assets/maps/test/textures/tiles/tileset.png", 16))