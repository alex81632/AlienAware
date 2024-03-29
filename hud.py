import pygame as pg
from constants import Constants

class HUD:
    '''classe que desenha a HUD na tela'''
    def __init__(self, screen, constants):
        '''inicializa a classe'''
        self.screen = screen
        self.constants = constants
        self.logo = pg.image.load('assets/images/logo_simplificada.png')
        self.scale = 70*self.constants.pixel
        self.logo = pg.transform.scale(self.logo, (self.scale, self.scale)).convert_alpha()
        self.font = pg.font.Font('assets/fonts/dogicapixel.ttf', int(self.constants.font_size)//3)
        self.font_l = pg.font.Font('assets/fonts/dogicapixel.ttf', int(self.constants.font_size))

    def draw(self):
        '''desenha a HUD na tela'''
        # desenhar a logo na tela
        pg.draw.circle(self.screen, (210,0,0), (self.constants.padding+self.scale//2,self.constants.padding+self.scale//2), self.scale*0.8)
        pg.draw.circle(self.screen, (50,50,50), (self.constants.padding+self.scale//2,self.constants.padding+self.scale//2), self.scale*0.7)
        self.screen.blit(self.logo, (self.constants.padding, self.constants.padding))
        # desenhar a barra de vida
        health = self.constants.player_health*2
        lenght = self.constants.player_max_health*self.constants.pixel*2
        height = 10*self.constants.pixel
        # desenhar o fundo da barra de vida
        pg.draw.rect(self.screen, (100,100,100), (self.scale + self.constants.padding*2, self.constants.padding*1.5, lenght, height))
        pg.draw.rect(self.screen, (210,0,0), (self.scale + self.constants.padding*2, self.constants.padding*1.5, health, height))
        # desenhar o texto da barra de vida
        text = self.font.render("Vida", 1, (200,200,200))
        self.screen.blit(text, (self.scale + self.constants.padding*2, self.constants.padding*1.5 - text.get_height() - self.constants.padding//4))
        # desenhar os recursos
        text = self.font.render("Recursos: " + str(int(self.constants.player_coins)), 1, (200,200,200))
        self.screen.blit(text, (self.scale + self.constants.padding*2, self.constants.padding*2.5 - text.get_height() - self.constants.padding//4))
        # desenhar a munição
        text = self.font_l.render("Munição: " + str(int(self.constants.player_ammo)) + "/" + str(int(self.constants.player_max_ammo+self.constants.ammo_factor)), 1, (200,200,200))
        # desenhar no canto direto inferior
        self.screen.blit(text, (self.constants.width - text.get_width() - self.constants.padding, self.constants.height - text.get_height() - self.constants.padding))
        

