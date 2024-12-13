'''
Snake Game by: Nathaniel Yerage
File for scoreboard operations
'''

from setup import *

class Scoreboard(pygame.Surface):
    def __init__(self):
        super().__init__( (SB_WIDTH, SB_HEIGHT) )
        self.fill((SB_COLOR))