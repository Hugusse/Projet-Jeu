import pygame,os
from pygame.locals import *
pygame.init()

def load_sprite_sheet(file_path, num_frames):
    sprite= pygame.image.load(file_path).convert_alpha()

    frame_width = sprite.get_width() // num_frames
    frame_height = sprite.get_height()

    frames = []

    for i in range(num_frames):
        rect = pygame.Rect(i * frame_width, 0, frame_width, frame_height)
        frame = sprite.subsurface(rect)
        frames.append(frame)

    return frames

class Player:
    def __init__(self, spawn, image, player_walked_frames, speed, life):
        self.life = life
        self.speed = speed
        self.image = image
        self.image_left = pygame.transform.flip(image, True, False)
        self.pos = self.image.get_rect().move(spawn)
        self.velocity = 0
        self.jump_strength = 5
        self.state = 'still'
        self.on_ground = False
        self.roll_cooldown = 0
        self.is_rolling = False
        self.facing = 'R'
        self.is_invincible = False
        
        self.animations = {
            'still': [self.image],
            'moveleft': [pygame.transform.flip(frame, True, False) for frame in player_walked_frames],
            'moveright': player_walked_frames,
            'jump': [pygame.image.load(os.path.join("Assets", "Player", "jump.png")).convert()],
            'jump_left': [pygame.transform.flip(pygame.image.load(os.path.join("Assets", "Player", "jump.png")).convert(), True, False)],
            'roll': [pygame.image.load(os.path.join("Assets","Player", "idle.png")).convert()]
        }
        self.animation_index = 0
        self.image = self.animations['still'][self.animation_index]

    def reinit(self,spawn):
        self.pos = self.image.get_rect().move(spawn)
        self.state = 'still'


    def move(self, keys, platforms):
        
        walk_offset = 7

        if self.is_rolling:
            if self.roll_cooldown == 0:
                self.is_rolling = False
            if self.facing == 'L':
                self.pos = self.pos.move(-self.speed * 2, 0)
            if self.facing == 'R':
                self.pos = self.pos.move(self.speed * 2, 0)
            self.roll_cooldown -= 1
            self.update_animation('roll')

        elif keys[K_LEFT]:
            self.pos = self.pos.move(-self.speed, 0)
            self.state = "moveleft"
            self.facing = 'L'
            if self.on_ground:
                self.update_animation('moveleft')
        elif keys[K_RIGHT]:
            self.pos = self.pos.move(self.speed, 0)
            self.state = "moveright"
            self.facing = 'R'
            if self.on_ground:
                self.update_animation('moveright')
        else:
            self.update_animation('still')
            if self.facing == 'R':
                self.image = self.image
            else:
                self.image = self.image_left

        self.velocity += 1
        self.pos = self.pos.move(0, self.velocity)

        self.on_ground = False
        for platform in platforms:
            if platform.check_collision(self.pos) and self.velocity > 0:
                self.pos.bottom = platform.rect.top
                self.velocity = 0
                self.on_ground = True

        if not self.on_ground:
            self.velocity = min(self.velocity, 3)

        if keys[pygame.K_SPACE] and self.on_ground:
            self.velocity = -self.jump_strength
            self.pos = self.pos.move(0, self.velocity)
            if self.facing == 'R' :
                self.update_animation('jump')
            else :
                self.update_animation('jump_left')

        if keys[pygame.K_r] :
            self.is_rolling = True
            self.roll_cooldown = 10
            self.update_animation('roll')
        
        if self.state in ['moveleft', 'moveright']:
            self.image_rect = self.image.get_rect(topleft=self.pos.topleft)
            self.image_rect.y -= walk_offset

    def update_animation(self, state):
        if state not in self.animations or len(self.animations[state]) == 0:
            return
        
        if self.animation_index >= len(self.animations[state]) - 1:
            self.animation_index = 0
        else:
            self.animation_index += 1
        self.image = self.animations[state][self.animation_index]




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