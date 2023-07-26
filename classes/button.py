import pygame

class Button:
    def __init__(self, x, y, image):
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False

    def draw(self):
        self.screen.blit(self.image,self.rect) # 버튼을 화면에 그림
        mouse_pos = pygame.mouse.get_pos()        
        mouse_click = pygame.mouse.get_pressed() 
        
        # 마우스가 버튼 위에 있고, 클릭이 발생하면 True를 반환, 그 외의 경우에는 아무것도 반환하지 않음          
        if self.rect.collidepoint(mouse_pos) and mouse_click[0] == 1:
            self.clicked = True
            return True
        else:
            self.clicked = False
            return 
                             