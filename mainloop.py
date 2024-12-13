'''
Snake Game by: Nathaniel Yerage
File for mainloop control of pygame
'''


from setup import *
import gamewindow as gw
import scoreboard as sb

screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption('Snake!')
clock = pygame.time.Clock()


scoreboard = sb.Scoreboard()
gamewindow = gw.GameWindow()


running = True
while running:

    key = None
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    
    screen.fill(WIN_COLOR)

    screen.blit(scoreboard, (0,0))
    screen.blit(gamewindow, (25, SB_HEIGHT))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()