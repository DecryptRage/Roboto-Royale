import pygame
from pygame.locals import *
from GameObject import GameObject
import random

class objectGenerator(GameObject):

    @staticmethod
    def init():
        objectGenerator.images = {'wood': pygame.image.load('images/wood.png').convert_alpha(),
                                'tree1': pygame.image.load('images/tree1.png').convert_alpha(),
                                'tree2': pygame.image.load('images/tree2.png').convert_alpha(),
                                'well': pygame.image.load('images/well.png').convert_alpha()}

    def __init__(self, x, y):
        obstacle = random.choice(["wood", "tree1", "tree2", "well"])
        w, h = objectGenerator.images[obstacle].get_size()
        image = objectGenerator.images[obstacle]
        image = pygame.transform.scale(image, (int(w * .3), int(h * .3)))
        super(objectGenerator, self).__init__(x, y, image)


    def update(self, screenWidth, screenHeight):
        super(objectGenerator, self).update(screenWidth, screenHeight)

