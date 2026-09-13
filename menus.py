import pygame
import configs as cfg
import assets as ast


def draw_shutting_down_conformation(screen, font):
    screen.fill(cfg.BG_COLOUR)

    title = font.render('PyClicker', True, (0, 0, 0))
    title_rect = title.get_rect(center=(cfg.SCREEN_WIDTH // 2, 80))
    screen.blit(title, title_rect)

    prompt = font.render('Are you sure you want to quit?', True, (0, 0, 0))
    prompt_rect = prompt.get_rect(center=(cfg.SCREEN_WIDTH // 2, cfg.SCREEN_HEIGHT // 2 - 20))
    screen.blit(prompt, prompt_rect)

    screen.blit(ast.yes_button, ast.yes_img_rect)
    screen.blit(ast.no_button, ast.no_img_rect)
