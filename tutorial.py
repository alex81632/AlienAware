import pygame as pg
import math
import time
import os

class Tutorial:
    def __init__(self, screen, constants):
        self.screen = screen
        self.constants = constants
        # importe o arquivo de imagem saveOverlay.png da pasta assets/overlays
        self.tutorial = pg.image.load('assets/overlays/tutorial.png')
        # redimensione a imagem para o tamanho da tela
        self.tutorial = pg.transform.scale(self.tutorial, (self.constants.width, self.constants.height))


    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.constants.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    self.constants.state = 1
        
    def draw(self):
        # fundo preto
        self.screen.fill((0,0,0))
        
        self.screen.blit(self.tutorial, (0, 0))