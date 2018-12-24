import pygame
from sprite import FacingSprite
from sprite import vec


class Player(FacingSprite):
    def __init__(self, start):
        (startX, startY) = start
        super().__init__(startX, startY, 52, 52, 'Images/Dino')
        self.player_acc = 0.5
        self.vel = vec(0, 0)
        self.grav = 0.8
        self.acc = vec(0, self.grav)
        self.jump_count = 0
        self.standing = True
        self.footbox = (self.pos.x + 19, self.pos.y + 50, 16, 4)
        self.image_heart = pygame.image.load('Images/Dino/Heart.png')
        self.image_life = pygame.image.load('Images/Dino/Lives.png')
        self.gun = True
        self.touching_platform = False
        self.friction = -0.12
        self.hearts = 3
        self.lives = 3
        self.startX = startX
        self.startY = startY
        self.bounds = pygame.Rect(0, 0, 800, 480)
        self.dead = False

    def draw(self, win):
        super().draw(win)

        self.footbox = (self.pos.x + 19, self.pos.y + 50, 16, 4)

        self.get_hearts(win)
        self.get_lives(win)
        #pygame.draw.rect(win, (255,0,0), self.footbox, 2)
        # pygame.draw.rect(win, (255, 0, 0), self.rect, 2)

    def hit(self, enemy):
        if self.rect.bottom <= (enemy.rect.centery - (enemy.rect.height // 4)
                                ) and self.rect.bottom >= enemy.rect.top:
            enemy.die()
        else:
            if enemy.rect.left <= self.rect.left:
                enemy.knockback(left=True)
            else:
                enemy.knockback(left=False)
            self.walk_count = 0
            self.hearts -= 1

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
            self.vel.y = -13
            self.jump_count += 1
            self.pos.y += 5

    def touch_down(self, platform_rect, friction):
        if self.rect.bottom >= platform_rect.top and self.rect.bottom <= platform_rect.bottom:
            if self.pos.x >= platform_rect.left and self.pos.x <= platform_rect.right:
                # print('top', self.rect, platform_rect)
                self.vel.y = 0
                self.pos.y = platform_rect.top
                self.jump_count = 0
                self.friction = friction
        elif self.rect.right >= platform_rect.left and self.rect.right <= platform_rect.centerx:
            # print('right', self.rect, platform_rect)
            self.vel.x = 0
            self.pos.x = platform_rect.left - (self.rect.width // 2)
        elif self.rect.left <= platform_rect.right and self.rect.left >= platform_rect.centerx:
            # print('left', self.rect, platform_rect)
            self.vel.x = 0
            self.pos.x = platform_rect.right + self.rect.width // 2
        elif self.rect.top >= platform_rect.centery and self.rect.top <= platform_rect.bottom:
            # print('Bottom', self.rect, platform_rect)
            self.vel.y = 0
            self.pos.y = platform_rect.bottom + self.rect.height

    def update_location(self, screen_height, screen_width):
        self.acc.y = self.grav

        self.acc.x += self.vel.x * self.friction

        self.vel += self.acc
        self.pos += self.vel + self.acc
        self.acc = vec(0, self.grav)
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
        self.dead = True
        self.hearts = 3

    def reset(self):
        self.dead = False
