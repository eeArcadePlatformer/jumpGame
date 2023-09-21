import pygame
from utils import resource_path

class ExitDoor(pygame.sprite.Sprite):
    def __init__(self, x, y, tile_size):
        super().__init__()

        image_path = resource_path('img/exit.png')
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (tile_size, int(tile_size * 1.5)))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y