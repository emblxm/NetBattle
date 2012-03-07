import sys
import pygame
from pygame.locals import *

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

BASIC = "g"

TILES = {
    "g": pygame.image.load("resources/img/basicTile.png"),
    "s": pygame.image.load("resources/img/stripTile.png")
}


class Map(object):
    def __init__(self, data):
        self.table = data

    def createMap(self):
        y = 0
        mapTable = []
        for line in self.table:
            x = 0
            for t in line.split(","):
                if t in TILES:
                    mapTable.append(Tile(t, x, y))
                x += 1
            y += 1

        return mapTable


class Tile(object):
    def __init__(self, ttype, x, y):
        self.tile = TILES[ttype]
        self.x, self.y = ((x * 30) + (y * 30)), ((y * 15) + (x * -15))
        self.speed_multi = 1

    def pyCoord(self, x, y):
        return x * -62, y * 31

    def drawTile(self, surf, offx, offy):
        surf.blit(self.tile, (self.x - offx, self.y - offy))


class Player(object):
    def __init__(self):
        self.image = pygame.image.load("resources/img/megarotate.gif")
        self.offset_x = self.offset_y = 0

    def handleInput(self):
        keys = pygame.key.get_pressed()
        if keys[K_LSHIFT]:
            self.speed_multi = 2
        else:
            self.speed_multi = 1
        if keys[K_w]:
            self.offset_y -= .15 * self.speed_multi
        if keys[K_a]:
            self.offset_x -= .3 * self.speed_multi
        if keys[K_s]:
            self.offset_y += .15 * self.speed_multi
        if keys[K_d]:
            self.offset_x += .3 * self.speed_multi

    def drawPlayer(self, disp):
        disp.blit(self.image, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))


def main():

    map1 = Map(open("map1.txt", "r")).createMap()

    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Turd")
    done = False

    player = Player()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        screen.fill((255, 255, 255))

        player.handleInput()

        for tile in map1:
            tile.drawTile(screen, player.offset_x, player.offset_y)

        player.drawPlayer(screen)

        pygame.display.flip()

if __name__ == '__main__':
    sys.exit(main())
