import pygame
import configs as cfg

pygame.init()
pygame.mixer.init()

# --- DIMENSIONS ---
MAIN_ICON_SIZE = (220, 220)
TOP_BAR_ICON_SIZE = (44, 44)
BOTTOM_BAR_ICON_SIZE = (54, 54)
ACTION_BUTTON_SIZE = (140, 140)


# Helper function to load and scale images cleanly
def load_and_scale(file_path, dimensions):
    img = pygame.image.load(file_path).convert_alpha()
    return pygame.transform.smoothscale(img, dimensions)

# --- 1. GAMEPLAY ICON (CENTER) ---
python_icon = load_and_scale(cfg.PYTHON_ICON_FILE, MAIN_ICON_SIZE)
img_rect = python_icon.get_rect(center=(cfg.SCREEN_WIDTH // 2, cfg.SCREEN_HEIGHT // 2))

# --- 2. TOP BAR BUTTONS ---
dark_mode_toggle = load_and_scale(cfg.DARK_MODE_FILE, TOP_BAR_ICON_SIZE)
dark_img_rect = dark_mode_toggle.get_rect(topleft=(20, 20))

light_mode_toggle = load_and_scale(cfg.LIGHT_MODE_FILE, TOP_BAR_ICON_SIZE)
light_img_rect = light_mode_toggle.get_rect(topleft=(74, 20))  # Offset by width + 10px spacing

reset_score_button = load_and_scale(cfg.RESET_SCORE_BUTTON_FILE, TOP_BAR_ICON_SIZE)
reset_img_rect = reset_score_button.get_rect(topright=(cfg.SCREEN_WIDTH - 20, 20))

# --- 3. BOTTOM BAR NAVIGATION ---
shopping_button = load_and_scale(cfg.SHOPPING_BUTTON_FILE, BOTTOM_BAR_ICON_SIZE)
shopping_img_rect = shopping_button.get_rect(topleft=(20, cfg.SCREEN_HEIGHT - 74))

home_button = load_and_scale(cfg.HOME_BUTTON_FILE, BOTTOM_BAR_ICON_SIZE)
home_img_rect = home_button.get_rect(topleft=(84, cfg.SCREEN_HEIGHT - 74))

power_button = load_and_scale(cfg.POWER_BUTTON_FILE, BOTTOM_BAR_ICON_SIZE)
power_img_rect = power_button.get_rect(topright=(cfg.SCREEN_WIDTH - 20, cfg.SCREEN_HEIGHT - 74))

mute_button = load_and_scale(cfg.MUTE_BUTTON_FILE, BOTTOM_BAR_ICON_SIZE)
mute_img_rect = mute_button.get_rect(topleft=(665, cfg.SCREEN_HEIGHT - 74))

unmute_button = load_and_scale(cfg.UNMUTE_BUTTON_FILE, BOTTOM_BAR_ICON_SIZE)
unmute_img_rect = unmute_button.get_rect(topleft=(645, cfg.SCREEN_HEIGHT - 74))

# --- 4. ACTION / MODAL BUTTONS ---
play_button = load_and_scale(cfg.PLAY_BUTTON_FILE, ACTION_BUTTON_SIZE)
play_img_rect = play_button.get_rect(center=(cfg.SCREEN_WIDTH // 2, cfg.SCREEN_HEIGHT // 2 + 60))

yes_button = load_and_scale(cfg.YES_BUTTON_FILE, ACTION_BUTTON_SIZE)
yes_img_rect = yes_button.get_rect(center=(cfg.SCREEN_WIDTH // 2 + 80, cfg.SCREEN_HEIGHT // 2 + 60))

no_button = load_and_scale(cfg.EXIT_BUTTON_FILE, ACTION_BUTTON_SIZE)
no_img_rect = no_button.get_rect(center=(cfg.SCREEN_WIDTH // 2 + 80, cfg.SCREEN_HEIGHT // 2 + 60))

back_button = load_and_scale(cfg.BACK_BUTTON_FILE, ACTION_BUTTON_SIZE)
back_img_rect = back_button.get_rect(center=(cfg.SCREEN_WIDTH // 2 - 80, cfg.SCREEN_HEIGHT // 2 + 60))

# --- 5. AUDIO ASSETS ---
click_sound = pygame.mixer.Sound(cfg.CLICK_SOUND_EFFECT_FILE)
reset_sound = pygame.mixer.Sound(cfg.RESET_SOUND_EFFECT_FILE)
one_hundred_score_mark = pygame.mixer.Sound(cfg.ONE_HUNDRED_SCORE_MARK_FILE)
toggle = pygame.mixer.Sound(cfg.DARK_LIGHT_MODE_TOGGLE_SOUND_EFFECT_FILE)
power_off = pygame.mixer.Sound(cfg.POWER_OFF_SOUND_FILE)
teleportation_sound = pygame.mixer.Sound(cfg.TELEPORTATION_SOUND_EFFECT_FILE)
purchase = pygame.mixer.Sound(cfg.PURCHASE_SOUND_EFFECT_FILE)
broke = pygame.mixer.Sound(cfg.BROKE_SOUND_EFFECT_FILE)

# --- 6. SHUTTING DOWN MENU BUTTONS ---
exit_button = load_and_scale(cfg.EXIT_BUTTON_FILE, ACTION_BUTTON_SIZE)
exit_img_rect = exit_button.get_rect(center=(cfg.SCREEN_WIDTH // 2 - 80, cfg.SCREEN_HEIGHT // 2 + 60))

# --- 7. SHOP ITEMS LAYOUT ---
item_width = 300
item_height = 55
start_y = 150
spacing = 70

shop_items = [
    {
        "id": "power_1",
        "name": "+1 CLICK POWER",
        "cost": 10,
        "power_increase": 1,
        "rect": pygame.Rect(cfg.SCREEN_WIDTH // 2 - item_width // 2, start_y, item_width, item_height)
    },
    {
        "id": "power_2",
        "name": "+5 CLICK POWER",
        "cost": 50,
        "power_increase": 5,
        "rect": pygame.Rect(cfg.SCREEN_WIDTH // 2 - item_width // 2, start_y + spacing, item_width, item_height)
    },
    {
        "id": "power_3",
        "name": "+25 CLICK POWER",
        "cost": 200,
        "power_increase": 25,
        "rect": pygame.Rect(cfg.SCREEN_WIDTH // 2 - item_width // 2, start_y + (spacing * 2), item_width, item_height)
    }
]

ALL_SOUNDS = [
    click_sound, reset_sound,
    one_hundred_score_mark, toggle,
    power_off, teleportation_sound,
    purchase, broke,
]



def set_sound_volume(volume_level):
    for sound in ALL_SOUNDS:
        sound.set_volume(volume_level)