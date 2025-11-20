import random
import pygame
from typing import List
from utils import vec, rand_color
import math

class Particle:
    def __init__(self, pos, vel, life, radius=3, color=None):
        self.pos = vec(pos)
        self.vel = vec(vel)
        self.life = life
        self.max_life = life
        self.radius = radius
        self.color = color or rand_color()

    def update(self, dt):
        self.life -= dt
        self.pos += self.vel * dt
        # apply small drag
        self.vel *= 0.99

    def draw(self, surf, camera):
        if self.life <= 0:
            return
        alpha = int(255 * max(0, self.life / self.max_life))
        s = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(s, (*self.color, alpha), (self.radius, self.radius), self.radius)
        surf.blit(s, (self.pos.x - self.radius - camera.x, self.pos.y - self.radius - camera.y))

class ParticleSystem:
    def __init__(self):
        self.particles: List[Particle] = []

    def emit(self, pos, count=10, spread=80, speed=150, life=0.6):
        for _ in range(count):
            ang = random.random() * 2 * math.pi
            r = random.random() * spread
            vel = vec(math.cos(ang) * r, math.sin(ang) * r) * (speed / 100)
            p = Particle(pos=pos, vel=vel, life=life, radius=random.randint(2, 6))
            self.particles.append(p)

    def update(self, dt):
        for p in self.particles:
            p.update(dt)
        # remove dead
        self.particles = [p for p in self.particles if p.life > 0]

    def draw(self, surf, camera):
        for p in self.particles:
            p.draw(surf, camera)
