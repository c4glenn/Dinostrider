import pygame
from player import Player
from projectile import Projectile
from gamePlatform import Platform


class Game:
    def __init__(self):
        pygame.init()
        self.screen_width = 800
        self.screen_height = 480
        self.win = pygame.display.set_mode((self.screen_width,
                                            self.screen_height))
        pygame.display.set_caption("Dinostrider")
        self.music = pygame.mixer.music.load('Sound/music.wav')
        pygame.mixer.music.play(-1)

    def start_screen(self):
        font1 = pygame.font.SysFont('Arial', 50)
        text1 = font1.render('Press Space to start', 1, (255, 0, 0))
        self.win.blit(text1, (250 - (text1.get_width() / 2), 200))
        pygame.display.update()
        while True:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                return True
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False

    def game_loop(self):
        score = 0
        bg = pygame.image.load('Images/bg.jpg')
        clock = pygame.time.Clock()
        bulletSound = pygame.mixer.Sound('Sound/bullet.wav')
        hitSound = pygame.mixer.Sound('Sound/hit.wav')
        #mainloop
        self.font = pygame.font.SysFont('arial', 30, True)
        man = Player(300, 410)
        shootLoop = 0
        platforms = []
        platforms.append(Platform(110, 390, 120, 20, (0, 0, 0), 0,
                                  390))  # level 1
        bullets = []
        while True:
            clock.tick(27)

            if shootLoop > 0:
                shootLoop += 1
            if shootLoop > 3:
                shootLoop = 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
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
                return

            if keys[pygame.K_SPACE] and shootLoop == 0 and man.gun == True:
                if man.left:
                    facing = -1
                else:
                    facing = 1

                if len(bullets) < 5:
                    bullets.append(
                        Projectile(
                            round(man.x + man.width // 2),
                            round(man.y + man.height // 2), 6, (0, 0, 0),
                            facing))
                    bulletSound.play()
                shootLoop = 1
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                man.move_left()

            elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                man.move_right(self.screen_width)
            else:
                man.stop()

            if keys[pygame.K_UP] or keys[pygame.K_w]:
                man.jump()

            man.update_location(self.screen_height)

            self.win.blit(bg, (0, 0))
            text = self.font.render('Score:' + str(score), 1, (0, 0, 0))
            self.win.blit(text, (0, 10))
            man.draw(self.win)
            for platform in platforms:
                platform.draw(self.win)
            for bullet in bullets:
                bullet.draw(self.win)
            pygame.display.update()


game = Game()
if game.start_screen():
    game.game_loop()
pygame.quit()
