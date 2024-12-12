'''
file for objects of snake program, and all that jazz
idk, just helps make everything a little cleaner
'''

from snake_misc import *


class Scoreboard(pygame.Surface):
    def __init__(self, width, height):
        super().__init__( (width, height) )

        self.font = pygame.font.Font(None, 50)
        self.font2 = pygame.font.Font(None, 35)

    def update_sb(self, fruit, len, time):
        self.fill( SB_COLOR )
        title = self.font.render('Snake!', True, SB_TEXT_COLOR)
        fruit_counter = self.font2.render(f'Fruit: {fruit}', True, SB_TEXT_COLOR)
        len_counter = self.font2.render(f'Length: {len}', True, SB_TEXT_COLOR)
        time_counter = self.font2.render(f'Time: {time}', True, SB_TEXT_COLOR)

        self.blit(title, (10,10))
        self.blit(fruit_counter, (175, 15))
        self.blit(len_counter, (275, 15))
        self.blit(time_counter, (400,15))


class PopScreen(pygame.Surface):
    def __init__(self, width, height):
        super().__init__( (width, height) )
        self.fill( (255,255,255) )

        self.width = width
        self.height = height

        self.font = pygame.font.Font(None, 25)
    
    def popup(self, message):
        self.fill( (255, 255, 255) )

        h = self.height / 2 - 15

        for line in message:
            mes = self.font.render(line, True, (0,0,0))
            self.blit(mes, ( 20, h))
            h += 20
