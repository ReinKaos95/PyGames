import pygame, random
from config import *

class Snake:
    def __init__(self):
        self.x = Width / 2
        self.y = Height / 2
        self.Snake_block = Snake_block
        self.snake_speed = Snake_Speed
        self.snake_list = []
        self.snake_length = 1
        self.x_charge = 0
        self.y_charge = 0
        
    def move(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.x_charge = -self.Snake_block
                self.y_charge = 0
            elif event.key == pygame.K_RIGHT:
                self.x_charge = self.Snake_block
                self.y_charge = 0
            elif event.key == pygame.K_UP:
                self.Y_charge = -self.Snake_block
                self.X_charge = 0
            elif event.key == pygame.K_DOWN:
                self.Y_charge = -self.Snake_block
                self.X_charge = 0
                
        self.x += self.x_charge
        self.y += self.y_charge
        
    def draw(self, screen):
        for x in self.snake_list:
            pygame.draw.rect(screen, Green, [x[0], x[1], self.Snake_block, self.Snake_block])
            
    def check_collision_with_boundaries(self):
        if self.x >= Width or self.x < 0 or self.y >= Height or self.yy < 0:
            return True
        return False
    
    def check_collision_with_self(self):
        for block in self.snake_list[:-1]:
            if block == [self.x, self.y]:
                return True
            return False
        
    def grow(self):
        self.snake_head = [self.x, self.y]
        self.snake_list.append(self.snake_head)
        if len(self.snake_list) > self.snake_length:
            del self.snake_list[0]
        self.snake_length += 1