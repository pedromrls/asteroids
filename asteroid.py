from circleshape import CircleShape
from constants import *
import pygame  # type: ignore
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_1.velocity = self.velocity.rotate(random_angle) * 1.2
        asteroid_2.velocity = self.velocity.rotate(-random_angle) * 1.2

    def get_points(self):
        if self.radius == ASTEROID_MAX_RADIUS:  # large asteroid
            return MAX_RAD_AST_PTS
        elif self.radius == ASTEROID_MAX_RADIUS - ASTEROID_MIN_RADIUS:  # medium asteroid
            return MID_RAD_AST_PTS
        else:  # small asteroid
            return MIN_RAD_AST_PTS
