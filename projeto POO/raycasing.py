import pygame as pg
import math
from conf import*

class RayCasting:

    def __init__(self, jogo):
        self.jogo = jogo
        self.resultado_raycasting = []
        self.objetos_renderizar = []
        self.texturas = self.jogo.object_render.textura_parede

    def objetos_para_renderizar(self):
        self.objetos_renderizar = []
        for raio,valores in enumerate(self.resultado_raycasting):
            profundidade, altura_projetada, textura, offset = valores
            if altura_projetada < comprimento:
                coluna_parede = self.texturas[textura].subsurface(offset * (tamanho_textura - escala), 0, escala, tamanho_textura)
                coluna_parede = pg.transform.scale(coluna_parede, (escala, altura_projetada))
                posicao_parede = (raio * escala, meia_comprimeto - altura_projetada//2)
            else:
                altura_textura = tamanho_textura*comprimento / altura_projetada
                coluna_parede = self.texturas[textura].subsurface(offset * (tamanho_textura - escala), metade_tamanho_textura - altura_textura//2, escala, altura_textura)
                coluna_parede = pg.transform.scale(coluna_parede, (escala, comprimento))
                posicao_parede = (raio * escala, 0)


            self.objetos_renderizar.append((profundidade, coluna_parede, posicao_parede))


    def ray_cast(self):
        self.resultado_raycasting = []
        ox, oy = self.jogo.jogador.pos
        x_mapa, y_mapa = self.jogo.jogador.pos_mapa
        angulo_raio = self.jogo.jogador.angulo - metade_FOV + 0.000001

        vert_textura, hort_textura = 1,1

        for raio in range(raios_totais):
            seno_a = math.sin(angulo_raio)
            cos_a = math.cos(angulo_raio)

            #horizontais
            if seno_a > 0:
                y_hor = y_mapa + 1
                dy = 1
            else:
                y_hor = y_mapa - 0.000000001
                dy = -1

            profundidade_horizontal = (y_hor - oy)/seno_a
            x_hor = ox + profundidade_horizontal*cos_a

            variacao_prof = dy/seno_a
            dx = variacao_prof*cos_a

            for i in range(profundidade_maxima):
                horizontal_contato = int(x_hor), int(y_hor)
                if horizontal_contato in self.jogo.mapa.mapa_complt:
                    hort_textura = self.jogo.mapa.mapa_complt[horizontal_contato]
                    break
                x_hor += dx
                y_hor += dy
                profundidade_horizontal += variacao_prof

            #verticais
            if cos_a > 0:
                x_vert = x_mapa + 1
                dx = 1
            else:
                x_vert = x_mapa - 0.000000001
                dx = -1

            profundidade_vertical = (x_vert - ox)/cos_a
            y_vert = oy + profundidade_vertical*seno_a

            variacao_prof = dx/cos_a
            dy = variacao_prof*seno_a

            for i in range(profundidade_maxima):
                vertical_contato = int(x_vert), int(y_vert)
                if vertical_contato in self.jogo.mapa.mapa_complt:
                    vert_textura = self.jogo.mapa.mapa_complt[vertical_contato]
                    break
                x_vert += dx
                y_vert += dy
                profundidade_vertical += variacao_prof

            if profundidade_vertical < profundidade_horizontal:
                profundidade,textura = profundidade_vertical,vert_textura
                y_vert %=1
                offset = y_vert if cos_a > 0 else (1-y_vert)
            else:
                profundidade,textura = profundidade_horizontal,hort_textura
                x_hor %=1
                offset = (1- x_hor) if seno_a > 0 else x_hor

            #removendo distorcao
            profundidade *= math.cos(self.jogo.jogador.angulo - angulo_raio)

            #debugador
            # pg.draw.line(self.jogo.tela, 'green', (100 * ox, 100 * oy), (100*ox+100*profundidade*cos_a, 100*oy+100*profundidade*seno_a), 2)

            #projeção do raio
            altura_projetada = distancia_parede/(profundidade+0.00001)

            #desenhar parede
            self.resultado_raycasting.append((profundidade, altura_projetada, textura, offset))

            angulo_raio += angulo_interno

    def atualiza(self):
        self.ray_cast()
        self.objetos_para_renderizar()