from dino_runner.utils.constants import HAMMER, HAMMER_TYPE, SCREEN_WIDTH
from dino_runner.components.power_ups.power_up import PowerUp

class Hammer(PowerUp):
    def __init__(self):
        self.image = HAMMER
        self.type = HAMMER_TYPE
        super().__init__(self.image, self.type)

    def set_pos_hammer(self, dino_rect):
        self.rect.x = dino_rect.x
        self.rect.y = dino_rect.y

    def update_hammer(self, game_speed, powerup):
        self.rect.x += game_speed + 10
        if self.rect.x >= SCREEN_WIDTH:
            self.rect.x = -200

    def draw_hammer(self, screen):
        screen.blit(self.image, self.rect)