import pygame
from config import *
from snake import Snake
from food import Food

def main():
    pygame.init()
    screen = pygame.display.set_mode((Width, Height))
    pygame.display.set_caption(Title)
    clock = pygame.time.Clock()
    
    snake = Snake()
    food = Food()
    score = 0
    
    
    running = True
    game_over = False
    
    
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
                
            if snake.check_collision():
                game_over = True
                
        screen.fill(Black)
        snake.draw(screen)
        food.draw(screen)
        
        
        font = pygame.font.SysFont(None, 35)
        score_text = font.render(f"Score: {score}", True, White)
        screen.blit(score_text, (10,10))
        
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
                game_over = False
            elif keys[pygame.K_q]:
                running = False
            
            
        pygame.display.flip()
        clock.tick(FPS)
        
    pygame.quit()
    
if __name__ == "__main__":
    main()