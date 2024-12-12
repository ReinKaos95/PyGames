import pygame, sys
from config import *
from player import Player
from ball import Ball
from menu import Menu
from pause_menu import PauseMenu
from difficulty_menu import DifficultyMenu
from fonts import Fonts
from endgame import EndGame

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode(RES)
        self.title = pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.fonts = Fonts()
        
        
        # puntuaciones
        self.score1 = 0  # Puntuación del jugador 1
        self.score2 = 0  # Puntuación del jugador 2
        
        # Mostrar puntuaciones
        self.score_font = self.fonts.get_score_font()
        
        #pausa
        self.pause_menu = PauseMenu(self.screen)
        
        # Detener la música cuando se ingrese al juego
        if not pygame.mixer.get_init():
            pygame.mixer.init()
            
        
        # Mostrar menú de dificultad
        difficulty_menu = DifficultyMenu(self.screen)
        selected_difficulty = difficulty_menu.show()
        
        # Configurar la velocidad según la dificultad
        if selected_difficulty == "easy":
            ball_speed_x, ball_speed_y = 3, 3
        elif selected_difficulty == "medium":
            ball_speed_x, ball_speed_y = 5, 5
        elif selected_difficulty == "hard":
            ball_speed_x, ball_speed_y = 7, 7
        else:
            ball_speed_x, ball_speed_y = 3, 3  # Por defecto
            
        #players
        
        # Jugador 1 (izquierda)
        self.player1 = Player(20, Res_Height // 2 - 30, 20, 60, WHITE, PLAYER_SPEED)
        
        # Jugador 2 (derecha)
        self.player2 = Player(Res_Width - 40, Res_Height // 2 - 30, 20, 60, WHITE, PLAYER_SPEED)
                
        # Pelota
        self.ball = Ball(Res_Width // 2 - 15, Res_Height // 2 - 15, 30, 30, WHITE, 3, 3)
        
        # Asignar la velocidad a la pelota

        self.ball.speed_x = ball_speed_x
        self.ball.speed_y = ball_speed_y

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
        pygame.mixer.music.stop()
        """Ciclo principal del juego."""
        while True:
            self.events()
            self.screen.fill(BLACK) # Fondo negro

            # Dibujar la línea central
            pygame.draw.rect(self.screen, WHITE, (Res_Width // 2 - 1, 0, 2, Res_Height))  # Línea central de 2 píxeles de ancho
            
            # Dibujar jugadores
            self.player1.draw(self.screen)
            self.player2.draw(self.screen)
            self.ball.draw(self.screen)
            self.draw_score()  # Dibujar las puntuaciones
            # Movimiento de los jugadores
            
            self.player1.move(pygame.K_w, pygame.K_s, Res_Height) # Jugador 1: W/S
            self.player2.move(pygame.K_UP, pygame.K_DOWN, Res_Height) # Jugador 2: Flechas
                  
            point_side, multiplier = self.ball.move(Res_Width, Res_Height)
            if point_side == "left":
                self.score1 += 1 * multiplier
                self.reset_ball()
            if point_side == "right":
                self.score2 += 1 * multiplier
                self.reset_ball()
            
            # Comprobar si se ha alcanzado el puntaje máximo
            if self.score1 >= MAX_SCORE or self.score2 >= MAX_SCORE:
                winner = "Player 1" if self.score1 >= MAX_SCORE else "Player 2"
                end_game_screen = EndGame(self.screen, winner)
                action = end_game_screen.show()

                if action == "restart":
                    self.reset_game()  # Reiniciar el juego
                    continue
                else:
                    break  # Salir del juego
                
            self.ball.check_collision(self.player1, self.player2)
            
            self.update()
    
    def reset_game(self):
        """Reinicia el juego para una nueva partida."""
        self.score1 = 0
        self.score2 = 0
        self.reset_ball()
        
if __name__ == '__main__':
    game = Game()
    menu = Menu(game.screen)
    menu.show()
    game.run()