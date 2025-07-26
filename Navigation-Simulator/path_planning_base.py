import math
import pygame as pg
import robot 
import goal

class PathPlanning:
    def __init__(self, robot: robot.Robot, goal: goal.Goal, block_size, grid_size):

        self.robot = robot
        self.goal = goal
        self.blocksize = block_size
        self.path = []
        self.grid_size = grid_size

    def getNeighbors(self, robot_position, list_of_obstacles=[]):

        x = robot_position[0]
        y = robot_position[1]
        potential_neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

        # now we need to see if each neighbor is a acceptable (not hitting a wall etc)
        # if any of the tuples have a value below or above the limit, we discard them (out of bounds)
        limit_x = (0, self.grid_size -1)
        limit_y = (0, self.grid_size -1)

        valid_neighbors = []
        
        grid_obstacles = [(ox // self.block_size, oy // self.block_size) for ox, oy in list_of_obstacles]

        for nx, ny in potential_neighbors:
            if nx > limit_x[1] or nx < limit_x[0]:
                continue
            if ny > limit_y[1] or ny < limit_y[0]:
                continue
            if (nx, ny) in grid_obstacles:
                continue
            else:
                valid_neighbors.append((nx, ny))
            

        return valid_neighbors
        
    def plan_path(self):
        pass

    def draw_path(self, screen):
        path = self.path

        for x, y in path:
            # Create a semi-transparent surface for each block
            overlay = pg.Surface((self.blocksize, self.blocksize), pg.SRCALPHA)
            overlay.fill(
                (50, 50, 50, 50)
            )  # RGBA — A=100 for transparency (0=fully transparent, 255=opaque)

            # Blit the transparent block onto the screen
            screen.blit(overlay, (x * self.blocksize, y * self.blocksize))
