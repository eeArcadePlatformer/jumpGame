import pygame

class HighScoreUI:
    # pygame의 Surface 객체(screen)와 폰트(font)를 인자로 받아 초기화 작업을 수행.
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font
        self.high_scores = self.load_high_scores()

    # 화면에 상위 10개의 최고 점수를 표시.
    def draw(self):
        y_offset = 50  # 각 점수 항목의 세로 간격
        text_color = (255, 255, 255)  # 텍스트 색상 : 흰색
        font_size = 30 # 폰트 크기
        font = pygame.font.Font(None, font_size)

        # 각 점수 항목을 화면에 그림
        for i, score in enumerate(self.high_scores):
            text = font.render(f"{i+1}. {score}", True, text_color)
            text_rect = text.get_rect(center=(self.screen.get_width() // 2, y_offset))
            self.screen.blit(text, text_rect)
            y_offset += 30  # 다음 항목으로 이동

    # 리스트를 새로운 상위 10개의 점수로 업데이트
    def update_high_scores(self, new_scores):
        self.high_scores = new_scores[:10] # 새로운 상위 점수로 업데이트.
        self.save_high_scores() # 점수를 파일에 저장