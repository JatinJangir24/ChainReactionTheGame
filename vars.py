display = (800,600)
gameMode = 1


if gameMode == 1:
    currently_selected_cube = [0,0,0]

    grid_x = 0
    grid_y = 0

    masterGrid = list()

    rx, ry, rz = (0,0,0)
    tx, ty = (0,0)
    zpos = 0
    zrotate = rotate = move = False
    distance_from_grid = 0

    CurrentPlayer = 1

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