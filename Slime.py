from Enemies import enemy
import pygame


class slime(enemy):
    def __init__(self, x, y, Vel, Path):
        super().__init__(x, y, 50, 50, Path)

    def draw(self, win):
        pygame.draw.rect(win, (0, 200, 0), self.rect)
