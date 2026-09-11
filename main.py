import time
import colorama
from colorama import init, Fore, Back, Style
import keyboard

init(autoreset=True)

score = 0

def update_score_display():
    print(f"\r{Style.BRIGHT}Score: {score}", end="", flush=True)

def increment_score():
    global score
    score += 1
    update_score_display()

print(Fore.BLUE + "PyClicker")
print(Style.BRIGHT + "==============")


update_score_display()


keyboard.add_hotkey("enter", increment_score)


print(f"\n{Style.DIM}(Press ENTER to click, or ESC to exit)")
keyboard.wait("esc")

print("\n\nThanks for playing!")