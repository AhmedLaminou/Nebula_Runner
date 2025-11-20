import pygame
from utils import draw_text

class UI:
    def __init__(self):
        pass

    def draw_hud(self, surf, player):
        draw_text(surf, f"HP: {player.health}/{player.max_health}", 38, 20, 20)
