# Colour Squares

import pygame, sys, random
from pygame.locals import *

# Initialize pygame
pygame.init()

#Create game window
WIDTH = 1800
HEIGHT = 900

windowSurface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('Colour squares')

gravity = False
liquid = False

# Set up fonts
basicFont = pygame.font.SysFont(None, 48)

# Fill background
BACKGROUND = (200,200,200)
windowSurface.fill(BACKGROUND)

PIXEL_SIZE = 10

# Set parameters
offset = (PIXEL_SIZE,PIXEL_SIZE)
size = (WIDTH - PIXEL_SIZE * 2, HEIGHT - PIXEL_SIZE * 2)

totalSections = (int(size[0]/PIXEL_SIZE), int(size[1]/PIXEL_SIZE))

def getGrid():
    random.seed("debug")
    
    grid = []
    for x in range(totalSections[0]):
        col = []
        b = random.randint(64, 180)
        for y in range(totalSections[1]):
            if (random.randrange(10) <= 1):
                col.append((int((x * 255)/totalSections[0]), random.randint(1, 255), b))
            else:
                col.append((255, 255, 255))
        grid.append(col)
    return grid


grid = getGrid()


def getSquarePosFromPixelPos(pos):
    x = (pos[0] - PIXEL_SIZE) / offset[0]
    y = (pos[1] - PIXEL_SIZE) / offset[1]
    return (int(x),int(y))
         

def renderGrid(surface):
    for x in range(totalSections[0]):
        for y in range(totalSections[1]):
            pygame.draw.rect(surface, grid[x][y], (x*PIXEL_SIZE + offset[0] + 1, y*PIXEL_SIZE + offset[1] + 1, PIXEL_SIZE - 2, PIXEL_SIZE - 2))
            #pygame.draw.circle(surface, grid[x][y], (x*PIXEL_SIZE + offset[0] + int(PIXEL_SIZE / 2), y*PIXEL_SIZE + offset[1] + int(PIXEL_SIZE / 2)), int(PIXEL_SIZE / 2))
    return surface


def swapPositions(x1, y1, x2, y2):
    temp = grid[x1][y1]
    grid[x1][y1] = grid[x2][y2]
    grid[x2][y2] = temp

def applyHole():
    for x in range(totalSections[0]):
        grid[x][totalSections[1]-1] == (255,255,255)

def applyGravity():
    sideY = 1
    if liquid:
        sideY = 0
    
    for x in range(totalSections[0]):
        # check from bottom, but not the bottom row (thus -2)
        for y in range(totalSections[1] - 2, -1, -1):
            if grid[x][y] != (255, 255, 255):

                # Normal falling
                if grid[x][y+1] == (255, 255, 255):
                    grid[x][y+1] = grid[x][y]
                    grid[x][y] = (255, 255, 255)
                else:
                    # sideways
                    canFallLeft = False
                    canFallRight = False
                    if x >= 1:
                        canFallLeft = grid[x-1][y+sideY] == (255, 255, 255)
                    if x <= totalSections[0] - 2:
                        canFallRight = grid[x+1][y+sideY] == (255, 255, 255)

                    if canFallLeft and canFallRight:
                        if random.randint(0,1) == 0:
                            swapPositions(x, y, x+1, y+sideY)
                        else:
                            swapPositions(x, y, x-1, y+sideY)
                    elif canFallLeft:
                        swapPositions(x, y, x-1, y+sideY)
                    elif canFallRight:
                        swapPositions(x, y, x+1, y+sideY)
        
    return grid


windowSurface = renderGrid(windowSurface)


# Draw the window onto the screen.
pygame.display.update()

# Run the game loop.
time_elapsed_since_last_action = 0
clock = pygame.time.Clock()

while True:
    dt = clock.tick() 
    time_elapsed_since_last_action += dt
    
    for event in pygame.event.get():
        gridUpdated = False
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePosition = pygame.mouse.get_pos()
            gridPosition = getSquarePosFromPixelPos(mousePosition)
            r = random.randrange(1,256)
            g = random.randrange(1, 256)
            b = random.randrange(1, 256)
            for x in range(-3,4):
                for y in range(-3, 4):
                    if (gridPosition[0] + x >= 0 and gridPosition[0] + x < totalSections[0] and gridPosition[1] + y >= 0 and gridPosition[1] + y < totalSections[1]):
                        grid[gridPosition[0] + x][gridPosition[1] + y] = (r, g, b)
                        gridUpdated = True
            
        if event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                gravity = not gravity

            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                pygame.quit()
                sys.exit()

            if pygame.key.get_pressed()[pygame.K_r]:
                grid = getGrid()
                gridUpdated = True

            if pygame.key.get_pressed()[pygame.K_l]:
                liquid = not liquid

    if gravity and time_elapsed_since_last_action > 50:
        grid = applyGravity()
        applyHole()
        time_elapsed_since_last_action = 0
        gridUpdated = True

    

    if gridUpdated:
        windowSurface = renderGrid(windowSurface)
        pygame.display.update()
            
        
        

    
