""" This is the main game file for 447's FLL Project for Into Orbit """
import pygame
from player import Player
from projectile import Projectile
from game_platform import Platform
from Level import level
from Leveldemo import leveldemo
from Slime import slime
from sprite import vec
from Level1 import level1


class Game:
    """ This has the start screen and game loop """

    def __init__(self):
        pygame.init()
        self.screen_width = 800
        self.screen_height = 480
        self.score = 0
        self.levels = [
            level1(self.screen_height, self.screen_width),
        ]
        self.level = self.levels[0]
        self.win = pygame.display.set_mode((self.screen_width,
                                            self.screen_height))
        pygame.display.set_caption("Dinostrider")

        # music = pygame.mixer.music.load('Sound/music.wav')
        # pygame.mixer.music.play(-1)

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

    def end_screen(self, dino):
        pygame.draw.rect(self.win, (0, 0, 0), (0, 0, 800, 480))
        end_text = pygame.font.SysFont('Arial', 50).render(
            'You Win', 1, (255, 0, 0))
        end_score = pygame.font.SysFont('Arial', 20).render(
            'Final Score: ' + str(self.score), 1, (255, 0, 0))
        end_hearts = pygame.font.SysFont('Arial', 20).render(
            'Final Hearts: ' + str(dino.hearts), 1, (255, 0, 0))
        end_lives = pygame.font.SysFont('Arial', 20).render(
            'Final Lives: ' + str(dino.lives), 1, (255, 0, 0))
        self.win.blit(end_text, (400 - (end_text.get_width() / 2), 100))
        self.win.blit(end_score, (400 - (end_score.get_width() / 2), 200))
        self.win.blit(end_hearts, (400 - (end_hearts.get_width() / 2), 300))
        self.win.blit(end_lives, (400 - (end_lives.get_width() / 2), 350))
        pygame.display.update()
        while True:
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return False

    def game_loop(self):
        """ This is the main game loop """
        clock = pygame.time.Clock()
        bullet_sound = pygame.mixer.Sound('Sound/bullet.wav')
        score_font = pygame.font.SysFont('arial', 30, True)
        shoot_loop = 0
        bullets = []
        dino = Player(self.level.get_player_start_position())

        while True:
            clock.tick(27)

            dino.gun = self.level.dino_gun

            if dino.pos.x + 350 > self.screen_width:
                self.level.shift_world(-5, 0)
                dino.slide(-5, 0)
            if dino.pos.x - 350 <= 0 and self.level.world_shift_x < 0:
                self.level.shift_world(5, 0)
                dino.slide(5, 0)
            if self.level.world_shift_x <= self.level.level_limit:
                try:
                    self.level = self.levels[self.levels.index(self.level) + 1]
                    dino.reset()
                except:
                    if self.end_screen(dino):
                        return False

            if shoot_loop > 0:
                shoot_loop += 1
            if shoot_loop > 4:
                shoot_loop = 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        dino.jump()
                    if event.key == pygame.K_BACKQUOTE:
                        for enemy in self.level.enemys:
                            enemy.debug_draw(
                                draw_bounds=not enemy.draw_bounds,
                                draw_hitbox=not enemy.draw_hitbox)
                        dino.debug_draw(draw_hitbox=not dino.draw_hitbox)

            for bullet in bullets:
                remove = False
                hits = pygame.sprite.spritecollide(bullet,
                                                   self.level.platforms, False)
                if hits:
                    remove = True
                if (bullet.pos.x < self.screen_width) and (bullet.pos.x > 0):
                    bullet.update_location()
                else:
                    remove = True

                hits = pygame.sprite.spritecollide(bullet, self.level.enemys,
                                                   False)
                for i in range(0, len(hits)):
                    self.score += 5
                    hits[i].hit()
                    remove = True

                if remove:
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
            if keys[pygame.K_a]:
                print(dino.pos.x - self.level.world_shift_x)

            if keys[pygame.K_SPACE] and shoot_loop == 0 and dino.gun:
                if dino.facing_left:
                    facing = -1
                else:
                    facing = 1

                if len(bullets) < 5:
                    bullets.append(
                        Projectile(
                            int(dino.rect.centerx), int(dino.rect.centery), 6,
                            (0, 0, 0), facing))
                    bullet_sound.play()
                shoot_loop = 1

            dino.update_location(self.screen_height, self.screen_width)

            self.win.blit(self.level.background, (0, 0))
            text = score_font.render('Score:' + str(self.score), 1, (0, 0, 0))
            self.win.blit(text, (0, 10))

            hits = pygame.sprite.spritecollide(dino, self.level.platforms,
                                               False)
            for i in range(0, len(hits)):
                dino.touch_down(hits[i].rect, hits[i].friction)

            hits = pygame.sprite.spritecollide(dino, self.level.enemys, False)
            for i in range(0, len(hits)):
                dino.hit(hits[i])
                if dino.rect.bottom <= (
                        hits[i].rect.centery - (hits[i].rect.height // 4)
                ) and dino.rect.bottom >= hits[i].rect.top:
                    self.score += 20
            if dino.dead:
                self.level.shift_world(0 - self.level.world_shift_x,
                                       0 - self.level.world_shift_y)
                dino.reset()
            self.level.draw(self.win)
            dino.draw(self.win)
            for bullet in bullets:
                bullet.draw(self.win)
            pygame.display.update()


game = Game()
if game.start_screen():
    game.game_loop()
pygame.quit()
