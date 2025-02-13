import pygame, random
from config import *


class PowerUp:
    def __init__(self):
        self.color = Yellow
        self.timer = 100
        self.x = 0
        self.y = 0
        self.active = False
        self.timer = 0
        
    def respawn(self, snake_body):
        while True:
            self.x = random.randint(0, (Width // Block_size) - 1) * Block_size
            self.y = random.randint(0, (Height // Block_size) - 1) * Block_size
            if [self.x, self.y] not in snake_body:
                self.active = True
                self.timer = pygame.time.get_ticks()
                break
                
    def draw(self, screen):
        if self.active:
            pygame.draw.rect(screen, self.color, (self.x, self.y, Block_size, Block_size))