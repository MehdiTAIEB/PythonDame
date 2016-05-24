import os, sys
import pygame
from pygame.locals import *

class Builder(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10, 10])
        self.image.fill((0, 0, 0, 0))
        self.rect = self.image.get_rect()

    def update(self):
         return

    def load_image(self, name, color=None):
        fullname = os.path.abspath("misc/image/" + name)
        try:
            image = pygame.image.load(fullname)
        except pygame.error, message:
            print 'Cannot load image:', fullname
            raise SystemExit, message
        image = image.convert()
        if color is not None:
            if color is -1:
                color = image.get_at((0,0))
            image.set_colorkey(color, RLEACCEL)
        return image, image.get_rect()

    def load_sound(self, name):
        class NoneSound:
            def play(self): pass
        if not pygame.mixer or not pygame.mixer.get_init():
            return NoneSound()
        fullname = os.path.abspath("misc/sound/" + name)
        try:
            sound = pygame.mixer.Sound(fullname)
        except pygame.error, message:
            print 'Cannot load sound:', fullname
            raise SystemExit, message
        return sound

