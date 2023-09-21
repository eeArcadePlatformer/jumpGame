import pygame as pg
from utils import draw_text, resource_path

class Player():
    def __init__(self, x, y, screen):
        self.reset(x, y, screen)

    def update(self, game_over, tile_list, groups):
        dx = 0
        dy = 0
        walk_cooldown = 5
        col_thresh = 20

        if game_over == 0:
            key = pg.key.get_pressed()
            if key[pg.K_SPACE] and self.jumped == False and self.in_air == False:
                self.vel_y = -15
                self.jumped = True
            if key[pg.K_SPACE] == False:
                self.jumped = False
            if key[pg.K_LEFT]:
                dx -= 5
                self.counter += 1
                self.direction = -1
            if key[pg.K_RIGHT]:
                dx += 5
                self.counter += 1
                self.direction = 1
            if key[pg.K_LEFT] == False and key[pg.K_RIGHT] == False:
                self.counter = 0
                self.index = 0
                if self.direction == 1:
                    self.image = self.images_right[self.index]
                if self.direction == -1:
                    self.image = self.images_left[self.index]

            #handle animation
            if self.counter > walk_cooldown:
                self.counter = 0	
                self.index += 1
                if self.index >= len(self.images_right):
                    self.index = 0
                if self.direction == 1:
                    self.image = self.images_right[self.index]
                if self.direction == -1:
                    self.image = self.images_left[self.index]


			#add gravity
            self.vel_y += 1
            if self.vel_y > 10:
                self.vel_y = 10
            dy += self.vel_y

			#check for collision

            self.in_air = True
            for tile in tile_list:
                #check for collision in x direction
                if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    dx = 0
                #check for collision in y direction
                if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                    #check if below the ground i.e. jumping
                    if self.vel_y < 0:
                        dy = tile[1].bottom - self.rect.top
                        self.vel_y = 0
                    #check if above the ground i.e. falling
                    elif self.vel_y >= 0:
                        dy = tile[1].top - self.rect.bottom
                        self.vel_y = 0
                        self.in_air = False

            # collision with objects
            blob_group=groups["blob_group"]
            lava_group=groups["lava_group"]
            exit_group=groups["exit_group"]
            platform_group=groups["platform_group"]
            
            #check for collision with enemies
            if pg.sprite.spritecollide(self, blob_group, False):
                game_over = -1

            #check for collision with lava
            if pg.sprite.spritecollide(self, lava_group, False):
                game_over = -1

            #check for collision with exit
            if pg.sprite.spritecollide(self, exit_group, False):
                game_over = 1

            #check for collision with platforms
            for platform in platform_group:
                #collision in the x direction
                if platform.rect.colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    dx = 0
                #collision in the y direction
                if platform.rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                    #check if below platform
                    if abs((self.rect.top + dy) - platform.rect.bottom) < col_thresh:
                        self.vel_y = 0
                        dy = platform.rect.bottom - self.rect.top
                    #check if above platform
                    elif abs((self.rect.bottom + dy) - platform.rect.top) < col_thresh:
                        self.rect.bottom = platform.rect.top - 1
                        self.in_air = False
                        dy = 0
                    #move sideways with the platform
                    if platform.move_x != 0:
                        self.rect.x += platform.move_direction
            self.rect.x += dx
            self.rect.y += dy

        elif game_over == -1:
            self.image = self.dead_image
            draw_text(self.screen,'GAME OVER!', self.font, (0, 0, 255), (self.screen_width // 2) - 200, self.screen_height // 2)
            if self.rect.y > 200:
                self.rect.y -= 5

        self.screen.blit(self.image, self.rect)

        return game_over

    def reset(self, x, y, screen):
        self.screen = screen
        self.screen_width, self.screen_height = pg.display.get_surface().get_size()
        
        self.images_right = []
        self.images_left = []
        self.index = 0
        self.counter = 0
        
        for num in range(1, 5):
            img_right = pg.image.load(resource_path(f'img/guy{num}.png'))
            img_right = pg.transform.scale(img_right, (40, 80))
            img_left = pg.transform.flip(img_right, True, False)
            self.images_right.append(img_right)
            self.images_left.append(img_left)
        
        self.dead_image = pg.image.load(resource_path('img/ghost.png'))
        self.image = self.images_right[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jumped = False
        self.direction = 0
        self.in_air = True
        
        self.font = pg.font.SysFont('Bauhaus 93', 70)
