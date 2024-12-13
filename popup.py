'''
Snake Game by: Nathaniel Yerage
File for popup windows of game (paused, starting, p1 wins, p2 wins, etc)
'''

from setup import *

class PopScreen(pygame.Surface):
    def __init__(self, screen):
        self.width = WIN_WIDTH / 4
        self.height = WIN_HEIGHT / 4

        super().__init__( (self.width, self.height) )
        self.fill( POP_COLOR )

        self.rect = self.get_rect()
        self.font = pygame.font.Font(None, 30)

        self.rect.center = (WIN_WIDTH / 2, WIN_HEIGHT / 2)
        self.screen = screen
    
    def draw(self):
        self.screen.blit(self, self.rect)
        


class PauseScreen(PopScreen):
    def __init__(self, screen):
        super().__init__(screen)

        topText = self.font.render('The game is paused', True, TEXT_COLOR)
        topRect = topText.get_rect()
        topRect.center = (self.width / 2, 50)
        self.blit(topText, topRect)

        row2 = self.font.render('Press (p) or (esc) to resume', True, TEXT_COLOR)
        row2Rect = row2.get_rect()
        row2Rect.center = (self.width / 2, 100)
        self.blit(row2, row2Rect)

        self.draw()



