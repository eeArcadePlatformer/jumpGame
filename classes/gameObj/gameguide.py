import pygame as pg
from pygame.locals import *
import sys

from utils import *

class GameIntro:
    def __init__(self, screen):
        self.screen = screen
        self.font = pg.font.Font(None, 36)  # 사용할 폰트 설정
        self.text_color = (0, 0, 0)  # 텍스트 색상 설정

        self.instructions = [
            "Welcome to Our Platformer Game!",
            "Instructions:",
            "- Use arrow keys to move left and right.",
            "- Press the spacebar to jump.",
            "Press Enter to start the game."
        ]

    def show_intro(self):
        intro = True
        while intro:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                        intro = False

            # 텍스트를 화면에 표시
            y = 400
            for line in self.instructions:
                text_surface = self.font.render(line, True, self.text_color)
                text_rect = text_surface.get_rect(center=(self.screen.get_width() // 2, y))
                self.screen.blit(text_surface, text_rect)
                y += 40

            pg.display.update()

if __name__ == "__main__":
    pg.init()

    screen_width = 1000
    screen_height = 1000
    screen = pg.display.set_mode((screen_width, screen_height))
    pg.display.set_caption('Game Intro')

    game_intro = GameIntro(screen)

    run = True
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        keys = pg.key.get_pressed()
        if keys[pg.K_RETURN]:
            run = False

        game_intro.show_intro()