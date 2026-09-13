import pygame
import configs as cfg
import score_func as sf
import time

pygame.init()

screen = pygame.display.set_mode((cfg.SCREEN_WIDTH, cfg.SCREEN_HEIGHT))
pygame.display.set_caption('PyClicker')

import assets as ast

FONT = pygame.font.Font(cfg.FONT_NAME, cfg.FONT_SIZE)
font_colour = pygame.Color('black')

score = sf.read_score(cfg.SCORE_FILE)

dark_mode = False
light_mode = True

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                ast.power_off.play()
                print('Shutting down...')
                time.sleep(3)
                running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if ast.img_rect.collidepoint(event.pos):
                    ast.click_sound.play()
                    score += 1
                    sf.save_score(cfg.SCORE_FILE, score)

                    if score > 0 and score % 100 == 0:
                        ast.one_hundred_score_mark.play()

                elif ast.reset_img_rect.collidepoint(event.pos):
                    ast.reset_sound.play()
                    score = 0
                    sf.save_score(cfg.SCORE_FILE, score)

                elif ast.light_img_rect.collidepoint(event.pos):
                    light_mode = True
                    dark_mode = False
                    ast.dark_light_mode_toggle.play()

                elif ast.dark_img_rect.collidepoint(event.pos):
                    dark_mode = True
                    light_mode = False
                    ast.dark_light_mode_toggle.play()

                elif ast.power_img_rect.collidepoint(event.pos):
                    ast.power_off.play()
                    print('Shutting down...')
                    time.sleep(3)
                    running = False

    if light_mode:
        cfg.BG_COLOUR = cfg.LIGHT_MODE_BG_COLOUR
        font_colour = pygame.Color('black')
    elif dark_mode:
        cfg.BG_COLOUR = cfg.DARK_MODE_BG_COLOUR
        font_colour = pygame.Color('white')

    screen.fill(cfg.BG_COLOUR)

    screen.blit(ast.python_icon, ast.img_rect)

    score_surface = FONT.render(f"Score: {score}", True, font_colour)
    score_rect = score_surface.get_rect(center=(cfg.SCREEN_WIDTH // 2, 40))
    screen.blit(score_surface, score_rect)

    screen.blit(ast.reset_score_button, ast.reset_img_rect)

    screen.blit(ast.dark_mode_toggle, ast.dark_img_rect)
    screen.blit(ast.light_mode_toggle, ast.light_img_rect)
    screen.blit(ast.power_button, ast.power_img_rect)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()