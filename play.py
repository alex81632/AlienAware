import pygame as pg
from hud import HUD
from player import Player
from gameMap import GameMap
from objectRender import ObjectRender
from rayCasting import RayCasting

class Play:
    def __init__(self, screen, constants):
        self.screen = screen
        self.constants = constants
        self.HUD = HUD(self.screen, self.constants)
        self.player = Player(self)
        self.gameMap = GameMap(self)
        self.objectRender = ObjectRender(self)
        self.raycasting = RayCasting(self)

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.constants.running = False
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                self.constants.state = 2

    def update(self):
        self.player.update()
        self.raycasting.update()
        pg.display.flip()

    def draw(self):
        self.objectRender.draw()
        self.HUD.draw()        