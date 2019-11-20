import pygame
import math
from GameObject import GameObject


class Player(GameObject):

    @staticmethod
    def init():
        images = [pygame.image.load('images/Robot_Light_1.png').convert_alpha(),
                        pygame.image.load('images/Robot_Light_2.png').convert_alpha(),
                        pygame.image.load('images/Robot_Light_3.png').convert_alpha()]
        Player.images = []
        factor = .2
        for player in images:
            w, h = player.get_size()
            Player.images.append(pygame.transform.scale(player, (int(w * factor), int(h * factor))))

    def __init__(self, x, y):
        self.count = 0
        self.images = Player.images
        super(Player, self).__init__(x, y, Player.images[self.count])
        self.health = 100
        self.hasGun = False

        self.angle = 0  
        self.invincibleTime = 1500
        self.timeAlive = 0

        self.speed = 5
        self.faceLeft = True

    def grabGun(self):
        self.hasGun = True

    def checkForFlip(self, x, y):
        if x > self.x and self.faceLeft:
            self.faceLeft = False
            for i in range(len(self.images)):
                self.images[i] = pygame.transform.flip(self.images[i], True, False)
            self.run(0)
            return True
        elif x < self.x and not self.faceLeft:
            self.faceLeft = True
            for i in range(len(self.images)):
                self.images[i] = pygame.transform.flip(self.images[i], True, False)
            self.run(0)
            return True
        return False

    def update(self, dt, keysDown, screenWidth, screenHeight):
        self.timeAlive += dt

        if keysDown(pygame.K_w):
            self.run(dt)
            self.y -= self.speed
        elif keysDown(pygame.K_s):
            self.run(dt)
            self.y += self.speed
        elif keysDown(pygame.K_a):
            self.run(dt)
            self.x -= self.speed
        elif keysDown(pygame.K_d):
            self.run(dt)
            self.x += self.speed


        super(Player, self).update(screenWidth, screenHeight)


    def run(self, dt):
        if(dt % 5 == 0):
            self.count += 1
            if self.count >= len(self.images):
                self.count = 0
            self.image = self.images[self.count]

    def isInvincible(self):
        return self.timeAlive < self.invincibleTime
