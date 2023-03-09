import pygame as pg
import sys
from constants import Constants

class Game:
    def __init__(self):
        pg.init()
        pg.mouse.set_visible(False)
        self.running = True
        self.screen = pg.display.set_mode((0,0), pg.FULLSCREEN)
        self.clock = pg.time.Clock()
        self.constants = Constants(self.screen.get_width(), self.screen.get_height())
        
    def update(self):
        pg.display.flip()

    def display_fps(self):
        # display fps at the top of the screen
        font = pg.font.Font('assets/fonts/dogicapixel.ttf', int(self.constants.width/70))
        text = font.render("FPS: " + str(int(self.clock.get_fps())), 1, (255,255,255))
        self.screen.blit(text, (10,10))

    def draw(self):
        self.screen.fill('black')
        # draw point at center of screen
        pg.draw.circle(self.screen, 'white', (self.constants.half_width, self.constants.half_height), 3)

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.running = False

    def run(self):
        while self.running:
            self.check_events()
            self.update()
            self.draw()
            self.display_fps()
        pg.quit()


if __name__ == '__main__':
    game = Game()
    game.run()