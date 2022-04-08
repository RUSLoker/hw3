import pygame
from pygame.draw import *
from random import randrange
from math import sin

pygame.init()

FPS = 60
screen = pygame.display.set_mode((400, 400))


clock = pygame.time.Clock()
finished = False
t = 0

while not finished:
    t += clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

    screen.fill((255, 255, 255))
    circle(screen, (255, 255, 0), (200, 175), 100)
    circle(screen, (0, 0, 0), (200, 175), 100, 1)

    circle(screen, (255, 0, 0), (160, 150), 20)
    circle(screen, (0, 0, 0), (160, 150), 20, 1)
    circle(screen, (0, 0, 0),
           (160 + randrange(-2, 2), 150 + randrange(-2, 2)),
           8)

    circle(screen, (255, 0, 0), (240, 150), 15)
    circle(screen, (0, 0, 0), (240, 150), 15, 1)
    circle(screen, (0, 0, 0),
           (240 + randrange(-2, 2), 150 + randrange(-2, 2)),
           8)

    rect(screen, (0, 0, 0), (150, 220, 100, 20 + 10 * sin(t * 0.03)))

    polygon(screen, (0, 0, 0),
            ((105, 101),
             (110, 93),
             (194, 137),
             (190, 143)))

    line(screen, (0, 0, 0), (218, 133), (300, 118), 9)

    pygame.display.update()

pygame.quit()
 
