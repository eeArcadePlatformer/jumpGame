import pygame
from utils import resource_path
class Lava(pygame.sprite.Sprite):
    def __init__(self, tile_size, x, y):
        super().__init__()
        self.image = pygame.image.load(resource_path('img/lava.png'))
        self.image = pygame.transform.scale(self.image, (tile_size, tile_size // 2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
