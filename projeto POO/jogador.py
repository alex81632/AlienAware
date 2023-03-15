from conf import *
import pygame as pg
import math

class Jogador:
    def __init__(self, jogo):
        self.jogo = jogo
        self.x, self.y = jogador_pos_inicial
        self.angulo = jogador_angulo_inicial

    def movimento(self):
        sen_a = math.sin(self.angulo)
        cos_a = math.cos(self.angulo)
        dx, dy = 0,0
        velocidade = velocidade_linear_jogador * self.jogo.dif_tempo
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
        self.olhar_colisao(dx,dy)

        # if keys[pg.K_LEFT]:
        #     self.angulo -= velocidade_angular_jogador * self.jogo.dif_tempo
        # if keys[pg.K_RIGHT]:
        #     self.angulo += velocidade_angular_jogador * self.jogo.dif_tempo
        self.angulo %=2*math.pi

    def colisao_parede(self, x, y):
        return (x,y) not in self.jogo.mapa.mapa_complt

    def olhar_colisao(self, dx, dy):
        escala = tamanho_jogador_escala / self.jogo.dif_tempo
        if self.colisao_parede(int(self.x + dx*escala), int(self.y)):
            self.x += dx
        if self.colisao_parede(int(self.x), int(self.y + dy*escala)):
            self.y += dy

    def desenho(self):
        # pg.draw.line(self.jogo.tela, 'green', (self.x*100, self.y*100),
        #             (self.x*100 + largura*math.cos(self.angulo),
        #             self.y*100 + largura*math.sin(self.angulo)), 2)
        pg.draw.circle(self.jogo.tela, 'blue', (self.x*100, self.y*100), 15)

    def controle_mouse(self):
        mx,my = pg.mouse.get_pos()
        if mx < borda_esquer_mouse or mx>borda_dirt_mouse:
            pg.mouse.set_pos([meia_largura,meia_comprimeto])
        self.rel = pg.mouse.get_rel()[0]
        self.rel = max(-max_mouse, min(max_mouse,self.rel))
        self.angulo += self.rel * sensibilidade_mouse * self.jogo.dif_tempo

    def atualiza(self):
        self.movimento()
        self.controle_mouse()

    @property
    def pos(self):
        return self.x, self.y

    @property
    def pos_mapa(self):
        return int(self.x),int(self.y)