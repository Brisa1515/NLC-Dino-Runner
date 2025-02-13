import pygame

from pygame.sprite import Sprite
from dino_runner.utils.constants import DUCKING, RUNING
from dino_runner.utils.constants import JUMPING
class Dinosaur(Sprite):
    X_POS = 80
    Y_POS = 310 
    JUMP_VEL = 8.5

    def __init__(self):
        self.image = RUNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.dino_run = True
        self.dino_jum = False
        self.jump_vel = self.JUMP_VEL
    def update(self,user_imput):
        if self.dino_run:
            self.run()
        elif self.dino_jum:
            self.jump ()

        if user_imput[pygame.K_UP] and not self.dino_jum:
            self.dino_jum = True
            self.dino_run = False
        elif not self.dino_jum:
            self.dino_jum = False
            self.dino_run = True

        if self.step_index >=10:
             self.step_index = 0 


    def jump(self):
        self.image = JUMPING
        if self.dino_jum:
            self.dino_rect.y -=self.jump_vel * 4
            print(self.dino_rect.y)
            self.jump_vel -= 0.8
            print(self.jump_vel)

        if self.jump_vel < -self.JUMP_VEL:
            self.dino_rect.y = self.Y_POS
            self.dino_run = False
            self.jump_vel = self.JUMP_VEL
        

    def run(self):
        self.image = RUNING[0] if self.step_index < 5 else RUNING[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1


    def draw(self, secreen: pygame.Surface):
        self.screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))


    
    def duck(self):
        self.image= DUCKING
        if self.dino_duck:
            self.dino_rect.y -=self.duck * 4
            print(self.dino_rect.y)
            self.duck_vel -= 0.8
            print(self.duck_vel)

        if self.duck_vel < -self.DUCK_VEL:
            self.dino_rect.y = self.Y_POS
            self.dino_run = False
            self.duck_vel = self.DUCK_VEL