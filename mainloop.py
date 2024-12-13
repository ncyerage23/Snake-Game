'''
Snake Game by: Nathaniel Yerage
File for mainloop control of pygame
'''


from setup import *
import gamewindow as gw
import scoreboard as sb
import popup as pop

screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption('Snake!')
clock = pygame.time.Clock()


scoreboard = sb.Scoreboard()
gamewindow = gw.GameWindow()

states = ['PLAYING', 'WIN', 'PAUSE']
mode = states[0]

timer = 0
mini_time = 0


running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        
        elif event.type == KEYDOWN:
            #maybe make it so if p1 pauses, only he resumes and v.v. (later)
            if event.key == K_p or event.key == K_ESCAPE:
                if mode == states[0]:
                    pop.PauseScreen(screen)
                    mode = states[2]
                elif mode == states[2]:
                    mode = states[0]
    
    if mode == 'PLAYING':

        screen.fill(WIN_COLOR)

        scoreboard.update_sb(timer, (0,0), (0,0))

        screen.blit(scoreboard, (0,0))
        screen.blit(gamewindow, (25, SB_HEIGHT))

        mini_time += 1
        if mini_time % FPS == 0:
            timer += 1

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()