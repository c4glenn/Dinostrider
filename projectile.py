import pygame
from sprite import Sprite


class Projectile(Sprite):
    def __init__(self, x, y, radius, color, facing):
        super().__init__(x, y)
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)
