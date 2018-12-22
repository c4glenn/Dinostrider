import pygame

from Level import level
from game_platform import Platform
from Slime import slime


class level1(level):
    def __init__(self, screen_height, screen_width):
        super().__init__(screen_height, screen_width)
        self.background = pygame.image.load('Images/bg.jpg')
        self.platforms.empty()
        self.enemys.empty()
        self.platforms.add(
            Platform(0, self.screen_height - 40,
                     (self.screen_width // 2) - 200, 40, (0, 0, 0), 0, 0,
                     -0.099))  # level 1
        self.platforms.add(
            Platform(0, self.screen_height - 300,
                     (self.screen_width // 2) - 200, 40, (0, 0, 0), 0, 0,
                     -0.099))  # level 1
        self.platforms.add(
            Platform((self.screen_width // 2) + 200, self.screen_height - 40,
                     (self.screen_width // 2) - 40, 40, (0, 0, 0), 0, 0,
                     -0.099))  # level 1
        self.platforms.add(
            Platform(self.screen_width // 2 - 150,
                     self.screen_height // 2 + 150, 100, 30, (0, 0, 0), 0, 0,
                     -0.12))  # level 1
        self.platforms.add(
            Platform(self.screen_width // 2 - 50,
                     self.screen_height // 2 + 100, 100, 30, (0, 0, 0), 0, 0,
                     -0.12))  # level 1
        self.platforms.add(
            Platform(self.screen_width // 2 + 50, self.screen_height // 2 + 50,
                     100, 30, (0, 0, 0), 0, 0, -0.12))  # level 1
        self.enemys.add(slime(700, 390, 0, 0))

    def draw(self, win):
        for platform in self.platforms:
            platform.draw(win)
