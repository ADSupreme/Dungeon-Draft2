import pygame
import pygame.freetype
from level import Level
from settings import *
from stopwatch import stopwatch, win_screen


class Game:
    def __init__(self):
        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        pygame.display.set_caption('Dungeon')
        self.clock = pygame.time.Clock()
        self.level = Level()

        self.font = pygame.freetype.SysFont(None, 34)
        self.font.origin = True
        self.out = None
        self.final_time = None
        self.is_paused = False
        self.start_timer = False

    def run(self, login_name, login_password, level_loaded, Player_val, difficulty_rating, email):
        total_time = 0
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        self.level.toggle_menu()
                    if event.key == pygame.K_ESCAPE:
                        self.level.toggle_escape()
                        self.is_paused = not self.is_paused

            self.screen.fill('black')
            self.clock.tick(FPS)
            self.level.run()
            if self.level.is_dead_now:
                add_string = str(email) + " " + str(login_name) + " " + str(login_password) + " " + str(level_loaded) + " " + str(difficulty_rating) + " " + self.out
                print(add_string)
                score_file = open(r"Score_file.txt", "a+")
                score_file.write(add_string)
                score_file.write('\n')
                score_file.close()
                win_screen()

            if self.is_paused:
                time_elapsed = 0
            else:
                time_elapsed = 1
            total_time = total_time + int(time_elapsed)
            self.out = stopwatch(total_time)
            self.font.render_to(self.screen, (1080, 60), self.out, pygame.Color('dodgerblue'))
            pygame.display.update()
