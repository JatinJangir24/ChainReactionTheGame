"""
Made by Jatin Omprakash Jangir
"""

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
    (0,0,0), # <= This color will never show up.
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
distance_from_grid = max(grid_x,grid_y)*1.414
MainGrid = np.zeros((grid_y,grid_x)) # I have just replaced the x and y
PlayerRecordGrid = np.zeros((grid_y,grid_x))
Grid = []
GameOver = False

#main algorithm
def SolveGrid(passed_grid):
    grid = np.copy(passed_grid)
    for i in range(grid_x):
        for j in range(grid_y):
            if j==0 or j==grid_x-1:
                if i==0 or i==grid_x-1:
                    # Corners Code Start
                    if grid[j][i] > 1:
                        if j==0  and  i==0:
                            grid[j][i] = 0
                            grid[j+1][i] += 1
                            PlayerRecordGrid[j+1][i] = PlayerRecordGrid[j][i]
                            grid[j][i+1] += 1
                            PlayerRecordGrid[j][i+1] = PlayerRecordGrid[j][i]
                            PlayerRecordGrid[j][i] = 0
                        if j==grid_x-1 and i==0:
                            grid[j][i] = 0
                            grid[j-1][i] += 1
                            PlayerRecordGrid[j-1][i] = PlayerRecordGrid[j][i]
                            grid[j][i+1] += 1
                            PlayerRecordGrid[j][i+1] = PlayerRecordGrid[j][i]
                            PlayerRecordGrid[j][i] = 0
                        if j==0 and i==grid_x-1:
                            grid[j][i] = 0
                            grid[j][i-1] += 1
                            PlayerRecordGrid[j][i-1] = PlayerRecordGrid[j][i]
                            grid[j+1][i] += 1
                            PlayerRecordGrid[j+1][i] = PlayerRecordGrid[j][i]
                            PlayerRecordGrid[j][i] = 0
                        if j==grid_x-1 and i==grid_x-1:
                            grid[j][i] = 0
                            grid[j-1][i] += 1
                            PlayerRecordGrid[j-1][i] = PlayerRecordGrid[j][i]
                            grid[j][i-1] += 1
                            PlayerRecordGrid[j][i-1] = PlayerRecordGrid[j][i]
                            PlayerRecordGrid[j][i] = 0
                        # Corners Code End
                # Edge Code Start
                else:
                    if grid[j][i] > 2:
                        if j==0:
                            grid[j][i] = 0
                            grid[j+1][i] += 1
                            PlayerRecordGrid[j+1][i] = PlayerRecordGrid[j][i]
                            grid[j][i+1] += 1
                            PlayerRecordGrid[j][i+1] = PlayerRecordGrid[j][i]
                            grid[j][i-1] += 1
                            PlayerRecordGrid[j][i-1] = PlayerRecordGrid[j][i]
                            PlayerRecordGrid[j][i] = 0
                        if j==grid_x-1:
                            grid[j][i] = 0
                            grid[j-1][i] += 1
                            PlayerRecordGrid[j-1][i] = PlayerRecordGrid[j][i]
                            grid[j][i+1] += 1
                            PlayerRecordGrid[j][i+1] = PlayerRecordGrid[j][i]
                            grid[j][i-1] += 1
                            PlayerRecordGrid[j][i-1] = PlayerRecordGrid[j][i]
                            PlayerRecordGrid[j][i] = 0
                        if i==0:
                            grid[j][i] = 0
                            grid[j][i+1] += 1
                            PlayerRecordGrid[j][i+1] = PlayerRecordGrid[j][i]
                            grid[j+1][i] += 1
                            PlayerRecordGrid[j+1][i] = PlayerRecordGrid[j][i]
                            grid[j-1][i] += 1
                            PlayerRecordGrid[j-1][i] = PlayerRecordGrid[j][i]
                            PlayerRecordGrid[j][i] = 0
                        if i==grid_x-1:
                            grid[j][i] = 0
                            grid[j][i-1] += 1
                            PlayerRecordGrid[j][i-1] = PlayerRecordGrid[j][i]
                            grid[j+1][i] += 1
                            PlayerRecordGrid[j+1][i] = PlayerRecordGrid[j][i]
                            grid[j-1][i] += 1
                            PlayerRecordGrid[j-1][i] = PlayerRecordGrid[j][i]
                            PlayerRecordGrid[j][i] = 0
            if i == 0 or i == grid_x-1:
                if grid[j][i] > 2:
                    if j==0:
                        grid[j][i] = 0
                        grid[j+1][i] += 1
                        PlayerRecordGrid[j+1][i] = PlayerRecordGrid[j][i]
                        grid[j][i+1] += 1
                        PlayerRecordGrid[j][i+1] = PlayerRecordGrid[j][i]
                        grid[j][i-1] += 1
                        PlayerRecordGrid[j][i-1] = PlayerRecordGrid[j][i]
                        PlayerRecordGrid[j][i] = 0
                    if j==grid_x-1:
                        grid[j][i] = 0
                        grid[j-1][i] += 1
                        PlayerRecordGrid[j-1][i] = PlayerRecordGrid[j][i]
                        grid[j][i+1] += 1
                        PlayerRecordGrid[j][i+1] = PlayerRecordGrid[j][i]
                        grid[j][i-1] += 1
                        PlayerRecordGrid[j][i-1] = PlayerRecordGrid[j][i]
                        PlayerRecordGrid[j][i] = 0
                    if i==0:
                        grid[j][i] = 0
                        grid[j][i+1] += 1
                        PlayerRecordGrid[j][i+1] = PlayerRecordGrid[j][i]
                        grid[j+1][i] += 1
                        PlayerRecordGrid[j+1][i] = PlayerRecordGrid[j][i]
                        grid[j-1][i] += 1
                        PlayerRecordGrid[j-1][i] = PlayerRecordGrid[j][i]
                        PlayerRecordGrid[j][i] = 0
                    if i==grid_x-1:
                        grid[j][i] = 0
                        grid[j][i-1] += 1
                        PlayerRecordGrid[j][i-1] = PlayerRecordGrid[j][i]
                        grid[j+1][i] += 1
                        PlayerRecordGrid[j+1][i] = PlayerRecordGrid[j][i]
                        grid[j-1][i] += 1
                        PlayerRecordGrid[j-1][i] = PlayerRecordGrid[j][i]
                        PlayerRecordGrid[j][i] = 0
                    # Edge Code End
            
            #Middle Body Code Start
            else:
                if grid[j][i]>3:
                    grid[j][i] = 0
                    grid[j][i+1] += 1
                    PlayerRecordGrid[j][i+1] = PlayerRecordGrid[j][i]
                    grid[j+1][i] += 1
                    PlayerRecordGrid[j+1][i] = PlayerRecordGrid[j][i]
                    grid[j-1][i] += 1
                    PlayerRecordGrid[j-1][i] = PlayerRecordGrid[j][i]
                    grid[j][i-1] += 1
                    PlayerRecordGrid[j][i-1] = PlayerRecordGrid[j][i]
                    PlayerRecordGrid[j][i] = 0
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
        new_vert.append(-new_y)
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
for y in range(grid_y):
    gr = []
    for x in range(grid_x):
        gr.append(set_vertices(x,y))
    Grid.append(gr)
###############################################

# For now game will be starting in the console
NoOfPlayers = int(input("Enter No. of Players(Current Max = 10):\n"))
PlayerFailingBias = np.ones(NoOfPlayers) # This ensures that each player has atleast one turn
PlayerDead = np.zeros(NoOfPlayers)
CurrentPlayer = 1
Played = False

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
    glTranslatef(-grid_x/2 + 0.5, grid_y/2 - 0.5, -distance_from_grid)

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
            if e.type == KEYDOWN and e.key == K_DOWN:
                if currently_selected_cube[1] < grid_y-1:
                    currently_selected_cube[1]+=1
            elif e.type == KEYDOWN and e.key == K_UP:
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
                if PlayerRecordGrid[currently_selected_cube[1]][currently_selected_cube[0]] == 0 or PlayerRecordGrid[currently_selected_cube[1]][currently_selected_cube[0]] == CurrentPlayer:
                    MainGrid[currently_selected_cube[1]][currently_selected_cube[0]] += 1
                    PlayerRecordGrid[currently_selected_cube[1]][currently_selected_cube[0]] = CurrentPlayer
                    Played = True
                else:
                    print("WRONG MOVE! Warning Issued! Try Again!")
                
                # Drawing the Blob
                make_Blobs(1,(currently_selected_cube[1],currently_selected_cube[0],0),player_color[CurrentPlayer])


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
        
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        #this whole part is for the rotation implimentation, the two translates are required to make the center of rotation be the center of rotation.
        glTranslatef(-(0.5-grid_x/2),(0.5-grid_y/2), 0)
        glTranslate(tx/20., ty/20., - zpos)
        glRotate(ry, 1, 0, 0)
        glRotate(rx, 0, 1, 0)
        glRotate(rz, 0, 0, 1)
        glTranslatef((0.5-grid_x/2),-(0.5-grid_y/2), 0)
        rx, ry, rz = (0,0,0)
        tx, ty = (0,0)
        zpos = 0
        #makes the grid
        for y in range(grid_y):
            for x in range(grid_x):
                if not (x==currently_selected_cube[0] and y == currently_selected_cube[1]):
                    Cube(Grid[y][x], player_color[CurrentPlayer], 1)
                else:
                    Cube(Grid[y][x], (1-player_color[CurrentPlayer][0],1-player_color[CurrentPlayer][1],1-player_color[CurrentPlayer][2]), 2)
        
        # Fill the Grid
        for j in range(grid_y):
            for i in range(grid_x):
                if PlayerRecordGrid[j][i] != 0:
                    make_Blobs(MainGrid[j][i], (i,-j,0), player_color[int(PlayerRecordGrid[j][i])])

        if PlayerDead[CurrentPlayer-1]:
            CurrentPlayer += 1
            continue
        
        pygame.display.flip()


if __name__ == '__main__':
    main()