import pygame as pg
import math

class MiniMap:
    '''classe que desenha o mini mapa'''
    def __init__(self, game):
        '''inicializa o mini mapa'''
        self.game = game
        self.map = self.game.gameMap.map_inversed
        self.player = self.game.player
        # fazer um dicionario com as coordenadas do mapa e uma escala de 0 até 3 para o alfa se o jogador já passou por perto
        self.map_alpha = {}
        for x,y in self.map:
            self.map_alpha[(x,y)] = 0
        
    def draw(self):
        '''desenha o mini mapa'''
        # desenhar o mini mapa no canto direito da tela

        # fazer a superficie do mini mapa
        mini_map = pg.Surface((self.game.constants.minimap_size, self.game.constants.minimap_size))
        mini_map.fill(self.game.constants.minimap_background_color)

        # desenhar o mapa no mini mapa

        # desenhar o mapa
        for x,y in self.map:
            yoffset = (y - self.player.y) * self.game.constants.minimap_scale + self.game.constants.minimap_size//2
            xoffset = (x - self.player.x) * self.game.constants.minimap_scale + self.game.constants.minimap_size//2

            # se a distância estiver a menos de 10 blocos, aumentar alfa para 1
            if math.sqrt((x-self.player.x)**2 + (y-self.player.y)**2) < 5 and self.map_alpha[(x,y)] == 0:
                self.map_alpha[(x,y)] = 1
            # se a distância estiver a menos de 5 blocos, aumentar alfa para 3
            if math.sqrt((x-self.player.x)**2 + (y-self.player.y)**2) < 2 and self.map_alpha[(x,y)] == 1:
                self.map_alpha[(x,y)] = 3
            # desenhar o bloco no mini mapa com a cor e o alfa correspondente
            c = self.map_alpha[(x,y)]*85
            pg.draw.rect(mini_map, (c, c, c) , (xoffset-1, yoffset-1, self.game.constants.minimap_scale+1, self.game.constants.minimap_scale+1))

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