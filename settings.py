import pygame

# Window
WIDTH = 1280
HEIGHT = 720
FPS = 60
TITLE = "Nebula Runner"

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (40, 40, 40)

# Player
PLAYER_SPEED = 320  # pixels per second
PLAYER_RADIUS = 18
PLAYER_JUMP_IMPULSE = -420
PLAYER_MAX_HEALTH = 100

# Physics
GRAVITY = 1400  # px/s^2
TERMINAL_VEL = 1000

# Level
TILE_SIZE = 48
LEVEL_WIDTH = 80
LEVEL_HEIGHT = 16

# Gameplay
MAX_ENEMIES = 14
SPAWN_PADDING = 3

# UI
FONT_NAME = None  # default pygame font

# Paths
ASSETS_DIR = "assets"
