'''
Snake Game by: Nathaniel Yerage
File for gamewindow operations
'''

from setup import *
import snakes
import obstacles as ob


class GameWindow(pygame.Surface):
    def __init__(self):
        super().__init__((GW_WIDTH, GW_HEIGHT))
        self.fill(GW_COLOR)

        self.p1 = snakes.Snake((0,1), K_d, P1_COLOR)
        self.p2 = snakes.Snake((GW_GRID_X - 1, GW_GRID_Y - 2), K_LEFT, P2_COLOR)

        self.obstacles = []
        self.set_obstacles()
    
    @property
    def p1_len(self):
        return self.p1.length

    @property
    def p2_len(self):
        return self.p2.length

    def set_obstacles(self):
        self.obstacles.append(ob.Wall((2,3), (8,3)))
        self.obstacles.append(ob.Wall((4,3), (4,6)))

        self.obstacles.append(ob.Wall((17,-1), (17,9)))
        self.obstacles.append(ob.Wall((16,6), (19,6)))
        self.obstacles.append(ob.Wall((14,3), (20,3)))

        self.obstacles.append(ob.Wall((2,10), (2,16)))

        self.obstacles.append(ob.Wall((8,12), (14,12)))
        self.obstacles.append(ob.Wall((8,13), (14,13)))
        self.obstacles.append(ob.Wall((8,12), (8,13)))
        self.obstacles.append(ob.Wall((14,12), (14,13)))
                
            
    
    def update_gw(self, p1key, p2key):
        self.p1.update_snake(p1key)
        self.p2.update_snake(p2key)

        a, b = self.p1.getInfo(), self.p2.getInfo()
        c = False

        #checking for collisions between snakes
        p1_curr = self.p1.head
        while p1_curr:
            p2_curr = self.p2.head
            while p2_curr:
                if p1_curr.rect.colliderect(p2_curr.rect):
                    c = True
                p2_curr = p2_curr.next
            p1_curr = p1_curr.next
        
        #bush/wall collision
        for obs in self.obstacles:
            if self.p1.head.rect.colliderect(obs.rect):
                c = True
            
            if self.p2.head.rect.colliderect(obs.rect):
                c = True


        return a, b, c

    def draw_lines(self):
        x = GW_GRID_STEP
        while x < GW_WIDTH:
            pygame.draw.line(self, BLACK, (x, 0), (x, GW_HEIGHT), 1)
            x += GW_GRID_STEP
        
        y = GW_GRID_STEP
        while y < GW_HEIGHT:
            pygame.draw.line(self, BLACK, (0, y), (GW_WIDTH, y), 1)
            y += GW_GRID_STEP

    def draw_gw(self, screen):
        self.fill(GW_COLOR)

        self.p1.draw(self)
        self.p2.draw(self)

        for obs in self.obstacles:
            obs.draw(self)

        screen.blit(self, (WIN_OFFSET, SB_HEIGHT))

        

