import pygame as pg
import random

class Goal:
    def __init__(self, block_size, grid_size):
        self.x = 0
        self.y = 0
        self.blocksize = block_size
        self.grid_size = grid_size
        self.COLOUR = (0, 255, 0)

    # here we generate a random goal position
    def makeRandomPosition(self):
        self.x = random.randint(0, self.grid_size-1) * self.blocksize
        self.y = random.randint(0, self.grid_size-1) * self.blocksize

    def drawGoal(self, screen):
        pg.draw.rect(
            screen, self.COLOUR, (self.x, self.y, self.blocksize, self.blocksize)
        )

    def hasMoved(self, value):
        if self.x != value[0] or self.y != value[1]:
            self.x = value[0]
            self.y = value[1]
            self.getPositon()

    def getPosition(self):
        return (self.x, self.y)