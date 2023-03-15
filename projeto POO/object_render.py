import pygame as pg
from conf import *

class ObjectRender:

    def __init__(self, jogo):
        self.jogo = jogo
        self.tela = jogo.tela
        self.textura_parede = self.carregar_textura_parede()
        self.image_ceu = self.pegar_textura('Recursos\Texturas\sky2.png', (largura, meia_comprimeto))
        self.ceu_offset = 0

    def desenha(self):
        self.desenhar_background()
        self.objetos_para_renderizar_no_jogo()

    def desenhar_background(self):
        self.ceu_offset = (self.ceu_offset + 4.0 * self.jogo.jogador.rel) % largura
        self.tela.blit(self.image_ceu, (-self.ceu_offset, 0))
        self.tela.blit(self.image_ceu, (-self.ceu_offset + largura, 0))
        # RES = WIDTH, HEIGHT = 1600, 900
        # pg.draw.rect(self.screen, FLOOR_COLOR, (0, HALF_HEIGHT, WIDTH, HEIGHT))

        # self.sky_offset = (self.sky_offset + 4.5 * self.game.player.rel) % WIDTH
        # self.screen.blit(self.sky_image, (-self.sky_offset, 0))
        # self.screen.blit(self.sky_image, (-self.sky_offset + WIDTH, 0))
        # # floor
        # pg.draw.rect(self.screen, FLOOR_COLOR, (0, HALF_HEIGHT, WIDTH, HEIGHT))

        pg.draw.rect(self.tela, cor_piso, (0, meia_comprimeto, largura, comprimento))

    def objetos_para_renderizar_no_jogo(self):
        lista_objetos = self.jogo.raycasting.objetos_renderizar
        for profundidade, imagem, posicao in lista_objetos:
            self.tela.blit(imagem, posicao)

    @staticmethod
    def pegar_textura(path, res= (tamanho_textura,tamanho_textura)):
        textura = pg.image.load(path).convert_alpha()
        return pg.transform.scale(textura, res)

    def carregar_textura_parede(self):
        return{1: self.pegar_textura('Recursos\Texturas\pedro.png')}