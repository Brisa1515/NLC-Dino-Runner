import pygame
import random

from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.utils.constants import BG, ICON, RUNNING, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, CLOUD
from dino_runner.components.dinosaur import Dinosaur


FONT_STYLE = 'freesansbold.ttf'

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.playing = False
        self.running = False
        self.game_speed = 17
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.points = 0
        self.death_count = 0
        
        self.separation = random.randint(350, 450)
        self.x_pos_cloud1 = 0 + self.separation
        self.x_pos_cloud2 = 0 + self.separation*2
        self.x_pos_cloud3 = 0 + self.separation*3
        self.x_pos_cloud4 = 0 + self.separation*4
        self.y_pos_cloud1 = random.randint(100, 250)
        self.y_pos_cloud2 = random.randint(100, 250)
        self.y_pos_cloud3 = random.randint(100, 250)
        self.y_pos_cloud4 = random.randint(100, 250)
        self.separation = 250
    
    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
                
        pygame.display.quit()
        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups(self.points, self.player)
        self.playing = True
        self.game_speed = 20
        self.points = 0
        while self.playing:
            self.events()
            self.update()
            self.draw()
        
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        self.update_score()
        given_user_input = pygame.key.get_pressed()
        self.player.update(given_user_input)
        self.obstacle_manager.update(self)
        self.power_up_manager.update(self.points, self.game_speed, self.player )

    def update_score(self):
        self.points += 1
        if self.points % 100 == 0:
            self.game_speed += 5

    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f"Point: {self.points}", True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (100,50)
        self.screen.blit(text, text_rect)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.draw_score()
        self.player.draw(self.screen)
        self.player.check_invincibility(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def handle_key_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

            elif event.type == pygame.KEYDOWN:
                self.run()

    def show_menu(self):
        self.screen.fill((255, 255, 255))
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2

        if self.death_count == 0:
            font = pygame.font.Font(FONT_STYLE, 30)
            text = font.render("Press any key to start", True, (0, 0, 0))
            text_rect = text.get_rect()
            text_rect.center = (half_screen_width, half_screen_height)
            self.screen.blit(text, text_rect)
        elif self.death_count > 0:
            font = pygame.font.Font(FONT_STYLE, 50)
            text = font.render("Game Over", True, (0, 0, 0))
            text_rect = text.get_rect()
            text_rect.center = (half_screen_width, half_screen_height)
            self.screen.blit(text, text_rect)


        self.screen.blit(RUNNING[0], (half_screen_width-40, half_screen_height-140))
        pygame.display.update()
        self.handle_key_events_on_menu()


        def draw_clouds(self):
            self.screen.blit(CLOUD, (self.x_pos_cloud1, self.y_pos_cloud1))
            self.screen.blit(CLOUD, (self.x_pos_cloud2, self.y_pos_cloud2))
            self.screen.blit(CLOUD, (self.x_pos_cloud3, self.y_pos_cloud3))
            self.screen.blit(CLOUD, (self.x_pos_cloud4, self.y_pos_cloud4))
            self.x_pos_cloud1 -= self.game_speed // 2
            self.x_pos_cloud2 -= self.game_speed // 2
            self.x_pos_cloud3 -= self.game_speed // 2
            self.x_pos_cloud4 -= self.game_speed // 2
            if self.x_pos_cloud1 <=- SCREEN_WIDTH//4:
              self.x_pos_cloud1 = SCREEN_WIDTH
              self.y_pos_cloud1 = random.randint(100, 250)
            if self.x_pos_cloud2 <=- SCREEN_WIDTH//4:
              self.x_pos_cloud2 = SCREEN_WIDTH
              self.y_pos_cloud2 = random.randint(100, 250)
            if self.x_pos_cloud3 <=- SCREEN_WIDTH//4:
              self.x_pos_cloud3 = SCREEN_WIDTH
              self.y_pos_cloud3 = random.randint(100, 250)
            if self.x_pos_cloud4 <=- SCREEN_WIDTH//4:
              self.x_pos_cloud4 = SCREEN_WIDTH
              self.y_pos_cloud4 = random.randint(100, 250)


