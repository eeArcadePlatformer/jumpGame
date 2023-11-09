import pygame as pg
import time

class HighScoreUI:
    def __init__(self, screen, font, position, text_color=(255, 255, 255), font_size=30):
        self.screen = screen
        self.font = font
        self.text_color = text_color
        self.font_size = font_size
        self.position = position
        self.high_scores = []
        self.panel = pg.image.load('img/panel.png')  # 새로운 이미지 파일 로드

    def draw(self):
        y_offset = 0
        self.screen.blit(self.panel, (self.position[0] - 150, self.position[1] - 45))
        colors = [(255, 215, 0), (192, 192, 192), (205, 127, 50)]  # 금색, 은색, 동색 순으로 RGB값 설정
        for i, score in enumerate(self.high_scores):
            if i < 3:
                text = self.font.render(f"{i + 1}. {score}", True, colors[i])  # 1등: 금, 2등: 은, 3등: 동색으로 변경
            else:
                text = self.font.render(f"{i + 1}. {score}", True, self.text_color)
            text_rect = text.get_rect(center=self.position)
            text_rect.y += y_offset
            self.screen.blit(text, text_rect)
            y_offset += 40
            pg.display.flip()
            time.sleep(0.5)  # 0.5초마다 점수가 순차적으로 나타나도록 설정

    def update_high_scores(self, new_scores):
        self.high_scores = new_scores[:10]
        for i in range(len(self.high_scores)):
            temp_scores = self.high_scores[:i + 1]  # 점수 리스트에서 현재 인덱스까지의 점수들을 임시로 저장