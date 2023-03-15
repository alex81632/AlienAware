import math
import numpy as np

class Constants:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.half_width = width // 2
        self.half_height = height // 2
        self.resolution = (width, height)
        self.pixel = math.ceil(width / 1920)
        self.fps = 144
        self.actual_fps = 1
        self.running = True
        self.state = 0
        self.font_size = 30*self.pixel
        self.padding = 40*self.pixel
        self.random = np.random.RandomState(0)
        self.dt = 1

        # player
        self.player_initial_position = 1.5, 1.5
        self.player_initial_angle = 0
        self.player_speed = 0.004
        self.player_rotation_speed = 0.002
        self.player_fov_scale = 60
        self.player_fov = self.player_fov_scale*math.pi/180
        self.player_fov_half = self.player_fov/2
        self.player_scale = 60

        # raycasting
        self.total_rays = self.width//2
        self.half_total_rays = self.total_rays//2
        self.ray_angle = self.player_fov//self.total_rays
        self.max_depth = 20
        self.wall_distance = self.half_height/math.tan(self.player_fov_half)
        self.scale = self.width//self.total_rays

        # map
        self.textures_size = 256
        self.half_textures_size = self.textures_size//2
        self.floor_color = (30, 30, 30)

        # mouse
        self.mouse_sensitivity = 0.0003
        self.max_mouse = 40
        self.left_border_mouse = 100
        self.right_border_mouse = self.width - self.left_border_mouse

        # sound
        self.sound_volume = 1

    def redefine_fov(self, fov):
        self.player_fov_scale = fov
        self.player_fov = self.player_fov_scale*math.pi/180
        self.player_fov_half = self.player_fov/2
        self.ray_angle = self.player_fov//self.total_rays
        self.wall_distance = self.half_height/math.tan(self.player_fov_half)
        