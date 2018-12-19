import pygame
from sprite import Sprite
from sprite import vec


class Player(Sprite):
    def __init__(self, startX, startY, game):
        super().__init__(startX, startY)
        self.game = game
        self.Player_acc = 0.5
        self.vel = vec(0, 0)
        self.grav = 0.8
        self.acc = vec(0, self.grav)
        self.isJump = False
        self.jumpCount = 0
        self.left = False
        self.right = False
        self.walkCount = 0
        self.standing = True
        self.hitbox = (self.pos.x + 17, self.pos.y + 11, 29, 52)
        self.footbox = (self.pos.x + 19, self.pos.y + 50, 16, 4)
        self.width = 64
        self.height = 64
        self.walkRight = self.load('Images/Dino/Right/*.png')
        self.walkLeft = self.load('Images/Dino/Left/*.png')
        self.heart = self.load('Images/Dino/*.png')
        self.gun = False
        self.touching_platform = False
        self.friction = -0.12
        self.hearts = 3

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
        self.rect.x = self.pos.x + 17
        self.rect.y = self.pos.y + 11
        #self.getHearts(win)
        #pygame.draw.rect(win, (255,0,0), self.hitbox, 2)
        #pygame.draw.rect(win, (255,0,0), self.footbox, 2)

    def hit(self):
        self.walkCount = 0

    def move_left(self):
        self.acc = vec(0, self.grav)
        self.acc.x = -self.Player_acc
        self.left = True
        self.right = False
        self.standing = False

    def move_right(self):
        self.acc = vec(0, self.grav)
        self.acc.x = self.Player_acc
        self.left = False
        self.right = True
        self.standing = False

    def stop(self):
        self.acc = vec(0, self.grav)
        self.standing = True
        self.walkCount = 0

    def jump(self):
        if self.jumpCount < 2:
            self.walkCount = 0
            self.vel.y = -15
            self.jumpCount += 1
            print('jumped')

    def touchDown(self):
        self.vel.y = 0
        if self.pos.y <= self.game.hits[0].rect.top:
            self.pos.y = self.game.hits[0].rect.top - 50
            self.jumpCount = 0
        if self.pos.y >= self.game.hits[0].rect.bottom:
            self.pos.y = self.game.hits[0].rect.bottom + 17

    def update_location(self, screen_height, screen_width):
        self.acc.y = self.grav

        self.acc.x += self.vel.x * self.friction

        self.vel += self.acc
        print(self.vel)
        self.pos += self.vel + 0.5 * self.acc
        if self.pos.x + self.width > screen_width:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = screen_width - self.width
        self.acc = vec(0, self.grav)

    def getHearts(self, win):
        for x in range(0, self.hearts):
            print("Width:", win.get_width())
            win.blit(self.heart[0], win.get_width() - 40, 0)
