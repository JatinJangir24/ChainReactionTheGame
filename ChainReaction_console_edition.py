import numpy as np
import os
import time
def SolveGrid(passed_grid):
    grid = np.copy(passed_grid)
    for i in range(10):
        for j in range(10):
            if i==0 or i==9:
                if j==0 or j==9:
                    # Corners Code Start
                    if grid[i][j] > 1:
                        if i==0  and  j==0:
                            grid[i][j] = 0
                            grid[i+1][j] += 1
                            PlayerRecordGrid[i+1][j] = PlayerRecordGrid[i][j]
                            grid[i][j+1] += 1
                            PlayerRecordGrid[i][j+1] = PlayerRecordGrid[i][j]
                            PlayerRecordGrid[i][j] = 0
                        if i==9 and j==0:
                            grid[i][j] = 0
                            grid[i-1][j] += 1
                            PlayerRecordGrid[i-1][j] = PlayerRecordGrid[i][j]
                            grid[i][j+1] += 1
                            PlayerRecordGrid[i][j+1] = PlayerRecordGrid[i][j]
                            PlayerRecordGrid[i][j] = 0
                        if i==0 and j==9:
                            grid[i][j] = 0
                            grid[i][j-1] += 1
                            PlayerRecordGrid[i][j-1] = PlayerRecordGrid[i][j]
                            grid[i+1][j] += 1
                            PlayerRecordGrid[i+1][j] = PlayerRecordGrid[i][j]
                            PlayerRecordGrid[i][j] = 0
                        if i==9 and j==9:
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
                        if i==9:
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
                        if j==9:
                            grid[i][j] = 0
                            grid[i][j-1] += 1
                            PlayerRecordGrid[i][j-1] = PlayerRecordGrid[i][j]
                            grid[i+1][j] += 1
                            PlayerRecordGrid[i+1][j] = PlayerRecordGrid[i][j]
                            grid[i-1][j] += 1
                            PlayerRecordGrid[i-1][j] = PlayerRecordGrid[i][j]
                            PlayerRecordGrid[i][j] = 0
            if j == 0 or j == 9:
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
                    if i==9:
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
                    if j==9:
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

MainGrid = [[0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0]]

PlayerRecordGrid = [[0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0]]
NoOfPlayers = int(input("Enter No. of Players:\n"))
PlayerFailingBias = np.ones(NoOfPlayers) # This ensures that each player has atleast one turn
CurrentPlayer = 1
GameOver = False
ClearScreen = True

#this is the game loop
while True:
    if GameOver:
        break
    if ClearScreen:
        os.system('cls')
    ClearScreen = True
    print(MainGrid)
    #reset the current player loop
    if CurrentPlayer > NoOfPlayers and CurrentPlayer != 1:
        CurrentPlayer = 1
    
    
    bias = True # this variable is used only because I implimented the ClearScreen variable later on(I am Lazy),
    while bias:
        try:
            print("Player %s:"%CurrentPlayer)
            i = int(input("Enter y Coordinate\n"))
            j = int(input("Enter x Coordinate\n"))
            bias = False
        except ValueError:
            bias = True
            print("Please Input Something!")
            continue

    #Checking for Out of Bounds
    if i<1 or j<1 or i>10 or j>10:
        print("Wrong Input! Try Again!")
        ClearScreen = False
        continue
    #Checking if the player is 'stepping' on a already taken tile
    elif PlayerRecordGrid[i-1][j-1] == 0 or PlayerRecordGrid[i-1][j-1] == CurrentPlayer:
        MainGrid[i-1][j-1] += 1
        PlayerRecordGrid[i-1][j-1] = CurrentPlayer
    else:
        print("WRONG MOVE! Warning Issued! Try Again!")
        ClearScreen = False
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
                        ClearScreen = False
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