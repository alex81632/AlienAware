import pygame as pg
import time
from hud import HUD
from player import Player
from gameMap import GameMap
from objectRender import ObjectRender
from rayCasting import RayCasting
from minimap import MiniMap
from objectHandler import ObjectHandler
from weapon import Weapon
from sound import Sound
from pathFinding import PathFinding
from enemies import *

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
        self.object_handler = ObjectHandler(self)
        self.weapon = Weapon(self)
        self.sound = Sound(self)
        self.global_trigger = False
        self.global_event = pg.USEREVENT + 0
        pg.time.set_timer(self.global_event, 40)
        self.pathfinding = PathFinding(self)
        self.overlay = pg.image.load('assets/overlays/gameOverlay.png').convert_alpha()
        self.overlay = pg.transform.scale(self.overlay, (self.constants.width, self.constants.height))

    def check_events(self):
        self.global_trigger = False
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.constants.running = False
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                self.constants.state = 2
            if event.type == pg.KEYDOWN and event.key == pg.K_h and self.constants.mapa_atual == 0:
                self.constants.state = 5
            if event.type == pg.KEYDOWN and event.key == pg.K_m:
                self.constants.minimap_state = not self.constants.minimap_state
                self.constants.resize_minimap(self.constants.minimap_state)
            if event.type == pg.KEYDOWN and event.key == pg.K_h:
                self.constants.player_health -= 1
            
            # Transição de animação dos inimigos
            if event.type == self.global_event:
                self.global_trigger = True
            
            # Evento do tiro da arma
            self.player.single_fire_event(event)

    def update(self):
        self.player.update()
        self.raycasting.update()
        self.object_handler.update()
        self.weapon.update()
        pg.display.flip()
        # se o jogador chegou ao fim do mapa, vai para o próximo
        if self.player.y > self.constants.map_height - 1:
            # tela de transição
            self.constants.state = 4
            self.constants.time = time.time()
            # atualiza o mapa para o próximo            
            self.gameMap.next_map()
            self.object_handler.remove_enemies()
            self.pathfinding = PathFinding(self)
            self.object_handler.spawn_enemies(10)
            # atualiza o jogador para a nova posição
            self.player.x, self.player.y = self.constants.player_initial_position
            self.player.angle = self.constants.player_initial_angle

            # atualiza o minimapa para a nova posição
            self.miniMap = MiniMap(self)

        # se a vida for menor que 0, volta pro mapa inicial
        if self.constants.player_health <= 0 or self.constants.return_to_menu == True:
            self.constants.player_health = self.constants.player_max_health
            # tela de transição
            self.constants.state = 4
            self.constants.time = time.time()
            # atualiza o mapa para o inicial
            self.gameMap = GameMap(self)
            # atualiza os inimigos
            self.object_handler.remove_enemies()
            self.pathfinding = PathFinding(self)
            # atualiza o jogador para a nova posição
            self.player.x, self.player.y = self.constants.player_initial_position
            self.player.angle = self.constants.player_initial_angle

            # atualiza o minimapa para a nova posição
            self.miniMap = MiniMap(self)

        
    def draw(self):
        self.objectRender.draw()
        self.weapon.draw()
        self.screen.blit(self.overlay, (0,0))
        self.miniMap.draw()
        self.HUD.draw()        