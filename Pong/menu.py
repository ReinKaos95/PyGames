import pygame, sys
from config import *
from fonts import Fonts
from utils import draw_button

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.fonts = Fonts()

        # Cargar música de fondo
        pygame.mixer.music.load("audio/pong.wav")  # Asegúrate de que la ruta sea correcta
        pygame.mixer.music.play(-1, 0.0)  # Reproduce en bucle (-1 significa bucle infinito)
        
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
            
            title_surface = self.title_font.render("Pong", True, WHITE)
            self.screen.blit(title_surface, (Res_Width // 2 - title_surface.get_width() // 2, 50))
            
            start_button = pygame.Rect(Res_Width // 2 - 100, 150, 200, 50)
            draw_button(self.screen, start_button, "Start", self.button_font, BLACK, WHITE)
            
            quit_button = pygame.Rect(Res_Width // 2 -100, 250, 200, 50)
            draw_button(self.screen, quit_button, "Exit", self.button_font, BLACK, WHITE)
            
            # Detectar posición del mouse para hover
            mouse_pos = pygame.mouse.get_pos()
            if start_button.collidepoint(mouse_pos) or quit_button.collidepoint(mouse_pos):
                if not self.hover_sound_played:  # Reproducir sonido de hover una vez
                    self.hover_sound.play()
                    self.hover_sound_played = True
            else:
                self.hover_sound_played = False  # Restablecer para futuras reproducciones

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