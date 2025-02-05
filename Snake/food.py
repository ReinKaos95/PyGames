import pygame, random
from config import *

class Food:
    def __init__(self):
        self.x = random.randint(0, (Width - Block_size) // Block_size) * Block_size
        self.y = random.randint(0, (Height - Block_size) // Block_size) * Block_size
        
    def draw(self, snake_body):
        # Generar una nueva posición que no esté en el cuerpo de la serpiente
        while True:
        self.x = random.randint(0, (Width - Block_size) // Block_size) * Block_size
        self.y = random.randint(0, (Height - Block_size) // Block_size) * Block_size
        if [self.x, self.y] not in snake_body:
            break