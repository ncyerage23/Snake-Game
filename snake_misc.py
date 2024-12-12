'''
Extra stuff for all the files to have, idk
constants and stuff
'''


import pygame
import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_p
)

import random


pygame.display.init()
pygame.font.init()

GW_SIZE = 500
GRID_SIZE = GW_SIZE / 10
GRID_MID = GRID_SIZE / 2
SB_HEIGHT = 50

SNAKE_COLOR = (0,255,0)
GW_COLOR = (79, 60, 34)
FOOD_COLOR = (255,0,0)
SB_COLOR = (116, 204, 116)

SB_COLOR = (49, 145, 49)
SB_TEXT_COLOR = (255, 255, 255)

SEGMENT_SIZE = GRID_SIZE
STEP_SIZE = 1

DIRECTIONS = {
    K_RIGHT: (STEP_SIZE, 0),
    K_LEFT: (-STEP_SIZE, 0),
    K_DOWN: (0, STEP_SIZE),
    K_UP: (0, -STEP_SIZE)
}

LEGAL_MOVES = {
    K_RIGHT: (K_DOWN, K_UP),
    K_LEFT: (K_UP, K_DOWN),
    K_DOWN: (K_RIGHT, K_LEFT),
    K_UP: (K_RIGHT, K_LEFT)
}


def coord(x, y):
    newX = GRID_SIZE * x + GRID_MID
    newY = GRID_SIZE * y + GRID_MID
    return newX, newY

def backCoord(x, y):
    newX = (x - GRID_MID) / GRID_SIZE
    newY = (y - GRID_MID) / GRID_SIZE
    return newX, newY