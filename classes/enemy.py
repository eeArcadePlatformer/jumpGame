import pygame as pg
import random
from pygame.locals import *

class Enemy():
    def __init__(self, x, y) -> None:
        blob_img = pg.image.load('img/blob.png') # 블롭
	
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_counter = 0
        pass
    
    def update(self):
        random_value = random.randint(1, 9) # 임의의 값 생성 (1~9)

	# move_direction에 따라 x 좌표 변경, move_counter를 증가
        self.rect.x += self.move_direction
        self.move_counter += 1
	
	# move_counter가 임의의 값보다 크거나 같으면 move_direction, move_counter의 부호 변경
        if self.move_counter >= random_value:
            self.move_direction *= -1
            self.move_counter *= -1
        pass