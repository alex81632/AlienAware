import pygame as pg
import sys
from constants import Constants
from menu import Menu
from pause import Pause
from play import Play

class Game:
    def __init__(self):
        pg.init()
        pg.mouse.set_visible(False)
        self.running = True
        self.screen = pg.display.set_mode((0,0), pg.FULLSCREEN)
        self.clock = pg.time.Clock()
        self.constants = Constants(self.screen.get_width(), self.screen.get_height())
        self.menu = Menu(self.screen, self.constants)
        self.pause = Pause(self.screen, self.constants)
        self.play = Play(self.screen, self.constants)
        # 0 = menu, 1 = game, 2 = pause, 3 = cutscene
        self.state = 0 

    def display_fps(self):
        # display fps at the top of the screen
        font = pg.font.Font('assets/fonts/dogicapixel.ttf', int(self.constants.width/70))
        text = font.render("FPS: " + str(int(self.clock.get_fps())), 1, (200,200,200))
        self.screen.blit(text, (10,10))

    def cutscene(self):
        pass

    def run(self):
        while self.running:
            self.clock.tick(self.constants.fps)
            if self.state == 0:
                self.menu.state = 0
                self.running = self.menu.check_events()
                self.state = self.menu.update()
                self.menu.draw()
            elif self.state == 1:
                self.play.state = 1
                self.running = self.play.check_events()
                self.state = self.play.update()
                self.play.draw()
            elif self.state == 2:
                self.pause.state = 2
                self.running = self.pause.check_events()
                self.state = self.pause.update()
                self.pause.draw()
            elif self.state == 3:
                self.cutscene()
            self.display_fps()
        pg.quit()


if __name__ == '__main__':
    game = Game()
    game.run()

    