#/usr/bin/env python

import os, sys
import pygame
from pygame.locals import *
from sprites.basemap import Builder

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

class Game:
    def __init__(self):
        pygame.init()
        self.speList = {}
        self.target = ''
        screen = pygame.display.set_mode((400, 400))
        pygame.display.set_caption('Jeu de Dame')
        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill((250, 250, 250))

        screen.blit(background, (0, 0))
        pygame.display.flip()

        clock = pygame.time.Clock()
        sprites = self.mapFactory()

        while 1:
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                elif event.type == MOUSEBUTTONDOWN:
                    self.findClickedRect(pygame.mouse.get_pos())
            sprites.update()
            screen.blit(background, (0, 0))
            sprites.draw(screen)
            pygame.display.flip()

    def findClickedRect(self, pos):
        for key, value in self.speList.iteritems():
            row = key[0]
            if self.speList[key].rect.collidepoint(pos):
                self.speList[key].setFocus()
                if self.speList[key].isPawn == False:
                    if self.target != '':
                        print key, self.target
                        self.speList[key].setPawn(self.speList[self.target].player)
                        self.speList[self.target].unsetPawn() #recheck
                        self.target = ''
                        #change le tour
                    # if not a spawn if diagonale so redraw + 10 ou - 10 and limit a une case avec 10 aussi
                else: # change the way to store selftarget to redraw
                    self.target = key
            else:
                self.speList[key].unFocus()

    def getIndex(self, key):
        if len(key) == 3:
            num = str(key[1]) + str(key[2])
        else:
            num = str(key[1])
        return num

    def findPossibleMoves(self, row):
        targets = []
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        for i, c in enumerate(alpha):
            if c == 'a' and c == row:
                targets.append(alpha[i + 1])
            elif c == 'z' and c == row:
                targets.append(alpha[i - 1])
            elif c == row:
                targets.append(alpha[i + 1])
                targets.append(alpha[i - 1])

        return targets

    def mapFactory(self):
        isDame = False
        isPawn = False
        pOne = False
        pTwo = False
        ci = False
        i = 0
        offset = 0
        height = 360
        sp = []
        building = 1

        while building:
            isPawn, pOne, pTwo = self.determineIfPawn(i)
            if i % 10 == 0 and i != 0:
                if ci == False:
                    ci = True
                else:
                    ci = False
                offset = 0
                height = height - 40

            if i <= 100:
                if ci == True:
                    color = self.defineColor(i + 1)
                else:
                    color = self.defineColor(i)
                row = self.storeSprites(offset, height, color, isPawn, isDame, pOne, pTwo, i)
                sp.append(self.speList[row + str(i)])
                offset = offset + 40
                i = i + 1
            else:
                building = 0
        sprites = pygame.sprite.RenderPlain(sp)
        return sprites

    def defineRow(self, i):
        row = ''
        if i < 10:
            row = 'a'
        elif i < 20:
            row = 'b'
        elif i < 30:
            row = 'c'
        elif i < 40:
            row = 'd'
        elif i < 50:
            row = 'e'
        elif i < 60:
            row = 'f'
        elif i < 70:
            row = 'g'
        elif i < 80:
            row = 'h'
        elif i < 90:
            row = 'i'
        elif i < 100:
            row = 'j'
        return row

    def storeSprites(self, offset, height, color, isPawn, isDame, pOne, pTwo, i):
        row = self.defineRow(i)
        self.speList[row + str(i)] = Builder(offset, height, color, isPawn, isDame, pOne, pTwo)
        return row

    def determineIfPawn(self, i):
        pOne = False
        pTwo = False
        cic = i + 1
        if cic % 2 != 0 and i < 9:
            isPawn = True # setup color here or form
            pOne = True
        elif i > 9 and i < 20 and i % 2 != 0:
            isPawn = True
            pOne = True
        elif i >= 20 and i < 30 and i % 2 == 0:
            isPawn = True
            pOne = True
        elif i > 30 and i < 40 and i % 2 != 0:
            isPawn = True
            pOne = True
        elif i >= 60 and i < 70 and i % 2 == 0:
            isPawn = True
            pTwo = True
        elif i > 70 and i < 80 and i % 2 != 0:
            isPawn = True
            pTwo = True
        elif i >= 80 and i < 90 and i % 2 == 0:
            isPawn = True
            pTwo = True
        elif i > 90 and i < 100 and i % 2 != 0:
            isPawn = True
            pTwo = True
        else:
            isPawn = False
        return isPawn, pOne, pTwo

    def defineColor(self, number):
        if (number % 2 == 0):
            color = (99, 57, 0)
        else:
            color = (215, 157, 78)
        return color
Game();
