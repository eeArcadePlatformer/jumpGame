import pygame

class UsernameInputUI:
    def __init__(self, screen, font, input_box_pos=(200, 300), input_box_size=(300, 40), border_color=(255, 255, 255,0), border_thickness=5, text_color=(0, 0, 0)):
        self.screen = screen
        self.font = font
        self.input_string = ""
        self.input_box_pos = input_box_pos  # (x, y) 텍스트 박스 위치
        self.input_box_size = input_box_size  # (width, height) 텍스트 박스 크기
        self.border_color = border_color  # 테두리 색상
        self.border_thickness = border_thickness  # 테두리 두께
        self.text_color = text_color  # 텍스트 색상
        
    def draw(self):
        # 입력 상자 그리기
        input_box = pygame.Rect(*self.input_box_pos, *self.input_box_size)
        pygame.draw.rect(self.screen, self.border_color, input_box, self.border_thickness)

        # 입력한 텍스트 그리기
        text_surface = self.font.render(self.input_string, True, self.text_color)
        self.screen.blit(text_surface, (input_box.x + 5, input_box.y + 5))

        pygame.display.flip()

    def get_input(self):
        return self.input_string
    
    def set_input(self, default = ""):
        self.input_string = default

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # 엔터 키를 누르면 입력값 반환
                    return self.input_string
                elif event.key == pygame.K_BACKSPACE:
                    # 백스페이스 키를 누르면 입력값에서 문자 하나 삭제
                    self.input_string = self.input_string[:-1]
                else:
                    if len(self.input_string) < 10:
                        self.input_string += event.unicode

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((500, 300))
    font = pygame.font.Font(None, 36)
    ui = UsernameInputUI(screen, font, input_box_pos=(100, 200), input_box_size=(300, 40), border_color=(0, 0, 0), border_thickness=2, text_color=(0, 0, 0))

    while True:
        ui.draw()
        input_name = ui.handle_events(pygame.event.get())
        if input_name:
            print("사용자 이름:", input_name)
            break
