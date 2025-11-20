import random
import pygame
from settings import LEVEL_WIDTH, LEVEL_HEIGHT, TILE_SIZE
from utils import simple_noise

class Level:
    def __init__(self):
        # tilemap = 2D array of 0 (empty) and 1 (solid)
        self.map = [[0 for _ in range(LEVEL_HEIGHT)] for _ in range(LEVEL_WIDTH)]
        self.tiles = []  # rects for collisions

        self.generate()

    def generate(self):
        # basic terrain height using noise
        height_map = []
        for x in range(LEVEL_WIDTH):
            h = int(5 + simple_noise(42, x * 0.2) * 6)
            height_map.append(h)

        for x in range(LEVEL_WIDTH):
            ground_y = LEVEL_HEIGHT - height_map[x]
            for y in range(LEVEL_HEIGHT):
                if y >= ground_y:
                    self.map[x][y] = 1

        self.build_tiles()

    def build_tiles(self):
        self.tiles = []
        for x in range(LEVEL_WIDTH):
            for y in range(LEVEL_HEIGHT):
                if self.map[x][y] == 1:
                    rect = pygame.Rect(
                        x * TILE_SIZE,
                        y * TILE_SIZE,
                        TILE_SIZE,
                        TILE_SIZE
                    )
                    self.tiles.append(rect)

    def get_collisions(self, rect):
        return [t for t in self.tiles if rect.colliderect(t)]

    def draw(self, surf, camera):
        for rect in self.tiles:
            pygame.draw.rect(
                surf,
                (70, 70, 110),
                (rect.x - camera.x, rect.y - camera.y, rect.width, rect.height)
            )
