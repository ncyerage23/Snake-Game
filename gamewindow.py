'''
Snake Game by: Nathaniel Yerage
File for gamewindow operations
'''

from setup import *
import snakes


class GameWindow(pygame.Surface):
    def __init__(self, gameOver):
        super().__init__((GW_WIDTH, GW_HEIGHT))
        self.fill(GW_COLOR)

        self.p1 = snakes.Snake2((0,1), P1_COLOR, K_RIGHT)
        self.p2 = snakes.Snake2((GW_GRID_X - 1, GW_GRID_Y - 2), P2_COLOR, K_LEFT)

        self.gameOver = gameOver

        self.fruits = {}
        self.bushes = []
    
        #self.draw_lines()
    
    def draw_lines(self):
        x = GW_GRID_STEP
        while x < GW_WIDTH:
            pygame.draw.line(self, BLACK, (x, 0), (x, GW_HEIGHT), 1)
            x += GW_GRID_STEP
        
        y = GW_GRID_STEP
        while y < GW_HEIGHT:
            pygame.draw.line(self, BLACK, (0, y), (GW_WIDTH, y), 1)
            y += GW_GRID_STEP
    
    def update_gw(self, p1key, p2key):
        self.p1.update_snake(p1key)
        self.p2.update_snake(p2key)

        #fix this so other states are included
        #and for fruit placement, etc.
        test = [item for item in self.p1.body if item in self.p2.body]
        if test:
            self.gameOver()

        if not (self.p1.bounds() and self.p2.bounds()):
            self.gameOver()

        self.draw_gw()

    def draw_gw(self):
        self.fill(GW_COLOR)

        self.p1.draw(self)
        self.p2.draw(self)

        

