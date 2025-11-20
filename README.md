# Nebula Runner

A multi-file Pygame project (exploration + combat + items + simple AI + particles + procedural-ish level building).
![Nebula Runner Screenshot](/2.png)

Files:
- main.py           # entry point
- settings.py       # configuration constants
- engine.py         # game loop, state manager
- player.py         # Player class
- enemy.py          # Enemy classes and AI
- level.py          # Level generation and tile handling
- items.py          # Items, pickups, inventory
- particles.py      # Particle system
- ui.py             # HUD, menus
- utils.py          # helpers
- save.py           # simple save/load
- assets/           # folder for images/sounds (not included here)

Requirements:
- Python 3.8+
- pygame
- numpy (optional, used in some helpers)
- Pillow (optional, improves image handling)

How to run:
1. Install requirements: `pip install pygame numpy`
2. Place this project into a folder. Create an `assets` folder with placeholder images or let the code draw primitives.
3. Run: `python main.py`

Notes:
- Files are modular; you can refactor imports if you want different structure.
- Designed to be extended: boss levels, more enemies, music, save system improvements.
