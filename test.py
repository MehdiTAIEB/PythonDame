#/usr/bin/env python

import os, sys
import pygame
from pygame.locals import *
from sprites.basemap import Map

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

class Game:
    def __init__(self):
        pygame.init()
        screen = pygame.display.set_mode((468, 60))
        pygame.display.set_caption('Jeu de Dame')
        # all the miscs Map()
        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill((250, 250, 250))

        screen.blit(background, (0, 0))
        pygame.display.flip()

        clock = pygame.time.Clock()

        while 1:
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    return

    def load_image(name, color=None):
        fullname = os.path.join('misc', name)
        try:
            image = pygame.image.load(fullname)
        except pygame.error, message:
            print 'Cannot load image:', fullname
            raise SystemExit, message
        image = image.convert()
        if colorkey is not None:
            if color is -1:
                color = image.get_at((0,0))
            image.set_colorkey(color, RLEACCEL)
        return image, image.get_rect()

    def load_sound(name):
        class NoneSound:
            def play(self): pass
        if not pygame.mixer or not pygame.mixer.get_init():
            return NoneSound()
        fullname = os.path.join('misc', name)
        try:
            sound = pygame.mixer.Sound(fullname)
        except pygame.error, message:
            print 'Cannot load sound:', fullname
            raise SystemExit, message
        return sound

Game();
