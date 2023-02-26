import pygame as pg 

from constants import *

class Player():
    def __init__(self, game):
        self.playerImage = pg.image.load(PLAYER_IMAGE)
        self.x = 0
        self.y = 0
        self.game = game
        
    def move(self, dir):
        tile = self.game.map.grid[self.x][self.y]
        match dir:
            case 0: # UP
                if self.y > 0 and not tile.walls[UP]:
                    self.y -= 1
                return
            case 1: # RIGHT
                if self.x < DIMENSION[0] and not tile.walls[RIGHT]:
                    self.x += 1
                return
            case 2: # DOWN
                if self.y < DIMENSION[1] and not tile.walls[DOWN]:
                    self.y += 1
                return
            case 3: # LEFT
                if self.x > 0 and not tile.walls[LEFT]:
                    self.x -= 1
                return
            
    def draw(self):
        self.game.screen.blit(self.playerImage, (self.x * TILE_SIDE + 2, self.y * TILE_SIDE + 2))