import pygame as pg

_ = False

mapa_jogo = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, _, _, _, _, 1, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, _, _, _, _, _, _, _, 1, 1],
    [1, _, _, _, _, _, _, _, _, 1, 1, 1, 1, _, 1, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, 1, 1],
    [1, 1, 1, _, _, 1, 1, 1, 1, 1, _, _, _, _, 1, 1],
    [1, 1, 1, _, _, 1, 1, 1, 1, 1, _, _, _, _, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

class Mapa:
    def __init__(self, jogo):
        self.jogo = jogo
        self.mapa_jogo = mapa_jogo
        self.mapa_complt  = {}
        self.const_mapa()

    def const_mapa(self):
        for i,coluna in enumerate(self.mapa_jogo):
            for j, valor in enumerate(coluna):
                if valor == 1:
                    self.mapa_complt[(j,i)] = valor
    def desenho(self):
        [pg.draw.rect(self.jogo.tela, 'darkgray', (pos[0] * 100, pos[1] * 100, 100, 100), 2) for pos in self.mapa_complt]