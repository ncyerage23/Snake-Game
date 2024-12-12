'''
Version 3 of snake program in pygame

Things to implement:
    Better start pause and end windows.
    And a better way to implement them all / freeze the game. 
    Helper methods for gui setup and that kind of thing, all in snake_misc

    Better graphics (good luck)
    bigger playing surface
    local co-op (two snakes, controlled by different people)
    different kinds of fruits w/ different abilities (speed, idk what else lol)
    obstacles, and maybe a smaller grid
    put speed as a thing into the snake object, instead of increasing fps

    most of all, I want to figure out a way to make this all structured better. Idk, doing gamewindow.snake.head.rect is a little insane.
    So yeah, just optimization and cleanliness. 

    But, honestly, none of that seems too difficult now. Yeah. 

'''

from snake_misc import *
import snake_sb as sb
import snake_gw as gw



fruit_counter = 0
time = 0

mini_time = 0
fps = 60

pause = False
lose = False



screen = pygame.display.set_mode((GW_SIZE, GW_SIZE + SB_HEIGHT))
pygame.display.set_caption('Snake!')

clock = pygame.time.Clock()

gamewindow = gw.GameWindow( GW_SIZE )
scoreboard = sb.Scoreboard( GW_SIZE, SB_HEIGHT )
popup = sb.PopScreen(300, 100)


running = True
while running:

    key = None
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        
        elif event.type == KEYDOWN:
            if event.key in LEGAL_MOVES[gamewindow.snake.head.direction]:
                key = event.key
            elif event.key == K_p:
                if pause:
                    pause = False
                else:
                    pause = True
            elif event.key == K_ESCAPE:
                running = False
    
    if lose:
        popup.popup( ('You lost! Damn, you suck.', ) )
        screen.blit(popup, (100, 200))

    elif pause:
        popup.popup( ('You paused the game!', 'Press (p) or (esc) to resume') )
        screen.blit(popup, (100, 200))

    else:
        fruit, len, lose = gamewindow.update_gw(key)
        fruit_counter += fruit
        scoreboard.update_sb(fruit_counter, len, time)

        if lose:
            lose = True

        screen.blit(scoreboard, (0, 0) )
        screen.blit(gamewindow, (0, SB_HEIGHT) )
        
        mini_time += 1
        if mini_time % fps == 0:
            time += 1
    

    pygame.display.flip()
    clock.tick(fps + 5 * fruit_counter)

pygame.quit()