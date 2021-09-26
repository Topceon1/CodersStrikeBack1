import pygame as pg

from car import *

pg.init()
FPS = 60
clock = pg.time.Clock()
sc = pg.display.set_mode((600, 400))
car1 = Car(55, 80)
while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
    sc.fill((0, 0, 0))
    keys = pg.key.get_pressed()
    car1.x += 1
    pg.draw.circle(sc, (10, 30, 200), [car1.x, car1.y], 30)
    pg.display.flip()
    clock.tick(FPS)
