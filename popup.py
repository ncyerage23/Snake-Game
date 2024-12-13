'''
Snake Game by: Nathaniel Yerage
File for popup windows of game (paused, starting, p1 wins, p2 wins, etc)
'''

from setup import *

#maybe make popscreen have its own "geometry manager," instead of doing the whole thing I've been doing, lol
#might do that now

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

    def put_rows(self, rows):
        for r in range( len(rows) ):
            row = rows[r]
            line = self.font.render(row, True, TEXT_COLOR)
            line_rect = line.get_rect()

            line_rect.center = (self.width / 2, (r + 1) * self.height / (len(rows) + 2))

            self.blit(line, line_rect)
        
    
    def draw(self):
        self.screen.blit(self, self.rect)


class SetupScreen(PopScreen):
    def __init__(self, screen):
        super().__init__(screen)

        rows = ['Welcome to Snake Game!', '', 'P1 uses WASD keys to move', 'P2 uses the arrow keys', '', 'Press (SPACE) to begin!']
        self.put_rows(rows)

        self.draw()


class PauseScreen(PopScreen):
    def __init__(self, screen):
        super().__init__(screen)

        rows = ['The game is paused', 'Press (p) or (esc) to resume']
        self.put_rows(rows)

        self.draw()


#make this later, lol
class WinScreen(PopScreen):
    def __init__(self, screen):
        pass