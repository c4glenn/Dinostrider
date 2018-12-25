import pygame

from Level import level
from game_platform import Platform
from Slime import slime  #or whatever enemy ur using
from sprite import vec


class leveltemplate(level):  #change to level#        EX: class level1(level):
    def __init__(self, screen_height, screen_width):
        super().__init__(screen_height, screen_width)
        self.background = pygame.image.load(
            'Images/bg.jpg')  # where to get the background from
        self.platforms.empty()
        self.enemys.empty()
        self.dino_gun = False  # should he have a gun
        self.level_limit = -700  #changes per level
        level_platforms = [(0, screen_height - 5, -self.level_limit, 5),
                           (0, 0, 0), 0,
                           -0.12]  #populate with platforms 1 example in there

        for platform in level_platforms:
            self.platforms.add(Platform.from_list(platform))

        self.enemys.add(
            slime(700, 445, vec(3, 0),
                  pygame.Rect(600, 400, 200, 40)))  #customise and add more

    def get_player_start_position(self):  #per level
        return (10, 410)