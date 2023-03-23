import pygame as pg

class Settings:
    def __init__(self, screen, constants):
        self.screen = screen
        self.constants = constants
        self.selected = 0
        self.num_options = 2
        self.first = True
        self.font = pg.font.Font('assets/fonts/dogicapixel.ttf', self.constants.font_size)
        # importe o arquivo de imagem pauseOverlay.png da pasta assets/overlays
        self.pauseOverlay = pg.image.load('assets/overlays/settingsOverlay.png')
        # redimensione a imagem para o tamanho da tela
        self.pauseOverlay = pg.transform.scale(self.pauseOverlay, (self.constants.width, self.constants.height))
        self.fov_options = [50, 60, 70]
        self.fov = self.constants.player_fov_scale
        self.fov_index = self.fov_options.index(self.fov)
        self.fov_size = len(self.fov_options)
        self.sound_volume = self.constants.sound_volume
        self.sound_volume_state = "Ligado" if self.sound_volume > 0 else "Desligado"

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.constants.running = False
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                self.first = True
                self.constants.state = 0
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_DOWN:
                    self.selected += 1
                    self.selected %= self.num_options
                if event.key == pg.K_UP:
                    self.selected -= 1
                    self.selected %= self.num_options
                if event.key == pg.K_RETURN:
                    self.handle_selection()
    
    def update(self):
        pass
        
    def draw(self):
        if self.first:
            self.first = False
            # desenhe a imagem na tela
            self.screen.blit(self.pauseOverlay, (0, 0))
        
        if self.selected == 0:
            text = self.font.render("Estado do Som", 1, (255,0,0))
            data = self.font.render(self.sound_volume_state, 1, (255,0,0))
        else:
            text = self.font.render("Estado so Som", 1, (255,255,255))
            data = self.font.render(self.sound_volume_state, 1, (255,255,255))
        self.screen.blit(text, (self.constants.half_width - self.constants.padding*10, self.constants.half_height - text.get_height()//2 ))
        self.screen.blit(data, (self.constants.half_width + self.constants.padding*10 - data.get_width()//2, self.constants.half_height - text.get_height()//2 ))
        if self.selected == 1:
            text = self.font.render("Campo de Visão", 1, (255,0,0))
            data = self.font.render(str(self.fov), 1, (255,0,0))
        else:
            text = self.font.render("Campo de Visão", 1, (255,255,255))
            data = self.font.render(str(self.fov), 1, (255,255,255))
        self.screen.blit(text, (self.constants.half_width - self.constants.padding*10, self.constants.half_height - text.get_height()//2 + self.constants.padding*2))
        self.screen.blit(data, (self.constants.half_width + self.constants.padding*10 - data.get_width()//2, self.constants.half_height - text.get_height()//2 + self.constants.padding*2))
        if self.constants.state != 2:
            self.first = True

    def handle_selection(self):
        if self.selected == 0:
            # mudar estado do som
            if self.sound_volume > 0:
                self.sound_volume = 0
                self.sound_volume_state = "Desligado"
            else:
                self.sound_volume = 1
                self.sound_volume_state = "Ligado"
        elif self.selected == 1:
            # mudar fov
            self.fov_index += 1
            self.fov_index %= self.fov_size
            self.fov = self.fov_options[self.fov_index]
            self.constants.redefine_fov(self.fov)
    