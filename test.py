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
        screen = pygame.display.set_mode((900, 600))
        pygame.display.set_caption('Jeu de Dame')
        # all the miscs Map()
        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill((250, 250, 250))

        screen.blit(background, (0, 0))
        pygame.display.flip()

        clock = pygame.time.Clock()
        builder = Builder()
        sprites = pygame.sprite.RenderPlain((builder))

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

Game();
