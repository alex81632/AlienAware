import pygame as pg
import math

class MiniMap:
    def __init__(self, game):
        self.game = game
        self.map = self.game.gameMap.map_complt
        self.scale = self.game.constants.minimap_scale
        self.player = self.game.player

    def draw(self):
        # desenhar o mini mapa no canto direito dentro de um circulo com raio 100*self.constants.pixel_size

        # fazer a superficie do mini mapa
        mini_map = pg.Surface((self.game.constants.minimap_size, self.game.constants.minimap_size))
        mini_map.fill(self.game.constants.minimap_background_color)

        # desenhar o mapa no mini mapa
        # o jogador será representado por um ponto no centro do mini mapa

        # desenhar o mapa

        for x,y in self.map:
            yoffset = (y - self.player.y) * self.scale + self.game.constants.minimap_size//2
            xoffset = (x - self.player.x) * self.scale + self.game.constants.minimap_size//2
            # invertir o yoffset
            pg.draw.rect(mini_map, self.game.constants.minimap_wall_color, (xoffset, yoffset, self.scale, self.scale))

        # desenhar o jogador
        pg.draw.circle(mini_map, self.game.constants.minimap_player_color, (self.game.constants.minimap_size//2, self.game.constants.minimap_size//2), self.game.constants.minimap_player_radius)
        # desenhar a direção do jogador
        pg.draw.line(mini_map, self.game.constants.minimap_player_color, (self.game.constants.minimap_size//2, self.game.constants.minimap_size//2), (self.game.constants.minimap_size//2 + self.game.constants.minimap_player_radius * math.cos(self.player.angle) * self.game.constants.pixel*2, self.game.constants.minimap_size//2 + self.game.constants.minimap_player_radius * math.sin(self.player.angle)* self.game.constants.pixel*2), self.game.constants.minimap_player_line_width)

        # desenhar o mini mapa na tela
        self.game.screen.blit(mini_map, (self.game.constants.minimap_position_x, self.game.constants.minimap_position_y))