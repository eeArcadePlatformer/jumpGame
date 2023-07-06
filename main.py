import pygame as pg
from pygame.locals import *

pg.init()#pygame을 초기화

screen_width = 500
screen_height = 500

#스크린을 생성하고, 타이틀을 'Platformer'로 지정
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption('Platformer')

#define game variables
tile_size = 25  # 타일의 크기 설정

#이미지 로드
sun_img = pg.image.load('img/sun.png')#태양 이미지
bg_img = pg.image.load('img/sky.png')#배경 이미지

def draw_grid():
	#그리드 그리기 함수
	for line in range(0, 20):
		pg.draw.line(screen, (255, 255, 255), (0, line * tile_size), (screen_width, line * tile_size))
		pg.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, screen_height))

class Player():
    def __init__(self,x,y):
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
        self.speed_x = 2.5
        self.direction = 0 # right : 1, left : -1
        
    def update(self):
        dx = 0
        dy = 0
        walk_cooldown = 5
        
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
            self.velocuty_y = -7.5
            self.jumped = True
        if key[pg.K_SPACE] == False:
            self.jumped = False
            
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
        self.velocuty_y +=0.5
        if self.velocuty_y >5:
            self.velocuty_y = 5
        
        dy += self.velocuty_y
        
        #check collision
        # ...
        
        # update player x coordinate
        self.rect.x += dx
        self.rect.y += dy

        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height
            dy = 0
        
        # drawing
        screen.blit(self.image,self.rect)

class World():
    def __init__(self, data):
        dirt_img = pg.image.load('img/dirt.png') # 흙 (기본 이미지)
        grass_img = pg.image.load('img/grass.png')

        self.tile_list=[]
        
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
    
    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])

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

player = Player(50,screen_height-65)
world = World(world_data)

run = True
while run:
    screen.blit(bg_img, (0, 0)) # 배경 이미지 그리기
    screen.blit(sun_img, (100, 100)) # 태양 이미지 그리기

    # drawing, update
    draw_grid()#그리드 그리기
    world.draw()
    player.update()
    
    for event in pg.event.get():
		#종료 이벤트 처리
        if event.type == pg.QUIT:
            run = False

    pg.display.update()#스크린 업데이트

pg.quit()#게임 종료
