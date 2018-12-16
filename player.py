import os
import pygame
from sprite import Sprite


def load(path, type, extension):
    total = []
    if type == 'image':
        for x in range(1, 10):
            img_path = os.path.join(path, str(x) + extension)
            total.append(pygame.image.load(img_path))
    elif type == 'sound':
        pass
    print(total)
    return total


class Player(Sprite):
    def __init__(self, startX, startY):
        super().__init__(startX, startY)
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.standing = True
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        self.footbox = (self.x + 19, self.y + 50, 16, 4)
        self.width = 64
        self.height = 64
        self.walkRight = load('Images/Dino/Right', 'image', '.png')
        self.walkLeft = load('Images/Dino/Left', 'image', '.png')
        self.gun = False

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if not (self.standing):
            if self.left:
                win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                win.blit(self.walkRight[0], (self.x, self.y))
            else:
                win.blit(self.walkLeft[0], (self.x, self.y))
        self.hitbox = (self.x + 3, self.y + 5, 52, 48)
        self.footbox = (self.x + 19, self.y + 50, 16, 4)
        #pygame.draw.rect(win, (255,0,0), self.hitbox, 2)
        #pygame.draw.rect(win, (255,0,0), self.footbox, 2)

    def hit(self):
        self.x = 60
        self.y = 410
        self.walkCount = 0
        font1 = pygame.font.SysFont('Arial', 100)
        text = font1.render('-5', 1, (255, 0, 0))
        win.blit(text, (250 - (text.get_width() / 2), 200))
        pygame.display.update()
        i = 0
        while i < 300:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()
        self.jumpCount = 0
        self.isJump = False

    def move_left(self):
        self.x -= self.vel
        if self.x < 0:
            self.x = 0
        self.left = True
        self.right = False
        self.standing = False

    def move_right(self, screen_width):
        self.x += self.vel
        if (self.x + self.width) > screen_width:
            self.x = screen_width - self.width
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

    def update_location(self, screen_height):
        if self.isJump:
            if self.jumpCount >= -10:
                neg = 1
                if self.jumpCount < 0:
                    neg = -1
                change = (self.jumpCount**2) * 0.5 * neg
                if self.y - change + self.height < screen_height:
                    self.y -= change
                    self.jumpCount -= 1
                else:
                    self.isJump = False
                    self.jumpCount = 10
            else:
                self.isJump = False
                self.jumpCount = 10
