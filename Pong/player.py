import pygame

class Player():
    def __init__(self, x, y, width, height, color, speed):
        self.rect = pygame.Rect(x, y, width, height) # Crear el rectángulo del jugador
        self.color = color
        self.speed = speed
        
    def draw(self, screen):
        """Dibuja la barra del jugador en la pantalla."""
        pygame.draw.rect(screen, self.color, self.rect)
        
    def move(self, up_key, down_key, screen_height):
        """Permite mover la barra hacia arriba o abajo."""
        keys = pygame.key.get_pressed()
        if keys[up_key] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[down_key] and self.rect.bottom < screen_height:
            self.rect.y += self.speed
            
    def auto_move(self, ball, screen_height):
        if ball.rect.centery > self.rect.centery and self.rect.bottom < screen_height:
            self.rect.y += self.speed
            
        if ball.rect.centery < self.rect.centery and self.rect.top > 0:
            self.rect.y -= self.speed