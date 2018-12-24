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
        for platform in self.platforms:
            platform.rect.x += shift_x
            if platform.bounds:
                platform.bounds.x += shift_x
                platform.bounds.y += shift_y

        for enemy in self.enemys:
            enemy.pos.x += shift_x
            enemy.pos.y += shift_y
            enemy.bounds.x += shift_x
            enemy.bounds.y += shift_y
