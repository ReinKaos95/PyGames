import pygame
from config import *

def game_over(screen, score, high_score):
    font = pygame.font.SysFont(None, 40)
    title_font = pygame.font.SysFont(None, 60)
    
    title_text = title_font.render("Game Over", True, White)
    score_text = font.render(f"Your Score: {score}", True, White)
    high_score_text = font.render(f"High Score: {high_score}", True, White)
    restart_text = font.render("Press R to Restart", True, White)
    menu_text = font.render("Press M to Return to Menu", True, White)
    quit_text = font.render("Press Q to Quit", True, White)
    
    
    # Posiciones de los textos
    title_rect = title_text.get_rect(center=(Width // 2, Height // 4))
    score_rect = score_text.get_rect(center=(Width // 2, Height // 2.5))
    high_score_rect = high_score_text.get_rect(center=(Width // 2, Height // 2))
    restart_rect = restart_text.get_rect(center=(Width // 2, Height // 1.7))
    menu_rect = menu_text.get_rect(center=(Width // 2, Height // 1.5))
    quit_rect = quit_text.get_rect(center=(Width // 2, Height // 1.3))

    while True:
        screen.fill(Black)
        screen.blit(title_text, title_rect)
        screen.blit(score_text, score_rect)
        screen.blit(high_score_text, high_score_rect)
        screen.blit(restart_text, restart_rect)
        screen.blit(menu_text, menu_rect)
        screen.blit(quit_text, quit_rect)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return "restart"
                elif event.key == pygame.K_m:
                    return "menu"
                elif event.key == pygame.K_q:
                    return "quit"