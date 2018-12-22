import pygame
from sprite import Sprite


class Platform(Sprite):
    def __init__(self, x, y, width, height, color, vel, end, friction):
        super().__init__(x, y, height, width)
        self.color = color
        self.vel = vel
        self.end = end
        self.path = (self.pos.x, self.end)
        self.friction = friction

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        if self.vel > 0:
            if self.pos.x + self.vel < self.path[1]:
                self.pos.x += self.vel
            else:
                self.vel = self.vel * -1
        else:
            if self.pos.x + self.vel > self.path[0]:
                self.pos.x += self.vel
            else:
                self.vel = self.vel * -1
