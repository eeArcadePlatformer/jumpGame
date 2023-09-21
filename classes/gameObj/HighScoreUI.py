import pygame as pg

class HighScoreUI:
    # pygame의 Surface 객체(screen)와 폰트(font)를 인자로 받아 초기화 작업을 수행.
    def __init__(self, screen, font, position, text_color = (255, 255, 255), font_size = 30):
        self.screen = screen
        self.font = font
        self.text_color = text_color
        self.font_size = font_size
        self.position = position
        self.high_scores = []
    # 화면에 상위 10개의 최고 점수를 표시.
    def draw(self):
        y_offset = 0
        for i, score in enumerate(self.high_scores):
            text = self.font.render(f"{i+1}. {score}", True, self.text_color)
            text_rect = text.get_rect(center=self.position)
            text_rect.y += y_offset
            self.screen.blit(text, text_rect)
            y_offset +=40 # 각 점수 사이의 간격 조절

    # 리스트를 새로운 상위 10개의 점수로 업데이트
    def update_high_scores(self, new_scores):
        self.high_scores = new_scores[:10]