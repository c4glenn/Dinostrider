from sprite import FacingSprite
import pygame
from sprite import vec

STARTING_HEALTH = 3
KNOCKBACK_DISTANCE = 20


class enemy(FacingSprite):
    def __init__(self, x, y, width, height, path, vel=vec(0, 0)):
        super().__init__(x, y, height, width, 'Images/Goblin', vel)
        self.bounds = path
        self.health = STARTING_HEALTH

    def die(self):
        self.kill()

    def knockback(self, left):
        if left:
            self.pos.x -= KNOCKBACK_DISTANCE
        else:
            self.pos.x += KNOCKBACK_DISTANCE
        self.update_rectangle()

    def hit(self):
        self.health -= 1
        if self.health <= 0:
            self.die()
