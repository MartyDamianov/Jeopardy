import numpy as np
import pygame
import os

pygame.init()
class button(pygame.sprite.Sprite):
    def __init__(self, image, func, speed, x, y, num, mul, param):
        super(button, self).__init__()
        self.Image = image
        self.image_name = os.path.realpath(f"{image}.png")
        self.image = pygame.image.load(self.image_name)

        self.count = 0
        self.num = num
        self.num2 = 0
        self.size2 = pygame.image.load(self.image_name).get_rect().size
        self.size = (self.size2[0] / self.num, self.size2[1] / self.num)
        self.image = pygame.transform.scale(self.image, self.size)
        self.surface = self.image.convert(self.image)

        self.func = func
        self.x = x - (667 / (self.num * 2))
        self.y = y - (290 / (self.num * 2))

        self.index = 0
        self.speed = speed
        self.param = param
        self.sin = np.sin(np.linspace(0, 2 * np.pi, 50)) * mul

        self.rectangle = self.surface.get_rect()
        self.rectangle.center = [self.x, self.y]

    def shared(self, image):
        self.Image = image
        self.image_name = os.path.realpath(f"{image}.png")
        self.image = pygame.image.load(self.image_name)
        self.size2 = pygame.image.load(self.image_name).get_rect().size
        self.size = (self.size2[0] / self.num, self.size2[1] / self.num)
        self.image = pygame.transform.scale(self.image, self.size)

    def update(self, images):
        self.count = self.count + 1
        if self.count > 1:
            self.count = 0
        image = images[self.count]
        self.shared(image)

    def set(self, image):
        self.count = 0
        self.shared(image)
        
    def collide(self):
        x2, y2 = self.rectangle.center
        x, y = pygame.mouse.get_pos()
        if x > x2 and x < (x2 + self.size[0]) and y > y2 and y < (y2 + self.size[1]):
            return True
        return False

    def draw(self, window):
        self.num2 = self.num2 + 1
        self.index = self.index + self.speed
        if round(self.index, 1) == 49.5:
            self.index = 0
        self.rectangle.center = [self.x, self.y + self.sin[round(self.index)]]

        collide = self.collide()#self.rectangle.collidepoint(pygame.mouse.get_pos())
        if collide and pygame.mouse.get_pressed()[0] and self.num2 > 10:
            if self.param != None:
                self.func(self.param)
            elif self.param == None:
                self.func()
            self.num2 = 0
                
        window.blit(self.image, self.rectangle.center)



        
