'''
Snake Game by: Nathaniel Yerage
File for bushes & other obstacles
'''

from setup import *

'''
come up with more fun obstacles, maybe some that do things
not all have to be obstacles...
'''

class Wall(pygame.sprite.Sprite):
    def __init__(self, start, end):
        super(Wall, self).__init__()

        self.start = wall_toCoord(start)
        self.end = wall_toCoord(end)

        dx = self.end[0] - self.start[0]
        dy = self.end[1] - self.start[1]

        self.color = WALL_COLOR

        if dx == 0:
            self.dir = 'v'
        else:
            self.dir = 'h'
        
        if dx == 0:
            self.x = WALL_WIDTH + 5
            self.y = dy
        else:
            self.x = dx
            self.y = WALL_WIDTH + 5
        
        self.surf = pygame.Surface( (self.x, self.y), pygame.SRCALPHA )
        self.rect = self.surf.get_rect()
        
        if dx == 0:
            self.rect.centerx = self.start[0]
            self.rect.top = self.start[1]
        else:
            self.rect.centery = self.start[1]
            self.rect.left = self.start[0]

    def draw(self, screen):

        if self.dir == 'h':
            start_coord = (WALL_WIDTH // 2, self.rect.height // 2)
            end_coord = (self.x - WALL_WIDTH // 2, self.rect.height // 2)
        else:
            start_coord = (self.rect.width // 2, WALL_WIDTH // 2)
            end_coord = (self.rect.width // 2, self.y - WALL_WIDTH // 2)

        pygame.draw.line(self.surf, self.color, start_coord, end_coord, WALL_WIDTH)
        pygame.draw.circle(self.surf, self.color, start_coord, WALL_WIDTH // 2 - 1)
        pygame.draw.circle(self.surf, self.color, end_coord, WALL_WIDTH // 2 - 1)

        screen.blit(self.surf, self.rect)
