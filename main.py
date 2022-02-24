#use pygame to make a basic grid of colored squares



import math
import pygame
from pygame.locals import *

from vec3 import Vec3
from vec2 import Vec2

FAC = 9
WIDTH = 2**FAC
NUM_DIVS = 32

class Light:
    def __init__(self) -> None:
        self.pos = Vec2(0, 0)
        self.color = Vec3(255, 255, 255)
        self.brightness = 20.0

    def light(self, pos):
        dist_to_light = (self.pos - pos).mag() + 0.00001
        return self.color * self.brightness / dist_to_light**2

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, WIDTH))
    pygame.display.set_caption('Grid')
    clock = pygame.time.Clock()


    cam = Vec2(WIDTH / 2, WIDTH / 2)
    cam_speed = 10.0

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
        # move camera with wasd continuously
        # cam += Vec2(0, -1) * cam_speed
        keys = pygame.key.get_pressed()
        if keys[K_w]:
            cam += Vec2(0, -1) * cam_speed
        if keys[K_s]:
            cam += Vec2(0, 1) * cam_speed
        if keys[K_a]:
            cam += Vec2(-1, 0) * cam_speed
        if keys[K_d]:
            cam += Vec2(1, 0) * cam_speed

        screen.fill((0, 0, 0))

        mouse = Vec2(*pygame.mouse.get_pos())

        light = Light()
        light.color = Vec3(255, 255, 255)
        light.pos = mouse
        light.brightness = 255

        time = pygame.time.get_ticks() / 1000.0

        cam_dir = (mouse - cam).norm()
        cam_end = cam + cam_dir * 64.0
        # get line going right from cam end perpendicular to cam dir
        cam_left = cam_dir.rotate(-math.pi / 2).norm()
        cam_left_end = cam_end + cam_left * 64.0

        cam_right = cam_dir.rotate(math.pi / 2).norm()
        cam_right_end = cam_end + cam_right * 64.0

        square_dims = Vec2(WIDTH / NUM_DIVS, WIDTH / NUM_DIVS)
        half_square_dims = square_dims / 2.0
        start = Vec2(0, 0)
        for _ in range(NUM_DIVS):
            for _ in range(NUM_DIVS):
                center = start + half_square_dims

                col = light.light(center)
                col = col.clamp(0, 255)
                rect = pygame.Rect(start.x, start.y, square_dims.x, square_dims.y)
                pygame.draw.rect(screen, col.as_int_tuple(), rect)

                start.x += square_dims.x
            start.x = 0
            start.y += square_dims.y

        # draw cam
        pygame.draw.circle(screen, (255, 255, 255), cam.as_int_tuple(), 5)
        pygame.draw.line(screen,(255, 255, 255),cam.as_int_tuple(),cam_end.as_int_tuple(),3,)
        pygame.draw.line(screen,(255, 255, 255),cam_end.as_int_tuple(),cam_left_end.as_int_tuple(),3,)
        pygame.draw.line(screen,(255, 255, 255),cam_end.as_int_tuple(),cam_right_end.as_int_tuple(),3,)

        pygame.display.flip()
        clock.tick(60)

        pygame.display.flip()
        clock.tick(60)


        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()