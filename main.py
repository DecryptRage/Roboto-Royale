
import pygame
from mapgeneration import *
from bullets import Bullet
from pygamegame import PygameGame
from player import Player
from gun import Gun
import random


class Game(PygameGame):
    def init(self):
        self.bgColor = (11, 102, 35)
        Player.init()
        self.player = Player(self.width / 2, self.height / 2)
        self.playerGroup = pygame.sprite.Group(self.player)

        Gun.init()
        self.guns = pygame.sprite.Group()
        for i in range(3):
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            self.guns.add(Gun(x, y))

        objectGenerator.init()
        self.objectSet = pygame.sprite.Group()
        self.objectCoor = [(0,0)]
        self.test = objectGenerator(0, 0)
        while len(self.objectCoor) < 8:
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            if not self.isTouching(x, y):
                self.objectCoor.append((x,y))
                self.objectSet.add(objectGenerator(x, y))

        self.bullets = pygame.sprite.Group()

        self.roads = set()
        number = random.randint(1, 2)
        for i in range(number):
            self.roads.add(self.selectRoads())

    def isTouching(self, x, y):
        for coords in self.objectCoor:
                prevX, prevY = coords
                if abs(x-prevX) < self.test.radius or abs(y - prevY) < self.test.radius:
                    return True
        else:
            return False

    def keyPressed(self, code, mod):
        if code == pygame.K_SPACE:
            pass
        if code == pygame.K_g:
            for gun in self.guns:
                if ((self.player.x + self.player.radius) > gun.x and
                    (self.player.x - self.player.radius) < gun.x and
                    (self.player.y + self.player.radius) > gun.y and
                    (self.player.y - self.player.radius) < gun.y and
                    not self.player.hasGun):
                    self.player.grabGun()
                    gun.canShoot = True


    def mouseMotion(self, x, y):
        self.mouseX = x
        self.mouseY = y
        self.player.checkForFlip(self.mouseX, self.mouseY)
        for gun in self.guns:
            if gun.canShoot:
                gun.rotateGun(self.mouseX, self.mouseY, self.player.faceLeft)

    def mousePressed(self, x, y):
        if self.player.hasGun:
            self.bullets.add(Bullet(self.player.x, self.player.y, x, y, self.player.faceLeft))


    def timerFired(self, dt):
        self.playerGroup.update(dt, self.isKeyPressed,
                                self.width, self.height)

        self.bullets.update(self.width, self.height)

        """
        if ((not self.player.isInvincible()) and
             pygame.sprite.groupcollide(
             self.playerGroup, self.bullets, False, False,
             pygame.sprite.collide_circle)):

            self.player.health -= 20
            self.bullets.kill()"""

        for gun in self.guns:
            if gun.canShoot:
                gun.update(self.player.x, self.player.y, self.player.faceLeft, self.width, self.height)

        """if (pygame.sprite.groupcollide(
             self.playerGroup, self.objectSet, False, False,
             pygame.sprite.collide_circle)):"""
        
    def selectRoads(self):
        minNum = min(self.width, self.height)
        maxNum = int(minNum / 20)
        thick = random.randint(0, maxNum)
        loc = random.randint(0, minNum)
        ori = random.choice(["hor", "vert"])
        return (thick, loc, ori)
        

    def drawRoads(self, screen):
        for road in self.roads:
            (thick, loc, ori) = road
            GRAY = (112, 128, 144)
            if ori == "vert":
                pygame.draw.rect(screen,GRAY,(loc,0,loc + thick,self.height))
            else:
                pygame.draw.rect(screen,GRAY,(0,loc, self.width,loc + thick))

    def redrawAll(self, screen):
        self.drawRoads(screen)
        self.playerGroup.draw(screen)
        self.guns.draw(screen)
        self.bullets.draw(screen)
        self.objectSet.draw(screen)

Game(800, 500).run()