#!/usr/bin/python
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
sprite_x = sprite_y = 0

# main loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                sprite_x = event.pos[0]
                sprite_y = event.pos[1]

    # show sprite & refresh 
    window.blit(background, (0, 0))
    window.blit(sprite, (sprite_x, sprite_y))
    pygame.display.flip()
