import glob
import pygame

VEC = pygame.math.Vector2


class Sprite(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y, height, width, vel=VEC(0, 0)):
        #pygame.sprite.Sprite.__init__(self)
        super().__init__()
        self.pos = VEC(start_x, start_y)
        self.rect = pygame.Rect(start_x, start_y, width, height)
        self.bounds = None
        self.draw_bounds = False
        self.draw_hitbox = False
        self.vel = vel

    def debug_draw(self, draw_bounds=False, draw_hitbox=False):
        self.draw_bounds = draw_bounds
        self.draw_hitbox = draw_hitbox

    def draw(self, win):
        if self.draw_bounds:
            pygame.draw.rect(win, (255, 0, 0), self.bounds, 2)
        if self.draw_hitbox:
            pygame.draw.rect(win, (255, 0, 0), self.rect, 1)

    def load(self, path):
        total = []
        files = glob.glob(path)
        for file in files:
            total.append(pygame.image.load(file))
        return total

    def update_rectangle(self):
        self.rect.midbottom = self.pos


class FacingSprite(Sprite):
    def __init__(self,
                 start_x,
                 start_y,
                 height,
                 width,
                 imagesDir=None,
                 vel=VEC(0, 0)):
        super().__init__(start_x, start_y, height, width, vel)
        if imagesDir:
            self.images_right = self.load(imagesDir + '/Right/*.png')
            self.images_left = self.load(imagesDir + '/Left/*.png')
        self.facing_left = False
        self.walk_count = 0

    def draw(self, win):
        super().draw(win)
        if self.walk_count + 1 >= 27:
            self.walk_count = 0

        win.blit(self._get_image(), self.rect.topleft)
        self.walk_count += 1

    def _get_image(self):
        if self.facing_left:
            return self.images_left[self.walk_count // 3]
        else:
            return self.images_right[self.walk_count // 3]

    def move(self):
        if self.bounds:
            if self.pos.x + (self.rect.width // 2) > self.bounds.right:
                self.facing_left = True
                self.vel.x = -self.vel.x
            if self.pos.x < self.bounds.left:
                self.facing_left = False
                self.vel.x = -self.vel.x

            self.pos += self.vel
        self.update_rectangle()

    def update(self):
        self.move()
