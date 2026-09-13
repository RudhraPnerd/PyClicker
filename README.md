# PyClicker

PyClicker is a clean, modular desktop clicker game built using Python and Pygame. It features score tracking, persistence, light/dark mode toggling, custom rounded image borders, and sound effects.

---

## Features

* **Click Mechanics:** Interactive Python icon clicker with score updates and milestone sound triggers.
* **Persistent Scoring:** High scores automatically save to a local text file and reload upon launch.
* **Theme Support:** Dynamic light and dark mode switching with automatic text and background color updates.
* **Audio System:** Sound effects for clicking, resetting score, toggling themes, power options, and achieving 100-point milestones.
* **Custom Rounded Visuals:** Surface masking utility that programmatically applies border radius to image assets.
* **Graceful Shutdown:** Application termination sequence via a clickable UI power button or the `ESC` key.

---

## Project Structure

```text
PyClicker/
├── main.py              # Main execution loop, screen rendering, and event listener
├── assets.py            # Image asset loading, programmatic rounding, rect positions, and SFX
├── configs.py           # Project constants, file paths, dimensions, and color values
├── score_func.py        # File I/O operations for reading and saving game scores
├── assets/              # PNG image assets (icons, buttons, toggles)
└── sfx/                 # Sound effect files (.wav)
