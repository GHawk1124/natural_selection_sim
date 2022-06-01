import pygame
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 60

WIDTH = 800
HEIGHT = 600


def main():
    running = True
    pygame.init()

    # create window and set caption
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Natural Selection App")

    # create a clock
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
