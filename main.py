import pygame as pg
import sys
from pygame.locals import *

import maze
import tile
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
        self.characterPlayer = player.Player(self)
     
    def check_events(self):
        self.global_trigger = False
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                self.map.generate()
            elif event.type == self.global_event:
                self.global_trigger = True
            # self.player.single_fire_event(event)
    
    def update(self):
        pg.display.update()
    
    def draw(self):
        self.map.draw()
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