import pygame

class World:
    
    # 클래스를 초기화하고 경계를 설정.
    def __init__(self, tile_size, rows, cols):
        self.tile_size = tile_size
        self.rows = rows
        self.cols = cols
        self.world_data = [[0 for _ in range(cols)] for _ in range(rows)]  
    
    # 격자 렌더링.
    def draw_grid(self, screen, color):
        for y in range(0, self.rows * self.tile_size, self.tile_size):
            pygame.draw.line(screen, color, (0, y), (self.cols * self.tile_size, y))
        for x in range(0, self.cols * self.tile_size, self.tile_size):
            pygame.draw.line(screen, color, (x, 0), (x, self.rows * self.tile_size))
    
    # 현재 월드 데이터를 사용하여 맵 렌더링
    def draw_world(self, screen):
        for y, row in enumerate(self.world_data):
            for x, tile_type in enumerate(row):
                pygame.draw.rect(screen, (x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size))
    
    # 지정한 위치의 타일 종류를 변경.
    def update_tile(self, x, y, change):
        if 0 <= x < self.cols and 0 <= y < self.rows:
            self.world_data[y][x] = change