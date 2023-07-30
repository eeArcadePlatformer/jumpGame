import pygame as pg
import os
import pickle
from classes.gameObj.wolrd import World

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
def reset_level(level,player,blob_group, lava_group, exit_group, player_cor) -> World:
	player.reset(player_cor[0], player_cor[1])
	blob_group.empty()
	lava_group.empty()
	exit_group.empty()

	if os.path.exists(f'level{level}_data'):
		pickle_in = open(f'level{level}_data', 'rb')
		world_data = pickle.load(pickle_in)
	world = World(world_data)

	return world