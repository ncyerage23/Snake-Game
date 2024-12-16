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
'''

from setup import *
import gamewindow as gw
import scoreboard as sb
import popup as pop

screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption('Snake!')
clock = pygame.time.Clock()

def gameOver():
    global mode
    mode = states[1]

scoreboard = sb.Scoreboard()
gamewindow = gw.GameWindow(gameOver)

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
            
            elif (event.key == K_UP or event.key == K_DOWN or event.key == K_LEFT or event.key == K_RIGHT) and mode == states[0]:
                p2_key = event.key
            
            elif (event.key == K_w or event.key == K_a or event.key == K_s or event.key == K_d) and mode == states[0]:
                p1_key = event.key

            #maybe make it so if p1 pauses, only he resumes and v.v. (later)
            elif event.key == K_p or event.key == K_ESCAPE:
                if mode == states[0]:
                    pop.PauseScreen(screen)
                    mode = states[2]
                elif mode == states[2]:
                    mode = states[0]
    

    if mode == 'PLAYING':
        screen.fill(WIN_COLOR)

        scoreboard.update_sb(timer, (0,0), (0,0))
        
        gamewindow.update_gw(p1_key, p2_key)

        screen.blit(scoreboard, (WIN_OFFSET,0))
        screen.blit(gamewindow, (WIN_OFFSET, SB_HEIGHT))

        mini_time += 1
        if mini_time % FPS == 0:
            timer += 1

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()