import pygame as pg
import sys
from constants import Constants
from hud import HUD

class Play:
    def __init__(self, screen, constants):
        self.screen = screen
        self.constants = constants
        self.HUD = HUD(self.screen, self.constants)

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.constants.running = False
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                self.constants.state = 2

    def update(self):
        pass

    def draw(self):
        self.screen.fill((80,80,80))
        # draw point at center of screen
        pg.draw.circle(self.screen, 'white', (self.constants.half_width, self.constants.half_height), 3)
        self.HUD.draw()    