import pygame as pg

SIDE = 20

class Tile:    
    def __init__(self, game, isWall, coords):
        self.game = game
        self.isWall = isWall
        self.coords = coords
        
        
    def draw(self):
        color = 'black' if self.isWall else 'white'
        
        pg.draw.rect(self.game, color, (self.coords[0] * SIDE, 
                        self.coords[0] * SIDE, SIDE, SIDE), 2)
        