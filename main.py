import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pyclock = pygame.time.Clock()
    dt = 0

    # Game Loop
    while True:
        log_state()

        for event in pygame.event.get():
            # processing pygame event queue
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = pyclock.tick(60) / 1000


if __name__ == "__main__":
    main()
