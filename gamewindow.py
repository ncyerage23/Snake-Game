'''
Snake Game by: Nathaniel Yerage
File for gamewindow operations
'''

from setup import *
import snakes


class GameWindow(pygame.Surface):
    def __init__(self):
        super().__init__((GW_WIDTH, GW_HEIGHT))
        self.fill(GW_COLOR)

        self.p1 = snakes.Snake((0,1), K_RIGHT, P1_COLOR)
        self.p2 = snakes.Snake((GW_GRID_X - 1, GW_GRID_Y - 2), K_LEFT, P2_COLOR)

        self.fruits = {}
        self.bushes = []
    
        self.draw_lines()
    
    def draw_lines(self):
        x = GW_GRID_STEP
        while x < GW_WIDTH:
            pygame.draw.line(self, BLACK, (x, 0), (x, GW_HEIGHT), 1)
            x += GW_GRID_STEP
        
        y = GW_GRID_STEP
        while y < GW_HEIGHT:
            pygame.draw.line(self, BLACK, (0, y), (GW_WIDTH, y), 1)
            y += GW_GRID_STEP
    
    def update_gw(self):
        self.p1.update_segs()
        self.p2.update_segs()

        self.draw_gw()

    def draw_gw(self):
        self.fill(GW_COLOR)
        self.draw_lines()

        self.p1.draw(self)
        self.p2.draw(self)

        

