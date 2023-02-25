import pygame as pg
import sys
from pygame.locals import *

import maze
import tile

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
        self.new_game()
        
    def new_game(self):
        self.map = maze.Maze(self)
     
    def check_events(self):
        self.global_trigger = False
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            # elif event.type == self.global_event:
            #     self.global_trigger = True
            # self.player.single_fire_event(event)
    
    def update(self):
        pass
    
    def draw(self):
        pass
        
    def run(self):
        try :
            while True:
                self.check_events()
                self.update()
                self.draw()
        except SystemError:
            pg.quit()
            sys.exit()

            
if __name__ == "__main__":
    game = Game()
    game.run()