import os, sys
import pygame
from pygame.locals import *

class Builder(pygame.sprite.Sprite):
    def __init__(self, x, y, color, isPawn=False, isDame=False):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([40, 40])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y
        self.color = color
        self.isPawn = isPawn
        self.isDame = isDame

    def update(self):
        if self.isPawn:
            print 'pawn'
        return
