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
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    return
            sprites.update()
            screen.blit(background, (0, 0))
            sprites.draw(screen)
            pygame.display.flip()

    def mapFactory(self):
        isDame = False
        isPawn = False
        ci = False
        i = 0
        offset = 0
        height = 360
        sp = []
        building = 1

        while building:
            if i % 2 and i <= 10:
                isPawn = True
            else:
                isPawn = False
            if i % 10 == 0 and i != 0:
                if ci == False:
                    ci = True
                else:
                    ci = False
                offset = 0
                height = height - 40

            if i < 100:
                if ci == True:
                    color = self.defineColor(i + 1)
                else:
                     color = self.defineColor(i)
                sp.append(Builder(offset, height, color, isPawn, isDame))
                #push in dictionary to get repere
                offset = offset + 40
                i = i + 1
            else:
                building = 0

        sprites = pygame.sprite.RenderPlain(sp)
        return sprites

    def defineColor(self, number):
        if (number % 2 == 0):
            color = (99, 57, 0, 0.9)
        else:
            color = (215, 157, 78, 0.9)
        return color
Game();
