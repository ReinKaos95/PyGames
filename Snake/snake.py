import pygame
from config import *


class Snake:
    def __init__(self):
        self.x = Width // 2
        self.y = Height // 2
        self.dx = Block_size
        self.dy = 0
        self.body = [[self.x, self.y]]
        self.length = 1
        
    def move(self):
        # Actualizar la posición de la cabeza
        self.x += self.dx
        self.y += self.dy
        
        # Agregar la nueva cabeza al cuerpo
        self.body.append([self.x, self.y])
        
        # Mantener el cuerpo del tamaño correcto
        if len(self.body) > self.length:
            del self.body[0]
            
    def change_direction(self, dx, dy):
        # Evitar que la serpiente se mueva en la dirección opuesta
        if self.dx != -dx and self.dy != -dy:
            self.dx += dx
            self.dy += dy
            
    def draw(self, screen):
        for block in self.body:
            pygame.draw.rect(screen, Green, (*block, Block_size, Block_size))
            
    def check_collision(self):
        # Colisión con los límites
        if self.x < 0 or self.x >= Width or self.y < 0 >= Height:
            return True
        # Colisión consigo misma
        for block in self.body[:-1]:
            if block == [self.x self.y]:
                return True
        return False
    
    def grow(self):
        self.length += 1