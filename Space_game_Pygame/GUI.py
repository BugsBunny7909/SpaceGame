from pygame import *


class Button:
    def __init__(self, image_path, changed_image_path, pos_x, pos_y, size_x, size_y, text='',
                 hover_sound=None, click_sound=None, style_txt=None, size_txt=40, transparent=False):

        self.width = size_x
        self.height = size_y
        self.image = image.load(image_path)
        self.image = transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect(topleft=(pos_x, pos_y))
        self.changed_image = image.load(changed_image_path)
        self.changed_image = transform.scale(self.changed_image, (self.width, self.height))
        self.current_image = self.image
        self.font = font.Font(style_txt, size_txt)
        self.text = self.font.render(text, True, (0, 0, 0))
        self.text_rect = self.text.get_rect()
        self.hover_sound = hover_sound
        self.click_sound = click_sound
        self.true_play = True
        self.clicked = False
        self.is_pointing = False
        if transparent:
            self.image.set_alpha(0)
            self.changed_image.set_alpha(0)
            self.text.set_alpha(0)

    def draw(self, window):
        if self.is_pointing:
            self.current_image = self.changed_image
        else:
            self.current_image = self.image
        window.blit(self.current_image, self.rect.topleft)
        window.blit(self.text, (self.rect.centerx - self.text_rect.width/2, self.rect.centery - self.text_rect.height/2))

        if not self.is_pointing:
            self.true_play = True
        elif self.is_pointing and self.true_play:
            self.hover_sound.play()
            self.true_play = False

    def check_pointing(self, mouse_pos):
        self.is_pointing = self.rect.collidepoint(mouse_pos)
        return self.is_pointing

    def check_click_mouse(self, event):
        if self.is_pointing:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                self.clicked = True
            else:
                self.clicked = False

    def check_clicked(self):
        if self.is_pointing and self.clicked:
            self.click_sound.play()
            return True

    def emergence(self, alpha_volume):
        self.image.set_alpha(alpha_volume)
        self.changed_image.set_alpha(alpha_volume)
        self.text.set_alpha(alpha_volume)


class GUI:
    def __init__(self, window, win_width, win_height, hover_sound=None, click_sound=None):

        self.window = window

        self.button_Start = Button('btn_true.png', 'btn_false.png',
                                   win_width/2-250, 400, 500, 180,
                                   'СТАРТ', hover_sound, click_sound, 'Шрифт/VIVL Rail/vivl-rail.otf')

        self.button_Restart = Button('btn_true.png', 'btn_false.png',
                                     win_width/2-250, 500, 500, 180,
                                     'ЗАНОВО', hover_sound, click_sound, 'Шрифт/VIVL Rail/vivl-rail.otf',
                                     40, True)

        self.button_Quit_before_death = Button('btn_true.png', 'btn_false.png',
                                               win_width / 2 - 250, 700, 500, 180,
                                               'ВЫХОД', hover_sound, click_sound, 'Шрифт/VIVL Rail/vivl-rail.otf',
                                               40, True)

        self.button_Quit = Button('btn_true.png', 'btn_false.png',
                                  win_width/2-250, 600, 500, 180,
                                  'ВЫХОД', hover_sound, click_sound, 'Шрифт/VIVL Rail/vivl-rail.otf')

    def draw_main_menu(self, mouse_pos):
        self.button_Start.check_pointing(mouse_pos)
        self.button_Start.draw(self.window)

        self.button_Quit.check_pointing(mouse_pos)
        self.button_Quit.draw(self.window)

    def draw_death_menu(self, mouse_pos, alpha_volume):
        self.button_Restart.emergence(alpha_volume)
        self.button_Restart.check_pointing(mouse_pos)
        self.button_Restart.draw(self.window)

        self.button_Quit_before_death.emergence(alpha_volume)
        self.button_Quit_before_death.check_pointing(mouse_pos)
        self.button_Quit_before_death.draw(self.window)
