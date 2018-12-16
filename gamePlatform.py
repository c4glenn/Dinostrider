import pygame
from sprite import Sprite


class Platform(Sprite):
    def __init__(self, x, y, width, height, color, vel, end):
        super().__init__(x, y)
        self.width = width
        self.height = height
        self.color = color
        self.vel = vel
        self.end = end
        self.path = (self.x, self.end)

    def draw(self, win):
        self.move()
        pygame.draw.rect(win, self.color,
                         (self.x, self.y, self.width, self.height))

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
        else:
            if self.x + self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1