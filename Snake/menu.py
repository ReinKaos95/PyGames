import pygame
from config import *

def menu(screen):
    font = pygame.font.SysFont(None, 40)
    title_font = pygame.font.SysFont(None, 60)
    
    title_text = title_font.render("Snake Game", True, White)
    start_text = title_font.render("Press S to Start", True, White)
    reset_text = title_font.render("Press R to Restore score", True, White)
    quit_text = title_font.render("Press Q to Quit", True, White)
    
    title_rect = title_text.get_rect(center=(Width // 2 , Height // 3))
    start_rect = start_text.get_rect(center=(Width // 2 , Height // 2))
    reset_rect = reset_text.get_rect(center=(Width // 2 , Height // 2 + 50))
    quit_rect = quit_text.get_rect(center=(Width // 2 , Height // 2 + 100))
        
    # Mensaje de confirmación
    confirm_font = pygame.font.SysFont(None, 30)
    confirm_text = confirm_font.render("High Score Reset!", True, Green)
    confirm_rect = confirm_text.get_rect(center=(Width // 2, Height // 2 + 150))
    show_confirm = False  # Controla si se muestra el mensaje de confirmación
        
    while True:
        screen.fill(Black)
        screen.blit(title_text, title_rect)
        screen.blit(start_text, start_rect)
        screen.blit(reset_text, reset_rect)
        screen.blit(quit_text, quit_rect)
        
        if show_confirm:
            screen.blit(confirm_text, confirm_rect)
        
        pygame.display.flip()
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    return "start"
                elif event.key == pygame.K_r:
                    with open("high_score.dat", "w") as file:
                        file.write("0")
                    show_confirm = True
                elif event.key == pygame.K_q:
                    return "quit"