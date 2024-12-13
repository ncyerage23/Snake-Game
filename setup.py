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
    K_p
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
GW_HEIGHT = 650

WIN_OFFSET = 25

SB_WIDTH = 1200
GW_WIDTH = SB_WIDTH

WIN_HEIGHT = SB_HEIGHT + GW_HEIGHT + WIN_OFFSET
WIN_WIDTH = GW_WIDTH + 2 * (WIN_OFFSET)

WIN_COLOR = (125, 73, 21)

#Scoreboard stuff
SB_COLOR = WIN_COLOR
SB_TEXT_COLOR = (218, 242, 0)

#Gamewindow stuff
GW_COLOR = (4, 130, 8)


#Snake stuff
SNAKE1_COLOR = (67, 67, 168)
SNAKE2_COLOR = (255, 187, 0)
