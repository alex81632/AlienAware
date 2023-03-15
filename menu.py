import pygame as pg
import sys
from constants import Constants

class Menu:
    def __init__(self, screen, constants):
        self.screen = screen
        self.constants = constants
        self.selected = 0
        self.num_options = 3

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.constants.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_DOWN:
                    self.selected += 1
                    self.selected %= self.num_options
                if event.key == pg.K_UP:
                    self.selected -= 1
                    self.selected %= self.num_options
                if event.key == pg.K_RETURN:
                    if self.selected == 0:
                        self.constants.state = 1
                    elif self.selected == 2:
                        self.constants.running = False
    
    def update(self):
        pass
        
    def draw(self):
        # importar a logo do jogo
        logo = pg.image.load('assets/overlays/logoMenu.png')
        # redimensionar a logo para o tamanho da tela
        logo = pg.transform.scale(logo, (self.constants.width, self.constants.height))
        # desenhar a logo na tela
        self.screen.blit(logo, (0,0))
        font = pg.font.Font('assets/fonts/dogicapixel.ttf', self.constants.font_size)
        if self.selected == 0:
            text = font.render("Start", 1, (255,0,0))
        else:
            text = font.render("Start", 1, (255,255,255))
        self.screen.blit(text, (self.constants.width - text.get_width() - self.constants.padding, self.constants.half_height - text.get_height()//2 - self.constants.padding*2))
        if self.selected == 1:
            text = font.render("Settings", 1, (255,0,0))
        else:
            text = font.render("Settings", 1, (255,255,255))
        self.screen.blit(text, (self.constants.width - text.get_width() - self.constants.padding, self.constants.half_height - text.get_height()//2))
        if self.selected == 2:
            text = font.render("Quit", 1, (255,0,0))
        else:
            text = font.render("Quit", 1, (255,255,255))
        self.screen.blit(text, (self.constants.width - text.get_width() - self.constants.padding, self.constants.half_height - text.get_height()//2 + self.constants.padding*2))