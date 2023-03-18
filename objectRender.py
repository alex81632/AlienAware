import pygame as pg

class ObjectRender:

    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wall_texture = self.load_textures()
        self.sky_image = self.get_textures('Recursos\Texturas\sky2.png', (self.game.constants.width, self.game.constants.half_height))
        self.sky_offset = 0

    def draw(self):
        self.draw_bg()
        self.objects_for_render()

    def draw_bg(self):
        self.sky_offset = (self.sky_offset + 4.0 * self.game.player.rel) % self.game.constants.width
        self.screen.blit(self.sky_image, (-self.sky_offset, 0))
        self.screen.blit(self.sky_image, (-self.sky_offset + self.game.constants.width, 0))

        pg.draw.rect(self.screen, self.game.constants.floor_color, (0, self.game.constants.half_height, self.game.constants.width, self.game.constants.height))

    def objects_for_render(self):
        obj_list = self.game.raycasting.obj_to_render
        for depth, image, position in obj_list:
            self.screen.blit(image, position)

    @staticmethod
    def get_textures(path, res= (256, 256)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)

    def load_textures(self):
        return{1: self.get_textures('Recursos\Texturas\pedro.png')}