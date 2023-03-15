import pygame as pg

_ = False

game_map = [
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

class GameMap:
    def __init__(self, game):
        self.game = game
        self.game_map = game_map
        self.map_complt  = {}
        self.const_mapa()

    def const_mapa(self):
        for i,coluna in enumerate(self.game_map):
            for j, valor in enumerate(coluna):
                if valor == 1:
                    self.map_complt[(j,i)] = valor
    def draw(self):
        [pg.draw.rect(self.game.screen, 'darkgray', (pos[0] * 100, pos[1] * 100, 100, 100), 2) for pos in self.map_complt]