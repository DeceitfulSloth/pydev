# Colour Squares

import pygame, sys
from pygame.locals import *

# Initialize pygame
pygame.init()

#Create game window
windowSurface = pygame.display.set_mode((600,600), 0, 32)
pygame.display.set_caption('Hello world!')



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

# Set parameters
offset = (100,100)
size = (400, 400)
totalSections = (7,7)

for x in range(offset[0],offset[0]+size[0]):
    for y in range(offset[1],offset[1]+size[1]):

        xnormVal = x - offset[0]
        xpreScaled = xnormVal / size[0]
        xscaled = xpreScaled * totalSections[0]
        xdiscretized = int(xscaled)
        xexpanded = int((xdiscretized * 255) / totalSections[0])
        
        ynormVal = y - offset[1]
        ypreScaled = ynormVal / size[1]
        yscaled = ypreScaled * totalSections[1]
        ydiscretized = int(yscaled)
        yexpanded = int((ydiscretized * 255) / totalSections[1])
        
        
        pixArray[x][y] = (0, yexpanded, xexpanded)

del pixArray

# Draw the window onto the screen.
pygame.display.update()

# Run the game loop.
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
