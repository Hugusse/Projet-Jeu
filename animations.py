import sys, pygame,os
from pygame.locals import *
pygame.init()


class AnimationManager:
    def __init__(self):
        self.animations = {}

    def extract_frames(sprite, frame_width, frame_height, num_frames):
        frames = []
        for i in range(num_frames):
            frame = sprite.subsurface(pygame.Rect(i * frame_width, 0, frame_width, frame_height))
            frames.append(frame)
        return frames

    def load_animations(self): #On charge toutes les animations
        self.animations['moveright'] = self.extract_frames(os.path.join("Assets","Player", "walk.png"), 22, 136, 8)
        self.animations['moveleft'] = self.extract_frames(os.path.join("Assets","Player", "walk.png"), 22, 136, 8)
        self.animations['still'] = self.image
        # self.animations['jump'] = self.extract_frames(self.sprite_sheet, 22, 136, 4)  # Ajoute 'jump'
        # self.animations['roll'] = self.extract_frames(self.sprite_sheet, 22, 136, 6)  # Ajoute 'roll'

    def get_animation(self, state):
        return self.animations.get(state, [])