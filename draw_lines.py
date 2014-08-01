#!/usr/bin/env python

import pygame
from pygame.locals import *
import sys

# init pygame
pygame.init()
window = pygame.display.set_mode((640, 480))

# color constant
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# main loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        window.fill((0, 0, 0))
            
        # top-right-side laser spot
        for i in xrange(24):
            pygame.draw.line(window, RED, (0, 20 * i), (640, 0))

        # top-left-side laser spot
        for i in xrange(24):
            pygame.draw.line(window, BLUE, (0, 0), (640, 20 * i))
            
        # bottom-right-side laser spot
        for i in xrange(24):
            pygame.draw.line(window, RED, (0, 20 * i), (640, 480))

        # bottom-right-side laser spot
        for i in xrange(24):
            pygame.draw.line(window, BLUE, (0, 480), (640, 20 * i))
            
        pygame.display.flip()
