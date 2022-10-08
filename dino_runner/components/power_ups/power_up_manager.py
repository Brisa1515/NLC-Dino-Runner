from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.hammer import Hammer
from dino_runner.utils.constants import DEFAULT_TYPE, SHIELD_TYPE, HAMMER_TYPE

import pygame
import random

class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = 0
        self.points = 0
        self.option_numbers = list(range(1, 10))
        
        self.hammer = Hammer()
    def generate_power_ups(self, points, player):
        self.points = points
        if len(self.power_ups) == 0:
            if self.when_appears == self.points:
                self.when_appears = random.randint(self.when_appears * 200, self.when_appears * 300)
                if player.type == DEFAULT_TYPE:
                   self.power_ups.append(Shield())
                   self.power_ups.append(Hammer())

    def update(self, points, game_speed, player):
        self.generate_power_ups(points, player)
        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            if player.dino_rect.colliderect(power_up.rect):
                # sonido de escudo
                power_up.start_time = pygame.time.get_ticks()
                player.type = power_up.type
                time_random = random.randint(5, 8)
                player.shield_time_up = power_up.start_time + (time_random * 1000)
                print(player.shield_time_up)
                self.power_ups.remove(power_up)
                if player.type == SHIELD_TYPE:
                    player.shield = True
                    player.show_text = True
                    player.shield_time_up = power_up.start_time + (time_random * 1000)

                if player.type == HAMMER_TYPE:
                    player.hammer = True
                    player.hammer_time_up = power_up.start_time + (time_random*1000)
                


    def draw(self, screen):

        for power_up in self.power_ups:
            power_up.draw(screen)
    
    def reset_power_ups(self, points, player):
        self.power_ups = []
        self.points = points
        self.when_appears = random.randint(200, 300) + self.points
        player.hammer = False
        player.type = DEFAULT_TYPE

    
        