import math

#configurações do jogo
largura,comprimento = 1600,900
resol = tuple([largura, comprimento])
meia_largura = largura//2
meia_comprimeto = comprimento//2
fps = 60

jogador_pos_inicial= 1.5, 1.5
jogador_angulo_inicial = 0
velocidade_linear_jogador = 0.004
velocidade_angular_jogador = 0.002
tamanho_jogador_escala = 60

sensibilidade_mouse = 0.0003
max_mouse = 40
borda_esquer_mouse = 100
borda_dirt_mouse = largura - borda_esquer_mouse

cor_piso = (30,30,30)

FOV = 6*math.pi/18
metade_FOV = FOV/2
raios_totais = largura // 2
metade_numero_raios = raios_totais // 2
angulo_interno = FOV/raios_totais
profundidade_maxima = 20

distancia_parede = meia_comprimeto / math.tan(metade_FOV)
escala = largura//raios_totais

tamanho_textura = 256
metade_tamanho_textura = tamanho_textura//2