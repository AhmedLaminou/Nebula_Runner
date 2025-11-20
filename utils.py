import math
import random
import pygame
from typing import Tuple

vec = pygame.math.Vector2

def clamp(x, a, b):
    return max(a, min(b, x))

def lerp(a, b, t):
    return a + (b - a) * t

def draw_text(surface, text, size, x, y, color=(255, 255, 255), center=False):
    font = pygame.font.Font(None, size)
    txt = font.render(text, True, color)
    rect = txt.get_rect()
    if center:
        rect.center = (x, y)
    else:
        rect.topleft = (x, y)
    surface.blit(txt, rect)

def rand_color():
    return (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))

# small lightweight perlin-like noise using random gradients
def simple_noise(seed, x):
    random.seed(seed + int(math.floor(x)))
    return random.random()
