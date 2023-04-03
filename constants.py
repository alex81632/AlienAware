import math
import numpy as np
import time

class Constants:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.half_width = width // 2
        self.half_height = height // 2
        self.resolution = (width, height)
        self.pixel = math.ceil(width / 1920)
        self.fps = 60
        self.actual_fps = 1
        self.running = True
        self.state = 0
        self.font_size = 30*self.pixel
        self.padding = 40*self.pixel
        self.random = np.random.RandomState(0)
        self.dt = 1
        self.invencible = False
        self.invisibilidade = False
        self.transp_factor = 1.5

        # map
        self.map_width = 7
        self.map_height = 8
        self.textures_size = 256
        self.half_textures_size = self.textures_size//2
        self.floor_color = (30, 30, 30)
        self.minimap_size = 200*self.pixel
        self.minimap_background_color = (0, 0, 0)
        self.minimap_wall_color = (215, 215, 215)
        self.minimap_player_color = (255, 0, 0)
        self.minimap_scale = self.minimap_size/self.map_width
        self.minimap_player_radius = 3*self.pixel
        self.minimap_position_x = self.width - self.minimap_size - self.padding
        self.minimap_position_y = self.padding
        self.minimap_player_line_width = 2*self.pixel
        self.minimap_border_width = 10*self.pixel
        self.minimap_border_color = (215, 0, 0)
        self.minimap_state = 0
        self.mapa_atual = 0

        # player
        self.player_initial_position = self.map_width/2, 1.5
        self.player_initial_angle = math.pi/2
        self.player_speed = 0.002
        self.player_rotation_speed = 0.002
        self.player_fov_scale = 60
        self.player_fov = self.player_fov_scale*math.pi/180
        self.player_fov_half = self.player_fov/2
        self.player_scale = 100*self.pixel
        self.player_health = 100
        self.player_max_health = 100
        self.player_coins = 0
        self.player_ammo = 5
        self.player_max_ammo = 5

        # raycasting
        self.total_rays = self.width//2
        self.half_total_rays = self.total_rays//2
        self.ray_angle = self.player_fov/self.total_rays
        self.max_depth = 20
        self.wall_distance = self.half_height/math.tan(self.player_fov_half)
        self.scale = self.width//self.total_rays

        # mouse
        self.mouse_sensitivity = 0.0001
        self.max_mouse = 40
        self.left_border_mouse = 100
        self.right_border_mouse = self.width - self.left_border_mouse

        # sound
        self.sound_volume = 1

        # time
        self.time = time.time()

        # inimigos

        # control flow
        self.return_to_menu = False
        self.finished = False
        self.max_level = 0
        self.enemies_killed = 0
        self.time_played = 0

        # hability tree constants
        self.restart_tree = False
        # se existir um arquivo save.txt, carrega os valores salvos
        self.coins_factor = 1
        self.precision_factor = 1
        self.time_factor = 1
        self.damage_factor = 1
        self.ammo_factor = 1
        self.furtivity_factor = 1
        self.short_range_factor = 1
        self.long_range_factor = 1
        self.health_factor = 1
        self.flasks_factor = 0
        self.flask_room = 0 
        self.speed_factor = 1

    def load_game(self):
        try:
            with open('save.txt', 'r') as file:
                self.coins_factor = float(file.readline())
                self.precision_factor = float(file.readline())
                self.time_factor = float(file.readline())
                self.damage_factor = float(file.readline())
                self.ammo_factor = float(file.readline())
                self.furtivity_factor = float(file.readline())
                self.short_range_factor = float(file.readline())
                self.long_range_factor = float(file.readline())
                self.health_factor = float(file.readline())
                self.flasks_factor = float(file.readline())
                self.flask_room = float(file.readline())
                self.speed_factor = float(file.readline())
                self.player_coins = float(file.readline())
                self.max_level = float(file.readline())
                self.enemies_killed = float(file.readline())
                self.time_played = float(file.readline())
        # se não existir, cria um arquivo save.txt com os valores padrão
        except:
            with open('save.txt', 'w') as file:
                file.write('1\n')
                file.write('1\n')
                file.write('1\n')
                file.write('1\n')
                file.write('1\n')
                file.write('1\n')
                file.write('1\n')
                file.write('1\n')
                file.write('1\n')
                file.write('0\n')
                file.write('0\n')
                file.write('1\n')
                file.write('0\n')
                file.write('0\n')
                file.write('0\n')
                file.write('0\n')
            with open('save.txt', 'r') as file:
                self.coins_factor = float(file.readline())
                self.precision_factor = float(file.readline())
                self.time_factor = float(file.readline())
                self.damage_factor = float(file.readline())
                self.ammo_factor = float(file.readline())
                self.furtivity_factor = float(file.readline())
                self.short_range_factor = float(file.readline())
                self.long_range_factor = float(file.readline())
                self.health_factor = float(file.readline())
                self.flasks_factor = float(file.readline())
                self.flask_room = float(file.readline())
                self.speed_factor = float(file.readline())
                self.player_coins = float(file.readline())
                self.max_level = float(file.readline())
                self.enemies_killed = float(file.readline())
                self.time_played = float(file.readline())
        
    def save_game(self):
        with open('save.txt', 'w') as file:
            file.write(str(self.coins_factor) + '\n')
            file.write(str(self.precision_factor) + '\n')
            file.write(str(self.time_factor) + '\n')
            file.write(str(self.damage_factor) + '\n')
            file.write(str(self.ammo_factor) + '\n')
            file.write(str(self.furtivity_factor) + '\n')
            file.write(str(self.short_range_factor) + '\n')
            file.write(str(self.long_range_factor) + '\n')
            file.write(str(self.health_factor) + '\n')
            file.write(str(self.flasks_factor) + '\n')
            file.write(str(self.flask_room) + '\n')
            file.write(str(self.speed_factor) + '\n')
            file.write(str(self.player_coins) + '\n')
            file.write(str(self.max_level) + '\n')
            file.write(str(self.enemies_killed) + '\n')
            file.write(str(self.time_played) + '\n')
            

    def redefine_fov(self, fov):
        self.player_fov_scale = fov
        self.player_fov = self.player_fov_scale*math.pi/180
        self.player_fov_half = self.player_fov/2
        self.ray_angle = self.player_fov/self.total_rays
        self.wall_distance = self.half_height/math.tan(self.player_fov_half)
    
    def resize_minimap(self, state):
        print(self.minimap_scale)
        # se estado for 0, redimensiona o minimapa para o tamanho original
        if state == 0:
            self.minimap_size = 200*self.pixel
            self.minimap_scale = self.minimap_size/self.map_width
            self.minimap_player_radius = 3*self.pixel
            self.minimap_position_x = self.width - self.minimap_size - self.padding
            self.minimap_position_y = self.padding
            self.minimap_player_line_width = 2*self.pixel
            self.minimap_border_width = 10*self.pixel
        # se estado for 1, redimensiona o minimapa para o tamanho da tela
        else:
            self.minimap_size = self.height - 2*self.padding
            self.minimap_scale = self.minimap_size/self.map_width
            self.minimap_scale *= 0.5
            self.minimap_player_radius = 6*self.pixel
            # mapa fica no centro da tela
            self.minimap_position_x = self.width//2 - self.minimap_size//2
            self.minimap_position_y = self.padding
            self.minimap_player_line_width = 4*self.pixel
            self.minimap_border_width = 20*self.pixel


        