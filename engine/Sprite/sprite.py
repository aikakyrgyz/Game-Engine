import os

import pygame

IMG_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'images')


class Sprite:
    def __init__(self, image):
        image = os.path.join(IMG_PATH, image)
        self.image = pygame.image.load(image).convert_alpha()

    def get_surface(self):
        return self.image

    # helper function
    def loadImage(self):
        # need to read the file and convert to an image
        pass

    def set_size(self, w):
        self.w = w