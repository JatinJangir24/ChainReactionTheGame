display = (800,600)

grid_x = 0
grid_y = 0

rx, ry, rz = (0,0,0)
tx, ty = (0,0)
zpos = 0
zrotate = rotate = move = False
distance_from_grid = 0

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