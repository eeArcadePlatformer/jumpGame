import pygame

class Camera:
    def __init__(self, width, height, map_width, map_height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height
        self.map_width = map_width
        self.map_height = map_height

    def apply(self, entity):
        # 주어진 엔터티의 위치에 카메라 변환을 적용하고, 변환된 위치 반환
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        # 카메라의 중앙을 타겟의 위치로 업데이트
        x = -target.rect.centerx + int(self.width / 2)
        y = -target.rect.centery + int(self.height / 2)

        # 카메라가 맵 경계를 넘지 않도록 함
        x = min(0, x)  # 왼쪽 경계
        x = max(-(self.map_width - self.width), x)  # 오른쪽 경계
        y = min(0, y)  # 위쪽 경계
        y = max(-(self.map_height - self.height), y)  # 아래쪽 경계

        self.camera = pygame.Rect(x, y, self.width, self.height)
