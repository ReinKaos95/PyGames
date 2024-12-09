import pygame

class Fonts:
    def __init__(self):
        pygame.font.init()
        self.title_font = pygame.font.Font(None, 74)  # Fuente del título
        self.button_font = pygame.font.Font(None, 36)  # Fuente de botones
        self.score_font = pygame.font.Font(None, 50)  # Fuente para la puntuación
        self.custom_font = pygame.font.Font('Comic Sans MS.ttf', 36)  # Ejemplo de fuente personalizada (opcional)
        
    def get_title_font(self):
        return self.title_font
    
    def get_button_font(self):
        return self.button_font
    
    def get_score_font(self):
        return self.score_font