import pygame, sys
from config import *
from fonts import Fonts
from utils import draw_button

class EndGame:
    def __init__(self, screen, winner):
        self.screen = screen
        self.fonts = Fonts()
        self.title_font = self.fonts.get_title_font()
        self.button_font = self.fonts.get_button_font()
        self.winner = winner
        
        if not pygame.mixer.get_init():
            pygame.mixer.init()
        
        # Cargar sonidos (opcional)
        self.click_sound = pygame.mixer.Sound("audio/click.wav")  # Sonido al hacer clic
        self.hover_sound = pygame.mixer.Sound("audio/hover.wav")  # Sonido al pasar el mouse
        
    def show(self):
        running = True
        while running:
            self.screen.fill(BLACK)
            
            # Título dependiendo de si el jugador ganó o perdió
            title_text = "¡Ganaste!" if self.winner == "Player 1" else "¡Perdiste!"
            title_surface = self.title_font.render(title_text, True, WHITE)
            self.screen.blit(title_surface, (Res_Width // 2 - title_surface.get_width() // 2, 50))
            
            restart_button = pygame.Rect(Res_Width // 2 - 100, 150, 200, 50)
            draw_button(self.screen, restart_button, "Reiniciar", self.button_font, BLACK, WHITE)
            
            quit_button = pygame.Rect(Res_Width // 2 - 100, 250, 200, 50)
            draw_button(self.screen, quit_button, "Salir", self.button_font, BLACK, WHITE)

            pygame.display.flip()

            # Manejo de eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if restart_button.collidepoint(event.pos):
                        self.click_sound.play()  # Sonido de clic
                        running = False
                        return "restart"  # Retorna "restart" para reiniciar el juego
                    if quit_button.collidepoint(event.pos):
                        self.click_sound.play()  # Sonido de clic
                        pygame.quit()
                        sys.exit()