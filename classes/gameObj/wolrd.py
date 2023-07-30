import pygame as pg
from pygame.locals import *
from classes.gameObj.enemy import Enemy
from classes.gameObj.lava import Lava
from classes.gameObj.coin import Coin
from classes.gameObj.ExitDoor import ExitDoor
from classes.gameObj.platform import Platform
class World():
    def __init__(self, screen, data, tile_size, groups):
        dirt_img = pg.image.load('img/dirt.png') # 흙 (기본 이미지)
        grass_img = pg.image.load('img/grass.png')

        self.tile_list=[]
        
        # 스프라이트 그룹
        self.blob_group = groups["blob_group"]
        # print(type(self.blob_group))
        self.lava_group = groups["lava_group"]
        self.coin_group = groups["coin_group"]
        self.exit_group = groups["exit_group"]
        self.platform_group = groups["platform_group"]
        
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
                    
                if tile == 3:
                    blob = Enemy(col_count * tile_size, row_count * tile_size + 15)
                    self.blob_group.add(blob)
                if tile == 4:
                    platform = Platform(col_count * tile_size, row_count * tile_size, 1, 0)
                    self.platform_group.add(platform)
                if tile == 5:
                    platform = Platform(col_count * tile_size, row_count * tile_size, 0, 1)
                    self.platform_group.add(platform)

                if tile == 6:
                    lava = Lava(x=col_count * tile_size, y=row_count * tile_size + (tile_size // 2),tile_size= tile_size)
                    self.lava_group.add(lava)
                if tile == 7:
                    coin = Coin(x=col_count * tile_size + (tile_size // 2), y=row_count * tile_size + (tile_size // 2),tile_size= tile_size)
                    self.coin_group.add(coin)
                if tile == 8:
                    exit = ExitDoor(x=col_count * tile_size,y= row_count * tile_size - (tile_size // 2),tile_size= tile_size)
                    self.exit_group.add(exit)
                
    def draw(self):
        for tile in self.tile_list:
            self.screen.blit(tile[0], tile[1])
            pg.draw.rect(self.screen, (255,255,255), tile[1], 2)