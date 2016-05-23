import os, sys
import pygame
from pygame.locals import *
from sprites.basemap import Map

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

class Game:
    def __init__(self):
        print('asd')
        test = Map()

Game();
