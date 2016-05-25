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
        self.displayPawn(pOne, pTwo)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.focus = False

    def displayPawn(self, pOne, pTwo):
        if pOne == True:
            pygame.draw.circle(self.image, (255, 255, 255), (20, 20), 10)
        elif pTwo == True:
            pygame.draw.circle(self.image, (0, 0, 0), (20, 20), 10)

    def update(self):
        return

    def updateColor(self, color):
        self.color = color
        self.image.fill(self.color)

    def setFocus(self): #rework focus to set with new dispatch
        if self.focus == False:
            if self.isPawn and self.player == '1': # compare with le tour du mec
                color = (41, 95, 255, 0.5) # donner en param et mit en self.tour
            elif self.isPawn and self.player == '2':
                color = (255, 0, 0, 0.5)
            else:
                color = self.originalColor
            self.updateColor(color)
            self.focus = True
        else:
            if self.isPawn and self.player == '1':
                color = (255, 255, 255)
            elif self.isPawn and self.player == '2':
                color = (0, 0, 0)
            else:
                color = self.originalColor
            self.updateColor(color)
            self.focus = False

    def unFocus(self):
        if self.isPawn and self.player == '1':
            color = (255, 255, 255)
        elif self.isPawn and self.player == '2':
            color = (0, 0, 0)
        else:
            color = self.originalColor
        self.updateColor(color)
        self.focus = False

    def determinePlayer(self, pOne, pTwo):
        if pOne == True:
            self.player = '1'
        elif pTwo == True:
            self.player = '2'

    def setColor(self, color):
        self.color = color
        self.originalColor = color
