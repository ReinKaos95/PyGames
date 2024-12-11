import pygame, sys
from config import *
from player import Player
from ball import Ball
from menu import Menu
from pause_menu import PauseMenu
from fonts import Fonts

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode(RES)
        self.title = pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.fonts = Fonts()
        
        #players
        
        # Jugador 1 (izquierda)
        self.player1 = Player(20, Res_Height // 2 - 30, 20, 60, WHITE, PLAYER_SPEED)
        
        # Jugador 2 (derecha)
        self.player2 = Player(Res_Width - 40, Res_Height // 2 - 30, 20, 60, WHITE, PLAYER_SPEED)
        
        # Pelota
        self.ball = Ball(Res_Width // 2 - 15, Res_Height // 2 - 15, 30, 30, WHITE, 3, 3)
        
        # puntuaciones
        self.score1 = 0  # Puntuación del jugador 1
        self.score2 = 0  # Puntuación del jugador 2
        
        # Mostrar puntuaciones
        self.score_font = self.fonts.get_score_font()
        
        #pausa
        self.pause_menu = PauseMenu(self.screen)
        
    def reset_ball(self):
        """Reinicia la pelota al centro del campo."""
        self.ball.rect.x = Res_Width // 2 - self.ball.rect.width // 2
        self.ball.rect.y = Res_Height // 2 - self.ball.rect.height // 2
        self.ball.speed_x *= -1  # Cambia la dirección horizontal
        
    def draw_score(self):
        """Dibuja las puntuaciones en la pantalla."""
        score1_surface = self.score_font.render(str(self.score1), True, WHITE)
        score2_surface = self.score_font.render(str(self.score2), True, WHITE)
        
        # Posición de las puntuaciones
        self.screen.blit(score1_surface, (Res_Width // 4, 20))  # Puntuación del jugador 1
        self.screen.blit(score2_surface, (3 * Res_Width // 4, 20))  # Puntuación del jugador 2

    def select_difficulty(self):
        print("selecciona una dificultad: 1. Facil 2. Medio 3. Dificil")
        level = int(input("Elige una opción: "))
        if level == 1:
            self.ball.speed_x, self.ball.speed_y = 3, 3
        elif level == 2:
            self.ball.speed_x, self.ball.speed_y = 5, 5
        elif level == 3:
            self.ball.speed_x, self.ball.speed_y = 7, 7
        
        
    def update(self):
        """Actualiza la pantalla y controla los FPS."""
        pygame.display.flip()
        self.clock.tick(FPS)
        
    def events(self):
        """Gestiona los eventos del juego."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Tecla ESC para pausar
                    self.pause_menu.show()  # Mostrar el menú de pausa
                
    def run(self):
        """Ciclo principal del juego."""
        while True:
            self.events()
            self.screen.fill(BLACK) # Fondo negro
            
            # Dibujar jugadores
            self.player1.draw(self.screen)
            self.player2.draw(self.screen)
            self.ball.draw(self.screen)
            self.draw_score()  # Dibujar las puntuaciones
            # Movimiento de los jugadores
            
            self.player1.move(pygame.K_w, pygame.K_s, Res_Height) # Jugador 1: W/S
            self.player2.move(pygame.K_UP, pygame.K_DOWN, Res_Height) # Jugador 2: Flechas
            
            # Movimiento de la pelota y detección de puntos
            if self.ball.move(Res_Width, Res_Height):
                if self.ball.rect.left <= 0:  # Punto para el jugador 2
                    self.score2 += 1
                    self.reset_ball()
                elif self.ball.rect.right >= Res_Width:  # Punto para el jugador 1
                    self.score1 += 1
                    self.reset_ball()
                
            if self.score1 == MAX_SCORE or self.score2 == MAX_SCORE:
                print(f"Jugador {'1' if self.score1 == MAX_SCORE else '2'} gana!")
                break
                
            self.ball.check_collision(self.player1, self.player2)
            
            self.update()
        
if __name__ == '__main__':
    game = Game()
    menu = Menu(game.screen)
    menu.show()
    game.select_difficulty() 
    game.run()