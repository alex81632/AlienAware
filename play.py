import pygame as pg
import time
from hud import HUD
from player import Player
from gameMap import GameMap
from objectRender import ObjectRender
from rayCasting import RayCasting
from minimap import MiniMap

class Play:
    def __init__(self, screen, constants):
        self.screen = screen
        self.constants = constants
        self.HUD = HUD(self.screen, self.constants)
        self.player = Player(self)
        self.gameMap = GameMap(self)
        self.miniMap = MiniMap(self)
        self.objectRender = ObjectRender(self)
        self.raycasting = RayCasting(self)

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.constants.running = False
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                self.constants.state = 2
            if event.type == pg.KEYDOWN and event.key == pg.K_m:
                self.constants.minimap_state = not self.constants.minimap_state
                self.constants.resize_minimap(self.constants.minimap_state)

    def update(self):
        self.player.update()
        self.raycasting.update()
        pg.display.flip()
        # se o jogador chegou ao fim do mapa, vai para o próximo
        if self.player.y > self.constants.map_height - 2:
            # tela de transição
            self.constants.state = 4
            self.constants.time = time.time()
            # atualiza o mapa para o próximo            
            self.gameMap.next_map()
            # atualiza o jogador para a nova posição
            self.player.x, self.player.y = self.constants.player_initial_position
            self.player.angle = self.constants.player_initial_angle

            # atualiza o minimapa para a nova posição
            self.miniMap = MiniMap(self)

        
    def draw(self):
        self.objectRender.draw()
        self.miniMap.draw()
        self.HUD.draw()        