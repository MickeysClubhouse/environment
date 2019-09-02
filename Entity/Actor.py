from constant import *


class Actor:
    x = -1
    y = -1
    direction = 0  # 0=down 1=up 2=left 3=right
    carriage = 0  # 0=nothing 1=apple 2=banana

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_playground(self, playground):
        self.playground = playground

    def move(self, key_input):
        if key_input == "w":
            self.direction = 1
            if self.x - 1 >= 0 and self.playground.get(self.x - 1, self.y) == CELL_EMPTY:
                self.x -= 1
        if key_input == "s":
            self.direction = 0
            if self.x + 1 < PLAYGROUND_HEIGHT and self.playground.get(self.x + 1, self.y) == CELL_EMPTY:
                self.x += 1
        if key_input == "a":
            self.direction = 2
            if self.y - 1 >= 0 and self.playground.get(self.x, self.y - 1) == CELL_EMPTY:
                self.y -= 1
        if key_input == "d":
            self.direction = 3
            if self.y + 1 < PLAYGROUND_WIDTH and self.playground.get(self.x, self.y + 1) == CELL_EMPTY:
                self.y += 1

        self.playground.update()

    def take(self):
        # the actor pick up something from storage or ground
        if self.carriage == 0:
            if self.direction == 0:
                if self.playground.get(self.x + 1, self.y) == CELL_APPLE_STORAGE_CLOSE:
                    self.carriage = CELL_APPLE
                elif self.playground.get(self.x + 1, self.y) == CELL_APPLE:
                    self.carriage = CELL_APPLE
                    self.playground.remove(self.x + 1, self.y)
            if self.direction == 1:
                if self.playground.get(self.x - 1, self.y) == CELL_APPLE_STORAGE_CLOSE:
                    self.carriage = CELL_APPLE
                elif self.playground.get(self.x - 1, self.y) == CELL_APPLE:
                    self.carriage = CELL_APPLE
                    self.playground.remove(self.x - 1, self.y)
            if self.direction == 2:
                if self.playground.get(self.x, self.y - 1) == CELL_APPLE_STORAGE_CLOSE:
                    self.carriage = CELL_APPLE
                elif self.playground.get(self.x, self.y - 1) == CELL_APPLE:
                    self.carriage = CELL_APPLE
                    self.playground.remove(self.x, self.y - 1)
            if self.direction == 3:
                if self.playground.get(self.x, self.y + 1) == CELL_APPLE_STORAGE_CLOSE:
                    self.carriage = CELL_APPLE
                elif self.playground.get(self.x, self.y + 1) == CELL_APPLE:
                    self.carriage = CELL_APPLE
                    self.playground.remove(self.x, self.y + 1)

    def drop(self):
        # the actor drop carriage to the ground
        if self.carriage != 0:
            if self.direction == 0 and self.x + 1 < self.playground.dimension_x:
                if self.playground.get(self.x + 1, self.y) == CELL_EMPTY:
                    self.playground.add(CELL_APPLE, self.x + 1, self.y)
                    self.carriage = 0
            if self.direction == 1 and self.x - 1 >= 0:
                if self.playground.get(self.x - 1, self.y) == CELL_EMPTY:
                    self.playground.add(CELL_APPLE, self.x - 1, self.y)
                    self.carriage = 0
            if self.direction == 2 and self.y - 1 >= 0:
                if self.playground.get(self.x, self.y - 1) == CELL_EMPTY:
                    self.playground.add(CELL_APPLE, self.x, self.y - 1)
                    self.carriage = 0
            if self.direction == 3 and self.y + 1 < self.playground.dimension_y:
                if self.playground.get(self.x, self.y + 1) == CELL_EMPTY:
                    self.playground.add(CELL_APPLE, self.x, self.y + 1)
                    self.carriage = 0
