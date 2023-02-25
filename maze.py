import numpy as np
from tile import *

from constants import *

class Maze:
    def __init__(self, game):
        self.game = game
        self.minimap = MINIMAP
        self.world_map = np.ndarray(DIMENSION, Tile)
        self.generate()
        
    def generate(self):
        for j, row in enumerate(self.minimap):
            for i, value in enumerate(row):
                if value: self.world_map[j][i] = Tile(self.game, value, (j, i))
            