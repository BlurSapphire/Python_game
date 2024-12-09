import pygame as pg
import sys
from player import Player
from settings import *
from random import randint
from debug import debug


def init():
    pg.init()


def event_handler():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()


class Window():
    def __init__(self):
        init()
        self.win = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Dungeon Master v0.02")
        icon = pg.image.load("res/icon/role-playing-game.png").convert()
        pg.display.set_icon(icon)
        self.clock = pg.time.Clock()
        self.dt = 0
        self.visible_sprites = pg.sprite.Group()

        for x in range(1):
            for y in range(1):
                self.player = Player((x*10, y*10),self.visible_sprites)

    def render(self):
        self.win.fill((214, 195, 201))
        self.visible_sprites.draw(self.win)

        debug(f'FPS[{self.clock.get_fps() :.0f}]')
        pg.display.flip()

    def update(self):
        self.dt = self.clock.tick(148) / 1000
        self.visible_sprites.update(self.dt)

    def run(self):
        while 1:
            event_handler()
            self.render()
            self.update()


if __name__ == '__main__':
    window = Window()
    window.run()
