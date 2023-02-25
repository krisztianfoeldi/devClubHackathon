import numpy as np
from tile import *

from constants import *

class Maze:
    def __init__(self, game):
        self.game = game
        self.grid = np.ndarray(shape=DIMENSION, dtype=Tile)
        self.generate()
        
    def generate(self):
        for j in range(DIMENSION[1]):
            for i in range(DIMENSION[0]):
                self.grid[i][j] = Tile(self, i, j)
        
        done = False
        cur_cell = self.grid[0][0]
        stack = []
        
        while not done:
            cur_cell.set = True
            
            next_cell = cur_cell.checkNeighbours()
            
            if next_cell != False:
                cur_cell.neighbours = []
                stack.append(cur_cell)
                self.setWalls(cur_cell, next_cell)
                cur_cell = next_cell
                
            elif len(stack) == 0:
                done = True
                
            else:
                cur_cell = stack.pop()
    
    def setWalls(self, cur_cell, next_cell):
        x = cur_cell.x - next_cell.x
        y = cur_cell.y - next_cell.y
        if x == -1:
            cur_cell.walls[1] = next_cell.walls[3] = False
        elif x == 1: 
            cur_cell.walls[3] = next_cell.walls[1] = False
        elif y == -1: 
            cur_cell.walls[2] = next_cell.walls[0] = False
        elif y == 1: 
            cur_cell.walls[0] = next_cell.walls[2] = False            
    
    def draw(self):
        for row in self.grid:
            for tile in row:
                tile.draw()
        