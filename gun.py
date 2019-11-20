import pygame
import math
from GameObject import GameObject


class Gun(GameObject):
    # we only need to load the image once, not for every ship we make!
    #   granted, there's probably only one ship...

    @staticmethod
    def init():
        Gun.gunImage = pygame.image.load('images/lasergun.png').convert_alpha()

    def __init__(self, x, y):
        w, h = Gun.gunImage.get_size()
        gun = pygame.transform.scale(Gun.gunImage, (int(w * .2), int(h * .2)))
        super(Gun, self).__init__(x, y, gun)
        self.originalImage = self.image
        self.canShoot = False
        self.marginX = 20
        self.marginY = 10

    def update(self, x, y, ori, width, height):
        self.x = x + self.marginX
        self.y = y - self.marginY
        if ori:
            self.image = pygame.transform.flip(self.image, True, False)
            self.x -= 2 * self.marginX

        super(Gun, self).update(width, height)
        
    def rotateGun(self, x, y, ori):
        if ori:
            image = pygame.transform.flip(self.originalImage, False, True)
            angle = angle = (180 / math.pi) * math.atan2((y - self.y), (self.x - x))
        else:
            image = self.originalImage
            angle = (180 / math.pi) * -math.atan2((y - self.y), (x - self.x))
        self.image = pygame.transform.rotate(image, int(angle))
        self.rect = self.image.get_rect(center=(self.x, self.y))