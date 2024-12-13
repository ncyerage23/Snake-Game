'''
Snake Game by: Nathaniel Yerage
File for snakes & stuff
'''

from setup import *


#this time, imma make the segments as circles
#they're still gonna operate on the grid, but you know.
#also speed increases here, not with fps lol

#instead of how I did it before, make it like this:
#have snake hold a list of segments and a separate list of functions
#every update adds a new thing to the list of functions, and removes the back of it
#then we go down the line of segments and call the function on that segment
#this is definitely way better, lol
#be sure to draw from back to front
#only allowed to change direction on a grid spot

#i could draw circles over and over from back to front???
#idk though.


'''
instead of doing segments, I could mark the head and tail and any turns?
idk if that would even work though. 

yeah, before moving forward, I need to decide how this'll be done. 
maybe mark each head, tail, and turn, and then draw circles to connect? 
but how would I detect collision? 
'''


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
        print(dir == K_LEFT)
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