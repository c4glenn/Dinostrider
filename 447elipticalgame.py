import pygame
from player import Player
from projectile import Projectile
pygame.init()
swidth = 800
sheight = 480
win = pygame.display.set_mode((swidth, sheight))

pygame.display.set_caption("First Game")

bg = pygame.image.load('Images/bg.jpg')
clock = pygame.time.Clock()

bulletSound = pygame.mixer.Sound('Sound/bullet.wav')
#hitSound = pygame.mixer.Sound('hit.wav')

#music = pygame.mixer.music.load('music.wav')
#pygame.mixer.music.play(-1)

score = 0
started = False
gun = True
Run = True
level = 1

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
man = Player(300, 410)
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
                bullets.append(Projectile(round(man.x + man.width //2), round(man.y + man.height//2), 6, (0,0,0), facing))
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