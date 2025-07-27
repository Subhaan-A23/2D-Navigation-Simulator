import pygame as pg
import goal
import robot
import path_planning_base


obstacle_colour = (10, 10, 10)

def drawGrid(screen, COLOUR, blocksize=20, window_size=(500, 500)):
    for x in range(0, window_size[0], blocksize):
        for y in range(0, window_size[0], blocksize):
            pg.draw.rect(screen, COLOUR, (x, y, blocksize, blocksize), 1)
            
            
def drawScene(screen, grid_colour, block_size, robot: robot.Robot, goal_point: goal.Goal, WINDOW_SIZE):
    
    drawGrid(screen, grid_colour, block_size, WINDOW_SIZE)
    
    robot.drawRobot(screen)
    goal_point.drawGoal(screen)
    
def drawObstacles(screen, obstacle_coords, block_size):
    for x, y in obstacle_coords:
        pg.draw.rect(screen, (0,0,0), (x, y, block_size, block_size))
    
background_colour = (255, 255, 255) 
grid_colour = (0, 0, 0)

