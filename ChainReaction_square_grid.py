"""
Made by Jatin Omprakash Jangir
"""

"""
TODO
Edit the files to accomodate the changes made because of making multiple files.
Files to edit:
ChainReaction_opengl.py (this file)
DrawGraphics.py
GridSolver.py
"""

"""
TODO
Rewrite the MainGrid into Mastergrid to include the player data into itself so as to reduse the amount of global variables.
"""

import pygame
from pygame.locals import *
from GridSolver import *
from DrawGraphics import *
import vars

#Variables/Constants
vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
    )
edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )

currently_selected_cube = [0,0,0]

"""
TODO
Make this part in the PyGame Window.
"""
#####################################################
vars.grid_x = int(input("Enter Grid Size in X-direction:\n"))
vars.grid_y = int(input("Enter Grid Size in Y-direction:\n"))
#####################################################
vars.distance_from_grid = max(vars.grid_x,vars.grid_y)*1.414
MainGrid = np.zeros((vars.grid_y,vars.grid_x))
PlayerRecordGrid = np.zeros((vars.grid_y,vars.grid_x))
Grid = []
GameOver = False

# To make the grid Matrix
###############################################
for y in range(vars.grid_y):
    gr = []
    for x in range(vars.grid_x):
        gr.append(set_vertices(x,y))
    Grid.append(gr)
###############################################

"""
TODO
Make the whole game in one Window.
"""
# For now game will be starting in the console
NoOfPlayers = int(input("Enter No. of Players(Current Max = 10):\n"))
# TODO impliment the PlayerFailingBias into the MasterGrid
PlayerFailingBias = np.ones(NoOfPlayers) # This ensures that each player has atleast one turn
PlayerDead = np.zeros(NoOfPlayers)
CurrentPlayer = 1
Played = False

# check this function
def handleEvents():
    global Played
    for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif e.type == MOUSEBUTTONDOWN:
                if e.button == 4: zpos = zpos-1
                elif e.button == 5: zpos += 1
                elif e.button == 1: vars.rotate = True
                elif e.button == 2: vars.zrotate = True
                elif e.button == 3: vars.move = True
            elif e.type == MOUSEBUTTONUP:
                if e.button == 1: rotate = False
                elif e.button == 2: zrotate = False
                elif e.button == 3: move = False
            elif e.type == MOUSEMOTION:
                i, j = e.rel
                if vars.zrotate:
                    vars.rz += (i+j)/4
                if vars.rotate:
                    vars.rx += i/2
                    vars.ry += j/2
                if vars.move:
                    vars.tx += i/5
                    vars.ty -= j/5
            if e.type == KEYDOWN and e.key == K_DOWN:
                if currently_selected_cube[1] < vars.grid_y-1:
                    currently_selected_cube[1]+=1
            elif e.type == KEYDOWN and e.key == K_UP:
                if currently_selected_cube[1] > 0:
                    currently_selected_cube[1]-=1
            elif e.type == KEYDOWN and e.key == K_LEFT:
                if currently_selected_cube[0] > 0:
                    currently_selected_cube[0]-=1
            elif e.type == KEYDOWN and e.key == K_RIGHT:
                if currently_selected_cube[0] < vars.grid_x-1:
                    currently_selected_cube[0]+=1
            elif e.type == KEYDOWN and (e.key == K_RETURN or e.key == K_SPACE):
                # Registering in the Array
                if PlayerRecordGrid[currently_selected_cube[1]][currently_selected_cube[0]] == 0 or PlayerRecordGrid[currently_selected_cube[1]][currently_selected_cube[0]] == CurrentPlayer:
                    MainGrid[currently_selected_cube[1]][currently_selected_cube[0]] += 1
                    PlayerRecordGrid[currently_selected_cube[1]][currently_selected_cube[0]] = CurrentPlayer
                    Played = True
                else:
                    print("WRONG MOVE! Warning Issued! Try Again!")
                
                # Drawing the Blob
                make_Blobs(1,(currently_selected_cube[1],currently_selected_cube[0],0),vars.player_color[CurrentPlayer])

def main():
    global GameOver, CurrentPlayer, MainGrid, PlayerRecordGrid, NoOfPlayers, PlayerFailingBias, Played
    pygame.init()
    vars.display = (800,600)
    pygame.display.set_mode(vars.display, DOUBLEBUF|OPENGL)
    clock = pygame.time.Clock()
    pygame.display.set_caption('Chain Reaction')

    gl_init()

    while True:
        clock.tick(30)
        
        handleEvents() # check this function

        if GameOver:
            break
        
        if Played:
            if CurrentPlayer >= NoOfPlayers and CurrentPlayer != 1:
                CurrentPlayer = 0
            while True:
                MainGrid = SolveGrid(MainGrid)
                if (PlayerFailingBias == 0).all(): #this if statement checks if the first round is compleated
                    for p in range(NoOfPlayers):
                        try:
                            #the following monstrocity checks if a player is missing from the player board
                            list(np.array(PlayerRecordGrid).flatten()).index(p+1)
                        except ValueError:
                            #if you are here it means the player 'p' is missing from the board, since we have already checked that
                            #the first turns have finished i.e. player 'p' is dead.
                            if PlayerFailingBias[p - 1] == 0:
                                print("Player no. %s eliminated!"%(p+1))
                                PlayerDead[p] = 1
                            #checking if anyone has won
                            if len(set(np.array(PlayerRecordGrid).flatten())) == 2: # <=2 because there may be a '0' left behind in the grid
                                print("Player %s has Won!"%(list(set(np.array(PlayerRecordGrid).flatten()))[1]))
                                GameOver = True
                            if len(set(np.array(PlayerRecordGrid).flatten())) == 1: # the winner takes all the spaces!
                                print("Player %s has Won and has conqured all the spaces!"%(list(set(np.array(PlayerRecordGrid).flatten()))[0]))
                                GameOver = True
                            else:
                                pass
                # Checks if the MainGrid is ready for the next Player i.e. no explosions are taking place.
                if(MainGrid == SolveGrid(MainGrid)).all():
                    PlayerFailingBias[CurrentPlayer - 1] = 0 # marks that the CurrentPlayer has played his first move
                    CurrentPlayer+=1 #Changes the player for next round
                    break
            Played = False
        
        asdasdasd()

        if PlayerDead[CurrentPlayer-1]:
            CurrentPlayer += 1
            continue
        
        pygame.display.flip()


if __name__ == '__main__':
    main()