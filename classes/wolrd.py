import pygame as pg
from pygame.locals import *

class World():
    def __init__(self, screen, data, tile_size):
        dirt_img = pg.image.load('img/dirt.png') # 흙 (기본 이미지)
        grass_img = pg.image.load('img/grass.png')

        self.tile_list=[]
        self.screen = screen
        
        for row_count, row in enumerate(data):# 세로로 각 행에 대해
            for col_count, tile in enumerate(row):
                if tile == 1:
                    img = pg.transform.scale(dirt_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size # 열 개수 * 타일사이즈 => 즉, 타일 개수만큼 이동
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    
                    self.tile_list.append(tile)
                    
                if tile == 2:
                    img = pg.transform.scale(grass_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                    
                if tile == 3: # enemy rendering
                    pass
    def draw(self):
        for tile in self.tile_list:
            self.screen.blit(tile[0], tile[1])
            pg.draw.rect(self.screen, (255,255,255), tile[1], 2)