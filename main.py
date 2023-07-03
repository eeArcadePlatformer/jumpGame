import pygame
from pygame.locals import *

pygame.init()#pygame을 초기화

screen_width = 1000
screen_height = 1000

#스크린을 생성하고, 타이틀을 'Platformer'로 지정
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Platformer')

#define game variables
tile_size = 50  # 타일의 크기 설정

#이미지 로드
sun_img = pygame.image.load('img/sun.png')#태양 이미지
bg_img = pygame.image.load('img/sky.png')#배경 이미지

def draw_grid():
	#그리드 그리기 함수
	for line in range(0, 20):
		pygame.draw.line(screen, (255, 255, 255), (0, line * tile_size), (screen_width, line * tile_size))
		pygame.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, screen_height))

run = True
while run:

	screen.blit(bg_img, (0, 0))#배경 이미지 그리기
	screen.blit(sun_img, (100, 100))#태양 이미지 그리기

	draw_grid()#그리드 그리기

	for event in pygame.event.get():
		#종료 이벤트 처리
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()#스크린 업데이트

pygame.quit()#게임 종료
