import pygame, random
from config import *

class Food:
    def __init__(self):
        self.food_block  = Snake_block
        self.x = round(random.randrange(0, Width - self.food_block) / 10.0) * 10.0
        self.y = round(random.randrange(0, Height - self.food_block) / 10.0) * 10.0
        
    def draw(self):
        pygame.draw.rect(screen, Yellow, [self.x, self.y, self.food_block, self.food_block])
    
    def new_position(self):
        self.x = round(random.randrange(0, Width - self.food_block / 10.0) * 10.0)
        self.y = round(random.randrange(0, Height - self.food_block / 10.0) * 10.0)