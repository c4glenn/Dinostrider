import pygame


class level(object):
    def __init__(self, screen_height, screen_width):
        self.platforms = pygame.sprite.Group()
        self.screen_height = screen_height
        self.screen_width = screen_width

    def draw(self, win):
        pass