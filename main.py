import pygame as pg
import sys
from pygame.locals import *

import maze
import enemy
import player

from constants import *

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.dt = 1
        self.global_trigger = False
        self.global_event = pg.USEREVENT
        pg.time.set_timer(self.global_event, 40)

        #game title and icon
        pg.display.set_caption("aMazing")
        gameIcon = pg.image.load(ICON)
        pg.display.set_icon(gameIcon)

        self.new_game()
        
    def new_game(self):
        self.map = maze.Maze(self)
        self.characterEnemy = enemy.Enemy(self)
        self.characterPlayer = player.Player(self)
     
    def check_events(self):
        self.global_trigger = False
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.map.generate()
                elif event.key == pg.K_UP:
                    self.characterPlayer.move(UP)
                elif event.key == pg.K_RIGHT:
                    self.characterPlayer.move(RIGHT)
                elif event.key == pg.K_DOWN:
                    self.characterPlayer.move(DOWN)
                elif event.key == pg.K_LEFT:
                    self.characterPlayer.move(LEFT)

                elif event.key == pg.K_w:
                    self.characterEnemy.enemyMove(UP)
                elif event.key == pg.K_d:
                    self.characterEnemy.enemyMove(RIGHT)
                elif event.key == pg.K_s:
                    self.characterEnemy.enemyMove(DOWN)
                elif event.key == pg.K_a:
                    self.characterEnemy.enemyMove(LEFT)

            elif event.type == self.global_event:
                self.global_trigger = True
    
    def update(self):
        pg.display.update()
    
    def draw(self):
        self.map.draw()
        self.characterEnemy.draw()
        self.characterPlayer.draw()

        pg.display.flip()
        
    def run(self):
        try :
            while True:
                self.check_events()
                self.update()
                self.draw()
        except SystemExit:
            pg.quit()
            sys.exit()

            
if __name__ == "__main__":
    game = Game()
    game.run()