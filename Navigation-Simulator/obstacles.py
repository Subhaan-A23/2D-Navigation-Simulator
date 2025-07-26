import pygame as pg
from random import randint

class Obstacles():
    def __init__(self, block_size, grid_size, num_obstacles):
        self.block_size = block_size
        self.grid_size = grid_size
        self.num_obstacles = num_obstacles
        self.list_of_obstacles = []
        
    def compute_obstacle_positions(self, robot_position, goal_position):
        self.list_of_obstacles = []

        while len(self.list_of_obstacles) < self.num_obstacles:
            obstacle_x = randint(0, self.grid_size - 1) * self.block_size
            obstacle_y = randint(0, self.grid_size - 1) * self.block_size
            pos = (obstacle_x, obstacle_y)

            # Avoid placing on robot or goal or duplicate obstacle
            if pos != robot_position and pos != goal_position and pos not in self.list_of_obstacles:
                self.list_of_obstacles.append(pos)

            

            
            
        
