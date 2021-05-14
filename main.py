from graph import Graph
from character import Character
import ui_file
import random
import pygame
import time
import queue
from collections import deque
import os
import login

# function to set the position of the display window
def set_window_position(x, y):
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

# creates a grid of size (size)*(size)
def create_grid(size):

        # create a graph for the grid
        grid = Graph()

        # add the vertices of the grid
        for i in range(size):
                for j in range(size):
                        grid.add_vertex((i,j))

        # return the constructed grid
        return grid

# creates a maze when a grid and its vertices are passed in
def create_maze(grid, vertex, completed=None, vertices=None):
        
        if vertices is None:
                vertices = grid.get_vertices()
        if completed is None:
                completed = [vertex]

        # select a random direction
        paths = list(int(i) for i in range(4))
        random.shuffle(paths)

        # vertices in the direction from current vertex
        up = (vertex[0],vertex[1]-1)
        down = (vertex[0],vertex[1]+1)
        left = (vertex[0]-1,vertex[1])
        right = (vertex[0]+1,vertex[1])

        for direction in paths:
                if direction == 0:
                        if up in vertices and up not in completed:
                                # add the edges
                                grid.add_edge((vertex,up))
                                grid.add_edge((up,vertex))
                                completed.append(up)
                                create_maze(grid, up, completed, vertices)
                elif direction == 1:
                        if down in vertices and down not in completed:
                                grid.add_edge((vertex,down))
                                grid.add_edge((down,vertex))
                                completed.append(down)
                                create_maze(grid, down, completed, vertices)
                elif direction == 2:
                        if left in vertices and left not in completed:
                                grid.add_edge((vertex,left))
                                grid.add_edge((left,vertex))
                                completed.append(left)
                                create_maze(grid, left, completed, vertices)
                elif direction == 3:
                        if right in vertices and right not in completed:
                                grid.add_edge((vertex,right))
                                grid.add_edge((right,vertex))
                                completed.append(right)
                                create_maze(grid, right, completed, vertices)

        return grid


# draw maze function
# takes in a (size)x(size) maze and prints a "colour" path
# side_length is the length of the grid unit and border_width is its border thickness
def draw_maze(screen, maze, size, colour, side_length, border_width):
        # for every vertex in the maze:
        for i in range(size):
                for j in range(size):
                        # if the vertex is not at the left-most side of the map
                        if (i != 0):
                                # check if the grid unit to the current unit's left is connected by an edge
                                if maze.is_edge(((i,j),(i-1,j))):
                                        # if connected, draw the grid unit without the left wall
                                        pygame.draw.rect(screen,colour,[(side_length+border_width)*i, border_width+(side_length+border_width)*j,\
                                                                         side_length+border_width, side_length])
                        # if the vertex is not at the right-most side of the map
                        if (i != size-1):
                                if maze.is_edge(((i,j),(i+1,j))):
                                        # draw the grid unit without the right wall (extend by border_width)
                                        pygame.draw.rect(screen,colour,[border_width+(side_length+border_width)*i,\
                                                                         border_width+(side_length+border_width)*j, side_length+border_width, side_length])
                        # if the vertex is not at the top-most side of the map
                        if (j != 0):
                                if maze.is_edge(((i,j),(i,j-1))):
                                        pygame.draw.rect(screen,colour,[border_width+(side_length+border_width)*i,\
                                                                         (side_length+border_width)*j, side_length, side_length+border_width])
                        # if the vertex is not at the bottom-most side of the map
                        if (j != size-1):
                                if maze.is_edge(((i,j),(i,j+1))):
                                        pygame.draw.rect(screen,colour,[border_width+(side_length+border_width)*i,\
                                                                         border_width+(side_length+border_width)*j, side_length, side_length+border_width])

# draw position of grid unit
def draw_position(screen, side_length, border_width, current_point, colour):
        pygame.draw.rect(screen, colour, [border_width+(side_length+border_width)*current_point[0],\
                                         border_width+(side_length+border_width)*current_point[1], side_length, side_length])

# run the maze game
# takes in a game mode parameter along with grid size and side length for the maze
def runGame(grid_size, side_length, mode):
        # initialize the game engine
        pygame.init()

        # Defining colours (RGB) ...
        BLACK = (0,0,0)
        GRAY = (100,100,100)
        WHITE = (255,255,255)
        GOLD = (249,166,2)
        GREEN = (0,255,0)
        RED = (255,0,0)
        BLUE = (0,0,255)

        # set the grid size and side length of each grid
        # grid_size = 20 # this is the maximum size before reaching recursion limit on maze buidling function
        # side_length = 10

        # scale the border width with respect to the given side length
        border_width = side_length//5

        # initialize the grid for the maze
        grid = create_grid(grid_size)
        # create the maze using the grid
        maze = create_maze(grid, (grid_size//2,grid_size//2)) # use the starting vertex to be middle of the map

        # Opening a window ...
        # set the screen size to match the grid
        size = (grid_size*(side_length+border_width)+border_width,\
                        grid_size*(side_length+border_width)+border_width)

        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("\"Esc\" to exit")

        # set the continue flag
        carryOn = True

        # set the clock (how fast the screen updates)
        clock = pygame.time.Clock()

        # have a black background
        screen.fill(BLACK)

        # get all of the vertices in the maze
        vertices = maze.get_vertices()

        # draw the maze
        draw_maze(screen, maze, grid_size, WHITE, side_length, border_width)

        # initialize starting point of character and potential character 2
        start_point = (0,0)
        # opposing corner
        start_point2 = (grid_size-1,grid_size-1)

        # set end-point for the maze
        end_point = (grid_size-1,grid_size-1)

        # randomize a start and end point
        choice = random.randrange(4)

        if choice == 0:
                start_point = (grid_size-1,grid_size-1)
                start_point2 = (0,0)
                end_point = (0,0)
                end_point2 = (grid_size-1,grid_size-1)

        # initialize winner variable
        winner = 0

        # initialize the character
        player1 = Character(screen, side_length, border_width, vertices,\
                                                start_point, end_point, start_point, GREEN, WHITE)

        # draw the end-point
        draw_position(screen, side_length, border_width, end_point, RED)

        # update the screen
        pygame.display.flip()

        # set cooldown for key presses
        cooldown = 100

        # initialize the cooldown timer
        start_timer = pygame.time.get_ticks()

        # initialize game timer for solo mode
        game_timer = 0
        # if solo mode is selected, start game timer
        if mode == 0:
                game_timer = time.time()

        # main loop
        while carryOn:
                # action (close screen)
                for event in pygame.event.get():# user did something
                        if event.type == pygame.QUIT:
                                carryOn = False
                                # mode = -1 means just exit
                                mode = -1
                        elif event.type == pygame.KEYDOWN:
                                #Pressing the Esc Key will quit the game
                                if event.key == pygame.K_ESCAPE:
                                        carryOn = False
                                        mode = -1

                # get the pressed keys
                keys = pygame.key.get_pressed()
                
                if (pygame.time.get_ticks() - start_timer > cooldown):
                        # get the current point of character
                        current_point = player1.get_current_position()
                        # move character right
                        if keys[pygame.K_RIGHT]:
                                # check if the next point is in the maze
                                if (current_point[0]+1,current_point[1]) in vertices:
                                        next_point = (current_point[0]+1,current_point[1])
                                        # check if the next point is connected by an edge
                                        if (maze.is_edge((current_point,next_point))):
                                                player1.move_character_smooth(next_point,5)
                                # restart cooldown timer
                                start_timer = pygame.time.get_ticks()
                        # move character left
                        elif keys[pygame.K_LEFT]:
                                if (current_point[0]-1,current_point[1]) in vertices:
                                        next_point = (current_point[0]-1, current_point[1])
                                        if (maze.is_edge((current_point,next_point))):
                                                player1.move_character_smooth(next_point,5)
                                # restart cooldown timer
                                start_timer = pygame.time.get_ticks()
                        # move character up
                        elif keys[pygame.K_UP]:
                                if (current_point[0],current_point[1]-1) in vertices:
                                        next_point = (current_point[0], current_point[1]-1)
                                        if (maze.is_edge((current_point,next_point))):
                                                player1.move_character_smooth(next_point,5)
                                # restart cooldown timer
                                start_timer = pygame.time.get_ticks()
                        # move character down
                        elif keys[pygame.K_DOWN]:
                                if (current_point[0],current_point[1]+1) in vertices:
                                        next_point = (current_point[0], current_point[1]+1)
                                        if (maze.is_edge((current_point,next_point))):
                                                player1.move_character_smooth(next_point,5)
                                # restart cooldown timer
                                start_timer = pygame.time.get_ticks()

                # win conditions for the different modes
                if mode == 0:
                        if player1.reached_goal():
                                carryOn = False

                # limit to 60 frames per second (fps)
                clock.tick(60)

        # stop the game engine once exited the game
        pygame.quit()

        # solo mode
        if mode == 0:
                timer = int(time.time() - game_timer)
                return mode, timer
        # other modes
        else:
                return mode, winner

# main function
if __name__ == "__main__":

        # set the window display position
        set_window_position(50,50)

        # initialize states
        states = {0:"Main Menu", 1:"Gameplay"}
        current_state = states[0]

        # initialize variables
        grid_size = 0
        side_length = 0
        mode = 0

        # flag for main loop
        Run = True

        while Run:
                if current_state == states[0]:
                        Run, grid_size, side_length, mode = ui_file.startScreen()
                        current_state = states[1]
                elif current_state == states[1]:
                        mode, value = runGame(grid_size, side_length, mode)
                        if mode != -1:
                                ui_file.endGame(mode, value)

                        current_state = states[0]

        quit()