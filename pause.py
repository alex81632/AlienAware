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
        self.font = pg.font.Font('assets/fonts/dogicapixel.ttf', int(self.constants.font_size))
        self.font_description = pg.font.Font('assets/fonts/dogicapixel.ttf', int(self.constants.font_size/2))
        # importe o arquivo de imagem pauseOverlay.png da pasta assets/overlays
        self.pauseOverlay = pg.image.load('assets/overlays/pauseOverlay.png')
        # redimensione a imagem para o tamanho da tela
        self.pauseOverlay = pg.transform.scale(self.pauseOverlay, (self.constants.width, self.constants.height))

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.constants.running = False
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                self.first = True
                self.constants.state = 1
                self.selected = 0
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
                        self.selected = 0
                    elif self.selected == 1:
                        self.first = True
                        self.constants.state = 1
                        self.constants.return_to_menu = True
                        self.selected = 0
    
    def update(self):
        pass
        
    def draw(self):
        if self.first:
            self.first = False
            # desenhe a imagem na tela
            self.screen.blit(self.pauseOverlay, (0, 0))
        
        if self.selected == 0:
            text = self.font.render("Continuar", 1, (255,0,0))
        else:
            text = self.font.render("Continuar", 1, (255,255,255))
        self.screen.blit(text, (self.constants.half_width - text.get_width()//2, self.constants.half_height - text.get_height()//2 ))
        if self.selected == 1:
            text = self.font.render("Sair*", 1, (255,0,0))
            text_description = self.font_description.render("*O Jogo será salvo, mas você morerá", 1, (255,0,0))
            self.screen.blit(text_description, (self.constants.half_width - text_description.get_width()//2, self.constants.half_height - text_description.get_height()//2 + self.constants.padding*3))
        else:
            text = self.font.render("Sair*", 1, (255,255,255))
            text_description = self.font_description.render("*O Jogo será salvo, mas você morerá", 1, (0,0,0))
            self.screen.blit(text_description, (self.constants.half_width - text_description.get_width()//2, self.constants.half_height - text_description.get_height()//2 + self.constants.padding*3))
        
        self.screen.blit(text, (self.constants.half_width - text.get_width()//2, self.constants.half_height - text.get_height()//2 + self.constants.padding*2))
        if self.constants.state != 2:
            self.first = True