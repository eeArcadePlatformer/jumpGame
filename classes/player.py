import pygame as pg
from pygame.locals import *

class Player():
    def __init__(self,x,y,screen):
        self.screen = screen
        
        # 애니메이션을 위한 이미지 목록
        self.images_right = []
        self.images_left = []
        self.index = 0 # animation index
        self.counter = 0
        for num in range(1, 5):
            img_right = pg.image.load(f'img/guy{num}.png')
            img_right = pg.transform.scale(img_right, (20, 40))
            img_left = pg.transform.flip(img_right, True, False)
            self.images_right.append(img_right)
            self.images_left.append(img_left)
        
        # images_right의 idx번째 transform
        self.image = self.images_right[self.index]
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocuty_y = 0
        self.jumped = False
        self.speed_x = 2
        self.jumpForce = 3
        self.direction = 0 # right : 1, left : -1
        
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        
    def update(self, tile_list, game_over : bool):
        dx = 0
        dy = 0
        walk_cooldown = 2
        
        # get key press
        key = pg.key.get_pressed()
        
        # horizontal move
        if key[pg.K_LEFT]:
            dx -=self.speed_x
            self.counter += 1
            self.direction =-1
        if key[pg.K_RIGHT]:
            dx += self.speed_x
            self.counter += 1
            self.direction =1
            
        # jump
        if key[pg.K_SPACE] and self.jumped == False:
            self.velocuty_y = -self.jumpForce
            self.jumped = True
        if key[pg.K_SPACE] == False:
            self.jumped = False
        
        # walking animation
        if key[pg.K_LEFT] == False and key[pg.K_RIGHT] == False:
            self.counter = 0
            self.index = 0
            if self.direction == 1:
                self.image = self.images_right[self.index]
            if self.direction == -1:
                self.image = self.images_left[self.index]
        
        # handle animation
        if self.counter > walk_cooldown:
            self.counter = 0	
            self.index += 1
            if self.index >= len(self.images_right):
                self.index = 0
            if self.direction == 1:
                self.image = self.images_right[self.index]
            if self.direction == -1:
                self.image = self.images_left[self.index]
        
        # gravity
        self.velocuty_y +=0.1
        if self.velocuty_y >3:
            self.velocuty_y = 3
        
        dy += self.velocuty_y
        
        #check collision
        for tile in tile_list:
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx = 0
            if tile[1].colliderect(self.rect.x, self.rect.y+dy, self.width,self.height):
                if self.velocuty_y < 0:
                    dy = tile[1].bottom - self.rect.top
                    self.velocuty_y = 0
                elif self.velocuty_y >=0:
                    dy = tile[1].top - self.rect.bottom
                    self.velocuty_y = 0
        # update player x coordinate
        self.rect.x += dx
        self.rect.y += dy
        
        # drawing
        self.screen.blit(self.image,self.rect)
        pg.draw.rect(self.screen, (255,255,255), self.rect, 2) # for collision range rendering