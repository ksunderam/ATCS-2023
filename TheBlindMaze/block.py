import pygame

class Block(pygame.sprite.Sprite):
    WALL = 0
    BRICK = 1
    LIGHTSWITCH = 2
    BOOSTER = 3

    def __init__(self, x=50, y=50, wall_type=0):
        super().__init__()

        filepath = "/Users/kayansunderam/Documents/ATCS/ATCS-2023/TheBlindMaze/images/"

        # Load the image
        if wall_type == self.WALL:
            self.image = pygame.image.load("/Users/kayansunderam/Documents/ATCS/ATCS-2023/TheBlindMaze/images/wall.png")
        elif wall_type == self.BRICK:
            self.image = pygame.image.load(filepath+"brick.png")
        elif wall_type == self.LIGHTSWITCH:
            self.image = pygame.image.load(filepath+"LightSwitch.png")
        elif wall_type == self.BOOSTER:
            self.image = pygame.image.load(filepath+"booster.png")

        self.type = wall_type
        
        # Set the position to be the center of the image
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        