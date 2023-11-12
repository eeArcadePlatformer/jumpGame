import pygame as pg
import time
from utils import resource_path

class HighScoreUI:    
    def __init__(self, screen, font, position, text_color=(255, 255, 255), font_size=30):
        self.screen = screen
        self.font = font
        self.text_color = text_color
        self.font_size = font_size
        self.position = position
        self.high_scores = []
        self.panel = pg.image.load(resource_path('img/panel.png'))  # pannel image
        self.last_update_time = 0
        self.displayed_scores = 0
        self.score_update_interval = 500 

    def draw(self):
        y_offset = 0
        self.screen.blit(self.panel, (self.position[0] - 150, self.position[1] - 45))
        colors = [(255, 215, 0), (192, 192, 192), (205, 127, 50)]
        for i, score in enumerate(self.high_scores[:self.displayed_scores]):
            text = self.font.render(f"{i + 1}. {score}", True, colors[i] if i < 3 else self.text_color)
            text_rect = text.get_rect(center=self.position)
            text_rect.y += y_offset
            self.screen.blit(text, text_rect)
            y_offset += 40
        pg.display.flip()

    def update_high_scores(self, new_scores):
        self.high_scores = new_scores[:10]
        # self.last_update_time = pg.time.get_ticks()
        # self.displayed_scores = 0

    def update(self):
        current_time = pg.time.get_ticks()
        if (current_time - self.last_update_time) > self.score_update_interval and self.displayed_scores < len(self.high_scores):
            self.last_update_time = current_time
            self.displayed_scores += 1
            self.draw()