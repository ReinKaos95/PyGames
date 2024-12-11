import pygame, sys
from config import *
from fonts import Fonts
from utils import draw_button

class DifficultyMenu:
    def __init__(self, screen):
        self.screen = screen
        self.fonts = Fonts()
        
        if not pygame.mixer.get_init():
            pygame.mixer.init()
            
        self.title_font = self.fonts.get_title_font()
        self.button_font = self.fonts.get_button_font()
        
        # Cargar sonidos
        self.click_sound = pygame.mixer.Sound("audio/click.wav")  # Sonido al hacer clic
        self.hover_sound = pygame.mixer.Sound("audio/hover.wav")  # Sonido al pasar el mouse (opcional)
        self.hover_sound_played = False  # Para evitar reproducir el sonido de hover repetidamente
        
    def show(self):
        running = True
        while running:
            self.screen.fill(BLACK)
            
            # Título
            title_surface = self.title_font.render("Selecciona Dificultad", True, WHITE)
            self.screen.blit(title_surface, (Res_Width // 2 - title_surface.get_width() // 2, 50))
            
            # Botones de dificultad
            easy_button = pygame.Rect(Res_Width // 2 - 100, 150, 200, 50)
            draw_button(self.screen, easy_button, "Fácil", self.button_font, BLACK, WHITE)
            
            medium_button = pygame.Rect(Res_Width // 2 - 100, 250, 200, 50)
            draw_button(self.screen, medium_button, "Medio", self.button_font, BLACK, WHITE)
            
            hard_button = pygame.Rect(Res_Width // 2 - 100, 350, 200, 50)
            draw_button(self.screen, hard_button, "Difícil", self.button_font, BLACK, WHITE)
            
            pygame.display.flip()
            
            # Manejo de eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if easy_button.collidepoint(event.pos):
                        difficulty = "easy"
                        running = False
                    if medium_button.collidepoint(event.pos):
                        difficulty = "medium"
                        running = False
                    if hard_button.collidepoint(event.pos):
                        difficulty = "hard"
                        running = False

        return difficulty