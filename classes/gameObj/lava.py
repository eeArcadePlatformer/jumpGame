import pygame

class Lava(pygame.sprite.Sprite):
    def __init__(self, tile_size, x, y):
        super().__init__()
        self.image = pygame.image.load('img/lava.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (tile_size, tile_size // 2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
