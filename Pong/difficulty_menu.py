import pygame, sys
from config import *
from fonts import Fonts
from utils import draw_button

class DifficultyMenu:
    def __init__(self, screen):
        self.screen = screen
        self.fonts = Fonts()
            
        self.title_font = self.fonts.get_title_font()
        self.button_font = self.fonts.get_button_font()
                
    def show(self):
        running = True
        difficulty = None
        
        button_width = 200
        button_height = 30
        button_margin = 20  # Espacio entre los botones
        
        start_y = Res_Height // 2 - (button_height * 3 + button_margin * 2) // 2  # Centra los botones verticalmente
        
        while running:
            
            self.screen.fill(BLACK)
            
            # Título
            title_surface = self.title_font.render("Selecciona Dificultad", True, WHITE)
            self.screen.blit(title_surface, (Res_Width // 2 - title_surface.get_width() // 2, 50))
            
            # Botones de dificultad
            easy_button = pygame.Rect(Res_Width // 2 - button_width // 2, start_y, button_width, button_height)
            draw_button(self.screen, easy_button, "Fácil", self.button_font, BLACK, WHITE)
            
            medium_button = pygame.Rect(Res_Width // 2 - button_width // 2, start_y + button_height + button_margin, button_width, button_height)
            draw_button(self.screen, medium_button, "Medio", self.button_font, BLACK, WHITE)
            
            hard_button = pygame.Rect(Res_Width // 2 - button_width // 2, start_y + 2 * (button_height + button_margin), button_width, button_height)
            draw_button(self.screen, hard_button, "Difícil", self.button_font, BLACK, WHITE)
            
            pygame.display.flip()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if easy_button.collidepoint(event.pos):
                        difficulty = "easy"
                        print("easy")
                        running = False
                    elif medium_button.collidepoint(event.pos):
                        difficulty = "medium"
                        print("medium")
                        running = False
                    elif hard_button.collidepoint(event.pos):
                        difficulty = "hard"
                        print("hard")
                        running = False
            
        return difficulty