#!/usr/bin/env python
import pygame
from pygame.locals import *
import sys

pygame.init()

# main window
window = pygame.display.set_mode((640, 480), RESIZABLE)

# add background
background = pygame.image.load('images/background.jpg').convert()

# add a sprite
sprite = pygame.image.load('images/sprite.png').convert_alpha()
sprite.set_colorkey((255, 255, 255))
pos = sprite.get_rect()

# set keypress repeat
pygame.key.set_repeat(400, 30)

# main loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_UP:
                pos = pos.move(0, -3)
            elif event.key == K_DOWN:
                pos = pos.move(0, 3)
            elif event.key == K_LEFT:
                pos = pos.move(-3, 0)
            elif event.key == K_RIGHT:
                pos = pos.move(3, 0)

    # show sprite & refresh 
    window.blit(background, (0, 0))
    window.blit(sprite, pos)
    pygame.display.flip()
