import pygame
import math
from GameObject import GameObject

class Bullet(GameObject):
    speed = 10
    time = 50 * 2 # last 2 seconds
    size = 10

    def __init__(self, x, y, anglex, angley, ori):
        if ori:
            self.x = x - 40
        else:
            self.x = x + 40
        self.y = y - 13
        x = anglex
        y = angley

        angle = (180 / math.pi) * -math.atan2((y - self.y), (x - self.x))
        print(angle)
        size = Bullet.size
        image = pygame.Surface((Bullet.size, Bullet.size), pygame.SRCALPHA)
        pygame.draw.circle(image, (255, 255, 255), (size // 2, size // 2), size // 2)
        super(Bullet, self).__init__(self.x, self.y, image)
        vx = Bullet.speed * math.cos(math.radians(angle))
        vy = -Bullet.speed * math.sin(math.radians(angle))
        self.velocity = vx, vy
        self.timeOnScreen = 0

    def update(self, screenWidth, screenHeight):
        self.image = pygame.transform.rotate(self.baseImage, self.angle)
        vx, vy = self.velocity
        self.x += vx
        self.y += vy
        self.updateRect()
        self.timeOnScreen += 1
        if self.timeOnScreen > Bullet.time:
            self.kill()