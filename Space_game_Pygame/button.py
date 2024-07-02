import pygame

class Button:
    def __init__(self, image_path, changed_image_path, pos_x, pos_y, size_x, size_y, text='', hover_sound=None, click_sound = None, style_txt=None, size_txt=40):

        self.width = size_x
        self.height = size_y
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect(topleft=(pos_x, pos_y))

        self.changed_image = pygame.image.load(changed_image_path)
        self.changed_image = pygame.transform.scale(self.changed_image, (self.width, self.height))
        self.is_pointing = False
        self.current_image = self.image
        self.font = pygame.font.Font(style_txt, size_txt)
        self.text = self.font.render(text, True, (0, 0, 0))
        self.text_rect = self.text.get_rect()
        self.hover_sound = hover_sound
        self.click_sound = click_sound
        self.true_play = True
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

    def play_sound(self):
        self.hover_sound.play()
    def check_pointing(self, mouse_pos):
        self.is_pointing = self.rect.collidepoint(mouse_pos)
        return self.is_pointing


    def check_click(self, event):
        if self.is_pointing:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.click_sound.play()
                return True
                pygame.event.post(pygame.event.Event(pygame.USEREVENT, button=self))





