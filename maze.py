import numpy as np
from tile import *

from constants import *

class Maze:
    def __init__(self, game):
        self.game = game
        self.minimap = MINIMAP
        self.grid = np.ndarray(shape=DIMENSION, dtype=Tile)
        self.generate()
        
    def generate(self):
        for i, row in enumerate(self.minimap):
            for j, value in enumerate(row):
                if value: self.grid[j][i] = Tile(self.game, j, i)
    
    def draw(self):
        for row in self.grid:
            for tile in row:
                if tile != None: tile.draw()