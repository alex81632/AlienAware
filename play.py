import pygame as pg
import sys
from constants import Constants

class Play:
    def __init__(self, screen, constants):
        self.screen = screen
        self.constants = constants
        self.state = 1

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return False
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                self.state = 2
        return True

    def update(self):
        pg.display.flip()
        return self.state

    def draw(self):
        self.screen.fill((80,80,80))
        # draw point at center of screen
        pg.draw.circle(self.screen, 'white', (self.constants.half_width, self.constants.half_height), 3)

    