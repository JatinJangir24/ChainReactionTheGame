import numpy as np
"""
TODO
rewrite the MainGrid to include the player data into itself so as to reduse the amount of global variables.
"""
def SolveGrid(passed_grid):
    global PlayerR
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