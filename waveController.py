import pygame as pg
import random
import time

class waveController:
    def __init__(self, game):
        self.game = game
        self.wave_enemies = 50
        self.wave_enemies_spawned = 0
        self.wave_enemies_killed = 0
        self.wave_enemies_alive = 0
        self.wave_enemies_alive_max = 10
        self.font = pg.font.Font('assets/fonts/dogicapixel.ttf', int(self.game.constants.font_size)//3)
        self.font_l = pg.font.Font('assets/fonts/dogicapixel.ttf', int(self.game.constants.font_size))
        self.time = time.time()

    def update(self):
        while self.wave_enemies_alive < self.wave_enemies_alive_max and self.wave_enemies_spawned < self.wave_enemies:
            self.spawn_enemy()
        # se matou todos os inimigos da wave ou se passaram 3 minutos
        if self.wave_enemies_killed == self.wave_enemies or time.time() - self.time > 180:
            self.game.constants.finished = 1
            self.game.constants.outro = 1
            self.game.reset_game()
    
    def spawn_enemy(self):
        self.game.object_handler.spawn_enemies(1)
        self.wave_enemies_spawned += 1
        self.wave_enemies_alive += 1

    def draw(self):
        # desenha o tempo que falta para terminar os 3 minutos
        text = self.font_l.render("Time: " + str(int(180 - (time.time() - self.time))), 1, (200,200,200))
        self.game.screen.blit(text, (self.game.screen.get_width()//2 - text.get_width()//2, 10))
        # desenha a quantidade de inimigos que faltam para terminar a wave
        text = self.font.render("Enemies: " + str(int(self.wave_enemies - self.wave_enemies_killed)), 1, (200,200,200))
        self.game.screen.blit(text, (self.game.screen.get_width()//2 - text.get_width()//2, 10 + text.get_height() + 10))