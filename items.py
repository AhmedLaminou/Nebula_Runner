import pygame
from utils import vec, rand_color
from particles import ParticleSystem

ITEM_RADIUS = 14

class Item:
    def __init__(self, pos, kind="energy", value=10):
        self.pos = vec(pos)
        self.kind = kind
        self.value = value
        self.radius = ITEM_RADIUS
        self.color = rand_color()
        self.particles = ParticleSystem()
        self.timer = 0

    def update(self, dt):
        self.timer += dt
        # floating effect
        self.pos.y += 0.5 * pygame.math.sin(self.timer * 3)
        self.particles.emit(self.pos, count=1, spread=10, speed=30, life=0.3)
        self.particles.update(dt)

    def draw(self, surf, camera):
        pygame.draw.circle(
            surf,
            self.color,
            (int(self.pos.x - camera.x), int(self.pos.y - camera.y)),
            self.radius
        )
        self.particles.draw(surf, camera)

    def collides_with_point(self, point):
        return (self.pos - point).length() <= self.radius
