import pygame as pg

from constants import *

SIDE = 20

class Tile:    
    def __init__(self, game, x, y):
        self.x = x * SIDE
        self.y = y * SIDE
        
        self.game = game
        
        # top, right, bottom, left
        self.walls = [True, True, True, True] 
        
        
    def draw(self): 
        pg.draw.rect(self.game.screen, WHITE, (self.x * SIDE, 
                        self.y * SIDE, SIDE, SIDE), 2)
        if self.walls[0]:
            pg.draw.line(self.game.screen, BLACK, (self.x, self.y), (self.x + SIDE, self.y))
        if self.walls[1]:
            pg.draw.line(self.game.screen, BLACK, (self.x + SIDE, self.y), (self.x + SIDE, self.y + SIDE))
        if self.walls[2]:
            pg.draw.line(self.game.screen, BLACK, (self.x, self.y + SIDE), (self.x + SIDE, self.y + SIDE))
        if self.walls[3]:
            pg.draw.line(self.game.screen, BLACK, (self.x, self.y), (self.x, self.y + SIDE))
        
        