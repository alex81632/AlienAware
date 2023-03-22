import pygame as pg
import math

class MiniMap:
    def __init__(self, game):
        self.game = game
        self.map = self.game.gameMap.map_inversed
        self.player = self.game.player
        
    def draw(self):
        # desenhar o mini mapa no canto direito da tela

        # fazer a superficie do mini mapa
        mini_map = pg.Surface((self.game.constants.minimap_size, self.game.constants.minimap_size))
        mini_map.fill(self.game.constants.minimap_background_color)

        # desenhar o mapa no mini mapa

        # desenhar o mapa
        for x,y in self.map:
            yoffset = (y - self.player.y) * self.game.constants.minimap_scale + self.game.constants.minimap_size//2
            xoffset = (x - self.player.x) * self.game.constants.minimap_scale + self.game.constants.minimap_size//2

            pg.draw.rect(mini_map, self.game.constants.minimap_wall_color, (xoffset-1, yoffset-1, self.game.constants.minimap_scale+1, self.game.constants.minimap_scale+1))

        # inverter os eixos do mini mapa
        mini_map = pg.transform.flip(mini_map, True, True)

        # desenhar o jogador no mini mapa como um ponto
        pg.draw.circle(mini_map, self.game.constants.minimap_player_color, (self.game.constants.minimap_size//2, self.game.constants.minimap_size//2), self.game.constants.minimap_player_radius)
        # desenhar a direção do jogador no mini mapa
        pg.draw.line(mini_map, self.game.constants.minimap_player_color, (self.game.constants.minimap_size//2, self.game.constants.minimap_size//2), (self.game.constants.minimap_size//2 + math.cos(self.player.angle+math.pi) * self.game.constants.minimap_player_radius*2, self.game.constants.minimap_size//2 + math.sin(self.player.angle + math.pi) * self.game.constants.minimap_player_radius*2), self.game.constants.minimap_player_line_width)

        # fazer uma borda quadrada no mini mapa
        pg.draw.rect(mini_map, self.game.constants.minimap_border_color, (0, 0, self.game.constants.minimap_size, self.game.constants.minimap_size), self.game.constants.minimap_border_width)

        # desenhar o mini mapa na tela
        self.game.screen.blit(mini_map, (self.game.constants.minimap_position_x, self.game.constants.minimap_position_y))