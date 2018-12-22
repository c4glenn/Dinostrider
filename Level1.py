import pygame

from Level import level
from game_platform import Platform


class level1(level):
    def __init__(self, screen_height, screen_width):
        super().__init__(screen_height, screen_width)
        self.platforms.empty()
        self.platforms.add(
            Platform(0, self.screen_height - 20, (self.screen_width // 2) - 40,
                     20, (0, 0, 0), 0, 0))  # level 1
        self.platforms.add(
            Platform((self.screen_width // 2) + 40, self.screen_height - 20,
                     (self.screen_width // 2) - 40, 20, (0, 0, 0), 0,
                     0))  # level 1
        self.platforms.add(
            Platform(self.screen_width // 2 - 20,
                     self.screen_height // 2 + 100, 70, 30, (0, 0, 0), 0,
                     0))  # level 1

    def draw(self, win):
        for platform in self.platforms:
            platform.draw(win)
