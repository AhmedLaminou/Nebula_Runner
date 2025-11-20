import pygame
import random
from settings import TILE_SIZE, GRAVITY
from utils import vec, clamp
from particles import ParticleSystem

class Enemy
    def __init__(self, pos)
        self.pos = vec(pos)
        self.vel = vec(0, 0)
        self.width = 32
        self.height = 42
        self.color = (200, 40, 40)

        self.health = 40
        self.max_health = 40

        self.on_ground = False
        self.state = patrol  # patrol, chase
        self.direction = random.choice([-1, 1])
        self.speed = 90

        self.particles = ParticleSystem()

    def rect(self)
        return pygame.Rect(
            int(self.pos.x), int(self.pos.y),
            self.width, self.height
        )

    def update(self, dt, player, level)
        # Simple state-switching AI
        distance_to_player = (player.pos - self.pos).length()

        if distance_to_player  300
            self.state = chase
        elif distance_to_player  400
            self.state = patrol

        if self.state == patrol
            self.vel.x = self.direction  self.speed
            # Randomly flip direction
            if random.random()  0.005
                self.direction = -1

        elif self.state == chase
            if player.pos.x  self.pos.x
                self.vel.x = -self.speed  1.4
            else
                self.vel.x = self.speed  1.4

        # Apply gravity
        self.vel.y += GRAVITY  dt
        if self.vel.y  900
            self.vel.y = 900

        # Apply velocity
        self.pos += self.vel  dt

        # Tile collision
        self.handle_collisions(level)

        # Damage FX
        self.particles.update(dt)

    def handle_collisions(self, level)
        rect = self.rect()
        # Horizontal collision
        rect.x = int(self.pos.x)
        hit = level.get_collisions(rect)
        for tile in hit
            if self.vel.x  0
                rect.right = tile.left
                self.pos.x = rect.x
                self.direction = -1
            elif self.vel.x  0
                rect.left = tile.right
                self.pos.x = rect.x
                self.direction = -1

        # Vertical collision
        rect.y = int(self.pos.y)
        hit = level.get_collisions(rect)
        self.on_ground = False
        for tile in hit
            if self.vel.y  0
                rect.bottom = tile.top
                self.pos.y = rect.y
                self.vel.y = 0
                self.on_ground = True
            elif self.vel.y  0
                rect.top = tile.bottom
                self.pos.y = rect.y
                self.vel.y = 0

    def draw(self, surf, camera)
        pygame.draw.rect(
            surf,
            self.color,
            (self.pos.x - camera.x, self.pos.y - camera.y, self.width, self.height)
        )

        # Simple health bar
        ratio = self.health  self.max_health
        pygame.draw.rect(
            surf,
            (50, 0, 0),
            (self.pos.x - camera.x, self.pos.y - 10 - camera.y, self.width, 6)
        )
        pygame.draw.rect(
            surf,
            (200, 0, 0),
            (self.pos.x - camera.x, self.pos.y - 10 - camera.y, self.width  ratio, 6)
        )

        self.particles.draw(surf, camera)

    def hit(self, amount=10)
        self.health -= amount
        if self.health = 0
            self.health = 0
        self.particles.emit(self.pos, count=16, spread=80, speed=200, life=0.7)
