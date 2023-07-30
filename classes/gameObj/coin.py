import pygame

class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y, tile_size):
        super().__init__()
        self.image = pygame.image.load('img/coin.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (tile_size // 2, tile_size // 2))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)