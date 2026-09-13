import pygame

def read_score(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return int(file.read().strip())
    except (FileNotFoundError, ValueError):
        return 0

def save_score(file_path, score_val):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(str(score_val))

def get_rounded_image(image, corner_radius):
    rect = image.get_rect()
    mask_surface = pygame.Surface(rect.size, pygame.SRCALPHA)

    pygame.draw.rect(mask_surface, (255, 255, 255, 255), rect, border_radius=corner_radius)

    rounded_image = image.copy()
    rounded_image.blit(mask_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)

    return rounded_image
