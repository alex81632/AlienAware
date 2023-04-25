import pygame as pg
import time

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
        self.mun_out = pg.mixer.Sound(self.path + 'out_ammo.wav')
        self.reload = pg.mixer.Sound(self.path + 'glock_reload.mp3')
        # self.enemy_pain = pg.mixer.Sound(self.path + 'shotgun.wav') # Coloque a música tema do jogo aqui
        self.epic = pg.mixer.Sound('assets/musics/epic.mp3')
        self.tension = pg.mixer.Sound('assets/musics/tension.mp3')
        self.playing_music = False
        self.current_music = None
    
    def play_music(self):
        if not self.playing_music:
                self.current_music.set_volume(self.game.constants.sound_volume)
                pg.mixer.Sound.play(self.current_music)
                self.timer_music = time.time()
                self.playing_music = True
            
        if time.time() - self.timer_music > self.current_music.get_length():
            self.playing_music = False