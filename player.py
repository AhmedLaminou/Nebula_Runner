import pygame
from settings import PLAYER_SPEED, PLAYER_RADIUS, PLAYER_JUMP_IMPULSE, PLAYER_MAX_HEALTH, GRAVITY
from utils import vec
from particles import ParticleSystem

class Player:
    def __init__(self, pos):
        self.pos = vec(pos)
        self.vel = vec(0, 0)
        self.radius = PLAYER_RADIUS
        self.color = (80, 200, 255)
        self.on_ground = False
        self.health = PLAYER_MAX_HEALTH
        self.max_health = PLAYER_MAX_HEALTH
        self.attack_cooldown = 0.0
        self.particles = ParticleSystem()

    def rect(self):
        return pygame.Rect(
            int(self.pos.x - self.radius),
            int(self.pos.y - self.radius),
            self.radius * 2,
            self.radius * 2
        )

    def update(self, dt, keys, level, enemies):
        # Movement
        move = 0
        if keys[pygame.K_a]:
            move -= 1
        if keys[pygame.K_d]:
            move += 1

        self.vel.x = move * PLAYER_SPEED

        # Jump
        if keys[pygame.K_SPACE] and self.on_ground:
            self.vel.y = PLAYER_JUMP_IMPULSE
            self.on_ground = False

        # Gravity
        self.vel.y += GRAVITY * dt
        if self.vel.y > 1000:
            self.vel.y = 1000

        # Apply movement
        self.pos.x += self.vel.x * dt
        self.handle_horizontal(level)

        self.pos.y += self.vel.y * dt
        self.handle_vertical(level)

        # Attack cooldown
        if self.attack_cooldown > 0:
            self.attack_cooldown -= dt

        # Attack
        if keys[pygame.K_j] and self.attack_cooldown <= 0:
            self.attack(enemies)
            self.attack_cooldown = 0.35

        self.particles.update(dt)

    def handle_horizontal(self, level):
        rect = self.rect()
        rect.x = int(self.pos.x - self.radius)
        hits = level.get_collisions(rect)
        for h in hits:
            if self.vel.x > 0:
                rect.right = h.left
                self.pos.x = rect.x + self.radius
            elif self.vel.x < 0:
                rect.left = h.right
                self.pos.x = rect.x + self.radius

    def handle_vertical(self, level):
        rect = self.rect()
        rect.y = int(self.pos.y - self.radius)
        hits = level.get_collisions(rect)
        self.on_ground = False
        for h in hits:
            if self.vel.y > 0:
                rect.bottom = h.top
                self.pos.y = rect.y + self.radius
                self.vel.y = 0
                self.on_ground = True
            elif self.vel.y < 0:
                rect.top = h.bottom
                self.pos.y = rect.y + self.radius
                self.vel.y = 0

    def attack(self, enemies):
        for e in enemies:
            if (e.pos - self.pos).length() <= 60:
                e.hit(15)
                self.particles.emit(self.pos, count=8, spread=50, speed=160, life=0.4)

    def draw(self, surf, camera):
        pygame.draw.circle(
            surf, self.color,
            (int(self.pos.x - camera.x), int(self.pos.y - camera.y)),
            self.radius
        )
        # health bar
        ratio = self.health / self.max_health
        pygame.draw.rect(
            surf, (0, 0, 0),
            (self.pos.x - 25 - camera.x, self.pos.y - 40 - camera.y, 50, 6)
        )
        pygame.draw.rect(
            surf, (50, 200, 255),
            (self.pos.x - 25 - camera.x, self.pos.y - 40 - camera.y, 50 * ratio, 6)
        )
        self.particles.draw(surf, camera)
