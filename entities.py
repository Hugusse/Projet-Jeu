import pygame
pygame.init()

class Player:
    def __init__(self,spawn, image, speed):
        self.speed = speed
        self.image = image
        self.pos = self.image.get_rect().move(spawn)
        self.state = 'still'

    def reinit(self,spawn):
        self.pos = self.image.get_rect().move(spawn)
        self.state = 'still'

    def move_u(self):
        self.pos = self.pos.move(0, -self.speed)
        self.state = "moveup"

    def move_d(self):
        self.pos = self.pos.move(0, self.speed)
        self.state = "movedown"

    def move_l(self):
        self.pos = self.pos.move(-self.speed, 0)
        self.state = "moveleft"

    def move_r(self):
        self.pos = self.pos.move(self.speed, 0)
        self.state = "moveright"



class Rat:
    speed = 1
    def __init__(self, length, height,image):
        self.image = image
        self.pos = self.image.get_rect().move(length, height)
    def move(self): #A MODIF : doit faire avancer le mob vers le joueur mais on fera ca apres une fois qu'on aura def le joueur
        self.pos = self.pos.move(self.speed, 0)
        if self.pos.right >= 640:
            self.speed = -(self.speed)
        if self.pos.left <= 0:
            self.speed = -(self.speed)