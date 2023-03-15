import pygame as pg
from constants import Constants

class HUD:
    def __init__(self, screen, constants):
        self.screen = screen
        self.constants = constants
        self.logo = pg.image.load('assets/images/logo_simplificada.png')
        scale = 50*self.constants.pixel
        self.logo = pg.transform.scale(self.logo, (scale, scale))

    def draw(self):
        # desenhar a logo na tela
        self.screen.blit(self.logo, (self.constants.padding, self.constants.padding))

