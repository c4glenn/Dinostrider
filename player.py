import pygame
from sprite import Sprite
from sprite import vec


class Player(Sprite):
    def __init__(self, startX, startY):
        super().__init__(startX, startY, 52, 52)
        self.player_acc = 0.5
        self.vel = vec(0, 0)
        self.grav = 0.8
        self.acc = vec(0, self.grav)
        self.jump_count = 0
        self.facing_left = False
        self.walk_count = 0
        self.standing = True
        self.footbox = (self.pos.x + 19, self.pos.y + 50, 16, 4)
        self.images_right = self.load('Images/Dino/Right/*.png')
        self.images_left = self.load('Images/Dino/Left/*.png')
        self.image_heart = pygame.image.load('Images/Dino/Heart.png')
        self.gun = True
        self.touching_platform = False
        self.friction = -0.12
        self.hearts = 3

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

        self.footbox = (self.pos.x + 19, self.pos.y + 50, 16, 4)

        self.get_hearts(win)
        #pygame.draw.rect(win, (255,0,0), self.footbox, 2)
        pygame.draw.rect(win, (255, 0, 0), self.rect, 2)

    def hit(self):
        self.walk_count = 0

    def move_left(self):
        self.acc = vec(0, self.grav)
        self.acc.x = -self.player_acc
        self.facing_left = True
        self.standing = False

    def move_right(self):
        self.acc = vec(0, self.grav)
        self.acc.x = self.player_acc
        self.facing_left = False
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
            self.pos.y += 5

    def touch_down(self, platform_rect):
        if not (self.rect.centerx > platform_rect.right
                or self.rect.centerx < platform_rect.left):
            self.vel.y = 0
            if self.rect.y <= platform_rect.top:
                self.pos.y = platform_rect.top
                self.jump_count = 0
            if self.rect.y >= platform_rect.bottom:
                self.pos.y = platform_rect.bottom

    def update_location(self, screen_height, screen_width):
        self.acc.y = self.grav

        self.acc.x += self.vel.x * self.friction

        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        if self.pos.x + self.rect.width > screen_width:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = screen_width - self.rect.width
        self.acc = vec(0, self.grav)
        self.update_rectangle()

    def get_hearts(self, win):
        for i in range(0, self.hearts):
            win.blit(self.image_heart, (760 - (20 * i), 15))

    def gain_heart(self):
        self.hearts += 1

    def lose_heart(self):
        self.hearts -= 1
