'''
Snake Game by: Nathaniel Yerage
File for global vars and setup
to be used across all files
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
    K_p,
    K_SPACE,
    K_w,
    K_a,
    K_s,
    K_d
)

import random

pygame.display.init()
pygame.font.init()

#Constants

#Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#Overall stuff
FPS = 60

SB_HEIGHT = 50
GW_HEIGHT = 640

WIN_OFFSET = 25

SB_WIDTH = 1120
GW_WIDTH = SB_WIDTH

WIN_HEIGHT = SB_HEIGHT + GW_HEIGHT + WIN_OFFSET
WIN_WIDTH = GW_WIDTH + 2 * (WIN_OFFSET)

WIN_COLOR = (125, 73, 21)
TEXT_COLOR = (218, 242, 0)

#Scoreboard stuff
SB_COLOR = WIN_COLOR

#Gamewindow stuff
GW_COLOR = (4, 130, 8)

    #i think this is better, maybe (lol)
    #i could def come up with a better way though, that's way later
GW_GRID_X = 28
GW_GRID_Y = 16

GW_GRID_STEP = GW_HEIGHT / GW_GRID_Y
GW_GRID_MID = GW_GRID_STEP / 2

#Popup Window stuff
POP_COLOR = WIN_COLOR

#Snake stuff
P1_COLOR = (67, 67, 168)
P2_COLOR = (255, 187, 0)

SNAKE_START_SPEED = 1
SNAKE_RAD = GW_GRID_MID - 5

DIRECTIONS = {
    K_RIGHT: (1, 0),
    K_LEFT: (-1, 0),
    K_DOWN: (0, 1),
    K_UP: (0, -1),
    K_d: (1, 0),
    K_a: (-1, 0),
    K_s: (0, 1), 
    K_w: (0, -1)
}

LEGAL_MOVES_P1 = {
    K_d: (K_s, K_w),
    K_a: (K_s, K_w),
    K_s: (K_d, K_a),
    K_w: (K_d, K_a)
}

LEGAL_MOVES_P2 = {
    K_RIGHT: (K_DOWN, K_UP),
    K_LEFT: (K_UP, K_DOWN),
    K_DOWN: (K_RIGHT, K_LEFT),
    K_UP: (K_RIGHT, K_LEFT)
}

#Fruit stuff

#Obstacle stuff
ROCK_COUNT = 10

#grid stuff (grid to literal coords, literal to grid coords) (like old methods)
def toCoord(coord):
    out = []
    for c in coord:
        out.append(GW_GRID_STEP * c + GW_GRID_MID)
    return out

def fromCoord(coord):
    out = []
    for c in coord:
        out.append((c - GW_GRID_MID) / GW_GRID_STEP)
    return out