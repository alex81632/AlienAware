import pygame as pg
from random import randint

class ObjectRender:
    '''classe para renderizar os objetos do jogo'''
    def __init__(self, game):
        '''inicializa as variaveis'''
        self.game = game
        self.screen = game.screen
        self.wall_texture = self.load_textures()
        self.sky_image = self.get_textures('Recursos\Texturas\sky2.png', (self.game.constants.width, self.game.constants.half_height))
        self.sky_offset = 0
        self.blood_screen = self.get_textures('Recursos\Texturas\Blood_screen.png',(self.game.constants.width, self.game.constants.height))

    def draw(self):
        '''desenha os objetos na tela'''
        self.draw_bg()
        self.objects_for_render()

    def player_damage(self):
        '''desenha a tela de dano do jogador'''
        self.screen.blit(self.blood_screen, (0, 0))

    def draw_bg(self):
        '''desenha o background'''
        # desenhar o chão
        self.screen.fill(self.game.constants.floor_color)

    def objects_for_render(self):
        '''desenha os objetos na tela'''
        if self.game.constants.invisibilidade:
            obj_list = self.game.raycasting.obj_to_render
        else:
            obj_list = sorted(self.game.raycasting.obj_to_render, key=lambda t: t[0], reverse=True)
        for depth, image, position in obj_list:
            # para objetos mais distantes, diminuir o brightness
            # brightness = 220 - (255 * depth*self.game.constants.transp_factor / self.game.constants.max_depth)
            # if brightness < 0:
            #     brightness = 0
            # if brightness > 255:
            #     brightness = 255
            # image.fill((brightness, brightness, brightness), special_flags=pg.BLEND_RGB_MULT)

            self.screen.blit(image, position)

    @staticmethod
    def get_textures(path, res= (256, 256)):
        '''carrega as texturas'''
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)

    def load_textures(self, esc = 0):
        '''carrega as texturas do jogo'''
        path = f'Recursos\Texturas\lv{esc}.png'
        return{1: self.get_textures(path)}