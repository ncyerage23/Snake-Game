'''
Snake Game by: Nathaniel Yerage
File for mainloop control of pygame
'''

'''
Things to add later:
    Start countdown
    snakes start off screen, then roll in when game starts
    better way to switch from playing to pause & with setup screen, etc.
    show effects of snake on the snake (idk, little effects over top lol)
    texture for snake head
    maybe make globals (across the whole program) for time and screen and clock, idk. Might be simpler
    give the grass a texture, and maybe the scoreboard / border. Maybe draw it all myself
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

states = ['PLAYING', 'WIN', 'PAUSE', 'SETUP']
mode = states[3]

screen.fill(WIN_COLOR)
scoreboard.update_sb(0, (0,0), (0,0))
screen.blit(scoreboard, (WIN_OFFSET,0))
screen.blit(gamewindow, (WIN_OFFSET, SB_HEIGHT))
pop.SetupScreen(screen)

timer = 0
mini_time = 0


running = True
while running:
    p1_key = None
    p2_key = None

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        
        elif event.type == KEYDOWN:
            if event.key == K_SPACE and mode == states[3]:
                mode = states[0]
                #maybe make a countdown (later)
            
            elif event.key == K_SPACE and mode == states[1]:
                gamewindow = gw.GameWindow()
                scoreboard = sb.Scoreboard()
                mode = states[0]
            

            elif event.key in LEGAL_MOVES_P1[gamewindow.p1.direction] and mode == states[0]:
                p1_key = event.key
            
            elif event.key in LEGAL_MOVES_P2[gamewindow.p2.direction] and mode == states[0]:
                p2_key = event.key
            
            elif event.key == K_SPACE and mode == states[2]:
                running = False

            #maybe make it so if p1 pauses, only he resumes and v.v. (later)
            elif event.key == K_p or event.key == K_ESCAPE:
                if mode == states[0]:
                    pop.PauseScreen(screen)
                    mode = states[2]
                elif mode == states[2]:
                    mode = states[0]
    

    if mode == 'PLAYING':
        screen.fill(WIN_COLOR)

        p1, p2, touch = gamewindow.update_gw(p1_key, p2_key)

        if p1[1] or p2[1] or touch:
            mode = states[1]

        scoreboard.update_sb(timer, p1, p2)

        #fix this to be like gw
        screen.blit(scoreboard, (WIN_OFFSET,0))
        gamewindow.draw_gw(screen)

        mini_time += 1
        if mini_time % FPS == 0:
            timer += 1
    
    elif mode == states[1]:
        pop.WinScreen(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()