import pygame as pg
import sys
from conf import *
from mapa import *
from jogador import *
from raycasing import *
from object_render import *

class Jogo:
    def __init__(self):
        pg.init()
        pg.mouse.set_visible(False)
        self.tela = pg.display.set_mode(resol)
        self.tempo = pg.time.Clock()
        self.dif_tempo = 1
        self.novo_jogo()

    def novo_jogo(self):
        self.mapa = Mapa(self)
        self.jogador = Jogador(self)
        self.object_render = ObjectRender(self)
        self.raycasting = RayCasting(self)


    def atualiza(self):
        self.jogador.atualiza()
        self.raycasting.atualiza()
        pg.display.flip()
        self.dif_tempo = self.tempo.tick(fps)
        pg.display.set_caption(f'{self.tempo.get_fps() : .1f}')

    def desenho(self):
        # self.tela.fill('black')
        self.object_render.desenha()
        # self.mapa.desenho()
        # self.jogador.desenho()

    def eventos(self):
        for evento in pg.event.get():
            if evento.type == pg.QUIT or (evento.type == pg.KEYDOWN and evento.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    def rodar(self):
        while True:
            self.eventos()
            self.atualiza()
            self.desenho()

if __name__ == '__main__':
    jogo = Jogo()
    jogo.rodar()