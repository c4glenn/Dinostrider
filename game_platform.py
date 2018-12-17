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
        self.path = (self.pos.x, self.end)

    def draw(self, win):
        self.move()
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y
        pygame.draw.rect(win, self.color,
                         (self.pos.x, self.pos.y, self.width, self.height))

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