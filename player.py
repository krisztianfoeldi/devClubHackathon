import pygame as pg 

class Player():
    def __init__(self, game):
        self.playerImage = pg.image.load('Images\player_image.png')
        self.playerX = 50
        self.playerY = 200
        self.game = game
        
    def draw(self):
        self.game.screen.blit(self.playerImage, (self.playerX, self.playerY))