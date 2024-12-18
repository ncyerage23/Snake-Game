'''
Snake Game by: Nathaniel Yerage
File for snakes & stuff
'''

from setup import *


'''
Need them hitting themselves now, and that's basically it for the snakes I think. Good job.
Would it be simpler to just do it down the line rather than recursively? I'm not even sure.
We'll see, I guess. Later. Maybe it would be, idk. 
'''


class Segment(pygame.sprite.Sprite):
    def __init__(self, coords, color):
        super(Segment, self).__init__()
        self.surf = pygame.Surface((SNAKE_RAD * 2, SNAKE_RAD * 2), pygame.SRCALPHA)
        self.rect = self.surf.get_rect()
        self.color = color
        self.rect.center = coords

        width, height = self.rect.width, self.rect.height
        pygame.draw.circle(self.surf, color, (width / 2, height / 2), SNAKE_RAD)

        self.next = None

    def add_seg(self):
        if self.next:
            return self.next.add_seg()
        else:
            self.next = Segment((self.rect.centerx, self.rect.centery), self.color)
            return self.next

    def update_head(self, cx, cy, speed):
        oldX, oldY = self.rect.centerx, self.rect.centery
        self.rect.move_ip(cx * speed, cy * speed)
        
        if self.next:
            self.next.update_rest(oldX, oldY)

    def update_rest(self, newX, newY):
        oldX, oldY = self.rect.centerx, self.rect.centery
        self.rect.centerx, self.rect.centery = newX, newY

        if self.next:
            self.next.update_rest(oldX, oldY)

    def draw(self, screen):
        screen.blit(self.surf, self.rect)

        if self.next:
            self.next.draw(screen)


class Snake:
    def __init__(self, coords, direction, color):
        self.color = color
        self.direction = direction
        self.head = Segment(toCoord(coords), self.color)
        self.speed = SNAKE_START_SPEED * 2
        self.seg_count = 0
        self.body = [self.head]
        self.startPos = toCoord(coords)

        for i in range(100):
            self.add()
    
    #this is really cool, never done this
    @property
    def length(self):
        return self.seg_count // 10

    def add(self):
        self.seg_count += 1
        self.body.append(self.head.add_seg())
    
    def update_snake(self, dir):
        if dir:
            self.direction = dir
        
        cx, cy = DIRECTIONS[self.direction]
        self.head.update_head(cx, cy, self.speed)
    
    def draw(self, screen):
        self.head.draw(screen)
    
    def getInfo(self):
        lose = False
        if self.head.rect.left < 0 or self.head.rect.right > GW_WIDTH or self.head.rect.top < 0 or self.head.rect.bottom > GW_HEIGHT:
            lose = True

        #works, but a little weird. Best I got tho. 
        current = self.head.next
        while current:
            if current.rect.center == self.head.rect.center:
                lose = True
            current = current.next

        return (self.length, lose)

        