import pygame
vec = pygame.math.Vector2


class Sprite(pygame.sprite.Sprite):
    def __init__(self, startX, startY):
        pygame.sprite.Sprite.__init__(self)
        self.pos = vec(startX, startY)

    def draw(self, win):
        pass
