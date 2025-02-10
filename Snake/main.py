import pygame, random
from config import *
from snake import Snake
from food import Food
from powerup import PowerUp
from poison import Poison

def main():
    pygame.init()
    screen = pygame.display.set_mode((Width, Height))
    pygame.display.set_caption(Title)
    clock = pygame.time.Clock()
    
    snake = Snake()
    food = Food()
    powerup = PowerUp()
    poison = Poison()
    score = 0
    running = True
    game_over = False
    speed = Initial_speed # Velocidad inicial
    
    
    # Cargar high score
    global High_score
    try:
        with open("high_score.dat", "rb") as file:
            High_score = int(file.read())
    except FileNotFoundError:
        High_score = 0


    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if not game_over:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        snake.change_direction(-Block_size, 0)
                    elif event.key == pygame.K_RIGHT:
                        snake.change_direction(Block_size, 0)
                    elif event.key == pygame.K_UP:
                        snake.change_direction(0, -Block_size)
                    elif event.key == pygame.K_DOWN:
                        snake.change_direction(0, Block_size)
        
        
        if not game_over:
            snake.move()
            
            if snake.x == food.x and snake.y == food.y:
                snake.grow()
                food.respawn(snake.body)
                score += 1
                
                # Aumentar velocidad cada 5 puntos
                if score % 5 == 0:
                    speed += 1
                    
                # Actualizar high score
                if score > High_score:
                    High_score = score
                    with open("high_score.dat", "wb") as file:
                        file.write(str(High_score).encode())
            
            # Generar power-up aleatoriamente (1% de probabilidad por frame)
            if not powerup.active and random.randint(1, 100) == 1:
                powerup.respawn(snake.body)
                
            # Verificar si la serpiente come el power-up
            if powerup.active and snake.x == powerup.x and snake.y == powerup.y:
                score += 5
                powerup.active = False
                
            if not poison.active and random.randint(1, 10) == 1:
                poison.respawn(snake.body)
                
            if poison.active and snake.x == poison.x and snake.y == poison.y:
                snake.length = max(1, snake.length - 1)
                speed = max(5, speed - 2)
                poison.active = False
                
                        
            if snake.check_collision():
                game_over = True
                
        screen.fill(Black)
        snake.draw(screen)
        food.draw(screen)
        
        if powerup.active: powerup.draw(screen)
        if poison.active: poison.draw(screen)
        # Mostrar puntuación, high score y nivel
        
        font = pygame.font.SysFont(None, 35)
        score_text = font.render(f"Score: {score}", True, White)
        screen.blit(score_text, (10,10))
        
        # Mostrar high score en pantalla
        high_score_text = font.render(f"High Score: {High_score}", True, White)
        screen.blit(high_score_text, (Width - 200, 10))
        
        level_text = font.render(f"Level: {score // 5 + 1}", True, White)
        screen.blit(level_text, (Width // 2 - 50, 10))
        
        # Manejar Game Over, reinicio y salida
        
        if game_over:
            
            font = pygame.font.SysFont(None, 40)
            game_over_text = font.render("Game Over! Press R to restart, Q to quit", True, White)
            screen.blit(game_over_text, (Width // 2 - 150, Width // 2))
            # Reiniciar al presionar R
            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                snake = Snake()
                food = Food()
                score = 0
                speed = Initial_speed  # Reiniciar velocidad
                game_over = False
            elif keys[pygame.K_q]:
                running = False # Salir del juego
            
            
        pygame.display.flip()
        clock.tick(speed) # Usar la velocidad actual
        
    pygame.quit()
    
if __name__ == "__main__":
    main()