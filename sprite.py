import glob
import pygame

vec = pygame.math.Vector2


class Sprite(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y, height, width):
        #pygame.sprite.Sprite.__init__(self)
        super().__init__()
        self.pos = vec(start_x, start_y)
        self.rect = pygame.Rect(start_x, start_y, width, height)

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
