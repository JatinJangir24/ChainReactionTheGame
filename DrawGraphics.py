from OpenGL.GL import *
from OpenGL.GLU import *
import math
import vars

def gl_init():
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LESS)
    gluPerspective(45, (vars.display[0]/vars.display[1]), 0.1, 100)
    glTranslatef(-vars.grid_x/2 + 0.5, vars.grid_y/2 - 0.5, -vars.distance_from_grid)

def set_vertices(cube_position_in_x,cube_position_in_y):
    new_vertices = []
    for vert in vars.vertices:
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
    for edge in vars.edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    
    glEnd()
    glDisable(GL_LINE_SMOOTH)

def sphere(center, radius, slices, splices, color):    
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

# TODO Rename
def asdasdasd():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    #this whole part is for the rotation implimentation, the two translates are required to make the center of rotation be the center of rotation.
    glTranslatef(-(0.5-vars.grid_x/2),(0.5-vars.grid_y/2), 0)
    glTranslate(vars.tx/20., vars.ty/20., - vars.zpos)
    glRotate(vars.ry, 1, 0, 0)
    glRotate(vars.rx, 0, 1, 0)
    glRotate(vars.rz, 0, 0, 1)
    glTranslatef((0.5-vars.grid_x/2),-(0.5-vars.grid_y/2), 0)
    rx, ry, rz = (0,0,0)
    tx, ty = (0,0)
    zpos = 0
    #makes the grid
    for y in range(vars.grid_y):
        for x in range(vars.grid_x):
            if not (x==currently_selected_cube[0] and y == currently_selected_cube[1]):
                Cube(Grid[y][x], vars.player_color[vars.CurrentPlayer], 1)
            else:
                Cube(Grid[y][x], (1-vars.player_color[vars.CurrentPlayer][0],1-vars.player_color[vars.CurrentPlayer][1],1-vars.player_color[vars.CurrentPlayer][2]), 2)        
    # Fill the Grid
    for j in range(vars.grid_y):
        for i in range(vars.grid_x):
            if PlayerRecordGrid[j][i] != 0:
                make_Blobs(MainGrid[j][i], (i,-j,0), vars.player_color[int(PlayerRecordGrid[j][i])])