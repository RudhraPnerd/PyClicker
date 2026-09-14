import pygame
import configs as cfg
import assets as ast

rect_colour = (42, 114, 156)


def draw_shutting_down_confirmation(screen, font):
    screen.fill(cfg.BG_COLOUR)

    title = font.render('PyClicker', True, (0, 0, 0))
    title_rect = title.get_rect(center=(cfg.SCREEN_WIDTH // 2, 80))
    screen.blit(title, title_rect)

    prompt = font.render('Are you sure you want to quit?', True, (0, 0, 0))
    prompt_rect = prompt.get_rect(center=(cfg.SCREEN_WIDTH // 2, cfg.SCREEN_HEIGHT // 2 - 20))
    screen.blit(prompt, prompt_rect)

    screen.blit(ast.yes_button, ast.yes_img_rect)
    screen.blit(ast.no_button, ast.no_img_rect)


def draw_home(screen, font):
    screen.fill(cfg.BG_COLOUR)

    home_title = font.render('PyClicker', True, (0, 0, 0))
    home_rect = home_title.get_rect(center=(cfg.SCREEN_WIDTH // 2, 80))
    screen.blit(home_title, home_rect)

    screen.blit(ast.play_button, ast.play_img_rect)


def draw_shop(screen, font, button_font):
    screen.fill(cfg.BG_COLOUR)

    shop_title = font.render('SHOP', True, (0, 0, 0))
    shop_rect = shop_title.get_rect(center=(cfg.SCREEN_WIDTH // 2, 80))
    screen.blit(shop_title, shop_rect)

    rect_x, rect_y, rect_w, rect_h = 50, 100, 200, 60
    shop_button_rect = pygame.Rect(rect_x, rect_y, rect_w, rect_h)
    pygame.draw.rect(screen, rect_colour, shop_button_rect)

    one_click_power_text = button_font.render('ONE-CLICK POWER', True, (255, 255, 255))
    one_click_power_rect = one_click_power_text.get_rect(center=shop_button_rect.center)
    screen.blit(one_click_power_text, one_click_power_rect)

def draw_not_enough_points(screen, font):
    screen.fill(cfg.BG_COLOUR)

    message = font.render('NOT ENOUGH POINTS', True, (255, 255, 255))
    message_rect = message.get_rect(center=(cfg.SCREEN_WIDTH // 2, 80))

    screen.blit(message, message_rect)
    screen.blit(ast.no_button, ast.no_img_rect)