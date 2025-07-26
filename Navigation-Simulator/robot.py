import pygame as pg
import random

class Robot:
    def __init__(self, block_size, grid_size):
        self.x = 0
        self.y = 0
        self.blocksize = block_size
        self.grid_size = grid_size
        self.COLOUR = (255, 0, 0)

    def makeRandomPosition(self):
        self.x = random.randint(0, self.grid_size-1) * self.blocksize
        self.y = random.randint(0, self.grid_size-1) * self.blocksize

    def drawRobot(self, screen):
        pg.draw.rect(
            screen, self.COLOUR, (self.x, self.y, self.blocksize, self.blocksize)
        )

    def getPosition(self):
        return (self.x, self.y)

    def move_robot(self, value):
        if value == 1:  # move right
            self.x += self.blocksize
        elif value == 2:  # move left
            self.x -= self.blocksize
        elif value == 3:  # move down
            self.y += self.blocksize
        elif value == 4:  # move up
            self.y -= self.blocksize
