import random
import pygame as pg

from constants import *

class Tile:    
    def __init__(self, map, x, y):
        self.x = x
        self.y = y
        
        self.map = map
        self.game = map.game
        
        self.set = False
        self.neighbours = []
        
        # top, right, bottom, left
        self.walls = [True, True, True, True] 
        
    def checkNeighbours(self):
        if self.x >= 1:
            self.left = self.map.grid[self.x - 1][self.y]
            if not self.left.set:
                self.neighbours.append(self.left)
        if self.x < DIMENSION[0] - 1:
            self.right = self.map.grid[self.x + 1][self.y]
            if not self.right.set:
                self.neighbours.append(self.right)
        if self.y >= 1:
            self.top = self.map.grid[self.x][self.y - 1]
            if not self.top.set:
                self.neighbours.append(self.top)
        if self.y < DIMENSION[1] - 1:
            self.bottom = self.map.grid[self.x][self.y + 1]
            if not self.bottom.set:
                self.neighbours.append(self.bottom)
                
        if len(self.neighbours) > 0:
            self.next_cell = self.neighbours[random.randrange(len(self.neighbours))]
            return self.next_cell
        else:
            return False
        
    def draw(self): 
        xcoord = self.x * TILE_SIDE
        ycoord = self.y * TILE_SIDE
        pg.draw.rect(self.game.screen, BLACK, (xcoord, 
                        ycoord, TILE_SIDE, TILE_SIDE))
        if self.walls[0]:
            pg.draw.line(self.game.screen, WHITE, (xcoord, ycoord), (xcoord + TILE_SIDE, ycoord))
        if self.walls[1]:
            pg.draw.line(self.game.screen, WHITE, (xcoord + TILE_SIDE, ycoord), (xcoord + TILE_SIDE, ycoord + TILE_SIDE))
        if self.walls[2]:
            pg.draw.line(self.game.screen, WHITE, (xcoord, ycoord + TILE_SIDE), (xcoord + TILE_SIDE, ycoord + TILE_SIDE))
        if self.walls[3]:
            pg.draw.line(self.game.screen, WHITE, (xcoord, ycoord), (xcoord, ycoord + TILE_SIDE))
        
        