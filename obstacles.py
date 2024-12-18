'''
Snake Game by: Nathaniel Yerage
File for bushes & other obstacles
'''

from setup import *

'''
come up with more fun obstacles, maybe some that do things
not all have to be obstacles...
'''

class Rock(pygame.sprite.Sprite):
    def __init__(self, coords):
        super(Rock, self).__init__()
        self.surf = pygame.Surface((GW_GRID_STEP * 2, GW_GRID_STEP * 2), pygame.SRCALPHA)
        self.rect = self.surf.get_rect()
        self.coords = coords
        self.rect.center = toCoord(self.coords)

        self.image = pygame.image.load('rock2.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))
        self.surf.blit(self.image, (0,0))
    

