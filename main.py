import pygame as pg
import sys
from constants import Constants
from menu import Menu
from pause import Pause
from play import Play
from settings import Settings

class Game:
    def __init__(self):
        pg.init()
        pg.mouse.set_visible(False)
        self.screen = pg.display.set_mode((0,0), pg.FULLSCREEN)
        self.clock = pg.time.Clock()
        self.constants = Constants(self.screen.get_width(), self.screen.get_height())
        self.menu = Menu(self.screen, self.constants)
        self.pause = Pause(self.screen, self.constants)
        self.play = Play(self.screen, self.constants)
        self.settings = Settings(self.screen, self.constants)
        # 0 = menu, 1 = game, 2 = pause, 3 = cutscene

    def display_fps(self):
        # display fps at the top of the screen
        font = pg.font.Font('assets/fonts/dogicapixel.ttf', int(self.constants.font_size))
        text = font.render("FPS: " + str(int(self.clock.get_fps())), 1, (200,200,200))
        self.screen.blit(text, (10,10))
        self.constants.actual_fps = self.clock.get_fps()

    def run(self):
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
            self.display_fps()
            pg.display.flip()
        pg.quit()


if __name__ == '__main__':
    game = Game()
    game.run()

    