import numpy
from constant import *


class Playground:
    """
    class playground is a dimension_x* dimension_y grid
    mark the objects' position
    be shown by show() in trustGame.py
    """
    dimension_x = 0
    dimension_y = 0
    grid = numpy.zeros((1, 1), dtype=int)
    apples = []

    def __init__(self, dimension_x, dimension_y, principal, agent, storage):
        self.dimension_x = dimension_x
        self.dimension_y = dimension_y
        self.grid = numpy.zeros((dimension_x, dimension_y), dtype=int)
        # set P and A
        self.principal = principal
        self.agent = agent
        self.storage = storage
        self.update()

    def update(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                self.grid[i][j] = 0

        self.grid[self.principal.x][self.principal.y] = CELL_HUMAN
        self.grid[self.agent.x][self.agent.y] = CELL_AGENT
        self.grid[self.storage.x][self.storage.y] = CELL_APPLE_STORAGE_CLOSE
        for apple in self.apples:
            self.grid[apple[0], apple[1]] = CELL_APPLE

    def get(self, row, col):
        return self.grid[row][col]

    def add(self, object, row, col):
        # this part need to be altered when add other fruits
        self.apples.append([row, col])
        self.update()

    def remove(self, row, col):
        self.apples.remove([row, col])
        self.update()
