import pygame


class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super(GameObject, self).__init__()
        # x, y define the center of the object
        self.x, self.y, self.image = x, y, image
        self.baseImage = image.copy()
        w, h = image.get_size()
        self.radius = w / 2
        self.velocity = (0, 0)
        self.angle = 0
        self.updateRect()

    def updateRect(self):
        # update the object's rect attribute with the new x,y coordinates
        w, h = self.image.get_size()
        self.width, self.height = w, h
        self.rect = pygame.Rect(self.x - w / 2, self.y - h / 2, w, h)

    def update(self, screenWidth, screenHeight):
        self.updateRect()