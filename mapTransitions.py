import pygame as pg
import time

# classe para fazer um overlay de 3 segundos quando o jogador passa de mapa
class mapTransitions:
    def __init__(self, screen, constants):
        self.screen = screen
        self.constants = constants
        self.font = pg.font.Font('assets/fonts/dogicapixel.ttf', self.constants.font_size*5)  

    def draw(self):
        self.text = self.font.render("Mapa " + str(self.constants.mapa_atual), 1, (200,200,200))
        # fundo preto do tamanho da tela
        pg.draw.rect(self.screen, (0,0,0), (0,0, self.constants.width, self.constants.height))
        # texto no centro da tela
        self.screen.blit(self.text, (self.constants.width/2 - self.text.get_width()/2, self.constants.height/2 - self.text.get_height()/2))
        # se passou 3 segundos, volta ao jogo
        if time.time() - self.constants.time > 3:
            self.constants.state = 1