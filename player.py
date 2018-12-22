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
        self.image_life = pygame.image.load('Images/Dino/Lives.png')
        self.gun = True
        self.touching_platform = False
        self.friction = -0.12
        self.hearts = 3
        self.lives = 3
        self.startX = startX
        self.startY = startY

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
        self.get_lives(win)
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

    def touch_down(self, platform_rect, friction):
        if self.rect.top >= platform_rect.top and self.rect.top <= platform_rect.bottom:
            self.vel.y = 0
            self.rect.top = platform_rect.bottom
        if self.rect.bottom >= platform_rect.top and self.rect.bottom <= platform_rect.bottom:
            if self.pos.x >= platform_rect.left and self.pos.x <= platform_rect.right:
                self.vel.y = 0
                self.pos.y = platform_rect.top
                self.jump_count = 0
                self.friction = friction

    def update_location(self, screen_height, screen_width):
        self.acc.y = self.grav

        self.acc.x += self.vel.x * self.friction

        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.acc = vec(0, self.grav)

        if self.pos.x + self.rect.width > screen_width:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = screen_width - self.rect.width

        if self.pos.y > screen_height:
            self.lose_life()
        self.update_rectangle()

    def get_hearts(self, win):
        for i in range(0, self.hearts):
            win.blit(self.image_heart, (760 - (20 * i), 15))
        if self.hearts <= 0:
            self.lose_life()

    def gain_heart(self):
        self.hearts += 1

    def lose_heart(self):
        self.hearts -= 1


    def get_lives(self, win):
        for i in range(0, self.lives):
            win.blit(self.image_life, (760 - (20 * i), 35))

    def gain_life(self):
        self.lives += 1

    def lose_life(self):
        self.lives -= 1
        self.pos = vec(self.startX, self.startY)
        self.hearts = 3
