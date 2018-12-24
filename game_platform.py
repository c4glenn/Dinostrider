import pygame
from sprite import Sprite


class Platform(Sprite):
    def __init__(self, rect, color, vel, friction, bounds=None):
        self.rect = rect
        super().__init__(self.rect.x, self.rect.y, self.rect.height,
                         self.rect.width)
        self.color = color
        self.vel = vel
        self.bounds = bounds
        self.friction = friction

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        # if self.bounds:
        #     if self.pos.x + (self.rect.width // 2) > self.bounds.right:
        #         self.facing_left = True
        #         self.vel.x = -self.vel.x
        #     if self.pos.x < self.bounds.left:
        #         self.facing_left = False
        #         self.vel.x = -self.vel.x
        #     self.pos += self.vel
        # self.rect.topleft = self.pos
        pass

    @classmethod
    def from_list(cls, params):
        try:
            return cls(params[0], params[1], params[2], params[3], params[4])
        except:
            return cls(params[0], params[1], params[2], params[3])
