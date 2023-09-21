import pygame as pg
from pygame.locals import *

from classes.gameObj.wolrd import World
from classes.gameObj.player import Player
from classes.Managers.soundmanager import SoundManager
from classes.Managers.scoremanager import ScoreManager
from classes.gameObj.button import Button
from classes.gameObj.usernameInputUI import UsernameInputUI
from classes.gameObj.HighScoreUI import HighScoreUI

from utils import *

if __name__ == "__main__":
    pg.init()#pygame을 초기화
    
    sound_files = {
        'music': 'sound/music.wav',
        'coin': 'sound/coin.wav',
        'jump': 'sound/jump.wav',
        'game_over': 'sound/game_over.wav'
    }

    # manager class
    sound_manager = SoundManager(sound_files)
    score_manager = ScoreManager()

    # 사운드 설정
    sound_manager.sounds['coin'].set_volume(0.5)
    sound_manager.sounds['jump'].set_volume(0.5)
    sound_manager.sounds['game_over'].set_volume(0.5)

    # 배경 음악 재생
    pg.mixer.music.load('sound/music.wav')
    pg.mixer.music.play(-1, 0.0, 5000)

    screen_width = 1000
    screen_height = 1000

    #스크린을 생성하고, 타이틀을 'Platformer'로 지정
    screen = pg.display.set_mode((screen_width, screen_height))
    pg.display.set_caption('Platformer')
    
    # 오브젝트별 스프라이트 그룹
    blob_group = pg.sprite.Group()
    lava_group = pg.sprite.Group()
    coin_group = pg.sprite.Group()
    exit_group = pg.sprite.Group()
    platform_group = pg.sprite.Group()
    
    sprite_groups = {
        "blob_group" : blob_group,
        "lava_group" : lava_group,
        "coin_group" : coin_group,
        "exit_group" : exit_group,
        "platform_group" : platform_group
    }
    
    #define game variables
    MAX_LEVEL = 0
    START_LEVEL = 0
    
    tile_size = 50
    game_over = 0
    main_menu = True
    level = START_LEVEL
    score = 0

    #이미지 로드
    sun_img = pg.image.load('img/sun.png')#태양 이미지
    bg_img = pg.image.load('img/sky.png')#배경 이미지
    restart_img = pg.image.load('img/restart_btn.png')
    start_img = pg.image.load('img/start_btn.png')
    exit_img = pg.image.load('img/exit_btn.png')
    
    score_coin = Coin(tile_size // 2, tile_size // 2, tile_size)
    coin_group.add(score_coin)

    #load in level data and create world
    if os.path.exists(f'levels/level{level}_data'):
        pickle_in = open(f'levels/level{level}_data', 'rb')
        world_data = pickle.load(pickle_in)
    world = World(screen,world_data,tile_size, sprite_groups)


    #create buttons
    restart_button = Button(screen_width // 2 - 50, screen_height // 2 + 100, restart_img, screen, pg.K_RETURN)
    start_button = Button(screen_width // 2 - 350, screen_height // 2 - 200, start_img, screen, pg.K_RETURN)
    exit_button = Button(screen_width // 2 + 150, screen_height // 2 - 200, exit_img, screen, pg.K_ESCAPE)
    
    # font and color
    font = pg.font.SysFont('Bauhaus 93', 70)
    font_score = pg.font.SysFont('Bauhaus 93', 30)
    white = (255, 255, 255)
    blue = (0, 0, 255)
    
    # UI class
    input_active = False
    username_input_ui = UsernameInputUI(screen, font, input_box_pos=((screen_width // 2)- 200, screen_height // 2 ), input_box_size=(400,70))
    highscore_ui = HighScoreUI(screen, font_score, (screen.get_width()//2 , screen.get_height()//2),blue)
    
    player = Player(50,screen_height-65,screen)
    
    # clock
    clock = pg.time.Clock()
    fps = 60
    
    run = True
    while run:
        clock.tick(fps)

        screen.blit(bg_img, (0, 0))
        screen.blit(sun_img, (100, 100))
        
        events = pg.event.get()

        if main_menu == True:
            if exit_button.draw(events):
                run = False
            if start_button.draw(events):
                main_menu = False
                
            scores = score_manager.load_high_scores()
            highscore_ui.update_high_scores(scores)
            highscore_ui.draw()
        else:
            world.draw()

            if game_over == 0:
                blob_group.update()
                platform_group.update()
                # update score
                # check if a coin has been collected
                if pg.sprite.spritecollide(player, coin_group, True):
                    score += 1
                    sound_manager.play('coin')
                draw_text(screen,'X ' + str(score), font_score, white, tile_size - 10, 10)

            blob_group.draw(screen)
            platform_group.draw(screen)
            lava_group.draw(screen)
            coin_group.draw(screen)
            exit_group.draw(screen)

            game_over = player.update(tile_list=world.tile_list, game_over=game_over, groups=sprite_groups)

            # if player has died
            if game_over == -1:
                if restart_button.draw(events):
                    world_data = []
                    world = reset_level(level,player,blob_group,lava_group,exit_group, platform_group, coin_group, tile_size, screen)
                    game_over = 0
                    score = 0

            # if player has completed the level
            if game_over == 1:
                # reset game and go to next level
                level += 1
                if level <= MAX_LEVEL:
                    # reset level
                    world_data = []
                    world = reset_level(level,player,blob_group,lava_group,exit_group, platform_group, coin_group, tile_size, screen)
                    game_over = 0
                else:
                    draw_text(screen,'YOU WIN!', font, blue, (screen_width // 2) - 140, screen_height // 2 - 200)
                    draw_text(screen,'Write your name :', font, blue, (screen_width // 2) - 250, screen_height // 2 - 100)
                    # Save the score using ScoreManager
                    final_score = score_manager.calculate_score(level, score)
                    input_active = True
                    if len(username_input_ui.get_input()) >2:
                        if restart_button.draw(events):
                            # save score
                            score_manager.save_score(username_input_ui.get_input(), score)
                            input_active = False

                            # reset level
                            level = START_LEVEL
                            world_data = []
                            world = reset_level(level,player,blob_group,lava_group,exit_group, platform_group, coin_group, tile_size, screen)
                            game_over = 0
                            score = 0
                            main_menu = True 

        for event in events:
            if event.type == pg.QUIT:
                run = False
                
        if input_active:
            username_input_ui.handle_events(events)
            username_input_ui.draw()

        pg.display.update()

    pg.quit()
