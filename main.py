import pygame
import configs as cfg
import score_func as sf

pygame.init()

screen = pygame.display.set_mode((cfg.SCREEN_WIDTH, cfg.SCREEN_HEIGHT))
pygame.display.set_caption('PyClicker')

FONT = pygame.font.Font(cfg.FONT_NAME, cfg.FONT_SIZE)

score = sf.read_score(cfg.SCORE_FILE)

#===============================ASSETS==================================================

python_icon = pygame.image.load(cfg.PYTHON_ICON_FILE).convert_alpha()
python_icon = pygame.transform.scale(python_icon, (150, 150))

img_rect = python_icon.get_rect(center=(cfg.SCREEN_WIDTH // 2, cfg.SCREEN_HEIGHT // 2))

reset_score_button = pygame.image.load(cfg.RESET_SCORE_BUTTON_FILE).convert_alpha()
reset_score_button = pygame.transform.scale(reset_score_button, (80, 40))

reset_img_rect = reset_score_button.get_rect(center=(cfg.SCREEN_WIDTH - 60, 30))

#=======================================================================================

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if img_rect.collidepoint(event.pos):
                    score += 1
                    sf.save_score(cfg.SCORE_FILE, score)
                elif reset_img_rect.collidepoint(event.pos):
                    score = 0
                    sf.save_score(cfg.SCORE_FILE, score)

    screen.fill(cfg.BG_COLOUR)

    screen.blit(python_icon, img_rect)

    score_surface = FONT.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_surface, (20, 20))
    screen.blit(reset_score_button, reset_img_rect)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()