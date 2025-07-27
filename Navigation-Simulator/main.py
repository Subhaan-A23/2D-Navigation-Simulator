import pygame as pg
import numpy as np
import random
import math
import utility
import robot
import goal
import DFS_path_planning
import BFS_path_planning
import controller
import obstacles

#What are the things we want to control 
# -number of blocks (minimum length 5 -> 50)
# -window size
# -speed of controller

#initialise window size and block size
WINDOW_SIZE = (800, 800)
grid_size = 20
block_size = int(WINDOW_SIZE[0] / grid_size)

#specify controller speed (how quickly the robot moves)
controller_speed = 100 #in ms

pg.display.set_caption(f"Navigation Simulator - Grid Size: {grid_size}x{grid_size}")

screen = pg.display.set_mode(WINDOW_SIZE)

CLOCK = pg.time.Clock()

move_step = block_size

# make a goal and a robot
goal_point = goal.Goal(block_size, grid_size)
driver = robot.Robot(block_size, grid_size)
obstacles_list = obstacles.Obstacles(block_size, grid_size, 30)
obstacles_list.compute_obstacle_positions(driver.getPosition, goal_point.getPosition)


# place both of them in random areas
goal_point.makeRandomPosition()
driver.makeRandomPosition()

g = goal_point.getPosition()
d = driver.getPosition()

# then compute the path plan using dfs
BFS = BFS_path_planning.BFS(driver, goal_point, block_size, grid_size)
BFS.plan_path(obstacles_list.list_of_obstacles)

path = BFS.path
print(f"path is {path}")

robot_controller = controller.controller(driver, BFS)
robot_controller.compute_control_values()
robot_controller.moveRobot(screen, utility.grid_colour, block_size, goal_point, WINDOW_SIZE, obstacles_list.list_of_obstacles)

running = True
while running:
    #draw screen 
    screen.fill(utility.background_colour)
    #then draw grid, robot and goal
    utility.drawScene(screen, utility.grid_colour, block_size, driver, goal_point, WINDOW_SIZE)
    
    pg.display.flip()
    
    for event in pg.event.get():  # Here we get a list of events that were made
        if event.type == pg.QUIT:
            running = False
            
    # if robot hits goal then start again at random positions
    if driver.x == goal_point.x and driver.y == goal_point.y:
        print("goal hit")
        driver.makeRandomPosition()
        goal_point.makeRandomPosition()
        obstacles_list.compute_obstacle_positions(driver.getPosition(), goal_point.getPosition())
        BFS = BFS_path_planning.BFS(driver, goal_point, block_size, grid_size)
        BFS.plan_path(obstacles_list.list_of_obstacles)
        robot_controller = controller.controller(driver, BFS)
        robot_controller.compute_control_values()
        robot_controller.moveRobot(screen, utility.grid_colour, block_size, goal_point, WINDOW_SIZE, obstacles_list.list_of_obstacles)


#improvements:
#   -allow user to change speed of robot movement
#   -provide navigation time to user 
