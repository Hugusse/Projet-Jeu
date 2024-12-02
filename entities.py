import pygame
pygame.init()

class Player:
    def __init__(self, image, speed):
        self.speed = speed
        self.image = image
        self.pos = self.image.get_rect()
    def move(self,x,y):
        self.pos = self.pos.move(self.speed*x,self.speed*y)


class Rat:
    speed = 10
    def __init__(self, length, height,image):
        self.image = image
        self.pos = self.image.get_rect().move(length, height)
    def move(self): #A MODIF : doit faire avancer le mob vers le joueur mais on fera ca apres une fois qu'on aura def le joueur
        self.pos = self.pos.move(self.speed, 0)
        if self.pos.right >= 640:
            self.speed = -(self.speed)
        if self.pos.left <= 0:
            self.speed = -(self.speed)