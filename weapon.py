from spriteObject import AnimatedSprite
import pygame as pg
from collections import deque
import os
import time


class Weapon(AnimatedSprite):
    def __init__(self, game):
        self.game = game
        self.constants = game.constants        
        self.reloading = False
        self.frame_counter = 0
        self.damage = 50
        self.state = 'idle'
        self.screen = game.screen
        # estados: idle, walk, fire, reload
        self.idle = self.get_images('assets/weapon/idle')
        self.num_img_idle = len(self.idle)
        self.walk = self.get_images('assets/weapon/walk')
        self.num_img_walk = len(self.walk)
        self.fire = self.get_images('assets/weapon/fire')
        self.num_img_fire = len(self.fire)
        self.reload = self.get_images('assets/weapon/reload')
        self.num_img_reload = len(self.reload)
        self.fps = 30
        self.images = self.idle
        self.image = self.images[0]
        self.num_images = self.num_img_idle
        self.time_last_frame = time.time()
        self.time_per_frame = 1 / self.fps

    def change_state(self, state):
        if state != self.state:
            self.state = state
            if state == 'idle':
                self.images = self.idle
                self.num_images = self.num_img_idle
            elif state == 'walk':
                self.images = self.walk
                self.num_images = self.num_img_walk
            elif state == 'fire':
                self.images = self.fire
                self.num_images = self.num_img_fire
            elif state == 'reload':
                self.images = self.reload
                self.num_images = self.num_img_reload

            self.frame_counter = 0

    def update(self):
        # atualiza o frame da animação
        if time.time() - self.time_last_frame > self.time_per_frame:
            self.frame_counter += 1
            self.time_last_frame = time.time()
        # se o frame atual for maior que o número de frames da animação, volta para o primeiro frame
        if self.frame_counter >= self.num_images:
            self.frame_counter = 0
            # se estava atirando então agr está parado
            if self.state == 'fire':
                self.game.player.fire = False
                self.change_state('idle')
                self.reloading = False
            # se estava recarregando então agr está parado
            elif self.state == 'reload':
                self.game.player.fire = False
                self.change_state('idle')
                self.reloading = False
        
        self.image = self.images[self.frame_counter]

    
    def draw(self):
        self.screen.blit(self.image, (0,0))
 

    def get_images(self, path):
        images = deque()
        for file_name in os.listdir(path):
            if os.path.isfile(os.path.join(path, file_name)):
                img = pg.image.load(path + '/' + file_name).convert_alpha()
                # escalar a resolução da tela
                img = pg.transform.scale(img, (self.constants.width, self.constants.height))
                images.append(img)
        return images