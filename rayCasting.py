import pygame as pg
import math

# rc = raycasting

class RayCasting:

    def __init__(self, game):
        self.game = game
        self.rc_result = []
        self.obj_to_render = []
        self.textures = self.game.objectRender.wall_texture

    def objects_to_render(self):
        self.obj_to_render = []
        for ray,values in enumerate(self.rc_result):
            depth, projec_height, texture, offset = values
            if projec_height < self.game.constants.height:
                wall_column = self.textures[texture].subsurface(offset * (self.game.constants.textures_size - self.game.constants.scale), 0, self.game.constants.scale, self.game.constants.textures_size)
                wall_column = pg.transform.scale(wall_column, (self.game.constants.scale, projec_height))
                wall_position = (ray * self.game.constants.scale, self.game.constants.half_height - projec_height//2)
            else:
                texture_height = self.game.constants.textures_size*self.game.constants.height / projec_height
                wall_column = self.textures[texture].subsurface(offset * (self.game.constants.textures_size - self.game.constants.scale), self.game.constants.half_textures_size - texture_height//2, self.game.constants.scale, texture_height)
                wall_column = pg.transform.scale(wall_column, (self.game.constants.scale, self.game.constants.height))
                wall_position = (ray * self.game.constants.scale, 0)

            self.obj_to_render.append((depth, wall_column, wall_position))


    def ray_cast(self):
        self.rc_result = []
        ox, oy = self.game.player.pos
        x_map, y_map = self.game.player.map_position
        ray_angle = self.game.player.angle - self.game.constants.player_fov_half + 0.000001

        vert_texture, hor_texture = 1,1

        for ray in range(self.game.constants.total_rays):
            sin_a = math.sin(ray_angle)
            cos_a = math.cos(ray_angle)

            #horizontais
            if sin_a > 0:
                y_hor = y_map + 1
                dy = 1
            else:
                y_hor = y_map - 0.000000001
                dy = -1

            hor_depth = (y_hor - oy)/sin_a
            x_hor = ox + hor_depth*cos_a

            depth_vari = dy/sin_a
            dx = depth_vari*cos_a

            for i in range(self.game.constants.max_depth):
                hor_contac = int(x_hor), int(y_hor)
                if hor_contac in self.game.gameMap.map_complt:
                    hor_texture = self.game.gameMap.map_complt[hor_contac]
                    break
                x_hor += dx
                y_hor += dy
                hor_depth += depth_vari

            #verticais
            if cos_a > 0:
                x_vert = x_map + 1
                dx = 1
            else:
                x_vert = x_map - 0.000000001
                dx = -1

            vert_depth = (x_vert - ox)/cos_a
            y_vert = oy + vert_depth*sin_a

            depth_vari = dx/cos_a
            dy = depth_vari*sin_a

            for i in range(self.game.constants.max_depth):
                vert_contact = int(x_vert), int(y_vert)
                if vert_contact in self.game.gameMap.map_complt:
                    vert_texture = self.game.gameMap.map_complt[vert_contact]
                    break
                x_vert += dx
                y_vert += dy
                vert_depth += depth_vari

            if vert_depth < hor_depth:
                depth,texture = vert_depth,vert_texture
                y_vert %=1
                offset = y_vert if cos_a > 0 else (1-y_vert)
            else:
                depth,texture = hor_depth,hor_texture
                x_hor %=1
                offset = (1- x_hor) if sin_a > 0 else x_hor

            #removendo distorcao
            depth *= math.cos(self.game.player.angle - ray_angle)

            projec_height = self.game.constants.wall_distance/(depth+0.00001)

            #desenhar parede
            self.rc_result.append((depth, projec_height, texture, offset))

            ray_angle += self.game.constants.ray_angle

    def update(self):
        self.ray_cast()
        self.objects_to_render()