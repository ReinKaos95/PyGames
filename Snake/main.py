import pygame, time, sys
from config import *
from snake import Snake
from food import Food


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode(Res)
        self.title = pygame.display.set_caption(Title)
        self.clock = pygame.time.Clock()

        self.snake = Snake()
        self.food = Food()

        self.score = 0

        
    def update(self):
        pygame.display.flip()
        self.clock.tick(FPS)
        
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            self.snake.move(event)

    def draw_score(self):
        pygame.font.init()
        font = pygame.font.SysFont("Arial", 25)
        value = font.render(f"Tu puntuacion: {self.score}", True, Black)
        self.screen.blit(value, [0,0])

    def gameLoop(self):
        game_over = False
        game_close = False

        while not game_over:
            while game_close:
                self.screen.fill(Blue)
                message = "Perdiste! Precione C para continuar, o Q para salir"
                font = pygame.font.SysFont("bahnschrift", 25)
                msg = font.render(message, True, Red)
                self.screen.blit(msg, [Res[0] / 6, Res[1] / 3])
                self.draw_score()

                pygame.display.update()


                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                        if event.key == pygame.K_c:
                            self.snake = Snake()
                            self.food = Food()
                            self.score = 0
                            game_close = False

            self.events()


            if self.snake.x == self.food.x and self.snake.y == self.food.y:
                self.food.new_position()
                self.snake.grow()
                self.score += 1

            if self.snake.check_collision_with_boundaries() or self.snake.check_collision_with_self():
                game_close = True


            self.screen.fill(Blue)
        
            self.food.draw(self.screen)
            self.snake.draw(self.screen)

            self.draw_score()


            self.update()


        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    game = Game()
    game.gameLoop()