import pygame as pg
import os
import pickle
from classes.gameObj.wolrd import World
from classes.gameObj.coin import Coin

def draw_grid(screen, tile_size,screen_width, screen_height):
    #그리드 그리기 함수
	for line in range(0, 20):
		pg.draw.line(screen, (255, 255, 255), (0, line * tile_size), (screen_width, line * tile_size))
		pg.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, screen_height))

# 텍스트 그리는 함수
def draw_text(screen ,text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

# 레벨 리셋 함수
def reset_level(level, player, blob_group, lava_group, exit_group, platform_group, coin_group, tile_size):
    screen_width, screen_height = pg.display.get_surface().get_size()
    player.reset(100, screen_height - 130)
    blob_group.empty()
    platform_group.empty()
    coin_group.empty()
    lava_group.empty()
    exit_group.empty()
    # level read
    if os.path.exists(f'level{level}_data'):
        pickle_in = open(f'level{level}_data', 'rb')
        world_data = pickle.load(pickle_in)
    else:
        print('Level is Empty. plz check.')
        exit()
    world = World(world_data)

    score_coin = Coin(tile_size // 2, tile_size // 2)
    coin_group.add(score_coin)

    return world
