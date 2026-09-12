import pygame
import configs as cfg

pygame.init()

screen = pygame.display.set_mode((cfg.SCREEN_WIDTH, cfg.SCREEN_HEIGHT))
pygame.display.set_caption('PyClicker')

python_icon = pygame.image.load(cfg.PYTHON_ICON_FILE).convert_alpha()

python_icon = pygame.transform.scale(python_icon, (150, 150))

img_rect = python_icon.get_rect(center=(cfg.SCREEN_WIDTH // 2, cfg.SCREEN_HEIGHT // 2))

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(cfg.BG_COLOUR)
    screen.blit(python_icon, img_rect)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()