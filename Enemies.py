from sprite import FacingSprite
import pygame
from sprite import vec


class enemy(FacingSprite):
    def __init__(self, x, y, width, height, path, vel=vec(0, 0)):
        super().__init__(x, y, height, width, 'Images/Goblin', vel)
        self.bounds = path

    def die(self):
        self.kill()

    def knockback(self, left):
        if left:
            self.pos.x -= 20
        else:
            self.pos.x += 20
        self.update_rectangle()
