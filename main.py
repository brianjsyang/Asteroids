import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pyclock = pygame.time.Clock()

    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)  # type: ignore Verified working
    Asteroid.containers = (asteroids, updatable, drawable)  # type: ignore Verified working
    AsteroidField.containers = updatable  # type: ignore Verified working

    # Player
    Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    AsteroidField()

    dt = 0

    # Game Loop
    while True:
        log_state()

        for event in pygame.event.get():
            # processing pygame event queue
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = pyclock.tick(60) / 1000


if __name__ == "__main__":
    main()
