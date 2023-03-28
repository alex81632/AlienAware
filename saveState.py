import pygame as pg
import math
import time
import os

class saveState:
    def __init__(self, screen, constants):
        self.screen = screen
        self.constants = constants
        self.selected = 0
        self.num_options = 2
        self.font = pg.font.Font('assets/fonts/dogicapixel.ttf', int(self.constants.font_size))
        self.logo = pg.image.load('assets/overlays/logoMenu.png')
        self.logo = pg.transform.scale(self.logo, (self.constants.width, self.constants.height))
        # importe o arquivo de imagem saveOverlay.png da pasta assets/overlays
        self.saveOverlay = pg.image.load('assets/overlays/saveOverlay.png')
        # redimensione a imagem para o tamanho da tela
        self.saveOverlay = pg.transform.scale(self.saveOverlay, (self.constants.width, self.constants.height))
        self.stars = Stars(self.screen, self.constants)


    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.constants.running = False
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                self.first = True
                self.constants.state = 0
                self.selected = 0
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    self.selected -= 1
                    self.selected %= self.num_options
                if event.key == pg.K_RIGHT:
                    self.selected += 1
                    self.selected %= self.num_options
                if event.key == pg.K_RETURN:
                    self.handle_selection()
        
    def draw(self):
        # fundo preto
        self.screen.fill((0,0,0))
        # fundo estrelado saindo do centro
        self.stars.draw()
        # desenhar a logo na tela
        self.screen.blit(self.logo, (0,0))
        
        self.screen.blit(self.saveOverlay, (0, 0))
        
        # desenhar as estatisticas do save
        y = self.constants.half_height - self.constants.padding*3
        x = self.constants.half_width
        # tempo de jogo em h e m e s
        h = int(self.constants.time_played//3600)
        m = int((self.constants.time_played - h*3600)//60)
        s = int(self.constants.time_played - h*3600 - m*60)
        text = self.font.render("Tempo de jogo: {}h {}m {}s".format(h, m, s), True, (255,255,255))
        self.screen.blit(text, (x - text.get_width()//2, y))
        y = y + self.constants.font_size + self.constants.padding
        # quantidade de inimigos derrotados
        text = self.font.render("Inimigos derrotados: {}".format(self.constants.enemies_killed), True, (255,255,255))
        self.screen.blit(text, (x - text.get_width()//2, y))
        y = y + self.constants.font_size + self.constants.padding
        # recursos coletados
        text = self.font.render("Recursos coletados: {}".format(int(self.constants.player_coins)), True, (255,255,255))
        self.screen.blit(text, (x - text.get_width()//2, y))
        y = y + self.constants.font_size + self.constants.padding
        # se ainda não finalizou, printar o nivel máximo alcançado
        if not self.constants.finished:
            text = self.font.render("Nivel máximo alcançado: {}".format(self.constants.max_level), True, (255,255,255))
            self.screen.blit(text, (x - text.get_width()//2, y))
        # se finalizou, printar o nível maximo no modo infinito
        else:
            text = self.font.render("Nivel máximo alcançado no Infinito: {}".format(self.constants.max_level), True, (255,255,255))
            self.screen.blit(text, (x - text.get_width()//2, y))
        
        # desenhar as opções de save
        y = self.constants.half_height + self.constants.padding*4
        x = self.constants.half_width
        if self.selected == 0:
            text = self.font.render("Jogar", True, (255,0,0))
        else:
            text = self.font.render("Jogar", True, (255,255,255))
        self.screen.blit(text, (x - text.get_width() - self.constants.padding, y))
        if self.selected == 1:
            text = self.font.render("Apagar", True, (255,0,0))
        else:
            text = self.font.render("Apagar", True, (255,255,255))
        self.screen.blit(text, (x + self.constants.padding, y))




    def handle_selection(self):
        if self.selected == 0:
            self.constants.state = 1
            self.selected = 0
        if self.selected == 1:
            self.selected = 0
            # apagar o save
            # apagar o arquivo save.txt

            try:
                os.remove("save.txt")
            except:
                pass

            self.constants.load_game()

            # apagar o arquivo habilities.txt
            
            try:
                os.remove("habilities.txt")
            except:
                pass

            self.constants.restart_tree = True
    
    def update(self):
        self.stars.update()

        
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