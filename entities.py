import pygame
from pygame.locals import *
pygame.init()

class Player:
    def __init__(self,spawn, image, speed):
        self.speed = speed
        self.image = image
        self.pos = self.image.get_rect().move(spawn)
        self.velocity = 0
        self.jump_strength = 5
        self.state = 'still'
        self.on_ground = False

    def reinit(self,spawn):
        self.pos = self.image.get_rect().move(spawn)
        self.state = 'still'

    def move(self, keys, platforms):
        if keys[K_LEFT]:
            self.pos = self.pos.move(-self.speed, 0)
            self.state = "moveleft"
        if keys[K_RIGHT]:
            self.pos = self.pos.move(self.speed, 0)
            self.state = "moveright"
        
        self.velocity += 1
        self.pos = self.pos.move(0,self.velocity)

        self.on_ground = False
        for platform in platforms:
            if platform.check_collision(self.pos) and self.velocity > 0:
                self.pos.bottom = platform.rect.top
                self.velocity = 0
                self.on_ground = True

        if not self.on_ground:
            self.velocity = min(self.velocity, 3)

        if keys[K_SPACE]:
            if self.on_ground:
                self.velocity = -self.jump_strength
                self.pos = self.pos.move(0,self.velocity)


class Rat:
    speed = 1
    def __init__(self, length, height,image):
        self.image = image
        self.pos = self.image.get_rect().move(length, height)
        self.velocity = 0
        self.on_ground = False
    def move(self,player_position, platforms): #A MODIF : doit avoir un rayon de detection + et eviter de tomber si player en dehors du rayon
        if self.pos.right - player_position.right < 0 :
            self.pos = self.pos.move(self.speed, 0)
        if self.pos.left - player_position.left > 0 :
            self.pos = self.pos.move(-self.speed, 0)
        # if self.pos.right >= 640:
        #     self.speed = -(self.speed)
        # if self.pos.left <= 0:
        #     self.speed = -(self.speed)
        
        self.velocity += 1
        self.pos = self.pos.move(0,self.velocity)

        self.on_ground = False
        for platform in platforms:
            if platform.check_collision(self.pos) and self.velocity > 0:
                self.pos.bottom = platform.rect.top
                self.velocity = 0
                self.on_ground = True

        if not self.on_ground:
            self.velocity = min(self.velocity, 3)


class Platform:
    def __init__(self, x, y, width, height, color=(255, 255, 255)):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def check_collision(self, player_rect):
        return self.rect.colliderect(player_rect)
