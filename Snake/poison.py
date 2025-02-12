import pygame, random
from config import *


class Poison:
    def __init__(self):
        self.color = Purple
        self.x = 0
        self.y = 0
        self.active = False
        
    def respawn(self, snake_body):
        while True:
            self.x = random.randint(0, (Width // Block_size) - 1) * Block_size
            self.y = random.randint(0, (Height // Block_size) - 1) * Block_size
            if [self.x, self.y] not in snake_body:
                self.active = True
                break
        
    def draw(self, screen):
        if self.active:
            pygame.draw.rect(screen, self.color,(self.x, self.y, Block_size, Block_size))