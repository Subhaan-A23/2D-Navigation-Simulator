import path_planning_base
import goal
import robot
from collections import deque

class BFS(path_planning_base.PathPlanning):
    def __init__(self, robot: robot.Robot, goal: goal.Goal, block_size, grid_size):
        super().__init__(robot, goal, block_size, grid_size)
        
    def plan_path(self, list_of_obstacles):
        start_x = self.robot.x // self.blocksize
        start_y = self.robot.y // self.blocksize
        start = (start_x, start_y)
        
        goal_position = (self.goal.x // self.blocksize, self.goal.y // self.blocksize)
        
        queue = deque()
        queue.append(start)
        visited = set()
        visited.add(start)
        parent = dict()
        
        #make a queue
        while queue:
            
            #remove the leftmost term in the queue and add it to visited
            current = queue.popleft()

            #check if the current value is the goal
            
            if current == goal_position:
                break #we found the goal yay! 
        
            #if we havent found the goal yet get the neighbors
            #if there are no neighbors,then the queue will finish
            neighbors = self.getNeighbors(current, list_of_obstacles) #gives you a list of nighbors
            
            #then look into the neighbors
            for i in neighbors:
                #add neighbors to queue if not in visited
                if i not in visited:
                    queue.append(i)
                    visited.add(i)
                    #then store child and parent
                    parent[i] = current #the neighbor is a child of the current node
             
        #if we have broken from the while loop we have found the goal position       
        node = goal_position
        #now reconstruct the path
        path = []
        
        while node != start: 
            if node not in parent:
                self.path = []
                return
            path.insert(0, node) #keep inserting nodes backwards
            node = parent[node] #go to parent of node then find its parent
        
        #if loop has broken, then we have gotten to the start
        path.insert(0, start)
        self.path = path
                    
        
                    
            

            
            
            
            