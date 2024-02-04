# Convex Hull

import pygame, sys
from pygame.locals import *

# Initialize pygame
pygame.init()

#Create game window
WIDTH = 1800
HEIGHT = 900

windowSurface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('Colour squares')


# Set up colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set up fonts
basicFont = pygame.font.SysFont(None, 48)

# Fill background
windowSurface.fill(WHITE)

# Get a pixel array of the surface.
pixArray = pygame.PixelArray(windowSurface)






# Draw the window onto the screen.
pygame.display.update()

# Run the game loop.
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    
