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

        self.obstacles = {'ROCKS': []}
        self.set_obstacles()
    
    @property
    def p1_len(self):
        return self.p1.length

    @property
    def p2_len(self):
        return self.p2.length

    #this is good for now, but I need to fix it down the line
    #random is potentially bad, tbh. 
    #maybe have set places or something, idk. 
    def set_obstacles(self):
        used_coords = []

        count = 0
        while count < ROCK_COUNT:
            x, y = random.randint(0, GW_GRID_X), random.randint(0, GW_GRID_Y)
            if (x, y) not in used_coords or (x in range(0, 2) and y in range(0, 2)) or (x in range(GW_GRID_X - 2, GW_GRID_X) and y in range(GW_GRID_Y - 2, GW_GRID_Y)) or x < 2 or x > GW_GRID_X - 2 or y < 2 or y > GW_GRID_Y - 2:
                self.obstacles['ROCKS'].append(ob.Rock((x, y)))
                count += 1
                
            
    
    def update_gw(self, p1key, p2key):
        self.p1.update_snake(p1key)
        self.p2.update_snake(p2key)

        a, b = self.p1.getInfo(), self.p2.getInfo()
        c = False

        p1_curr = self.p1.head
        while p1_curr:
            p2_curr = self.p2.head
            while p2_curr:
                if p1_curr.rect.colliderect(p2_curr.rect):
                    c = True
                p2_curr = p2_curr.next
            p1_curr = p1_curr.next
        
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

        for rock in self.obstacles['ROCKS']:
            self.blit(rock.surf, rock.rect)

        screen.blit(self, (WIN_OFFSET, SB_HEIGHT))

        

