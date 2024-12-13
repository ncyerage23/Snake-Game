'''
Snake Game by: Nathaniel Yerage
File for scoreboard operations
'''

from setup import *

class Scoreboard(pygame.Surface):
    def __init__(self):
        super().__init__( (SB_WIDTH, SB_HEIGHT) )

        self.font = pygame.font.Font(None, 50)
        self.font2 = pygame.font.Font(None, 35)        
        
    def update_sb(self, time, p1, p2):
        self.fill((SB_COLOR))

        #add something for when there's effects on a snake (also do this in snake.py, but that's later)

        #making the text
        timer = self.font.render(f'Time: {time}', True, TEXT_COLOR)

        p1_text = self.font2.render(f'P1:  length: {p1[1]}', True, TEXT_COLOR)
        p2_text = self.font2.render(f'P2:  length: {p2[1]}', True, TEXT_COLOR)

        #getting the rects
        timer_rect = timer.get_rect()
        p1_rect = p1_text.get_rect()
        p2_rect = p2_text.get_rect()

        #setting the locations
        timer_rect.center = (SB_WIDTH / 2, SB_HEIGHT / 2)
        p1_rect.center = (SB_WIDTH / 4, SB_HEIGHT / 2)
        p2_rect.center = (3 * SB_WIDTH / 4, SB_HEIGHT / 2)

        #drawing it on the surface
        self.blit(timer, timer_rect)
        self.blit(p1_text, p1_rect)
        self.blit(p2_text, p2_rect)