import pygame
from pygame import *
from sys import exit
from random import randint
from upgrade_boxes import *
from GUI import *

font.init()
mixer.init()
pygame.init()

class GameSprite(sprite.Sprite):
    def __init__(self, sprite_image, pos_x, pos_y, size_x, size_y, speed=0):
        super().__init__()

        self.speed = speed
        self.size_x = size_x
        self.size_y = size_y
        self.sprite_image = sprite_image
        self.rand_size = randint(30, 50)

        self.image = transform.scale(image.load(self.sprite_image), (self.size_x, self.size_y))
        self.rect = self.image.get_rect()

        self.rect.x = pos_x
        self.rect.y = pos_y



class Player(GameSprite):
    def __init__(self, sprite_image, pos_x, pos_y, size_x, size_y, speed):
        super().__init__(sprite_image, pos_x, pos_y, size_x, size_y, speed)

        self.anim_idle = [image.load('Player_anim_v2/player_1.png'), image.load('Player_anim_v2/player_2.png'),
                          image.load('Player_anim_v2/player_3.png'), image.load('Player_anim_v2/player_4.png'),
                          image.load('Player_anim_v2/player_5.png')]

        self.surf = surface.Surface((120, 60))
        self.surf = self.surf.get_rect()
        self.anim_counter = 0
        self.lvl = 1

    def control(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 10:
            self.rect.x -= self.speed
        elif keys[K_RIGHT] and self.rect.x < win_width - 100:
            self.rect.x += self.speed
        elif keys[K_UP] and self.rect.y > 10:
            self.rect.y -= self.speed
        elif keys[K_DOWN] and self.rect.y < win_height - 100:
            self.rect.y += self.speed


    def fire(self):
        if self.lvl == 1:
            bullet_1 = Bullet('bullet_lazer.png', self.rect.centerx - 5, self.rect.y - 20, 11, 50, 30)
            bullets_group.add(bullet_1)
        elif self.lvl == 2:
            bullet_1 = Bullet('bullet_lazer.png', self.rect.centerx - 13, self.rect.y - 20, 11, 50, 30)
            bullet_2 = Bullet('bullet_lazer.png', self.rect.centerx + 5, self.rect.y - 20, 11, 50, 30)
            bullets_group.add(bullet_1, bullet_2)
        elif self.lvl == 3:
            bullet_1 = Bullet('bullet_lazer.png', self.rect.centerx - 15, self.rect.y - 20, 11, 50, 30)
            bullet_2 = Bullet('bullet_lazer.png', self.rect.centerx + 7, self.rect.y - 20, 11, 50, 30)
            bullet_3 = Bullet('bullet_lazer.png', self.rect.centerx - 5, self.rect.y - 20, 11, 50, 30)
            bullets_group.add(bullet_1, bullet_2, bullet_3)
        elif self.lvl == 4:
            bullet_1 = Bullet('bullet_lazer.png', self.rect.centerx - 15, self.rect.y - 20, 11, 50, 30)
            bullet_2 = Bullet('bullet_lazer.png', self.rect.centerx + 7, self.rect.y - 20, 11, 50, 30)
            bullet_3 = Bullet('bullet_lazer.png', self.rect.centerx - 5, self.rect.y - 20, 11, 50, 30)
            bullet_4 = Bullet('bullet_lazer.png', self.rect.centerx - 70, self.rect.y - 20, 11, 50, 30, 'left')
            bullet_5 = Bullet('bullet_lazer.png', self.rect.centerx + 35, self.rect.y - 20, 11, 50, 30, 'right')
            bullets_group.add(bullet_1, bullet_2, bullet_3, bullet_4, bullet_5)
        elif self.lvl == 5:
            bullet_1 = Bullet('bullet_lazer.png', self.rect.centerx - 15, self.rect.y - 20, 11, 50, 30)
            bullet_2 = Bullet('bullet_lazer.png', self.rect.centerx + 7, self.rect.y - 20, 11, 50, 30)
            bullet_3 = Bullet('bullet_lazer.png', self.rect.centerx - 5, self.rect.y - 20, 11, 50, 30)
            bullet_4 = Bullet('bullet_lazer.png', self.rect.centerx - 70, self.rect.y - 20, 11, 50, 30, 'left')
            bullet_5 = Bullet('bullet_lazer.png', self.rect.centerx - 80, self.rect.y - 20, 11, 50, 30, 'left')
            bullet_6 = Bullet('bullet_lazer.png', self.rect.centerx + 35, self.rect.y - 20, 11, 50, 30, 'right')
            bullet_7 = Bullet('bullet_lazer.png', self.rect.centerx + 45, self.rect.y - 20, 11, 50, 30, 'right')
            bullets_group.add(bullet_1, bullet_2, bullet_3, bullet_4, bullet_5, bullet_6, bullet_7)
        fire_sound.play()

    def animation(self):
        if self.anim_counter >= 15:
            self.anim_counter = 0
        self.image = transform.scale(self.anim_idle[self.anim_counter // 3], (self.size_x, self.size_y))
        window.blit(self.image, (self.rect.x, self.rect.y))
        self.anim_counter += 1


class Bullet(GameSprite):
    def __init__(self, sprite_image, pos_x, pos_y, size_x, size_y, speed, direction=None):
        super().__init__(sprite_image, pos_x, pos_y, size_x, size_y, speed)
        self.direction = direction
        if self.direction == 'left':
            self.image = transform.rotate(image.load(self.sprite_image), 45)
        elif self.direction == 'right':
            self.image = transform.rotate(image.load(self.sprite_image), -45)
    def update(self):
        if self.direction == None:
            self.rect.y += -self.speed
        elif self.direction == 'left':
            self.rect.y += -self.speed
            self.rect.x += -self.speed
        elif self.direction == 'right':
            self.rect.y += -self.speed
            self.rect.x += self.speed
        if self.rect.y < -100:
            self.kill()



class Asteroid(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 1100:
            self.rect.y = 0
            self.rect.x = randint(0, 1300)
            self.speed = randint(10, 13)
            self.size_y = self.rand_size
            self.size_x = self.rand_size
            self.image = transform.scale(image.load(self.sprite_image), (self.size_x, self.size_y))
    def set_boom(self, cor_x, cor_y):
        boom = Boom('Boom_anim/1.png', cor_x, cor_y, 100, 100, 5)
        booms_group.add(boom)


class Boom(GameSprite):
    def __init__(self, sprite_image, pos_x, pos_y, size_x, size_y, speed):
        super().__init__(sprite_image, pos_x, pos_y, size_x, size_y, speed)
        self.anim_boom = ['Boom_anim/1.png', 'Boom_anim/2.png', 'Boom_anim/3.png', 'Boom_anim/4.png',
                          'Boom_anim/5.png', 'Boom_anim/6.png', 'Boom_anim/7.png', 'Boom_anim/8.png',
                          'Boom_anim/9.png', 'Boom_anim/10.png', 'Boom_anim/11.png', 'Boom_anim/12.png',
                          'Boom_anim/13.png', 'Boom_anim/14.png', 'Boom_anim/15.png', 'Boom_anim/16.png',
                          'Boom_anim/17.png', 'Boom_anim/18.png', 'Boom_anim/19.png', 'Boom_anim/20.png',
                          'Boom_anim/21.png', 'Boom_anim/22.png', 'Boom_anim/23.png', 'Boom_anim/24.png',
                          'Boom_anim/25.png', 'Boom_anim/26.png', 'Boom_anim/27.png', 'Boom_anim/28.png',
                          'Boom_anim/29.png', 'Boom_anim/30.png', 'Boom_anim/31.png', 'Boom_anim/32.png',
                          'Boom_anim/33.png', 'Boom_anim/34.png', 'Boom_anim/35.png', 'Boom_anim/36.png',
                          'Boom_anim/37.png', 'Boom_anim/38.png', 'Boom_anim/39.png', 'Boom_anim/40.png',
                          'Boom_anim/41.png', 'Boom_anim/42.png', 'Boom_anim/43.png', 'Boom_anim/44.png',
                          'Boom_anim/45.png', 'Boom_anim/46.png', 'Boom_anim/47.png', 'Boom_anim/48.png']
        self.anim_counter = 0

    def update(self):
        if self.anim_counter >= 47:
            self.kill()
            self.anim_counter = 0
        self.image = transform.scale(image.load(self.anim_boom[self.anim_counter]), (100, 100))
        window.blit(self.image, (self.rect.x, self.rect.y))
        self.anim_counter += 1
        self.rect.y += self.speed

class Stars(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > win_height + 200:
            self.rect.x = randint(0, win_width)
            self.rect.y = 0
            self.speed = randint(4, 15)



win_width = 1300
win_height = 1000
window = display.set_mode((win_width, win_height))
display.set_caption('space_game')



background = transform.scale(image.load('fon.png'), (win_width, win_height))
background_2 = transform.scale(image.load('fon_2.png'), (win_width, win_height))


player = Player('Player_anim_v2/player_1.png', 500, 800, 120, 150, 10)


hearts_group = sprite.Group()

pos_x_for_heart = 400

health = 3
for i in range(health):
    heart = GameSprite('heart.png', pos_x_for_heart, 100, 50, 50)
    hearts_group.add(heart)
    pos_x_for_heart -= 50

pos_x_for_heart = 450

hover_button = mixer.Sound('Sounds/hover_button.ogg')
hover_button.set_volume(0.2)

click_button = mixer.Sound('Sounds/click_sound.ogg')
click_button.set_volume(0.7)

GUI = GUI(window, win_width, win_height, hover_button, click_button)

health_box_group = sprite.Group()
upgrade_box_group = sprite.Group()


bullets_group = sprite.Group()
asteroids_group = sprite.Group()
booms_group = sprite.Group()

for i in range(10):
    rand_size = randint(30, 50)
    asteroid = Asteroid('asteroid.png', randint(0, 1300), randint(-500, - 30), rand_size, rand_size, randint(10, 13))
    asteroids_group.add(asteroid)

stars_group = sprite.Group()
for i in range(1, 50):
    star = Stars('star.png', randint(0, win_width), randint(0, win_height), randint(1, 30), randint(1, 30), randint(4, 15))
    stars_group.add(star)


mixer.music.load('Sounds/music_fon.mp3')
#mixer.music.play(-1)
mixer.music.set_volume(0.2)
fire_sound = mixer.Sound('Sounds/fire_sound.ogg')
fire_sound.set_volume(1)
fly_sound = mixer.Sound('Sounds/fly_sound.ogg')
fly_sound.set_volume(0.08)
#fly_sound.play(-1)
boom_sound = mixer.Sound('Sounds/Boom_sound.ogg')
boom_sound.set_volume(0.15)
upgrade_sound = mixer.Sound('Sounds/upgrade_sound.ogg')
upgrade_sound.set_volume(0.5)
health_sound = mixer.Sound('Sounds/health_sound.ogg')
health_sound.set_volume(0.7)

clock = time.Clock()
FPS = 60
game = True
finish_game = False


kills = 0
kills_record = 0


my_font = font.Font('Шрифт/VIVL Rail/vivl-rail.otf', 45)

drop_box = 0
true_box = False
rand_num = randint(150, 300)
rand_num_2 = randint(150, 400)

move_bg = 0
move_bg_2 = - win_height

delay_fire = 20
fire_counter = delay_fire
play_boom = 0
fire_true = True

alpha_volume = 0

main_menu_true = True

while game:

    if not finish_game:
        events = event.get()
        for ev in events:
            if ev.type == QUIT:
                game = False
                pygame.quit()
                exit()
            GUI.button_Restart.check_click_mouse(ev)
            GUI.button_Start.check_click_mouse(ev)
            GUI.button_Quit.check_click_mouse(ev)
            GUI.button_Quit_before_death.check_click_mouse(ev)
        if key.get_pressed()[K_SPACE] and health > 0:
            if fire_counter == delay_fire:
                player.fire()
                fire_counter = 0
        if fire_counter < delay_fire:
            fire_counter += 1



        window.blit(background_2, (0, move_bg_2))
        window.blit(background, (0, move_bg))
        move_bg += 1
        move_bg_2 += 1

        if move_bg > win_height:
            move_bg = - win_height
        elif move_bg_2 > win_height:
            move_bg_2 = - win_height

        if play_boom > 0:
            booms_group.update()
            play_boom -= 1


        health_text = my_font.render('ЖИЗНИ:  ', True, (0, 196, 16))

        death_text = my_font.render('ПРОИГРЫШ', True, (190, 34, 34))
        death_text.set_alpha(alpha_volume)
        d_text_rect = death_text.get_rect()

        kills_text = my_font.render('СБИТО:  ' + str(kills), True, (20, 0, 190))
        k_text_rect = kills_text.get_rect()

        record_kills_text = my_font.render('РЕКОРД:  ' + str(kills_record), True, (218,165,32))
        rk_text_rect = record_kills_text.get_rect()

        stars_group.update()
        stars_group.draw(window)

        asteroids_group.draw(window)
        asteroids_group.update()


        if main_menu_true:
            GUI.draw_main_menu(mouse.get_pos())

            if GUI.button_Start.check_clicked():
                main_menu_true = False
                mixer_music.play(-1)
                fly_sound.play(-1)
            elif GUI.button_Quit.check_clicked():
                game = False
                pygame.quit()
                exit()


        elif health > 0:

            hearts_group.draw(window)
            collide_player_aster = sprite.spritecollide(player, asteroids_group, True)

            if collide_player_aster:
                health -= 1
                player.lvl = 1
                pos_x_for_heart -= 50
                for i in hearts_group:
                    pos_x_ = 0
                    for heart in hearts_group:
                        if heart.rect.x > pos_x_:
                            pos_x_ = heart.rect.x
                            heart_for_kill = heart
                    if collide_player_aster:
                        heart_for_kill.kill()
                        break


                boom_sound.play()
                for sp in collide_player_aster:
                    play_boom = 48
                    asteroid.set_boom(sp.rect.x - 30, sp.rect.y - 40)
                    boom_sound.play()
                    rand_size = randint(30, 50)
                    asteroid = Asteroid('asteroid.png', randint(0, 1300), randint(-500, - 30),
                                        rand_size, rand_size, randint(10, 13))

                    asteroids_group.add(asteroid)

            collide_bull_aster = sprite.groupcollide(bullets_group, asteroids_group, True, True)

            for sp in collide_bull_aster:
                kills += 1

                play_boom = 48
                asteroid.set_boom(sp.rect.x - 30, sp.rect.y - 40)
                boom_sound.play()

                rand_size = randint(30, 50)
                asteroid = Asteroid('asteroid.png', randint(0, 1300), randint(-500, - 30), rand_size, rand_size,
                                    randint(10, 13))
                asteroids_group.add(asteroid)


            #HealthBox
            if drop_box > rand_num and drop_box < 500:
                true_box = True
                drop_box += 1
            elif drop_box == 500:
                rand_num = randint(150, 300)
                drop_box = 0
                health_box = HealthBox('HealthBox_2.png', win_width, win_height, 70, 70, 5)
                health_box_group.add(health_box)

            else:
                drop_box += 1

            if true_box:
                health_box_group.update()

            #UpgradeBox
            if drop_box > rand_num_2 and drop_box < 500:
                true_box = True
                drop_box += 1
            elif drop_box == 500:
                rand_num_2 = randint(150, 300)
                drop_box = 0
                upgrade_box = HealthBox('UpgradeBox.png', win_width, win_height, 70, 70, 5)
                upgrade_box_group.add(upgrade_box)

            else:
                drop_box += 1

            if true_box:
                upgrade_box_group.update()
            print('Привет!')
            print('Еще что-то')

            collide_plr_health = sprite.spritecollide(player, health_box_group, True)
            if collide_plr_health:
                if len(hearts_group) < 3:
                    health_sound.play()
                    health += 1
                    heart = GameSprite('heart.png', pos_x_for_heart, 100, 50, 50)
                    hearts_group.add(heart)
                    pos_x_for_heart += 50

            collide_plr_upgrade = sprite.spritecollide(player, upgrade_box_group, True)
            if collide_plr_upgrade and player.lvl < 5:
                player.lvl += 1
                upgrade_sound.play()


            window.blit(health_text, (100, 100))
            window.blit(kills_text, (100, 200))
            player.control()
            player.animation()

            health_box_group.draw(window)
            upgrade_box_group.draw(window)
            bullets_group.draw(window)
            bullets_group.update()
        else:
            finish_game = GUI.button_Restart.check_clicked()
            fly_sound.stop()
            mixer.music.fadeout(4000)
            player.kill()
            for i in bullets_group:
                i.kill()

            if alpha_volume < 255:
                alpha_volume += 2
            death_text.set_alpha(alpha_volume)
            kills_text.set_alpha(alpha_volume)
            record_kills_text.set_alpha(alpha_volume)
            window.blit(death_text, (win_width/2 - (d_text_rect.width/2), win_height/3))
            window.blit(kills_text, (win_width/2 - (k_text_rect.width/2), win_height/3 - 200))

            if kills_record < kills:
                kills_record = kills
            window.blit(record_kills_text, (win_width / 2 - (rk_text_rect.width / 2), win_height / 3 - 150))

            GUI.draw_death_menu(mouse.get_pos(), alpha_volume)
            if GUI.button_Quit_before_death.check_clicked():
                game = False
                pygame.quit()
                exit()

        display.flip()

    else:

        for i in asteroids_group:
            i.kill()
        for i in booms_group:
            i.kill()
        health = 3
        kills = 0
        pos_x_for_heart = 400
        for i in range(health):
            heart = GameSprite('heart.png', pos_x_for_heart, 100, 50, 50)
            hearts_group.add(heart)
            pos_x_for_heart -= 50
        pos_x_for_heart = 450

        for i in range(10):
            rand_size = randint(30, 50)
            asteroid = Asteroid('asteroid.png', randint(0, 1300), randint(-500, - 30), rand_size, rand_size,
                                randint(10, 13))
            asteroids_group.add(asteroid)
        player = Player('Player_anim_v2/player_1.png', 500, 800, 120, 150, 10)
        fly_sound.play(-1)
        mixer.music.play()
        alpha_volume = 0
        finish_game = False
    clock.tick(FPS)

