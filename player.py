import os
import pygame
from sprite import *


def load(path, extension):
    total = []
    if extension == '.png':
        for x in range(1, 10):
            img_path = os.path.join(path, str(x) + extension)
            total.append(pygame.image.load(img_path))
    return total


class Player(Sprite):
    def __init__(self, startX, startY):
        super().__init__(startX, startY)
        self.Player_acc = 0.5
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.standing = True
        self.hitbox = (self.pos.x + 17, self.pos.y + 11, 29, 52)
        self.footbox = (self.pos.x + 19, self.pos.y + 50, 16, 4)
        self.width = 64
        self.height = 64
        self.walkRight = load('Images/Dino/Right', '.png')
        self.walkLeft = load('Images/Dino/Left', '.png')
        self.gun = False
        self.touching_platform = False
        self.grav = 5
        self.friction = -0.12

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if not self.standing:
            if self.left:
                win.blit(self.walkLeft[self.walkCount // 3],
                         (self.pos.x, self.pos.y))
                self.walkCount += 1
            elif self.right:
                win.blit(self.walkRight[self.walkCount // 3],
                         (self.pos.x, self.pos.y))
                self.walkCount += 1
        else:
            if self.right:
                win.blit(self.walkRight[0], (self.pos.x, self.pos.y))
            else:
                win.blit(self.walkLeft[0], (self.pos.x, self.pos.y))
        self.hitbox = (self.pos.x + 17, self.pos.y + 11, 29, 52)
        self.footbox = (self.pos.x + 19, self.pos.y + 50, 16, 4)
        self.image = pygame.Surface([29, 52])
        self.rect = self.image.get_rect()
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y
        #pygame.draw.rect(win, (255,0,0), self.hitbox, 2)
        #pygame.draw.rect(win, (255,0,0), self.footbox, 2)

    def hit(self):
        self.walkCount = 0

    def move_left(self):
        self.acc.x = -self.Player_acc

        #     self.x -= self.player_acc
        #     if self.x < 0:
        #         self.x = 0
        self.left = True
        self.right = False
        self.standing = False

    def move_right(self):
        self.acc.x = self.Player_acc
        # self.x += self.player_acc
        # if (self.x + self.width) > screen_width:
        #     self.x = screen_width - self.width
        self.left = False
        self.right = True
        self.standing = False

    def stop(self):
        self.standing = True
        self.walkCount = 0

    def jump(self):
        if not (self.isJump):
            self.isJump = True
            self.walkCount = 0

    def update_location(self, screen_height, screen_width):
        self.acc = vec(0, 0.5)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.move_left()
        if keys[pygame.K_RIGHT]:
            self.move_right()

        self.acc.x += self.vel.x * self.friction
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        if self.pos.x + self.width > screen_width:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = screen_width - self.width
