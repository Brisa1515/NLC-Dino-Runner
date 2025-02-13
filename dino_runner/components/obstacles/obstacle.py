from pygame.sprite import Sprite
#from email.mime import image
#from dino_runner.components.obstacles.obstacle import obstacle
from dino_runner.utils.constants  import SCREEN_WIDT


class Obstacle(Sprite):
    def __init__(self, image,type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDT
    
    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, screen):
        screen.blit(self.image[self.type], self.rect)