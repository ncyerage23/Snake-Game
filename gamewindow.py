'''
Snake Game by: Nathaniel Yerage
File for gamewindow operations
'''

from setup import *


class GameWindow(pygame.Surface):
    def __init__(self):
        super().__init__((GW_WIDTH, GW_HEIGHT))
        self.fill(GW_COLOR)