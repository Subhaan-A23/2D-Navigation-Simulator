import pygame as pg
import robot
import utility
import path_planning_base
class controller:
    def __init__(self, robot: robot.Robot, path_planner: path_planning_base.PathPlanning):
        self.path_planner = path_planner
        self.control_values = []
        self.robot = robot
        self.path = path_planner.path

    def getPath(self, path):
        self.path = path

    def compute_control_values(self):
        for i in range(1, len(self.path)):
            prev = self.path[i - 1]
            curr = self.path[i]

            dx = curr[0] - prev[0]
            dy = curr[1] - prev[1]

            if dx == 1:
                self.control_values.append(1)  # right
            elif dx == -1:
                self.control_values.append(2)  # left
            elif dy == 1:
                self.control_values.append(3)  # down
            elif dy == -1:
                self.control_values.append(4)  # up

    def moveRobot(self, screen, grid_colour, block_size, goal_point, WINDOW_SIZE, obstacles_coords=[]):
        
        for i in self.control_values:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()

            self.robot.move_robot(i)

            # Draw updated state
            screen.fill(utility.background_colour)
            utility.drawScene(screen, grid_colour, block_size, self.robot, goal_point, WINDOW_SIZE)
            utility.drawObstacles(screen, obstacles_coords, block_size)
            #then draw path
            self.path_planner.draw_path(screen)
            pg.display.flip()

            pg.time.delay(200)  # Delay for visibility

