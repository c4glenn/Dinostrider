import glob
import pygame

vec = pygame.math.Vector2


class Sprite(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y, height, width, vel=vec(0, 0)):
        #pygame.sprite.Sprite.__init__(self)
        super().__init__()
        self.pos = vec(start_x, start_y)
        self.rect = pygame.Rect(start_x, start_y, width, height)
        self.bounds = None

    def draw(self, win):
        # pygame.draw.rect(win, (255, 0, 0), self.bounds, 2)
        # pygame.draw.rect(win, (255, 0, 0), self.rect, 1)
        pass

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
                 vel=vec(0, 0)):
        super().__init__(start_x, start_y, height, width, vel)
        if imagesDir:
            self.images_right = self.load(imagesDir + '/Right/*.png')
            self.images_left = self.load(imagesDir + '/Left/*.png')
        self.facing_left = False
        self.walk_count = 0
        self.vel = vel

    def draw(self, win):
        super().draw(win)
        if self.walk_count + 1 >= 27:
            self.walk_count = 0
        if self.facing_left:
            win.blit(self.images_left[self.walk_count // 3], self.rect.topleft)
            self.walk_count += 1
        else:
            win.blit(self.images_right[self.walk_count // 3],
                     self.rect.topleft)
            self.walk_count += 1

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
        sef.move()
