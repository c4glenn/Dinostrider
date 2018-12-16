import pygame
import os
from operator import itemgetter, attrgetter, methodcaller
pygame.init()
swidth = 800
sheight = 480
win = pygame.display.set_mode((swidth, sheight))

pygame.display.set_caption("First Game")

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

#walkRight = [pygame.image.load('Images/Dino/Right/1.png'), pygame.image.load('Images/Dino/Right/2.png')]
#walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('Images/bg.jpg')
walkRight = load('Images/Dino/Right', 'image', '.png')
walkLeft = load('Images/Dino/Left', 'image', '.png')
clock = pygame.time.Clock()

#bulletSound = pygame.mixer.Sound('bullet.wav')
#hitSound = pygame.mixer.Sound('hit.wav')

#music = pygame.mixer.music.load('music.wav')
#pygame.mixer.music.play(-1)

score = 0
started = False
gun = False
Run = True
level = 1

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.standing = True
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        self.footbox = (self.x + 19, self.y + 50, 16, 4)
    
    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))
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
        win.blit(text, (250 - (text.get_width()/2), 200))
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
        

    pygame.display.update()

class projectile(object):
    def __init__(self, x, y, radius,color,facing):
            self.x = x
            self.y = y
            self.radius = radius
            self.color = color
            self.facing = facing
            self.vel = 8 * facing

    def draw(self, win):
        pygame.draw,pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

class platform(object):
    def __init__(self, x, y, width, height, color, vel, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.vel = vel
        self.end = end
        self.path = (self.x, self.end) 
    
    def draw(self, win):
        self.move()
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
    
    def move(self):
        if self.vel > 0:
            if self.x  + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
        else:
            if self.x + self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
def Level1():
    platforms.append(platform(110, 390, 120, 20, (0, 0, 0), 0, 390))

def redrawGameWindow():
    win.blit(bg, (0, 0))
    text = font.render('Score:' + str(score), 1, (0,0,0))
    win.blit(text, (0, 10))
    man.draw(win)
    for platform in platforms:
        platform.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()
    

#mainloop
font = pygame.font.SysFont('arial', 30, True)
man = player(300, 410, 64, 64)
shootLoop = 0
platforms = []
bullets = []
while Run:
    if started == True:
        clock.tick(27)

        if shootLoop > 0:
            shootLoop += 1
        if shootLoop > 3:
            shootLoop = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Run = False
        for bullet in bullets:
            if bullet.x < 500 and bullet.x > 0:
                bullet.x += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))
        
        for plat in platforms:
            pass
            #if man.hitbox[1] + man.hitbox[3] > plat.y + 5:
             #   if man.hitbox[0] <= plat.x + plat.width and man.hitbox[0] + man.hitbox[2] >= plat.x:
              #      platmiddle = (plat.width//2)+plat.x
               #     if man.hitbox[0] < platmiddle and not man.hitbox[1] + man.hitbox[3] <= plat.y:
                #        man.x = plat.x - man.hitbox[2]
                 #   else:
                  #      man.x = plat.x + plat.width
            if man.hitbox[1] + man.hitbox[3] >= plat.y:
                if man.footbox[0] <= plat.x + plat.width:
                    if man.footbox[0] + man.footbox[2] >= plat.x:
                        jumpCount = 0
                        man.y = plat.y - (man.hitbox[3] + 2)     


        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:                
                Run = False

        if keys[pygame.K_SPACE] and shootLoop == 0 and gun == True:
            if man.left:
                facing = -1
            else:
                facing = 1

            if len(bullets) < 5:
                bullets.append(projectile(round(man.x + man.width //2), round(man.y + man.height//2), 6, (0,0,0), facing))
                bulletSound.play()
            shootLoop = 1
        if keys[pygame.K_LEFT] and man.x > 0 or keys[pygame.K_a] and man.x > 0:
            man.x -= man.vel
            man.left = True
            man.right = False
            man.standing = False
        elif keys[pygame.K_RIGHT] and man.x < swidth - man.width or keys[pygame.K_d] and man.x < swidth - man.width:
            man.x += man.vel
            man.left = False
            man.right = True
            man.standing = False
        else:
            man.standing = True
            man.walkCount = 0

        if not(man.isJump):
            if keys[pygame.K_UP] or keys[pygame.K_w]:
                man.isJump = True
                man.left = False
                man.right = False
                man.walkCount = 0
        else:
            if man.jumpCount >= -10:
                neg = 1
                if man.jumpCount < 0:
                    neg = -1
                change = (man.jumpCount ** 2) * 0.5 * neg
                if man.y - change + man.height < sheight:
                    man.y -= change
                    man.jumpCount -= 1 
                else:
                    man.isJump = False
                    man.jumpCount = 10
            else:
                man.isJump = False
                man.jumpCount = 10
        if level == 1:
            Level1() 
        
        redrawGameWindow()

    else:
        font1 = pygame.font.SysFont('Arial', 50)
        text1 = font1.render('Press Space to start', 1, (255, 0, 0))
        win.blit(text1, (250 - (text1.get_width()/2), 200))
        pygame.display.update()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            started = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Run = False
pygame.quit()