import pygame, sys
from config import *
from player import Player
from ball import Ball
from menu import Menu
from pause_menu import PauseMenu

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode(RES)
        self.title = pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        
        #players
        
        # Jugador 1 (izquierda)
        self.player1 = Player(20, Res_Height // 2 - 30, 20, 60, WHITE, PLAYER_SPEED)
        
        # Jugador 2 (derecha)
        self.player2 = Player(Res_Width - 40, Res_Height // 2 - 30, 20, 60, WHITE, PLAYER_SPEED)
        
        # Pelota
        self.ball = Ball(Res_Width // 2 - 15, Res_Height // 2 - 15, 30, 30, WHITE, 3, 3)
        
        self.pause_menu = PauseMenu(self.screen)
        
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
            
            # Movimiento de los jugadores
            
            self.player1.move(pygame.K_w, pygame.K_s, Res_Height) # Jugador 1: W/S
            self.player2.move(pygame.K_UP, pygame.K_DOWN, Res_Height) # Jugador 2: Flechas
            
            if self.ball.move(Res_Width, Res_Height):
                print("Punto marcado")
                
            self.ball.check_collision(self.player1, self.player2)
            
            self.update()
        
if __name__ == '__main__':
    game = Game()
    menu = Menu(game.screen)
    menu.show()
    game.run()