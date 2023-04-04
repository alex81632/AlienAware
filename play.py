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
from habilityTree import HabilityTree
from waveController import waveController

class Play:
    def __init__(self, screen, constants):
        self.screen = screen
        self.constants = constants
        self.constants.load_game()
        self.HUD = HUD(self.screen, self.constants)
        self.player = Player(self)
        self.gameMap = GameMap(self)
        self.miniMap = MiniMap(self)
        self.objectRender = ObjectRender(self)
        self.raycasting = RayCasting(self)
        self.object_handler = ObjectHandler(self)
        self.weapon = Weapon(self)
        self.sound = Sound(self)
        self.waveController = waveController(self)
        self.habilityTree = HabilityTree(self.screen, self.constants)
        self.global_trigger = False
        self.global_event = pg.USEREVENT + 0
        pg.time.set_timer(self.global_event, 40)
        self.pathfinding = PathFinding(self)
        self.overlay = pg.image.load('assets/overlays/gameOverlay.png').convert_alpha()
        self.overlay = pg.transform.scale(self.overlay, (self.constants.width, self.constants.height))
        self.time_start = time.time()
        self.font = pg.font.Font('assets/fonts/dogicapixel.ttf', int(self.constants.font_size)//2)


    def check_events(self):
        self.global_trigger = False
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.constants.running = False
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                self.constants.state = 2
                # salva o objeto HabilityTree
                self.habilityTree.save_game()
                # adicona o numero de segundos jogados ao total
                self.constants.time_played += time.time() - self.time_start
                self.time_start = time.time()
                # salva as constantes
                self.constants.save_game()
            if event.type == pg.KEYDOWN and event.key == pg.K_h and self.constants.mapa_atual == 0 and self.player.x>1.5 and self.player.x<3 and self.player.y>5 and self.player.y<6:
                self.constants.state = 5
            if event.type == pg.KEYDOWN and event.key == pg.K_m:
                self.constants.minimap_state = not self.constants.minimap_state
                self.constants.resize_minimap(self.constants.minimap_state)
            if event.type == pg.KEYDOWN and event.key == pg.K_i:
                self.constants.invencible = not self.constants.invencible
            if event.type == pg.KEYDOWN and event.key == pg.K_p:
                self.constants.invisibilidade = not self.constants.invisibilidade
            if event.type == pg.KEYDOWN and event.key == pg.K_UP:
                self.constants.transp_factor += 0.1
            if event.type == pg.KEYDOWN and event.key == pg.K_DOWN:
                self.constants.transp_factor -= 0.1
            
            # Transição de animação dos inimigos
            if event.type == self.global_event:
                self.global_trigger = True
            
            # Evento do tiro da arma
            self.player.single_fire_event(event)
            self.player.reload()

    def update(self):
        if self.constants.restart_tree == True:
            self.habilityTree = HabilityTree(self.screen, self.constants)
            self.constants.restart_tree = False
        self.player.update()
        self.raycasting.update()
        self.object_handler.update()
        self.weapon.update()
        pg.display.flip()
        if self.constants.mapa_atual == 3 and not self.constants.finished:
            self.waveController.update()

        # se o jogador chegou ao fim do mapa, vai para o próximo
        if self.player.y > self.constants.map_height - 1:
            self.next_map()

        # se a vida for menor que 0, volta pro mapa inicial
        if self.constants.player_health <= 0 or self.constants.return_to_menu == True:
            self.reset_game()

    def next_map(self):
        # tela de transição
        self.constants.state = 4
        self.constants.time = time.time()
        # atualiza o mapa para o próximo            
        self.gameMap.next_map()
        if self.constants.mapa_atual == 3 and not self.constants.finished:
            self.waveController = waveController(self)
            self.objectRender.wall_texture = self.objectRender.load_textures(3)
            self.raycasting.textures = self.objectRender.wall_texture
        self.object_handler.remove_enemies()
        self.object_handler.remove_all_potions()
        self.pathfinding = PathFinding(self)
        if self.constants.mapa_atual == 1:
            self.object_handler.spawn_enemies(20)
            self.object_handler.spawn_potions(10 + int(self.constants.flasks_factor))
            self.objectRender.wall_texture = self.objectRender.load_textures(1)
            self.raycasting.textures = self.objectRender.wall_texture
        elif self.constants.mapa_atual == 2:
            self.object_handler.spawn_enemies(30)
            self.object_handler.spawn_potions(10 + int(self.constants.flasks_factor))
            self.objectRender.wall_texture = self.objectRender.load_textures(2)
            self.raycasting.textures = self.objectRender.wall_texture
        elif self.constants.mapa_atual > 3 or (self.constants.mapa_atual ==3 and self.constants.finished):
            self.object_handler.spawn_enemies(40)
            self.object_handler.spawn_potions(10 + int(self.constants.flasks_factor))
            self.objectRender.wall_texture = self.objectRender.load_textures(3)
            self.raycasting.textures = self.objectRender.wall_texture
        # atualiza o jogador para a nova posição
        self.player.x, self.player.y = self.constants.player_initial_position
        self.player.angle = self.constants.player_initial_angle

        # atualiza o minimapa para a nova posição
        self.miniMap = MiniMap(self)
        self.object_handler.remove_all_sprites()
        self.object_handler.spawn_portal()
    
    def reset_game(self):
        self.constants.player_health = self.constants.player_max_health
        # tela de transição
        self.constants.state = 4
        self.constants.time = time.time()
        # atualiza o mapa para o inicial
        self.gameMap = GameMap(self)
        # atualiza os inimigos
        self.object_handler.remove_enemies()
        self.object_handler.remove_all_potions()
        self.pathfinding = PathFinding(self)
        # atualiza o jogador para a nova posição
        self.player.x, self.player.y = self.constants.player_initial_position
        self.player.angle = self.constants.player_initial_angle

        # atualiza o minimapa para a nova posição
        self.miniMap = MiniMap(self)
        self.object_handler.remove_all_sprites()
        self.object_handler.spawn_portal()
        self.object_handler.spaw_initial_objects()
        self.objectRender.wall_texture = self.objectRender.load_textures()
        self.raycasting.textures = self.objectRender.wall_texture
        
    def draw(self):
        self.objectRender.draw()
        self.weapon.draw()
        self.screen.blit(self.overlay, (0,0))
        self.miniMap.draw()
        self.HUD.draw()
        if self.constants.mapa_atual == 3 and not self.constants.finished:
            self.waveController.draw()
        if self.constants.mapa_atual == 0 and self.player.x>1.5 and self.player.x<3 and self.player.y>5 and self.player.y<6:
            text = self.font.render("Pressione H para abrir a arvore de habilidades", True, (255, 255, 255))
            self.screen.blit(text, (self.constants.width/2 - text.get_width()/2, self.constants.height - text.get_height() - self.constants.padding)) 
        
        if self.constants.mapa_atual == 0 and self.player.x>3.5 and self.player.x<5 and self.player.y>5 and self.player.y<6:
            text = self.font.render("Máquina Quebrada, tente outra hora", True, (255, 255, 255))
            self.screen.blit(text, (self.constants.width/2 - text.get_width()/2, self.constants.height - text.get_height() - self.constants.padding))
        
        # desenhar dot no meio da tela
        pg.draw.circle(self.screen, (200, 200, 200), (self.constants.width//2, self.constants.height//2), 3)