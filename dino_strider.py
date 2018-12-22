""" This is the main game file for 447's FLL Project for Into Orbit """
import pygame
from player import Player
from projectile import Projectile
from game_platform import Platform
from Level import level
from Level1 import level1


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
        # pygame.mixer.music.play(-1

    def start_screen(self):
        start_text = pygame.font.SysFont('Arial', 50).render(
            'Press Space to start', 1, (255, 0, 0))
        self.win.blit(start_text, (250 - (start_text.get_width() / 2), 200))
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
        background = pygame.image.load('Images/bg.jpg')
        clock = pygame.time.Clock()
        bullet_sound = pygame.mixer.Sound('Sound/bullet.wav')
        score_font = pygame.font.SysFont('arial', 30, True)
        dino = Player(300, 410)
        shoot_loop = 0
        all_sprites = pygame.sprite.Group()
        all_sprites.add(dino)
        bullets = []
        level = level1(self.screen_height, self.screen_width)

        while True:
            clock.tick(27)
            if shoot_loop > 0:
                shoot_loop += 1
            if shoot_loop > 3:
                shoot_loop = 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        dino.jump()
                        score += 1
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
            else:
                dino.stop()

            if keys[pygame.K_ESCAPE]:
                return

            if keys[pygame.K_COMMA]:
                dino.gain_heart()

            if keys[pygame.K_PERIOD]:
                dino.lose_heart()

            if keys[pygame.K_SPACE] and shoot_loop == 0 and dino.gun:
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
                    bullet_sound.play()
                shoot_loop = 1

            dino.update_location(self.screen_height, self.screen_width)

            self.win.blit(background, (0, 0))
            text = score_font.render('Score:' + str(score), 1, (0, 0, 0))
            self.win.blit(text, (0, 10))
            level.draw(self.win)
            dino.draw(self.win)

            hits = pygame.sprite.spritecollide(dino, level.platforms, False)

            if hits:
                dino.touch_down(hits[0].rect)

            for bullet in bullets:
                bullet.draw(self.win)
            pygame.display.update()


game = Game()
if game.start_screen():
    game.game_loop()
pygame.quit()
