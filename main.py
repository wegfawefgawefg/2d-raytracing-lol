#use pygame to make a basic grid of colored squares



import math
import pygame
from pygame.locals import *

from vec3 import Vec3
from vec2 import Vec2

FAC = 9
WIDTH = 2**FAC
NUM_DIVS = 32

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, WIDTH))
    pygame.display.set_caption('Grid')
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if (
                event.type != QUIT
                and event.type == KEYDOWN
                and event.key in [K_ESCAPE, K_q]
                or event.type == QUIT
            ):
                running = False

        screen.fill((0, 0, 0))

        light = Vec3(255, 255, 255)
        brightness = 255.0
        mouse = Vec2(*pygame.mouse.get_pos())

        time = pygame.time.get_ticks() / 1000.0

        square_dims = Vec2(WIDTH / NUM_DIVS, WIDTH / NUM_DIVS)
        half_square_dims = square_dims / 2.0
        start = Vec2(0, 0)
        for y in range(NUM_DIVS):
            for x in range(NUM_DIVS):
                center = start + half_square_dims

                dist_to_light = (mouse - center).mag() + 0.00001
                col = brightness * light / dist_to_light**2
                col = col.clamp(0, 255)
                rect = pygame.Rect(start.x, start.y, square_dims.x, square_dims.y)
                pygame.draw.rect(screen, col.as_int_tuple(), rect)

                start.x += square_dims.x
            start.x = 0
            start.y += square_dims.y

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()