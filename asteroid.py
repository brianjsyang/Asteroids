import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # spawn 2 smaller asteroids
        log_event("asteroid_split")
        angle = random.uniform(20, 50)

        new_vector_1 = self.velocity.rotate(angle)
        new_vector_2 = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        spawn_1 = Asteroid(self.position.x, self.position.y, new_radius)
        spawn_2 = Asteroid(self.position.x, self.position.y, new_radius)

        spawn_1.velocity = new_vector_1 * 1.2
        spawn_2.velocity = new_vector_2 * 1.2
