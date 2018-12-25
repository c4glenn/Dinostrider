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
        self.dino_gun = False  # it shouldn't have a gun
        self.level_limit = -1300  #changes per level
        level_platforms = [
            [
                pygame.Rect(0, screen_height - 35,
                            screen_width - self.level_limit, 35),
                (0, 0, 0),
                0,
                -0.12  # ground
            ],
            [
                pygame.Rect(300, screen_height - 75, 217, 50),
                (0, 0, 0),
                0,
                -0.12  #first block
            ],
            [
                pygame.Rect(650, screen_height - 75, 615, 50),
                (0, 0, 0),
                0,
                -0.12  #second block
            ],
            [
                pygame.Rect(935, screen_height - 180, 60, 20),
                (0, 0, 0),
                0,
                -0.1  #special place ?what to put?
            ],
            [
                pygame.Rect(1347, screen_height - 130, 60, 20),
                (0, 0, 0),
                0,
                -0.12  #first air block
            ],
            [
                pygame.Rect(1500, screen_height - 180, 60, 20),
                (0, 0, 0),
                0,
                -0.12  #second air block
            ],
            [
                pygame.Rect(1660, screen_height - 230,
                            screen_width - self.level_limit, 205),
                (0, 0, 0),
                0,
                -0.12  #higher ground
            ]
        ]  #populate with platforms

        for platform in level_platforms:
            self.platforms.add(Platform.from_list(platform))

        # self.enemys.add(
        #     slime(920, 405, vec(0, 0),
        #           pygame.Rect(920, 405, 50, 60)))  #customise and add more

    def get_player_start_position(self):  #per level
        return (10, 410)