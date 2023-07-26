import pygame

class Platform(pygame.sprite.Sprite):
    def __init__(self, tile_size, x, y, move_x, move_y):
        super().__init__()
        self.image = pygame.image.load('img/platform.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (tile_size, tile_size // 2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_counter = 0
        self.move_x = move_x
        self.move_y = move_y

    def update(self):
        # move_direction에 따라 x, y 좌표를 변경하고, move_counter를 증가함.
        self.rect.x += self.move_direction
        self.rect.y += self.move_direction
        self.move_counter += 1

        # move_counter가 50의 절대값보다 크거나 같으면 move_direction과 move_counter의 부호를 변경.
        if abs(self.move_counter) >= 50:
            self.move_direction *= -1
            self.move_counter *= -1
