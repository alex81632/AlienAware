import pygame as pg
import math

class Menu:
    def __init__(self, screen, constants):
        self.screen = screen
        self.constants = constants
        self.selected = 0
        self.num_options = 3
        self.logo = pg.image.load('assets/overlays/logoMenu.png')
        self.logo = pg.transform.scale(self.logo, (self.constants.width, self.constants.height))
        self.font = pg.font.Font('assets/fonts/dogicapixel.ttf', int(self.constants.font_size))
        self.stars = Stars(self.screen, self.constants)        

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.constants.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_DOWN:
                    self.selected += 1
                    self.selected %= self.num_options
                if event.key == pg.K_UP:
                    self.selected -= 1
                    self.selected %= self.num_options
                if event.key == pg.K_RETURN:
                    if self.selected == 0:
                        self.constants.state = 1
                        self.selected = 0
                    elif self.selected == 1:
                        self.constants.state = 3
                        self.selected = 0
                    elif self.selected == 2:
                        self.constants.running = False
                        self.selected = 0
    
    def update(self):
        self.stars.update()
        
    def draw(self):
        # fundo preto
        self.screen.fill((0,0,0))
        # fundo estrelado saindo do centro
        self.stars.draw()
        # desenhar a logo na tela
        self.screen.blit(self.logo, (0,0))
        if self.selected == 0:
            text = self.font.render("Start", 1, (255,0,0))
        else:
            text = self.font.render("Start", 1, (255,255,255))
        self.screen.blit(text, (self.constants.width - text.get_width() - self.constants.padding, self.constants.half_height - text.get_height()//2 - self.constants.padding*2))
        if self.selected == 1:
            text = self.font.render("Settings", 1, (255,0,0))
        else:
            text = self.font.render("Settings", 1, (255,255,255))
        self.screen.blit(text, (self.constants.width - text.get_width() - self.constants.padding, self.constants.half_height - text.get_height()//2))
        if self.selected == 2:
            text = self.font.render("Quit", 1, (255,0,0))
        else:
            text = self.font.render("Quit", 1, (255,255,255))
        self.screen.blit(text, (self.constants.width - text.get_width() - self.constants.padding, self.constants.half_height - text.get_height()//2 + self.constants.padding*2))

class Stars:
    def __init__(self, screen, constants, num_stars=400):
        self.screen = screen
        self.constants = constants
        self.stars = []
        self.speed = []
        self.angles = []
        # gerar as estrelas saindo do centro começando no centro
        for i in range(num_stars):
            self.stars.append((self.constants.half_width, self.constants.half_height))
        # velocidade das estrelas diferentes
        for i in range(num_stars):
            self.speed.append(self.constants.random.randint(self.constants.pixel*3, self.constants.pixel*10))
        # angulo das estrelas diferentes
        for i in range(num_stars):
            self.angles.append(self.constants.random.randint(0, 360))
        self.color = (255,255,255)
        self.size = 1

        # rodar 400 interações para que as estrelas saiam do centro
        for i in range(400):
            self.update()
    
    def update(self):
        for i in range(len(self.stars)):
            self.stars[i] = (self.stars[i][0] + self.speed[i]*math.cos(math.radians(self.angles[i])), self.stars[i][1] + self.speed[i]*math.sin(math.radians(self.angles[i])))
            if self.stars[i][0] < 0 or self.stars[i][0] > self.constants.width or self.stars[i][1] < 0 or self.stars[i][1] > self.constants.height:
                self.stars[i] = (self.constants.half_width, self.constants.half_height)
                self.speed[i] = self.constants.random.randint(self.constants.pixel*3, self.constants.pixel*10)
                self.angles[i] = self.constants.random.randint(0, 360)
    
    def draw(self):
        for i in range(len(self.stars)):
            pg.draw.circle(self.screen, self.color, self.stars[i], self.size)