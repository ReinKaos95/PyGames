import pygame, sys
from config import *
from fonts import Fonts
from utils import draw_button

class PauseMenu:
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
            
            title_surface = self.title_font.render("Pausa", True, WHITE)
            self.screen.blit(title_surface, (Res_Width // 2 - title_surface.get_width() // 2, 50))
            
            start_button = pygame.Rect(Res_Width // 2 - 100, 150, 200, 50)
            pygame.draw.rect(self.screen, WHITE, start_button)
            start_text = self.button_font.render("Continue", True, BLACK)
            self.screen.blit(start_text, (start_button.x + (start_button.width - start_text.get_width()) // 2,
                                          start_button.y + (start_button.height - start_text.get_height()) // 2))
            
            quit_button = pygame.Rect(Res_Width // 2 -100, 250, 200, 50)
            pygame.draw.rect(self.screen, WHITE, quit_button)
            quit_text  = self.button_font.render("Exit", True, BLACK)
            self.screen.blit(quit_text, (quit_button.x + (quit_button.width - quit_text.get_width()) // 2,
                                          quit_button.y + (quit_button.height - quit_text.get_height()) // 2))
            
            pygame.display.flip()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if start_button.collidepoint(event.pos):
                        self.click_sound.play()  # Reproducir sonido de clic
                        running = False
                    if quit_button.collidepoint(event.pos):
                        self.click_sound.play() 
                        pygame.quit()
                        sys.exit()