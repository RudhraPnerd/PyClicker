import pygame
import configs as cfg
import score_func as sf
import time

pygame.init()

screen = pygame.display.set_mode((cfg.SCREEN_WIDTH, cfg.SCREEN_HEIGHT))
pygame.display.set_caption('PyClicker')

FONT = pygame.font.Font(cfg.FONT_NAME, cfg.FONT_SIZE)
font_colour = pygame.Color('black')

score = sf.read_score(cfg.SCORE_FILE)

dark_mode = False
light_mode = True

def get_rounded_image(image, corner_radius):
    rect = image.get_rect()
    mask_surface = pygame.Surface(rect.size, pygame.SRCALPHA)

    pygame.draw.rect(mask_surface, (255, 255, 255, 255), rect, border_radius=corner_radius)

    rounded_image = image.copy()
    rounded_image.blit(mask_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)

    return rounded_image

python_icon = pygame.image.load(cfg.PYTHON_ICON_FILE).convert_alpha()
python_icon = pygame.transform.scale(python_icon, (150, 150))
python_icon = get_rounded_image(python_icon, corner_radius=25)
img_rect = python_icon.get_rect(center=(cfg.SCREEN_WIDTH // 2, cfg.SCREEN_HEIGHT // 2))

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

click_sound = pygame.mixer.Sound(cfg.CLICK_SOUND_EFFECT_FILE)
reset_sound = pygame.mixer.Sound(cfg.RESET_SOUND_EFFECT_FILE)
one_hundred_score_mark = pygame.mixer.Sound(cfg.ONE_HUNDRED_SCORE_MARK_FILE)
dark_light_mode_toggle = pygame.mixer.Sound(cfg.DARK_LIGHT_MODE_TOGGLE_SOUND_EFFECT_FILE)
power_off = pygame.mixer.Sound(cfg.POWER_OFF_SOUND_FILE)

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                power_off.play()
                print('Shutting down...')
                time.sleep(3)
                running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if img_rect.collidepoint(event.pos):
                    click_sound.play()
                    score += 1
                    sf.save_score(cfg.SCORE_FILE, score)

                    if score > 0 and score % 100 == 0:
                        one_hundred_score_mark.play()

                elif reset_img_rect.collidepoint(event.pos):
                    reset_sound.play()
                    score = 0
                    sf.save_score(cfg.SCORE_FILE, score)

                elif light_img_rect.collidepoint(event.pos):
                    light_mode = True
                    dark_mode = False
                    dark_light_mode_toggle.play()

                elif dark_img_rect.collidepoint(event.pos):
                    dark_mode = True
                    light_mode = False
                    dark_light_mode_toggle.play()

                elif power_img_rect.collidepoint(event.pos):
                    power_off.play()
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

    screen.blit(python_icon, img_rect)

    score_surface = FONT.render(f"Score: {score}", True, font_colour)
    score_rect = score_surface.get_rect(center=(cfg.SCREEN_WIDTH // 2, 40))
    screen.blit(score_surface, score_rect)

    screen.blit(reset_score_button, reset_img_rect)

    screen.blit(dark_mode_toggle, dark_img_rect)
    screen.blit(light_mode_toggle, light_img_rect)
    screen.blit(power_button, power_img_rect)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()