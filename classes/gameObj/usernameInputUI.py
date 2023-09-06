import pygame

class UsernameInputUI:
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font
        self.input_string = ""

    def draw(self):
        
        # 입력 상자 그리기
        input_box = pygame.Rect(100, 200, 300, 40)
        pygame.draw.rect(self.screen, (0, 0, 0), input_box, 2)
        
        # 입력한 텍스트 그리기
        text_surface = self.font.render(self.input_string, True, (0, 0, 0))
        self.screen.blit(text_surface, (input_box.x + 5, input_box.y + 5))
        
        pygame.display.flip()

    def get_input(self):
        return self.input_string

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # 엔터 키를 누르면 입력값 반환
                    return self.input_string
                elif event.key == pygame.K_BACKSPACE:
                    # 백스페이스 키를 누르면 입력값에서 문자 하나 삭제
                    self.input_string = self.input_string[:-1]
                else:
                    # 다른 키 입력은 입력값에 추가
                    self.input_string += event.unicode

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((500, 300))
    font = pygame.font.Font(None, 36)
    ui = UsernameInputUI(screen, font)

    while True:
        ui.draw()
        input_name = ui.handle_events()
        if input_name:
            print("사용자 이름:", input_name)
            break
