import pygame, time
from config import *

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode(Res)
        self.title = pygame.display.set_caption(Title)
        self.clock = pygame.time.Clock()
        
    def update(self):
        pygame.display.flip()
        self.clock.tick(FPS)
        
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
    
        
if __name__ == '__main__':
    game = Game()
    game.run()