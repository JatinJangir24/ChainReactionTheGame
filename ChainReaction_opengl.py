"""
Made by Jatin Omprakash Jangir
"""
# TODO 
# Make a Active cube for taking input from the user
# movement by arrow keys.
# make its color inverse of the current grid color
# use pygame events to do it and if possible make it blink
# whenever the user presses the enter key a blob is placed.

import pygame
import numpy as np
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math
import sys

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
player_color = [
    (0,0,1),
    (0,1,0),
    (1,0,0),
    (0,1,1),
    (1,1,0),
    (1,0,1),
    (1,1,1),
    (0.75,0.75,0.75),
    (0.5,0,0),
    (0.5,0.5,0),]
currently_selected_cube = [0,0,0]

grid_x = int(input("Enter Grid Size in X-direction:\n"))
grid_y = int(input("Enter Grid Size in Y-direction:\n"))
distance_from_grid = max(grid_x,grid_y)*1.3
MainGrid = np.zeros((grid_x,grid_y))
PlayerRecordGrid = np.zeros((grid_x,grid_y))
Grid = []
GameOver = False

#main algorithm
def SolveGrid(passed_grid):
    grid = np.copy(passed_grid)
    for i in range(grid_x):
        for j in range(grid_y):
            if i==0 or i==grid_x-1:
                if j==0 or j==grid_y-1:
                    # Corners Code Start
                    if grid[i][j] > 1:
                        if i==0  and  j==0:
                            grid[i][j] = 0
                            grid[i+1][j] += 1
                            PlayerRecordGrid[i+1][j] = PlayerRecordGrid[i][j]
                            grid[i][j+1] += 1
                            PlayerRecordGrid[i][j+1] = PlayerRecordGrid[i][j]
                            PlayerRecordGrid[i][j] = 0
                        if i==grid_x-1 and j==0:
                            grid[i][j] = 0
                            grid[i-1][j] += 1
                            PlayerRecordGrid[i-1][j] = PlayerRecordGrid[i][j]
                            grid[i][j+1] += 1
                            PlayerRecordGrid[i][j+1] = PlayerRecordGrid[i][j]
                            PlayerRecordGrid[i][j] = 0
                        if i==0 and j==grid_y-1:
                            grid[i][j] = 0
                            grid[i][j-1] += 1
                            PlayerRecordGrid[i][j-1] = PlayerRecordGrid[i][j]
                            grid[i+1][j] += 1
                            PlayerRecordGrid[i+1][j] = PlayerRecordGrid[i][j]
                            PlayerRecordGrid[i][j] = 0
                        if i==grid_x-1 and j==grid_y-1:
                            grid[i][j] = 0
                            grid[i-1][j] += 1
                            PlayerRecordGrid[i-1][j] = PlayerRecordGrid[i][j]
                            grid[i][j-1] += 1
                            PlayerRecordGrid[i][j-1] = PlayerRecordGrid[i][j]
                            PlayerRecordGrid[i][j] = 0
                        # Corners Code End
                # Edge Code Start
                else:
                    if grid[i][j] > 2:
                        if i==0:
                            grid[i][j] = 0
                            grid[i+1][j] += 1
                            PlayerRecordGrid[i+1][j] = PlayerRecordGrid[i][j]
                            grid[i][j+1] += 1
                            PlayerRecordGrid[i][j+1] = PlayerRecordGrid[i][j]
                            grid[i][j-1] += 1
                            PlayerRecordGrid[i][j-1] = PlayerRecordGrid[i][j]
                            PlayerRecordGrid[i][j] = 0
                        if i==grid_x-1:
                            grid[i][j] = 0
                            grid[i-1][j] += 1
                            PlayerRecordGrid[i-1][j] = PlayerRecordGrid[i][j]
                            grid[i][j+1] += 1
                            PlayerRecordGrid[i][j+1] = PlayerRecordGrid[i][j]
                            grid[i][j-1] += 1
                            PlayerRecordGrid[i][j-1] = PlayerRecordGrid[i][j]
                            PlayerRecordGrid[i][j] = 0
                        if j==0:
                            grid[i][j] = 0
                            grid[i][j+1] += 1
                            PlayerRecordGrid[i][j+1] = PlayerRecordGrid[i][j]
                            grid[i+1][j] += 1
                            PlayerRecordGrid[i+1][j] = PlayerRecordGrid[i][j]
                            grid[i-1][j] += 1
                            PlayerRecordGrid[i-1][j] = PlayerRecordGrid[i][j]
                            PlayerRecordGrid[i][j] = 0
                        if j==grid_y-1:
                            grid[i][j] = 0
                            grid[i][j-1] += 1
                            PlayerRecordGrid[i][j-1] = PlayerRecordGrid[i][j]
                            grid[i+1][j] += 1
                            PlayerRecordGrid[i+1][j] = PlayerRecordGrid[i][j]
                            grid[i-1][j] += 1
                            PlayerRecordGrid[i-1][j] = PlayerRecordGrid[i][j]
                            PlayerRecordGrid[i][j] = 0
            if j == 0 or j == grid_y-1:
                if grid[i][j] > 2:
                    if i==0:
                        grid[i][j] = 0
                        grid[i+1][j] += 1
                        PlayerRecordGrid[i+1][j] = PlayerRecordGrid[i][j]
                        grid[i][j+1] += 1
                        PlayerRecordGrid[i][j+1] = PlayerRecordGrid[i][j]
                        grid[i][j-1] += 1
                        PlayerRecordGrid[i][j-1] = PlayerRecordGrid[i][j]
                        PlayerRecordGrid[i][j] = 0
                    if i==grid_x-1:
                        grid[i][j] = 0
                        grid[i-1][j] += 1
                        PlayerRecordGrid[i-1][j] = PlayerRecordGrid[i][j]
                        grid[i][j+1] += 1
                        PlayerRecordGrid[i][j+1] = PlayerRecordGrid[i][j]
                        grid[i][j-1] += 1
                        PlayerRecordGrid[i][j-1] = PlayerRecordGrid[i][j]
                        PlayerRecordGrid[i][j] = 0
                    if j==0:
                        grid[i][j] = 0
                        grid[i][j+1] += 1
                        PlayerRecordGrid[i][j+1] = PlayerRecordGrid[i][j]
                        grid[i+1][j] += 1
                        PlayerRecordGrid[i+1][j] = PlayerRecordGrid[i][j]
                        grid[i-1][j] += 1
                        PlayerRecordGrid[i-1][j] = PlayerRecordGrid[i][j]
                        PlayerRecordGrid[i][j] = 0
                    if j==grid_y-1:
                        grid[i][j] = 0
                        grid[i][j-1] += 1
                        PlayerRecordGrid[i][j-1] = PlayerRecordGrid[i][j]
                        grid[i+1][j] += 1
                        PlayerRecordGrid[i+1][j] = PlayerRecordGrid[i][j]
                        grid[i-1][j] += 1
                        PlayerRecordGrid[i-1][j] = PlayerRecordGrid[i][j]
                        PlayerRecordGrid[i][j] = 0
                    # Edge Code End
            
            #Middle Body Code Start
            else:
                if grid[i][j]>3:
                    grid[i][j] = 0
                    grid[i][j+1] += 1
                    PlayerRecordGrid[i][j+1] = PlayerRecordGrid[i][j]
                    grid[i+1][j] += 1
                    PlayerRecordGrid[i+1][j] = PlayerRecordGrid[i][j]
                    grid[i-1][j] += 1
                    PlayerRecordGrid[i-1][j] = PlayerRecordGrid[i][j]
                    grid[i][j-1] += 1
                    PlayerRecordGrid[i][j-1] = PlayerRecordGrid[i][j]
                    PlayerRecordGrid[i][j] = 0
            #Middle Body Code End
    return grid

def set_vertices(cube_position_in_x,cube_position_in_y):
    new_vertices = []
    for vert in vertices:
        new_vert = []
        new_x = vert[0]/2 + cube_position_in_x
        new_y = vert[1]/2 + cube_position_in_y
        new_z = vert[2]/2

        new_vert.append(new_x)
        new_vert.append(new_y)
        new_vert.append(new_z)

        new_vertices.append(new_vert)
    return new_vertices

def Cube(vertices, color, thickness):
    glEnable(GL_LINE_SMOOTH)
    glLineWidth(thickness)
    glBegin(GL_LINES)
    glColor3fv(color)
    for edge in edges: 
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    
    glEnd()
    glDisable(GL_LINE_SMOOTH)

def sphere(center, radius, slices, splices, color):
    #GL_TRIANGLES is only used for top and bottom.
    
    #finding the slice layers
    ##################################################
    slice_thickness = 2*radius/slices
    splice_angle = 2*math.pi/splices

    slices_arr = []
    # slice = ((x,y,z),(x,y,z),()...)

    for x in range(slices+1):
        slice = []
        slice_circle_radius = radius * math.sin(math.acos(abs(radius - slice_thickness*x) / radius))
        for y in range(splices):
            slice.append([slice_circle_radius * math.cos(splice_angle * y),slice_circle_radius * math.sin(splice_angle * y),radius - slice_thickness*x])
        slices_arr.append(slice)
    ##################################################

    #moving the circle according to the center parameter
    for slice in slices_arr:
        for coord in slice:
            coord[0] = coord[0] + center[0]
            coord[1] = coord[1] + center[1]
            coord[2] = coord[2] + center[2]
    
    
    glBegin(GL_QUADS)
    glColor3fv(color)
    for slice_no in range(len(slices_arr)-1):
        for x in range(splices):
            if x<splices-1:
                glVertex3fv(slices_arr[slice_no][x])
                glVertex3fv(slices_arr[slice_no][x+1])
                glVertex3fv(slices_arr[slice_no+1][x+1])
                glVertex3fv(slices_arr[slice_no+1][x])
            if x==splices-1:
                glVertex3fv(slices_arr[slice_no][x])
                glVertex3fv(slices_arr[slice_no][0])
                glVertex3fv(slices_arr[slice_no+1][0])
                glVertex3fv(slices_arr[slice_no+1][x])
    glEnd()

def make_Blobs(type, center, color):
    if type == 1:
        sphere(center, 0.5, 10, 10, color)
    elif type == 2:
        new_center1 = [0,0,0]
        new_center1[0] = center[0] + 0.15
        new_center1[1] = center[1] + 0.15
        new_center1[2] = center[2]
        new_center2 = [0,0,0]
        new_center2[0] = center[0] - 0.15
        new_center2[1] = center[1] - 0.15
        new_center2[2] = center[2]

        sphere(new_center1, 0.33, 10, 10, color)
        sphere(new_center2, 0.33, 10, 10, color)
    elif type == 3:
        new_center1 = [0,0,0]
        new_center1[0] = center[0] + 0.1
        new_center1[1] = center[1] + 0.1732
        new_center1[2] = center[2]
        new_center2 = [0,0,0]
        new_center2[0] = center[0] + 0.1
        new_center2[1] = center[1] - 0.1732
        new_center2[2] = center[2]
        new_center3 = [0,0,0]
        new_center3[0] = center[0] - 0.2
        new_center3[1] = center[1] 
        new_center3[2] = center[2]

        sphere(new_center1, 0.25, 10, 10, color)
        sphere(new_center2, 0.25, 10, 10, color)
        sphere(new_center3, 0.25, 10, 10, color)

# To make the grid Matrix
###############################################
for x in range(grid_x):
    gr = []
    for y in range(grid_y):
        gr.append(set_vertices(x,y))
    Grid.append(gr)
###############################################

# For now game will be starting in the console
NoOfPlayers = int(input("Enter No. of Players(Current Max = 10):\n"))
PlayerFailingBias = np.ones(NoOfPlayers) # This ensures that each player has atleast one turn
CurrentPlayer = 1
Played = False

def game_loop():
    global GameOver, CurrentPlayer, MainGrid
    ###########################################################################
    while True:
        if GameOver:
            break
        #reset the current player loop
        if CurrentPlayer > NoOfPlayers and CurrentPlayer != 1:
            CurrentPlayer = 1
        try:
            print("Player %s:"%CurrentPlayer)
            i = int(input("Enter y Coordinate\n"))
            j = int(input("Enter x Coordinate\n"))
        except ValueError:
            print("Please Input Something!")
            continue
        #Checking for Out of Bounds
        if i<1 or j<1 or i>grid_x or j>grid_y:
            print("Wrong Input! Try Again!")
            continue
        #Checking if the player is 'stepping' on a already taken tile
        elif PlayerRecordGrid[i-1][j-1] == 0 or PlayerRecordGrid[i-1][j-1] == CurrentPlayer:
            MainGrid[i-1][j-1] += 1
            PlayerRecordGrid[i-1][j-1] = CurrentPlayer
        else:
            print("WRONG MOVE! Warning Issued! Try Again!")
            continue
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
                        #checking if anyone has won
                        if len(set(np.array(PlayerRecordGrid).flatten())) == 2: # <=2 because there may be a '0' left behind in the grid
                            print("Player %s has Won!"%(list(set(np.array(PlayerRecordGrid).flatten()))[1]))
                            GameOver = True
                            time.sleep(2)
                        if len(set(np.array(PlayerRecordGrid).flatten())) == 1: # the winner takes all the spaces!
                            print("Player %s has Won and has conqured all the spaces!"%(list(set(np.array(PlayerRecordGrid).flatten()))[0]))
                            GameOver = True
                            time.sleep(2)
                        else:
                            pass
            # Checks if the MainGrid is ready for the next Player i.e. no explosions are taking place.
            if(MainGrid == SolveGrid(MainGrid)).all():
                PlayerFailingBias[CurrentPlayer - 1] = 0 # marks that the CurrentPlayer has played his first move
                CurrentPlayer+=1 #Changes the player for next round
                break
    ###########################################################################

def main():
    global GameOver, CurrentPlayer, MainGrid, PlayerRecordGrid, NoOfPlayers, PlayerFailingBias, Played
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    clock = pygame.time.Clock()
    pygame.display.set_caption('Chain Reaction')
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LESS)
    gluPerspective(45, (display[0]/display[1]), 0.1, 100)
    glTranslatef(0.5-grid_x/2,0.5-grid_y/2, -distance_from_grid)

    rx, ry, rz = (0,0,0)
    tx, ty = (0,0)
    zpos = 0
    zrotate = rotate = move = False
    while True:
        clock.tick(30)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif e.type == MOUSEBUTTONDOWN:
                if e.button == 4: zpos = zpos-1
                elif e.button == 5: zpos += 1
                elif e.button == 1: rotate = True
                elif e.button == 2: zrotate = True
                elif e.button == 3: move = True
            elif e.type == MOUSEBUTTONUP:
                if e.button == 1: rotate = False
                elif e.button == 2: zrotate = False
                elif e.button == 3: move = False
            elif e.type == MOUSEMOTION:
                i, j = e.rel
                if zrotate:
                    rz += (i+j)/4
                if rotate:
                    rx += i/2
                    ry += j/2
                if move:
                    tx += i/5
                    ty -= j/5
            if e.type == KEYDOWN and e.key == K_UP:
                if currently_selected_cube[1] < grid_y-1:
                    currently_selected_cube[1]+=1
            elif e.type == KEYDOWN and e.key == K_DOWN:
                if currently_selected_cube[1] > 0:
                    currently_selected_cube[1]-=1
            elif e.type == KEYDOWN and e.key == K_LEFT:
                if currently_selected_cube[0] > 0:
                    currently_selected_cube[0]-=1
            elif e.type == KEYDOWN and e.key == K_RIGHT:
                if currently_selected_cube[0] < grid_x-1:
                    currently_selected_cube[0]+=1
            elif e.type == KEYDOWN and (e.key == K_RETURN or e.key == K_SPACE):
                # Registering in the Array
                if PlayerRecordGrid[grid_x-currently_selected_cube[0]-1][grid_y-currently_selected_cube[1]-1] == 0 or PlayerRecordGrid[grid_x-currently_selected_cube[0]-1][grid_y-currently_selected_cube[1]-1] == CurrentPlayer:
                    MainGrid[grid_x-currently_selected_cube[1]-1][grid_y-currently_selected_cube[0]-1] += 1
                    PlayerRecordGrid[grid_x-currently_selected_cube[1]-1][grid_y-currently_selected_cube[0]-1] = CurrentPlayer
                    Played = True
                else:
                    print("WRONG MOVE! Warning Issued! Try Again!")
                
                # Drawing the Blob
                make_Blobs(1,(currently_selected_cube[0],currently_selected_cube[1],0),player_color[CurrentPlayer])


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
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        
        #uncomment this for rotation
        #glRotatef(1, grid_x/2, grid_y/2, 0)
        glTranslatef(-(0.5-grid_x/2),-(0.5-grid_y/2), 0)
        glTranslate(tx/20., ty/20., - zpos)
        glRotate(ry, 1, 0, 0)
        glRotate(rx, 0, 1, 0)
        glRotate(rz, 0, 0, 1)
        glTranslatef((0.5-grid_x/2),(0.5-grid_y/2), 0)
        rx, ry, rz = (0,0,0)
        tx, ty = (0,0)
        zpos = 0
        #makes the grid
        for x in range(grid_x):
            for y in range(grid_y):
                if not (x==currently_selected_cube[0] and y == currently_selected_cube[1]):
                    Cube(Grid[x][y], player_color[CurrentPlayer], 1)
                else:
                    Cube(Grid[x][y], (1-player_color[CurrentPlayer][0],1-player_color[CurrentPlayer][1],1-player_color[CurrentPlayer][2]), 2)
        
        # Fill the Grid
        for i in range(grid_y):
            for j in range(grid_x):
                if PlayerRecordGrid[j][i] != 0:
                    #print(i, j)
                    make_Blobs(MainGrid[j][i], (grid_y-i-1,grid_x-j-1,0), player_color[int(PlayerRecordGrid[j][i])])
        
        #sphere((2,1,0), 0.5, 10, 10, (1,0,1))
        #sphere((2,2,0), 0.5, 10, 10, (1,0,1))
        #make_Blobs(3, (3,1,0), (1,1,0))

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == '__main__':
    main()
    #game_loop()