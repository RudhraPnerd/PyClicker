import pygame
import configs as cfg

pygame.init()
pygame.display.set_mode((cfg.SCREEN_WIDTH, cfg.SCREEN_HEIGHT))

def get_rounded_image(image, corner_radius):
    rect = image.get_rect()
    mask_surface = pygame.Surface(rect.size, pygame.SRCALPHA)
    pygame.draw.rect(mask_surface, (255, 255, 255, 255), rect, border_radius=corner_radius)
    rounded_image = image.copy()
    rounded_image.blit(mask_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)
    return rounded_image

# --- Main Clicker Icon ---
python_icon = pygame.image.load(cfg.PYTHON_ICON_FILE).convert_alpha()
python_icon = pygame.transform.scale(python_icon, (150, 150))
python_icon = get_rounded_image(python_icon, corner_radius=25)
img_rect = python_icon.get_rect(center=(cfg.SCREEN_WIDTH // 2, cfg.SCREEN_HEIGHT // 2))

# --- UI Header Buttons ---
reset_score_button = pygame.image.load(cfg.RESET_SCORE_BUTTON_FILE).convert_alpha()
reset_score_button = pygame.transform.scale(reset_score_button, (80, 40))
reset_score_button = get_rounded_image(reset_score_button, corner_radius=10)
reset_img_rect = reset_score_button.get_rect(topright=(cfg.SCREEN_WIDTH - 80, 20))

dark_mode_toggle = pygame.image.load(cfg.DARK_MODE_FILE).convert_alpha()
dark_mode_toggle = pygame.transform.scale(dark_mode_toggle, (40, 40))
dark_mode_toggle = get_rounded_image(dark_mode_toggle, corner_radius=10)
dark_img_rect = dark_mode_toggle.get_rect(topright=(cfg.SCREEN_WIDTH - 20, 20))

light_mode_toggle = pygame.image.load(cfg.LIGHT_MODE_FILE).convert_alpha()
light_mode_toggle = pygame.transform.scale(light_mode_toggle, (40, 40))
light_mode_toggle = get_rounded_image(light_mode_toggle, corner_radius=10)
light_img_rect = light_mode_toggle.get_rect(topleft=(20, 20))

power_button = pygame.image.load(cfg.POWER_BUTTON_FILE).convert_alpha()
power_button = pygame.transform.scale(power_button, (40, 40))
power_button = get_rounded_image(power_button, corner_radius=10)
power_img_rect = power_button.get_rect(topleft=(70, 20))

shopping_button = pygame.image.load(cfg.SHOPPING_BUTTON_FILE).convert_alpha()
shopping_button = pygame.transform.scale(shopping_button, (80, 40))
shopping_button = get_rounded_image(shopping_button, corner_radius=10)
shopping_img_rect = shopping_button.get_rect(topleft=(120, 20))

# --- Shutdown Menu Buttons ---
yes_button = pygame.image.load(cfg.YES_BUTTON_FILE).convert_alpha()
yes_button = pygame.transform.scale(yes_button, (80, 40))
yes_button = get_rounded_image(yes_button, corner_radius=10)
yes_img_rect = yes_button.get_rect(center=(cfg.SCREEN_WIDTH // 2 - 60, cfg.SCREEN_HEIGHT // 2 + 50))

no_button = pygame.image.load(cfg.NO_BUTTON_FILE).convert_alpha()
no_button = pygame.transform.scale(no_button, (80, 40))
no_button = get_rounded_image(no_button, corner_radius=10)
no_img_rect = no_button.get_rect(center=(cfg.SCREEN_WIDTH // 2 + 60, cfg.SCREEN_HEIGHT // 2 + 50))

# --- Audio Assets ---
click_sound = pygame.mixer.Sound(cfg.CLICK_SOUND_EFFECT_FILE)
reset_sound = pygame.mixer.Sound(cfg.RESET_SOUND_EFFECT_FILE)
one_hundred_score_mark = pygame.mixer.Sound(cfg.ONE_HUNDRED_SCORE_MARK_FILE)
toggle = pygame.mixer.Sound(cfg.DARK_LIGHT_MODE_TOGGLE_SOUND_EFFECT_FILE)
power_off = pygame.mixer.Sound(cfg.POWER_OFF_SOUND_FILE)