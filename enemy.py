import pygame as pg
from pygame.locals import *

from constants import *

class Enemy():
    def __init__(self,game):
        self.enemyImage = pg.image.load(ENEMY)
        self.enemyX = 50
        self.enemyY = 200
        self.game = game

    def draw(self):
        self.game.screen.blit(self.enemyImage,(self.enemyX,self.enemyY))