import pygame

from Level import level
from game_platform import Platform


class level1(level):
    def __init__(self, screen_height, screen_width):
        super().__init__(screen_height, screen_width)
        self.background = pygame.image.load('Images/bg.jpg')
        self.platforms.empty()
        self.platforms.add(
            Platform(0, self.screen_height - 40, (self.screen_width // 2) - 40,
                     40, (0, 0, 0), 0, 0, -0.12))  # level 1
        self.platforms.add(
            Platform((self.screen_width // 2) + 40, self.screen_height - 40,
                     (self.screen_width // 2) - 40, 40, (0, 0, 0), 0, 0,
                     -0.12))  # level 1
        self.platforms.add(
            Platform(self.screen_width // 2 - 20, self.screen_height // 2 + 90,
                     70, 30, (0, 0, 0), 0, 0, -0.12))  # level 1

    def draw(self, win):
        for platform in self.platforms:
            platform.draw(win)
