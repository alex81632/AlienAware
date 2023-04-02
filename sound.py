import pygame as pg

class Sound:
    def __init__(self, game):
        self.game = game
        pg.mixer.init()
        self.path = 'Recursos/Som/'
        self.shotgun = pg.mixer.Sound(self.path + 'shotgun.wav')
        self.enemy_pain = pg.mixer.Sound(self.path + 'npc_pain.wav')
        self.enemy_death = pg.mixer.Sound(self.path + 'npc_death.wav')
        self.enemy_shot = pg.mixer.Sound(self.path + 'npc_attack.wav')
        self.enemy_attack = pg.mixer.Sound(self.path + 'npc_attack_2.wav')
        self.player_pain = pg.mixer.Sound(self.path + 'player_pain.wav')
        self.potion_heal = pg.mixer.Sound(self.path + 'cure.wav')
        # self.enemy_pain = pg.mixer.Sound(self.path + 'shotgun.wav') # Coloque a música tema do jogo aqui