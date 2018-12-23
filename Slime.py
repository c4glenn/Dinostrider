from Enemies import enemy
import pygame


class slime(enemy):
    def __init__(self, x, y, Vel, Path):
        super().__init__(x, y, 50, 60, Path, Vel)

    def draw(self, win):
        super().draw(win)
