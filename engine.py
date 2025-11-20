import pygame
from settings import WIDTH, HEIGHT, FPS
from utils import draw_text
from player import Player
from enemy import Enemy
from level import Level
from items import Item
from particles import ParticleSystem
import random

class GameEngine:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Nebula Runner")
        self.clock = pygame.time.Clock()
        self.running = True

        self.state = "menu"   # menu, game, pause

        # Camera
        self.camera = pygame.math.Vector2(0, 0)

        # Game objects
        self.level = None
        self.player = None
        self.enemies = []
        self.items = []
        self.fx = ParticleSystem()

    def start_game(self):
        self.level = Level()
        self.player = Player((100, 200))
        self.enemies = [Enemy((random.randint(400, 2000), 200))
                        for _ in range(10)]
        self.items = [Item((random.randint(300, 2000), 100)) for _ in range(8)]
        self.state = "game"

    def update(self, dt):
        if self.state == "menu":
            return

        keys = pygame.key.get_pressed()
        self.player.update(dt, keys, self.level, self.enemies)

        for e in self.enemies:
            e.update(dt, self.player, self.level)

        for it in self.items:
            it.update(dt)
            if it.collides_with_point(self.player.pos):
                if it.kind == "energy":
                    self.player.health = min(self.player.max_health, self.player.health + it.value)
                self.items.remove(it)
                break

        # Remove dead enemies
        self.enemies = [e for e in self.enemies if e.health > 0]

        # Camera follows player
        self.camera.x = self.player.pos.x - (WIDTH // 2)
        self.camera.y = self.player.pos.y - (HEIGHT // 2)

        self.fx.update(dt)

    def draw(self):
        self.screen.fill((20, 20, 30))

        if self.state == "menu":
            draw_text(self.screen, "NEBULA RUNNER", 68, WIDTH // 2, HEIGHT // 2 - 80, center=True)
            draw_text(self.screen, "Press ENTER to Start", 40, WIDTH // 2, HEIGHT // 2, center=True)
            return

        # Level
        self.level.draw(self.screen, self.camera)

        # Items
        for it in self.items:
            it.draw(self.screen, self.camera)

        # Enemies
        for e in self.enemies:
            e.draw(self.screen, self.camera)

        # Player
        self.player.draw(self.screen, self.camera)

        # FX
        self.fx.draw(self.screen, self.camera)

    def run(self):
        while self.running:
            dt = self.clock.tick(FPS) / 1000.0

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.running = False
                if e.type == pygame.KEYDOWN:
                    if self.state == "menu" and e.key == pygame.K_RETURN:
                        self.start_game()

            self.update(dt)
            self.draw()

            pygame.display.flip()

        pygame.quit()
