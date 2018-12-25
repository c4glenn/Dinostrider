import pygame

from Level import level
from game_platform import Platform
from Slime import slime  #or whatever enemy ur using
from sprite import vec


class level1(level):
    def __init__(self, screen_height, screen_width):
        super().__init__(screen_height, screen_width)
        self.background = pygame.image.load(
            'Images/bg.jpg')  # where to get the background from
        self.platforms.empty()
        self.enemys.empty()
        self.dino_gun = False  # should he have a gun
        self.level_limit = -1000  #changes per level
        level_platforms = [[
            pygame.Rect(0, screen_height - 25,
                        (self.screen_width - self.level_limit), 25), (0, 0, 0),
            0, -0.12
        ],
                           [
                               pygame.Rect(
                                   300, screen_height - 65,
                                   (self.screen_width - self.level_limit), 40),
                               (0, 0, 0), 0, -0.12
                           ]]  #populate with platforms

        for platform in level_platforms:
            self.platforms.add(Platform.from_list(platform))

        # self.enemys.add(
        #     slime(700, 445, vec(3, 0),
        #           pygame.Rect(600, 400, 200, 40)))  #customise and add more

    def get_player_start_position(self):  #per level
        return (10, 410)