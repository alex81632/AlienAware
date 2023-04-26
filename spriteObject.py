import pygame as pg
import math
import os
from collections import deque


class SpriteObject:
    '''inicializa o objeto sprite'''
    def __init__(self, game, path='Recursos\static_sprites\candlebra.png',
                 pos=(2, 2), scale=0.7, shift=0.27):
        '''inicializa o objeto sprite'''
        self.game = game
        self.player = game.player
        self.x, self.y = pos
        self.image = pg.image.load(path).convert_alpha()
        self.image_width = self.image.get_width()
        self.image_half_width = self.image.get_width() // 2
        self.image_ratio = self.image_width / self.image.get_height()
        self.dx, self.dy, self.theta, self.screen_x, self.dist, self.norm_dist = 0, 0, 0, 0, 1, 1
        self.sprite_half_width = 0
        self.sprite_scale = scale
        self.sprite_height_shift = shift

    def get_sprite_projection(self):
        '''projeção do sprite'''
        proj = self.game.constants.wall_distance / self.norm_dist * self.sprite_scale # SCREEN_DIST
        proj_width, proj_height = proj * self.image_ratio, proj

        image = pg.transform.scale(self.image, (proj_width, proj_height))

        self.sprite_half_width = proj_width // 2
        height_shift = proj_height * self.sprite_height_shift
        pos = self.screen_x - self.sprite_half_width, self.game.constants.half_height - proj_height // 2 + height_shift

        self.game.raycasting.obj_to_render.append((self.norm_dist, image, pos))

    def get_sprite(self):
        '''obtém o sprite'''
        dx = self.x - self.player.x
        dy = self.y - self.player.y
        self.dx, self.dy = dx, dy
        self.theta = math.atan2(dy, dx)

        delta = self.theta - self.player.angle
        if (dx > 0 and self.player.angle > math.pi) or (dx < 0 and dy < 0):
            delta += math.tau

        delta_rays = delta / self.game.constants.ray_angle
        self.screen_x = (self.game.constants.half_total_rays + delta_rays) * self.game.constants.scale

        self.dist = math.hypot(dx, dy)
        self.norm_dist = self.dist * math.cos(delta)
        if -self.image_half_width < self.screen_x < (self.game.constants.width + self.image_half_width) and self.norm_dist > 0.5:
            self.get_sprite_projection()

    def update(self):
        '''atualiza o sprite'''
        self.get_sprite()


class AnimatedSprite(SpriteObject):
    '''inicializa o objeto sprite animado'''
    def __init__(self, game, path="Recursos/animated_sprites/green_light/0.png",
                 pos=(2, 3.5), scale=0.8, shift=0.16, animation_time=120):
        '''inicializa o objeto sprite animado'''
        super().__init__(game, path, pos, scale, shift)
        self.animation_time = animation_time
        self.path = path.rsplit('/', 1)[0]
        self.images = self.get_images(self.path)
        self.animation_time_prev = pg.time.get_ticks()
        self.animation_trigger = False

    def update(self):
        '''atualiza o sprite'''
        super().update()
        self.check_animation_time()
        self.animate(self.images)

    def animate(self, images):
        '''anima o sprite'''
        if self.animation_trigger:
            images.rotate(-1)
            self.image = images[0]

    def check_animation_time(self):
        '''verifica o tempo de animação'''
        self.animation_trigger = False
        time_now = pg.time.get_ticks()
        if time_now - self.animation_time_prev > self.animation_time:
            self.animation_time_prev = time_now
            self.animation_trigger = True

    def get_images(self, path):
        '''obtém as imagens'''
        images = deque()
        for file_name in os.listdir(path):
            if os.path.isfile(os.path.join(path, file_name)):
                img = pg.image.load(path + '/' + file_name).convert_alpha()
                images.append(img)
        return images