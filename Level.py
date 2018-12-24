import pygame


class level(object):
    def __init__(self, screen_height, screen_width):
        self.platforms = pygame.sprite.Group()
        self.enemys = pygame.sprite.Group()
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.world_shift_x = 0
        self.world_shift_y = 0

    def draw(self, win):
        self.update(win)

    def update(self, win):
        for platform in self.platforms:
            platform.move()
            platform.draw(win)
        for enemy in self.enemys:
            enemy.move()
            enemy.draw(win)

    def shift_world(self, shift_x, shift_y):
        self.world_shift_x += shift_x
        self.world_shift_y += shift_y
