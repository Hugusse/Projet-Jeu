import pygame
from pygame.locals import *
pygame.init()

class Player:
    def __init__(self,spawn, image, speed,life):
        self.life = life
        self.speed = speed
        self.image = image
        self.pos = self.image.get_rect().move(spawn)
        self.velocity = 0
        self.jump_strength = 5
        self.state = 'still'
        self.on_ground = False
        self.roll_cooldown = 0
        self.is_rolling = False
        self.facing = 'R'
        self.is_invincible = False

    def reinit(self,spawn):
        self.pos = self.image.get_rect().move(spawn)
        self.state = 'still'

    def move(self, keys, platforms):
        if self.is_rolling : 
            if self.roll_cooldown == 0 :
                self.is_rolling = False
            if self.facing == 'L' :
                self.pos = self.pos.move(-self.speed * 2, 0)
            if self.facing == 'R' :
                self.pos = self.pos.move(self.speed * 2, 0)
            self.roll_cooldown -= 1

        if not self.is_rolling:

            if keys[K_LEFT]:
                self.pos = self.pos.move(-self.speed, 0)
                self.state = "moveleft"
                self.facing = 'L'
            if keys[K_RIGHT]:
                self.pos = self.pos.move(self.speed, 0)
                self.state = "moveright"
                self.facing = 'R'
            
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
        
        if keys[pygame.K_r] :
            self.is_rolling = True
            self.roll_cooldown = 10



class Rat: #juste une classe ennemie ap ??
    
    def __init__(self, length, height,image, speed, life):
        self.life = life
        self.speed = speed
        self.image = image
        self.pos = self.image.get_rect().move(length, height)
        self.velocity = 0
        self.on_ground = False
    def move(self,player_position, platforms): #A MODIF : doit avoir un rayon de detection en y mtn + bouger en random et eviter de tomber si player en dehors du rayon
        if self.pos.right - player_position.right < 0 and self.pos.right - player_position.right > -250:
            self.pos = self.pos.move(self.speed, 0)
        if self.pos.left - player_position.left > 0 and self.pos.left - player_position.left < 250:
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
