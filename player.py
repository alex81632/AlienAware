import pygame as pg
import math
import time

class Player:
    '''Classe com as constantes do jogador'''
    def __init__(self, game):
        '''Inicializa as constantes do jogador'''
        self.game = game
        self.x, self.y = self.game.constants.player_initial_position
        self.angle = self.game.constants.player_initial_angle
        self.rel = 0
        self.fire = False
        self.time = time.time()

    def get_damage(self, damage):
        '''Retira vida do jogador'''
        self.game.constants.player_health -= damage
        self.game.objectRender.player_damage()
        self.game.sound.player_pain.play()
    
    def single_fire_event(self, event):
        '''Evento de tiro do jogador'''
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1 and not self.fire and not self.game.weapon.reloading and self.game.constants.player_ammo > 0:
                self.game.sound.shotgun.play()
                self.fire = True
                self.game.weapon.reloading = True
                self.game.weapon.change_state('fire')
                self.game.constants.player_ammo -= 1
                if self.game.constants.player_ammo <= 0:
                    self.time = time.time()
            elif event.button == 1 and not self.game.weapon.reloading:
                self.game.sound.mun_out.play()
    
    def reload(self):
        '''Recarrega a arma'''
        if self.game.constants.player_ammo <= 0 and time.time() - self.time > 1.7 - self.game.constants.time_factor:
            self.game.weapon.change_state('reload')

        if self.game.constants.player_ammo <= 0 and time.time() - self.time > 3 - self.game.constants.time_factor:
            self.game.constants.player_ammo = self.game.constants.player_max_ammo + self.game.constants.ammo_factor
            self.game.sound.reload.play()

    def moviment(self):
        '''Movimenta o jogador'''
        sen_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0,0
        velocidade = self.game.constants.player_speed * self.game.constants.dt * self.game.constants.speed_factor
        velocidade_seno = velocidade * sen_a
        velocidade_cosseno = velocidade * cos_a

        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            dx += velocidade_cosseno
            dy += velocidade_seno
        if keys[pg.K_s]:
            dx += -velocidade_cosseno
            dy += -velocidade_seno
        if keys[pg.K_a]:
            dx += velocidade_seno
            dy += -velocidade_cosseno
        if keys[pg.K_d]:
            dx += -velocidade_seno
            dy += velocidade_cosseno
        self.look_for_colision(dx,dy)

        if (dx != 0 or dy != 0) and (self.game.weapon.state == 'idle' or self.game.weapon.state == 'walk'):
            self.game.weapon.change_state('walk')
        elif self.game.weapon.state == 'walk':
            self.game.weapon.change_state('idle')

        self.angle %=2*math.pi

    def wall_colision(self, x, y):
        '''Verifica se o jogador colidiu com uma parede'''
        return (x,y) not in self.game.gameMap.map_complt

    def look_for_colision(self, dx, dy):
        '''Verifica se o jogador colidiu com uma parede'''
        escala = self.game.constants.player_scale / self.game.constants.dt
        if self.wall_colision(int(self.x + dx*escala), int(self.y)):
            self.x += dx
        if self.wall_colision(int(self.x), int(self.y + dy*escala)):
            self.y += dy

    def mouse_control(self):
        '''Controla o mouse'''
        mx,my = pg.mouse.get_pos()
        if mx < self.game.constants.left_border_mouse or mx>self.game.constants.right_border_mouse:
            pg.mouse.set_pos([self.game.constants.half_width,self.game.constants.half_height])
        self.rel = pg.mouse.get_rel()[0]
        self.rel = max(-self.game.constants.max_mouse, min(self.game.constants.max_mouse,self.rel))
        self.angle += self.rel * self.game.constants.mouse_sensitivity * self.game.constants.dt

    def update(self):
        '''Atualiza o jogador'''
        self.moviment()
        self.mouse_control()

    @property
    def pos(self):
        '''Retorna a posição do jogador'''
        return self.x, self.y

    @property
    def map_position(self):
        '''Retorna a posição do jogador no mapa'''
        return int(self.x),int(self.y)