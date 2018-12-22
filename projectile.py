import pygame
from sprite import Sprite


class Projectile(Sprite):
    def __init__(self, x, y, radius, color, facing):
        super().__init__(x, y, radius * 2, radius * 2)
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (int(self.pos.x), int(self.pos.y)),
                           self.radius)
        self.update_rectangle()
        #pygame.draw.rect(win, (255, 0, 0), self.rect)
