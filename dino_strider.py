""" This is the main game file for 447's FLL Project for Into Orbit """
import pygame
from player import Player
from projectile import Projectile
from game_platform import Platform
from sprite import Sprite
from sprite import load
from sprite import vec


class Game:
    """ This has the start screen and game loop """

    def __init__(self):
        pygame.init()
        self.screen_width = 800
        self.screen_height = 480
        self.win = pygame.display.set_mode((self.screen_width,
                                            self.screen_height))
        pygame.display.set_caption("Dinostrider")
        # self.music = pygame.mixer.music.load('Sound/music.wav')
        # pygame.mixer.music.play(-1)

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
        """ This is the main game loop """
        score = 0
        bg = pygame.image.load('Images/bg.jpg')
        clock = pygame.time.Clock()
        bulletSound = pygame.mixer.Sound('Sound/bullet.wav')
        font = pygame.font.SysFont('arial', 30, True)
        dino = Player(300, 410)
        shootLoop = 0
        platforms = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(dino)
        p1 = platforms.add(
            Platform(0, self.screen_height - 20, self.screen_width, 20,
                     (0, 0, 0), 0, 0))  # level 1
        p2 = platforms.add(
            Platform(self.screen_width // 2 - 20, self.screen_height // 2 + 20,
                     40, 20, (0, 0, 0), 0, 0))  # level 1
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
                if bullet.pos.x < 500 and bullet.pos.x > 0:
                    bullet.pos.x += bullet.vel
                else:
                    bullets.pop(bullets.index(bullet))

            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT]:
                dino.move_left()
            elif keys[pygame.K_RIGHT]:
                dino.move_right()

            if keys[pygame.K_ESCAPE]:
                return

            if keys[pygame.K_SPACE] and shootLoop == 0 and dino.gun:
                if dino.left:
                    facing = -1
                else:
                    facing = 1

                if len(bullets) < 5:
                    bullets.append(
                        Projectile(
                            round(dino.pos.x + dino.width // 2),
                            round(dino.pos.y + dino.height // 2), 6, (0, 0, 0),
                            facing))
                    bulletSound.play()
                shootLoop = 1

            dino.update_location(self.screen_height, self.screen_width)

            self.win.blit(bg, (0, 0))
            text = font.render('Score:' + str(score), 1, (0, 0, 0))
            self.win.blit(text, (0, 10))
            dino.draw(self.win)
            for platform in platforms:
                platform.draw(self.win)

            hits = pygame.sprite.spritecollide(dino, platforms, False)

            if hits:
                dino.vel.y = 0
                dino.pos.y = hits[0].rect.top - 50

            for bullet in bullets:
                bullet.draw(self.win)
            pygame.display.update()


game = Game()
if game.start_screen():
    game.game_loop()
pygame.quit()
