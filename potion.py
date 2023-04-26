from spriteObject import *
from random import randint, random
import math
import pygame as pg


class Potion(SpriteObject):
    '''iniciliza o inimigo'''
    def __init__(self, game, path='Recursos/Inimigos/Zumbi-soldado/0.png', pos=(10.5, 5.5),
                 scale=0.6, shift=0.38):
        '''inicializa o inimigo'''
        super().__init__(game, path, pos, scale, shift)

        self.touched = False
    

    def consume(self):
        '''consumir a poção'''
        if self.game.constants.player_health != 100:
            self.game.sound.potion_heal.play()
            if (self.game.constants.player_health + 30) > 100:
                self.game.constants.player_health = 100
            else:
                self.game.constants.player_health += 30
            self.game.object_handler.remove_potion(self.x, self.y)
    

    def update(self):
        '''atualiza o inimigo'''
        super().update()
        self.check_distance()
        self.verify_existence()
        pass
    

    def check_distance(self):
        '''checa a distância do inimigo para o player'''

        dx = self.x - self.player.x
        dy = self.y - self.player.y

        dist = (dx**2 + dy**2)**0.5
        if dist < 0.5:
            self.touched = True
        else:
            self.touched = False
    
    def verify_existence(self):
        '''verifica se a poção ainda existe'''
        if self.touched:
            self.consume()