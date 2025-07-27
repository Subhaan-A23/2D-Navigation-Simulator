import path_planning_base
import goal
import robot

class Djikstra(path_planning_base.PathPlanning):
    def __init__(self, robot: robot.Robot, goal: goal.Goal, block_size, grid_size):
        super().__init__(robot, goal, block_size, grid_size)
        
    