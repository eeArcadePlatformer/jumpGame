import pygame as pg

class Button:
    def __init__(self, x, y, image, screen):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False
        self.screen = screen

    def draw(self, events):
        self.screen.blit(self.image, self.rect)
        mouse_pos = pg.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            for event in events:
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                        self.clicked = True
                        return True
        else:
            self.clicked = False
        return False
                             