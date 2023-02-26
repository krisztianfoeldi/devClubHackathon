import pygame as pg
from pygame.locals import *

from constants import *
import player

class Enemy():
    def __init__(self,game):
        self.enemyImage = pg.image.load(ENEMY)
        self.enemyX = 15
        self.enemyY = 15
        self.game = game

    def enemyMove(self, dirE):
        tile = self.game.map.grid[self.enemyX][self.enemyY]
        match dirE:
            case 0: # UP
                if self.enemyY > 0 and not tile.walls[UP]:
                    self.enemyY -= 1
                return
            case 1: # RIGHT
                if self.enemyX < DIMENSION[0] and not tile.walls[RIGHT]:
                    self.enemyX += 1
                return
            case 2: # DOWN
                if self.enemyY < DIMENSION[1] and not tile.walls[DOWN]:
                    self.enemyY += 1
                return
            case 3: # LEFT
                if self.enemyX > 0 and not tile.walls[LEFT]:
                    self.enemyX -= 1
                return
            
    def draw(self):
        self.game.screen.blit(self.enemyImage,(self.enemyX * TILE_SIDE + 2, self.enemyY * TILE_SIDE + 2))
    