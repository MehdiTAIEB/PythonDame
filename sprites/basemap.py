import os, sys
import pygame
from pygame.locals import *

class Builder(pygame.sprite.Sprite):
    def __init__(self, x, y, color, isPawn=False, isDame=False):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([40, 40])
        self.x = x
        self.y = y
        self.isPawn = isPawn
        self.isDame = isDame
        if self.isPawn == True:
            self.updateColor((255, 255, 255))
        else:
            self.updateColor(color)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        return
    def updateColor(self, color):
        self.color = color
