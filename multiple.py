#!/usr/bin/python
import pygame
from pygame.locals import *
import sys
from random import randrange

class GameObject:
    """
        Game object
    """
    def __init__(self, image, speed):
        self.speed = speed
        self.image = image
        self.pos = image.get_rect()

    def move(self):
        self.pos = self.pos.move(self.speed)

# init images
screen = pygame.display.set_mode((640, 480))
player = pygame.image.load('images/sprite.png').convert_alpha()
background = pygame.image.load('images/background.jpg').convert()
screen.blit(background, (0, 0))

# instantiate players, with random speed
objects = []
for x in xrange(10):
    o = GameObject(player, (randrange(10), randrange(10)))
    objects.append(o)

# game loop
while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            pygame.quit()
            sys.exit()

        # clear screen
        screen.blit(background, (0, 0))

        # move objects
        for o in objects:
            o.move()
            screen.blit(o.image, o.pos)

        # refresh screen
        pygame.display.update()
        pygame.time.delay(100)
