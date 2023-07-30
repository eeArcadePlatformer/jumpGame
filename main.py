import pygame as pg
from pygame.locals import *

from classes.gameObj.wolrd import World
from classes.gameObj.player import Player
from classes.gameObj.button import Button
from classes.gameObj.enemy import Enemy
from classes.gameObj.platform import Platform
from classes.gameObj.lava import Lava
from classes.gameObj.coin import Coin
from classes.gameObj.ExitDoor import ExitDoor
from classes.Managers.soundmanager import SoundManager

from utils import *

if __name__ == "__main__":
    if __name__ == "__main__":
        pg.init()#pygame을 초기화

    screen_width = 500
    screen_height = 500

    #스크린을 생성하고, 타이틀을 'Platformer'로 지정
    screen = pg.display.set_mode((screen_width, screen_height))
    pg.display.set_caption('Platformer')
    
    # 오브젝트별 스프라이트 그룹
    blob_group = pg.sprite.Group()
    lava_group = pg.sprite.Group()
    coin_group = pg.sprite.Group()
    exit_group = pg.sprite.Group()
    
    sprite_groups = {
        "blob_group" : blob_group,
        "lava_group" : lava_group,
        "coin_group" : coin_group,
        "exit_group" : exit_group
    }
    
    #define game variables
    tile_size = 25  # 타일의 크기 설정

    #이미지 로드
    sun_img = pg.image.load('img/sun.png')#태양 이미지
    bg_img = pg.image.load('img/sky.png')#배경 이미지
    
    world_data = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
    [1, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 1], 
    [1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 2, 2, 1], 
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 7, 0, 5, 0, 0, 0, 1], 
    [1, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 1], 
    [1, 7, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
    [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 7, 0, 0, 0, 0, 1], 
    [1, 0, 2, 0, 0, 7, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
    [1, 0, 0, 2, 0, 0, 4, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 1], 
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 1], 
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 7, 0, 0, 0, 0, 2, 0, 1], 
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 2, 2, 2, 2, 2, 1], 
    [1, 0, 0, 0, 0, 0, 2, 2, 2, 6, 6, 6, 6, 6, 1, 1, 1, 1, 1, 1], 
    [1, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
    [1, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
    [1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]
    
    player = Player(50,screen_height-65,screen)
    world = World(screen,world_data,tile_size, sprite_groups)
    
    run = True
    while run:
        screen.blit(bg_img, (0, 0)) # 배경 이미지 그리기
        screen.blit(sun_img, (50, 50)) # 태양 이미지 그리기
    
        # drawing, update
        # draw_grid()#그리드 그리기
        world.draw()    
        player.update(tile_list=world.tile_list, game_over=False)
        
        for event in pg.event.get():
    		#종료 이벤트 처리
            if event.type == pg.QUIT:
                run = False
    
        pg.display.update()#스크린 업데이트
    
    pg.quit()#게임 종료