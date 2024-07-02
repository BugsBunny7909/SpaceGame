import pygame
from random import randint


class GameSprite(pygame.sprite.Sprite):
    def __init__(self, sprite_image, win_width, win_height, size_x, size_y, speed=0):
        super().__init__()

        self.speed = speed
        self.size_x = size_x
        self.size_y = size_y
        self.win_width = win_width
        self.win_height = win_height

        self.sprite_image = sprite_image
        self.image = pygame.transform.scale(pygame.image.load(self.sprite_image), (self.size_x, self.size_y))

        self.rect = self.image.get_rect()
        self.rect.x = randint(10, win_width)
        self.rect.y = - 100


class HealthBox(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > self.win_height:
            self.kill()