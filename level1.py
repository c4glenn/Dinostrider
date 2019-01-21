import pygame

from level import Level
from game_platform import Platform


class Level1(Level):
    def __init__(self, screen_height, screen_width):
        super().__init__(screen_height, screen_width)
        self.background = pygame.image.load(
            'Images/bg.jpg')  # where to get the background from
        self.platforms.empty()
        self.enemys.empty()
        self.dino_gun = False  # it shouldn't have a gun
        self.level_limit = -3530  #changes per level
        level_platforms = [
            [
                pygame.Rect(-5, 0, 5, screen_height),
                (0, 0, 0),
                0,
                -0.12  # left safety wall
            ],
            [
                pygame.Rect(0, screen_height - 40, 1960, 40),
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
                pygame.Rect(1660, screen_height - 230, 100, 205),
                (0, 0, 0),
                0,
                -0.12  #high ground
            ],
            [
                pygame.Rect(2100, screen_height - 40, 400, 40),
                (0, 0, 0),
                0,
                -0.12  # ground
            ],
            [
                pygame.Rect(2640, screen_height - 70, 60, 30),
                (0, 0, 0),
                0,
                -0.12  # air platform
            ],
            [
                pygame.Rect(2880, screen_height - 40, 200, 40),
                (0, 0, 0),
                0,
                -0.12  # ground
            ],
            [
                pygame.Rect(3047, screen_height - 130, 60, 20),
                (0, 0, 0),
                0,
                -0.12  #first air block
            ],
            [
                pygame.Rect(3200, screen_height - 180, 60, 20),
                (0, 0, 0),
                0,
                -0.12  #second air block
            ],
            [
                pygame.Rect(3360, screen_height - 230, 100, 205),
                (0, 0, 0),
                0,
                -0.12  #high ground
            ],
            [
                pygame.Rect(3360, screen_height - 40,
                            screen_width - self.level_limit, 40),
                (0, 0, 0),
                0,
                -0.12  # ground
            ],
        ]  #populate with platforms

        for platform in level_platforms:
            self.platforms.add(Platform.from_list(platform))

        # self.enemys.add(
        #     slime(920, 405, vec(0, 0),
        #           pygame.Rect(920, 405, 50, 60)))  #customise and add more

    def get_player_start_position(self):  #per level
        return (10, 410)
