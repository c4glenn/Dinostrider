from sprite import FacingSprite
from sprite import VEC

STARTING_HEALTH = 3
KNOCKBACK_DISTANCE = 20


class Enemy(FacingSprite):
    def __init__(self,
                 x,
                 y,
                 width,
                 height,
                 walking_path,
                 image_dir,
                 vel=VEC(0, 0)):
        super().__init__(x, y, height, width, image_dir, vel)
        self.bounds = walking_path
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
