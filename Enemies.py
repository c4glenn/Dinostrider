from sprite import Sprite
import pygame


class enemy(Sprite):
    def __init__(self, x, y, width, height, path):
        super().__init__(x, y, height, width)