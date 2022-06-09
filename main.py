import pygame as pg
import pygame.sprite

import sprites
from settings import *
import random

class Game():
    def __init__(self):
        # initialize game window, etc
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()

        self.running = True
        self.player = None
        self.player_grp = None

        self.bg = pg.image.load("images/road.svg")
        self.bg = pg.transform.scale(self.bg, (WIDTH*2 - 60, HEIGHT*2))

        self.vehicles = []
        for i in range(2,6):
            path = f'images/car-truck{i}.png'
            vehicle = pg.image.load(path)
            vehicle = pg.transform.rotate(vehicle,180)
            self.vehicles.append(vehicle)

        self.crash = pg.mixer.Sound('images/crash.ogg')
        self.score = 0
        self.lives = None

    def display_score(self):
        score = MED_FONT.render(f'Score: {self.score}', True, BLACK)
        self.screen.blit(score, (70, 5))

    def new(self):
        '''create all game objects, sprites, and sprite groups and call run()'''
        self.score = 0

        # create sprite groups
        self.player_grp = pg.sprite.GroupSingle()
        self.enemy_grp = pg.sprite.Group()

        # create a player object and add it to the group
        self.player = sprites.Player(WIDTH//2, HEIGHT-2*P_SIZE)
        for i in range(ENEMY_COUNT):
            vehicle = random.choice(self.vehicles)
            rand_x = random.randint(2*E_SIZE, WIDTH - 4 * E_SIZE)
            rand_y = random.randint(-300, -150)
            self.enemy = sprites.Enemy(rand_x, rand_y, vehicle)
            self.enemy_grp.add(self.enemy)

        self.lives = []
        for i in range(LIVES):
            dimensions = (10,30)
            life = pg.Surface(dimensions)
            life.fill(RED)
            self.lives.append(life)

        self.player_grp.add(self.player)


        self.run()


    def run(self):
        '''contains main game loop'''

        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def detect_collision(self):
        hit_list = pygame.sprite.groupcollide(self.player_grp, self.enemy_grp, True, True)
        if hit_list:
            self.lives.pop()
            self.crash.play()


    def update(self):
        # game loop - update
        self.player_grp.update()
        self.enemy_grp.update()
        self.detect_collision()

        if len(self.enemy_grp) < ENEMY_COUNT:
            vehicle = random.choice(self.vehicles)
            rand_x = random.randint(2*E_SIZE, WIDTH - 4 * E_SIZE)
            rand_y = random.randint(-300, -150)
            self.enemy = sprites.Enemy(rand_x, rand_y, vehicle)
            self.enemy_grp.add(self.enemy)

        if len(self.player_grp) < 1:
            self.player = sprites.Player(WIDTH // 2, HEIGHT - 2 * P_SIZE)
            self.player_grp.add(self.player)

        if self.player.rect.y <= 55:
            self.score += 10

        if len(self.lives) == 0:
            self.playing = False

    def draw(self):
        '''fill screen, draw objects, sprites to the display, and flip'''
        self.screen.fill(WHITE)

        # anything to be drawn to screen goes here
        self.screen.blit(self.bg, (0, 0))
        pg.draw.rect(SCREEN, BLACK, (0, 50, WIDTH, 10))


        self.player_grp.draw(SCREEN)
        self.enemy_grp.draw(SCREEN)

        self.display_score()

        for index, life in enumerate(self.lives):
            location = (475 + index * 20, 15)
            self.screen.blit(life, location)

        pg.display.flip()




    def events(self):
        # game loop - events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                    quit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_d:
                    self.player.x_velo = 5
                if event.key == pg.K_a:
                    self.player.x_velo = -5
                if event.key == pg.K_w:
                    self.player.y_velo = -5
                if event.key == pg.K_s:
                    self.player.y_velo = 5
            if event.type == pg.KEYUP:
                self.player.x_velo = 0
                self.player.y_velo = 0


    def show_start_screen(self):
        # screen to start game
        pg.init()
        screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        clock = pg.time.Clock()
        running = True

        title = LRG_FONT.render('Reckless Drivers v1.0', True, WHITE)
        inst = MED_FONT.render('Press SPACE to start', True, WHITE)

        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    quit()

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        running = False

            screen.fill(BLACK)
            screen.blit(title, (45, 5))
            screen.blit(inst, (45, 70))
            pg.display.flip()

    def show_go_screen(self):
        insults = ["My grandma plays better than you.", "You drive worse than I do...", "What are you, 5?", "You really don't know how to drive, huh?", "Ouch. You coulda done better...", "A sloth could drive better than whatever that was."]
        rand_insult = random.choice(insults)
        # screen when game over
        pg.init()
        screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        clock = pg.time.Clock()
        running = True

        title = LRG_FONT.render('HA LOSER YOU DIED', True, RED)
        inst = MED_FONT.render('Press SPACE to restart', True, WHITE)
        inst2 = MED_FONT.render('Press Q to quit', True, WHITE)
        score = MED_FONT.render(f'Final Score: {self.score}', True, WHITE)
        insult = SML_FONT.render(f'{rand_insult}', True, WHITE)

        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    quit()

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        running = False

                    elif event.key == pg.K_q:
                        quit()

            screen.fill(BLACK)
            screen.blit(title, (45, 5))
            screen.blit(inst, (45, 70))
            screen.blit(inst2, (45, 115))
            screen.blit(score, (45, 160))
            screen.blit(insult, (45, 205))
            pg.display.flip()


#################################################
###                                   PLAY GAME                                            ###
#################################################

game = Game()
game.show_start_screen()

while game.running:
    game.new()
    game.show_go_screen()

pg.quit()