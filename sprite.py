import glob
import pygame

vec = pygame.math.Vector2


class Sprite(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y, height, width):
        #pygame.sprite.Sprite.__init__(self)
        super().__init__()
        self.pos = vec(start_x, start_y)
        self.rect = pygame.Rect(start_x, start_y, width, height)
        self.bounds = None

    def draw(self, win):
        pass

    def load(self, path):
        total = []
        files = glob.glob(path)
        for file in files:
            total.append(pygame.image.load(file))
        return total

    def update_rectangle(self):
        self.rect.midbottom = self.pos

    def move_bounce(self):
        if self.bounds:
            if self.pos.x + self.rect.width > self.bounds.right:
                pass
            if self.pos.x < self.bounds.left:
                pass


class FacingSprite(Sprite):
    def __init__(self, start_x, start_y, height, width, imagesDir):
        super().__init__(start_x, start_y, height, width)
        self.images_right = self.load(imagesDir + '/Right/*.png')
        self.images_left = self.load(imagesDir + '/Left/*.png')
        self.facing_left = False
        self.walk_count = 0

    def draw(self, win):
        if self.walk_count + 1 >= 27:
            self.walk_count = 0
        if self.facing_left:
            win.blit(self.images_left[self.walk_count // 3], self.rect.topleft)
            self.walk_count += 1
        else:
            win.blit(self.images_right[self.walk_count // 3],
                     self.rect.topleft)
            self.walk_count += 1