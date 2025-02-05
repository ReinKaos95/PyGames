import pygame

def draw_button(screen, rect, text, font, text_color, button_color):
    pygame.draw.rect(screen, button_color, rect)
    text_surface = font.render(text, True, text_color)
    screen.blit(text_surface, (
        rect.x + (rect.width - text_surface.get_width()) // 2,
        rect.y + (rect.height - text_surface.get_height()) // 2
    ))