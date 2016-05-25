import os, sys
import pygame
from pygame.locals import *

class Builder(pygame.sprite.Sprite):
    def __init__(self, x, y, color, isPawn=False, isDame=False, pOne=False, pTwo=False):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([40, 40])
        self.x = x
        self.y = y
        self.isPawn = isPawn
        self.isDame = isDame
        self.determinePlayer(pOne, pTwo)
        self.setColor(color)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        return

    def updateColor(self, color):
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

    def determinePlayer(self, pOne, pTwo):
        if pOne == True:
            self.player = '1'
        elif pTwo == True:
            self.player = '2'

    def setColor(self, color):
        if self.isPawn == True:
            if self.player == '1':
                self.color = (255, 255, 255)
            else:
                self.color = (0, 0, 0)
        else:
            self.color = color
