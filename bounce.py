#!/usr/bin/python
import pygame
from pygame.locals import *
import sys

pygame.init()

# main window
screen = pygame.display.set_mode((320, 240))

# add a sprite
sprite = pygame.image.load('images/sprite.png').convert_alpha()
sprite_rect = sprite.get_rect()
speed = [2, 2]

# create a clock
clock = pygame.time.Clock()

while 1:
    # fix the fps
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # move the ball
    sprite_rect = sprite_rect.move(speed) 

    # check for boundaries
    if sprite_rect.left < 0 or sprite_rect.right > 320:
        speed[0] = -speed[0]
    if sprite_rect.top < 0 or sprite_rect.bottom > 240:
        speed[1] = -speed[1]

    # refresh screen
    screen.fill((0, 0, 0))
    screen.blit(sprite, sprite_rect)
    pygame.display.flip()
