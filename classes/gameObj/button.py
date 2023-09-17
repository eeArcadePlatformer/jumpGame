import pygame as pg

class Button:
    def __init__(self, x, y, image, screen, Key):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False
        self.screen = screen
        self.key = Key # pg.KEY

    def draw(self, events):
        self.screen.blit(self.image, self.rect)
        for event in events:
            if event.type == pg.KEYDOWN:
                if event.key == self.key:
                    self.clicked = True
                    return True
        self.clicked = False
        return False   