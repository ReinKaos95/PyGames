import pygame

class Ball:
    def __init__(self, x, y, width, height, color, speed_x, speed_y):
        self.rect = pygame.Rect(x, y, width, height) 
        self.color = color
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.max_speed = 10 
    
    def draw(self, window):
        """Dibuja la pelota en la ventana."""
        pygame.draw.ellipse(window, self.color, self.rect)
        
    def move(self, screen_width, screen_height):
        """Mueve la pelota y verifica colisiones con los bordes."""
        self.rect.x += self.speed_x 
        self.rect.y += self.speed_y
        
        # Rebote en los bordes superior e inferior
        if self.rect.top <= 0 or self.rect.bottom >= screen_height:
            self.speed_y *= -1
            
        # Rebote en los bordes izquierdo y derecho (para reiniciar más adelante)
        if self.rect.left <= 0:
            return "right", abs(self.speed_x)
        elif self.rect.right >= screen_width:
            return "left", abs(self.speed_x)
        return None, None
    
    def bounce(self, is_horizontal=True):
        """Invierte la dirección horizontal de la pelota."""
        if is_horizontal:
            self.speed_x *= -1
        else:
            self.speed_y *= -1
            
        self.speed_x = max(min(self.speed_x, self.max_speed), -self.max_speed)
        self.speed_y = max(min(self.speed_y, self.max_speed), -self.max_speed)
        
        
    def check_collision(self, player1, player2):
        if self.rect.colliderect(player1.rect):
            self.speed_x = abs(self.speed_x)   # No reducir la velocidad
            self.adjust_speed(player1)
            
        if self.rect.colliderect(player2.rect):
            self.speed_x = -abs(self.speed_x) # No reducir la velocidad
            self.adjust_speed(player2)

    def adjust_speed(self, player):
        relative_intersect = (self.rect.centery - player.rect.centery) / (player.rect.height / 2)
        
        self.speed_y = relative_intersect * abs(self.speed_x) # Mantiene el ángulo
        
        self.speed_y = max(min(self.speed_y, 6), -6)