import pygame as pg
import sys
from constants import Constants

class Pause:
    def __init__(self, screen, constants):
        self.screen = screen
        self.constants = constants
        self.selected = 0
        self.num_options = 2
        self.first = True

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.constants.running = False
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                self.first = True
                self.constants.state = 1
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_DOWN:
                    self.selected += 1
                    self.selected %= self.num_options
                if event.key == pg.K_UP:
                    self.selected -= 1
                    self.selected %= self.num_options
                if event.key == pg.K_RETURN:
                    if self.selected == 0:
                        self.first = True
                        self.constants.state = 1
                    elif self.selected == 1:
                        self.first = True
                        self.constants.state = 0
    
    def update(self):
        pass
        
    def draw(self):
        if self.first:
            self.first = False
            # importe o arquivo de imagem pauseOverlay.png da pasta assets/overlays
            pauseOverlay = pg.image.load('assets/overlays/pauseOverlay.png')
            # redimensione a imagem para o tamanho da tela
            pauseOverlay = pg.transform.scale(pauseOverlay, (self.constants.width, self.constants.height))
            # desenhe a imagem na tela
            self.screen.blit(pauseOverlay, (0, 0))
        font = pg.font.Font('assets/fonts/dogicapixel.ttf', self.constants.font_size)
        if self.selected == 0:
            text = font.render("Resume", 1, (255,0,0))
        else:
            text = font.render("Resume", 1, (255,255,255))
        self.screen.blit(text, (self.constants.half_width - text.get_width()//2, self.constants.half_height - text.get_height()//2 ))
        if self.selected == 1:
            text = font.render("Quit", 1, (255,0,0))
        else:
            text = font.render("Quit", 1, (255,255,255))
        self.screen.blit(text, (self.constants.half_width - text.get_width()//2, self.constants.half_height - text.get_height()//2 + self.constants.padding*2))
        if self.constants.state != 2:
            self.first = True