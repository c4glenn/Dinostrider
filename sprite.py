import glob
import pygame

vec = pygame.math.Vector2


class Sprite(pygame.sprite.Sprite):
    def __init__(self, startX, startY):
        pygame.sprite.Sprite.__init__(self)
        self.pos = vec(startX, startY)

    def draw(self, win):
        pass

    def load(self, path):
        total = []
        files = glob.glob(path)
        for file in files:
            total.append(pygame.image.load(file))
        return total