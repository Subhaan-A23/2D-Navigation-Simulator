import path_planning_base
import goal
import robot

class DFS(path_planning_base.PathPlanning):
    def __init__(self, robot: robot.Robot, goal: goal.Goal, block_size, grid_size):
        super().__init__(robot, goal, block_size, grid_size)

    def plan_path(self):
        start = (self.robot.x // self.blocksize, self.robot.y // self.blocksize)
        goal = (self.goal.x // self.blocksize, self.goal.y // self.blocksize)
        came_from = {}
        open_list = [start]  # start the list with the start position
        visited = set()

        while open_list:
            current = open_list.pop()  # look at first term

            if current == goal:
                break

            for neighbor in self.getNeighbors(current):  # find all neighbors of current point
                if neighbor not in visited and neighbor not in open_list:
                    visited.add(neighbor)
                    came_from[neighbor] = current
                    open_list.append(neighbor)

        if goal not in came_from:
            return []

        current = goal
        while current != start:
            self.path.append(current)
            current = came_from[current]

        self.path.append(start)
        self.path.reverse()
