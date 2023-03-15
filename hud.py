import pygame as pg
from constants import Constants

class HUD:
    def __init__(self, screen, constants):
        self.screen = screen
        self.constants = constants

    def draw(self):
        # circulo com a logo
        # importar a logo_simplificada de imagens
        logo = pg.image.load('assets/images/logo_simplificada.png')
        # redimensionar a logo para 30 px
        scale = 30*self.constants.pixel
        logo = pg.transform.scale(logo, (scale, scale))

