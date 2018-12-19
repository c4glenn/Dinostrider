import pygame
from sprite import Sprite
from sprite import vec


class Player(Sprite):
    def __init__(self, startX, startY):
        super().__init__(startX, startY, 64, 64)
        self.player_acc = 0.5
        self.vel = vec(0, 0)
        self.grav = 0.8
        self.acc = vec(0, self.grav)
        self.jump_count = 0
        self.left = False
        self.right = False
        self.walk_count = 0
        self.standing = True
        self.hitbox = (self.pos.x + 17, self.pos.y + 11, 29, 52)
        self.footbox = (self.pos.x + 19, self.pos.y + 50, 16, 4)
        self.images_right = self.load('Images/Dino/Right/*.png')
        self.images_left = self.load('Images/Dino/Left/*.png')
        self.image_heart = pygame.image.load('Images/Dino/Heart.png')
        self.gun = False
        self.touching_platform = False
        self.friction = -0.12
        self.hearts = 3

    def draw(self, win):
        if self.walk_count + 1 >= 27:
            self.walk_count = 0
        if not self.standing:
            if self.left:
                win.blit(self.images_left[self.walk_count // 3],
                         (self.pos.x, self.pos.y))
                self.walk_count += 1
            elif self.right:
                win.blit(self.images_right[self.walk_count // 3],
                         (self.pos.x, self.pos.y))
                self.walk_count += 1
        else:
            if self.right:
                win.blit(self.images_right[0], (self.pos.x, self.pos.y))
            else:
                win.blit(self.images_left[0], (self.pos.x, self.pos.y))
        self.hitbox = (self.pos.x + 17, self.pos.y + 11, 29, 52)
        self.footbox = (self.pos.x + 19, self.pos.y + 50, 16, 4)

        #self.getHearts(win)
        #pygame.draw.rect(win, (255,0,0), self.hitbox, 2)
        #pygame.draw.rect(win, (255,0,0), self.footbox, 2)

    def hit(self):
        self.walk_count = 0

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
        self.walk_count = 0

    def jump(self):
        if self.jump_count < 2:
            self.walk_count = 0
            self.vel.y = -15
            self.jump_count += 1
            print('jumped')

    def touch_down(self, platform_rect):
        self.vel.y = 0
        if self.pos.y <= platform_rect.top:
            self.pos.y = platform_rect.top - 50
            self.jump_count = 0
        if self.pos.y >= platform_rect.bottom:
            self.pos.y = platform_rect.bottom + 17

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

    def get_hearts(self, win):
        for i in range(0, self.hearts):
            print("Width:", win.get_width())
            win.blit(self.image_heart, win.get_width() - 40, 0)
