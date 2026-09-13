import time
import pygame
import configs as cfg
import score_func as sf
import assets as ast
import menus

pygame.init()

screen = pygame.display.set_mode((cfg.SCREEN_WIDTH, cfg.SCREEN_HEIGHT))
pygame.display.set_caption('PyClicker')

FONT = pygame.font.Font(cfg.FONT_NAME, cfg.FONT_SIZE)
SCORE_FONT = pygame.font.Font(cfg.FONT_NAME, cfg.FONT_SIZE + 50)

font_colour = pygame.Color('black')

current_state = cfg.STATE_HOME
previous_state = cfg.STATE_HOME

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
                if current_state == cfg.STATE_GAME:
                    previous_state = cfg.STATE_GAME
                    current_state = cfg.STATE_SHUTTING_DOWN
                elif current_state == cfg.STATE_SHUTTING_DOWN:
                    current_state = previous_state
                elif current_state == cfg.STATE_SHOP:
                    current_state = cfg.STATE_GAME
                elif current_state == cfg.STATE_HOME:
                    previous_state = cfg.STATE_HOME
                    current_state = cfg.STATE_SHUTTING_DOWN

            elif event.key == pygame.K_SPACE:
                if current_state == cfg.STATE_HOME:
                    current_state = cfg.STATE_GAME

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if current_state == cfg.STATE_GAME:
                if ast.img_rect.collidepoint(event.pos):
                    ast.click_sound.play()
                    score += cfg.CLICK_POWER
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
                    ast.toggle.play()

                elif ast.dark_img_rect.collidepoint(event.pos):
                    dark_mode = True
                    light_mode = False
                    ast.toggle.play()

                elif ast.power_img_rect.collidepoint(event.pos):
                    ast.toggle.play()
                    previous_state = cfg.STATE_GAME
                    current_state = cfg.STATE_SHUTTING_DOWN

                elif ast.shopping_img_rect.collidepoint(event.pos):
                    ast.toggle.play()
                    current_state = cfg.STATE_SHOP

                elif ast.home_img_rect.collidepoint(event.pos):
                    ast.toggle.play()
                    current_state = cfg.STATE_HOME

            elif current_state == cfg.STATE_SHUTTING_DOWN:
                if ast.yes_img_rect.collidepoint(event.pos):
                    ast.power_off.play()
                    time.sleep(1)
                    running = False
                elif ast.no_img_rect.collidepoint(event.pos):
                    ast.toggle.play()
                    current_state = previous_state

            elif current_state == cfg.STATE_HOME:
                if ast.play_img_rect.collidepoint(event.pos):
                    ast.toggle.play()
                    time.sleep(1.5)
                    ast.teleportation_sound.play()
                    previous_state = cfg.STATE_HOME
                    current_state = cfg.STATE_GAME

    if light_mode:
        cfg.BG_COLOUR = cfg.LIGHT_MODE_BG_COLOUR
        font_colour = pygame.Color('black')
    elif dark_mode:
        cfg.BG_COLOUR = cfg.DARK_MODE_BG_COLOUR
        font_colour = pygame.Color('white')

    if current_state == cfg.STATE_GAME:
        screen.fill(cfg.BG_COLOUR)
        screen.blit(ast.python_icon, ast.img_rect)

        score_surface = SCORE_FONT.render(f"{score}", True, font_colour)
        score_rect = score_surface.get_rect(center=(cfg.SCREEN_WIDTH // 2, 90))
        screen.blit(score_surface, score_rect)

        screen.blit(ast.reset_score_button, ast.reset_img_rect)
        screen.blit(ast.dark_mode_toggle, ast.dark_img_rect)
        screen.blit(ast.light_mode_toggle, ast.light_img_rect)
        screen.blit(ast.power_button, ast.power_img_rect)
        screen.blit(ast.shopping_button, ast.shopping_img_rect)
        screen.blit(ast.home_button, ast.home_img_rect)

    elif current_state == cfg.STATE_SHUTTING_DOWN:
        menus.draw_shutting_down_confirmation(screen, FONT)

    elif current_state == cfg.STATE_HOME:
        menus.draw_home(screen, FONT)

    pygame.display.flip()
    clock.tick(cfg.FPS)

pygame.quit()