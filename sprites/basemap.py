import os, sys
import pygame
from pygame.locals import *

class Builder(pygame.sprite.Sprite):
    def __init__(self, x, y, color, isPawn=False, isDame=False, pOne=False, pTwo=False):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([50, 50])
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
            if self.isPawn and self.player == 1:
                pygame.draw.circle(self.image, (0,250,0), (5,5), 5)
            elif self.isPawn and self.player == 2:
                pygame.draw.circle(self.image, (250,0,0), (5,5), 5)
            self.focus = True
        else:
            self.unFocus()

    def unFocus(self):
        if self.isPawn and self.player == 1:
            pygame.draw.circle(self.image, (self.originalColor), (5,5), 5)
        elif self.isPawn and self.player == 2:
            pygame.draw.circle(self.image, (self.originalColor), (5,5), 5)
        else:
            color = self.originalColor
        self.focus = False

    def determinePlayer(self, pOne, pTwo):
        if pOne == True:
            self.player = 1
        elif pTwo == True:
            self.player = 2

    def setColor(self, color):
        self.color = color
        self.originalColor = color

    def setPawn(self, player):
        self.isPawn = True
        self.player = player # fake now must resolve
        if player == 1:
            one = True
            two = False
        else:
            one = False
            two = True
        self.displayPawn(one, two)
        self.focus = False

    def unsetPawn(self):
        self.isPawn = False
        self.player = 0
        self.focus = False
        self.updateColor(self.originalColor)
