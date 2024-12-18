#!/usr/bin/env python3

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import pygame  # type: ignore
import sys


def main():
    pygame.init()
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group() 
    shots = pygame.sprite.Group()

    # Player grouping
    Player.containers = (updatable, drawable)
    player = Player(x, y)

    # asteroids group
    Asteroid.containers = (asteroids, updatable, drawable)

    # Asteroid field
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    # shot 
    Shot.containers = (shots, drawable, updatable)

    # screen filling
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        dt = clock.tick(60) / 1000
        # player drawing
        for sprite in updatable:
            sprite.update(dt)
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                sys.exit()
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
