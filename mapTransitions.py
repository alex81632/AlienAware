import pygame as pg
import time

# classe para fazer um overlay de 3 segundos quando o jogador passa de mapa
class mapTransitions:
    def __init__(self, screen, constants):
        self.screen = screen
        self.constants = constants
        self.font = pg.font.Font('assets/fonts/dogicapixel.ttf', int(self.constants.font_size)*5)
        self.font_s = pg.font.Font('assets/fonts/dogicapixel.ttf', int(self.constants.font_size))
        self.time_death = 2
        self.time_next_map = 1
        self.time_finish = 4
        self.time = 10

    def draw(self):
        # fundo preto do tamanho da tela
        pg.draw.rect(self.screen, (0,0,0), (0,0, self.constants.width, self.constants.height))
        # texto no centro da tela
        if self.constants.outro:
            self.text = self.font.render("Parabens!", 1, (200,200,200))
            leg = self.font_s.render("Voce terminou o jogo! Agora está liberado o modo infinito", 1, (200,200,200))
            self.screen.blit(leg, (self.constants.width/2 - leg.get_width()/2, self.constants.height/2 - leg.get_height()/2 + 100))
            self.time = self.time_finish
        # se for o mapa 0, significa que houve morte
        elif self.constants.mapa_atual == 0:
            self.text = self.font.render("Morreu", 1, (200,200,200))
            self.time = self.time_death
        else:
            self.text = self.font.render("Mapa " + str(self.constants.mapa_atual), 1, (200,200,200))
            self.time = self.time_next_map
        self.screen.blit(self.text, (self.constants.width/2 - self.text.get_width()/2, self.constants.height/2 - self.text.get_height()/2))
        # se passou 3 segundos, volta ao jogo
        if time.time() - self.constants.time > self.time:
            self.constants.state = 1
            self.constants.outro = 0
            if self.constants.return_to_menu == True:
                self.constants.state = 0
                self.constants.return_to_menu = False