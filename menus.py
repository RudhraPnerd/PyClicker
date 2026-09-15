import pygame
import configs as cfg
import assets as ast

rect_colour = (42, 114, 156)
disabled_colour = (100, 100, 100)


def draw_shutting_down_confirmation(screen, font):
    screen.fill(cfg.BG_COLOUR)

    title = font.render('PyClicker', True, (0, 0, 0))
    title_rect = title.get_rect(center=(cfg.SCREEN_WIDTH // 2, 80))
    screen.blit(title, title_rect)

    prompt = font.render('Are you sure you want to quit?', True, (0, 0, 0))
    prompt_rect = prompt.get_rect(center=(cfg.SCREEN_WIDTH // 2, cfg.SCREEN_HEIGHT // 2 - 20))
    screen.blit(prompt, prompt_rect)

    screen.blit(ast.exit_button, ast.exit_img_rect)

def draw_home(screen, font):
    screen.fill(cfg.BG_COLOUR)

    home_title = font.render('PyClicker', True, (0, 0, 0))
    home_rect = home_title.get_rect(center=(cfg.SCREEN_WIDTH // 2, 80))
    screen.blit(home_title, home_rect)

    screen.blit(ast.play_button, ast.play_img_rect)


def draw_shop(screen, font, button_font, score):
    screen.fill(cfg.BG_COLOUR)

    shop_title = font.render('SHOP', True, (0, 0, 0))
    shop_rect = shop_title.get_rect(center=(cfg.SCREEN_WIDTH // 2, 40))
    screen.blit(shop_title, shop_rect)

    for item in ast.shop_items:
        can_afford = score >= item["cost"]
        color = rect_colour if can_afford else disabled_colour

        pygame.draw.rect(screen, color, item["rect"])

        text_str = f"{item['name']} (${item['cost']})"
        text_color = (255, 255, 255) if can_afford else (180, 180, 180)

        label_text = button_font.render(text_str, True, text_color)
        label_rect = label_text.get_rect(center=item["rect"].center)
        screen.blit(label_text, label_rect)


def draw_not_enough_points(screen, font):
    screen.fill(cfg.BG_COLOUR)

    title = font.render('Not Enough Points!', True, (255, 0, 0))
    title_rect = title.get_rect(center=(cfg.SCREEN_WIDTH // 2, cfg.SCREEN_HEIGHT // 2))
    screen.blit(title, title_rect)

    screen.blit(ast.no_button, ast.no_img_rect)

def draw_reset_confirmation(screen, font):
    screen.fill(cfg.BG_COLOUR)

    title = font.render('Are you sure you want to reset the game.'
                        'This cannot be undone', True, (255, 0, 0))
    title_rect = title.get_rect(center=(cfg.SCREEN_WIDTH // 2, 80))
    screen.blit(title, title_rect)
    screen.blit(ast.yes_button, ast.yes_img_rect)
    screen.blit(ast.back_button, ast.back_img_rect)