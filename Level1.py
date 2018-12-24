import pygame

from Level import level
from game_platform import Platform
from Slime import slime
from sprite import vec


class level1(level):
    def __init__(self, screen_height, screen_width):
        super().__init__(screen_height, screen_width)
        self.background = pygame.image.load('Images/bg.jpg')
        self.platforms.empty()
        self.enemys.empty()
        self.level_limit = 1000
        half_screen_width = self.screen_width // 2
        level_platforms = [[
            pygame.Rect(0, self.screen_height - 40, half_screen_width - 200,
                        40), (0, 0, 0), 0, -0.099
        ],
                           [
                               pygame.Rect(0, self.screen_height - 300,
                                           (self.screen_width // 2) - 200, 40),
                               (0, 0, 0), 0, -0.099
                           ],
                           [
                               pygame.Rect((self.screen_width // 2) + 200,
                                           self.screen_height - 40,
                                           (self.screen_width // 2) - 40, 40),
                               (0, 0, 0), 0, -0.099
                           ],
                           [
                               pygame.Rect(self.screen_width // 2 - 150,
                                           self.screen_height // 2 + 150, 100,
                                           30), (0, 0, 0), 0, -0.12
                           ],
                           [
                               pygame.Rect(self.screen_width // 2 - 60,
                                           self.screen_height // 2 + 100, 100,
                                           30), (0, 0, 0), 0, -0.12
                           ],
                           [
                               pygame.Rect(self.screen_width // 2 + 50,
                                           self.screen_height // 2 + 50, 100,
                                           30), (0, 0, 0), 0, -0.12
                           ]]
        for platform in level_platforms:
            self.platforms.add(Platform.from_list(platform))

        self.enemys.add(
            slime(700, 445, vec(3, 0), pygame.Rect(600, 400, 200, 40)))
        self.enemys.add(
            slime(20, 185, vec(3, 0),
                  pygame.Rect(0, screen_height - 400, 200, 40)))

    def get_player_start_position(self):
        return (25, 410)