import pygame as pg
import sys
from constants import Constants
from menu import Menu
from pause import Pause
from play import Play
from settings import Settings
from mapTransitions import mapTransitions
from saveState import saveState
from tutorial import Tutorial

class Game:
    def __init__(self):
        """ Initialize the game window, etc. """
        pg.init()
        pg.mouse.set_visible(False)
        self.screen = pg.display.set_mode((0,0), pg.FULLSCREEN)
        self.constants = Constants(self.screen.get_width(), self.screen.get_height())
        self.font = pg.font.Font('assets/fonts/dogicapixel.ttf', int(self.constants.font_size))
        # loading screen
        self.screen.fill((0,0,0))
        text = self.font.render("Loading...", 1, (200,200,200))
        self.screen.blit(text, (self.screen.get_width()/2 - text.get_width()/2, self.screen.get_height()/2 - text.get_height()/2))
        pg.display.flip()
        self.clock = pg.time.Clock()
        self.menu = Menu(self.screen, self.constants)
        self.pause = Pause(self.screen, self.constants)
        self.play = Play(self.screen, self.constants)
        self.settings = Settings(self.screen, self.constants)
        self.mapTransitions = mapTransitions(self.screen, self.constants)
        self.saveState = saveState(self.screen, self.constants)
        self.tutorial = Tutorial(self.screen, self.constants)
        
        
        # 0 = menu, 1 = game, 2 = pause, 3 = settings, 4 = mapTransitions, 5 = habilityTree, 6 = saves, 7 = tutorial

    def display_fps(self):
        ''' Show the programs FPS in the window handle.'''
        # display fps at the top of the screen
        text = self.font.render("FPS: " + str(int(self.clock.get_fps())), 1, (200,200,200))
        # fundo preto para o texto do tamanho do texto
        pg.draw.rect(self.screen, (0,0,0), (10,self.screen.get_height()-text.get_height()-10, text.get_width(), text.get_height()))
        self.screen.blit(text, (10,self.screen.get_height()-text.get_height()-10))
        self.constants.actual_fps = self.clock.get_fps()

    def run(self):
        ''' Run the game loop.'''
        while self.constants.running:
            self.constants.dt = self.clock.tick(self.constants.fps)
            if self.constants.state == 0:
                self.menu.check_events()
                self.menu.update()
                self.menu.draw()
            elif self.constants.state == 1:
                self.play.check_events()
                self.play.update()
                self.play.draw()
            elif self.constants.state == 2:
                self.pause.check_events()
                self.pause.update()
                self.pause.draw()
            elif self.constants.state == 3:
                self.settings.check_events()
                self.settings.update()
                self.settings.draw()
            elif self.constants.state == 4:
                self.mapTransitions.draw()
            elif self.constants.state == 5:
                self.play.habilityTree.check_events()
                self.play.habilityTree.update()
                self.play.habilityTree.draw()
            elif self.constants.state == 6:
                self.saveState.check_events()
                self.saveState.update()
                self.saveState.draw()
            elif self.constants.state == 7:
                self.tutorial.check_events()
                self.tutorial.draw()
            self.display_fps()
            pg.display.flip()
        pg.quit()


if __name__ == '__main__':
    ''' Create an instance of the Game class and start the game loop.'''
    game = Game()
    game.run()
