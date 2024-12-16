'''
Snake Game by: Nathaniel Yerage
File for snakes & stuff
'''

from setup import *


'''
I'm going to come back to snakes. Idk. It's such a pain in the ass.
I think I'll keep the way I've been doing it (sorta), where I just move
each segment to the place where the previous one was, then move that one

But, I'm gonna bring back the segment class with all the collidereact stuff, I think.
Idk, later. I'm done w this, lol. 
'''



class Snake2:
    def __init__(self, coords, color, start_dir):
        self.body = [toCoord(coords)]
        self.color = color
        self.speed = 2
        self.direction = start_dir
        self.length = 100
        self.head = self.body[0]
    
    def update_snake(self, dir=None):
        if dir:
            self.direction = dir
        
        head_coord = self.body[0]
        x, y = DIRECTIONS[self.direction]
        newX, newY = head_coord[0] + x*self.speed, head_coord[1] + y*self.speed
        self.body.insert(0, (newX, newY))

        if len(self.body) > self.length:
            self.body = self.body[:self.length]
        
        self.head = self.body[0]
        
    def draw(self, screen):
        for seg in self.body:
            pygame.draw.circle(screen, self.color, seg, SNAKE_RAD)
    
    def bounds(self):
        if self.head[0] < 0 or self.head[0] > GW_WIDTH or self.head[1] < 0 or self.head[1] > GW_HEIGHT:
            return False
        else:
            return True
        





class Segment(pygame.sprite.Sprite):
    def __init__(self, coords, color):
        super(Segment, self).__init__()
        self.surf = pygame.Surface((GW_GRID_STEP, GW_GRID_STEP), pygame.SRCALPHA)
        self.rect = self.surf.get_rect()
        self.color = color
        self.rect.center = coords

        width, height = self.rect.width, self.rect.height
        pygame.draw.circle(self.surf, color, (width / 2, height / 2), SNAKE_RAD)
    
    def move(self, dir, speed):
        x, y = DIRECTIONS[dir]
        self.rect.move_ip(speed * x, speed * y)


class Snake:
    def __init__(self, coords, direction, color):
        self.color = color
        self.direction = direction
        self.moves = []
        self.coords = toCoord(coords)
        self.segments = [Segment(self.coords, color)]

        self.speed = SNAKE_START_SPEED

        self.fruits = 0
    
    def update_segs(self):
        for seg in self.segments:
            seg.move(self.direction, self.speed)


    def draw(self, screen):
        #draw from back to front
        for seg in self.segments:
            screen.blit(seg.surf, seg.rect)