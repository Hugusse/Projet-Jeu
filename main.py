import sys, pygame,os
from pygame.locals import *
print("Répertoire courant :", os.getcwd())
pygame.init()

import entities


screen = pygame.display.set_mode((640,480))
player = pygame.image.load( os.path.join("Ressources", "Joueur.png")).convert()
background = pygame.image.load( os.path.join("Ressources", "BG.png")).convert()
eimage = pygame.image.load(os.path.join("Ressources", "Rat.png")).convert()
screen.blit(background,(0,0))

aliveenemies = []

p = entities.Player((320,240),player,2)

for i in range(10) : #Initialise 10 rats
    e = entities.Rat(i,20*i, eimage)
    aliveenemies.append(e)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_UP:
                print("key up")

    for e in aliveenemies:
        screen.blit(background,(0,0))
    for e in aliveenemies:
        e.move()
        screen.blit(e.image, e.pos)
    screen.blit(p.image,p.pos)
    pygame.display.update()
    pygame.time.delay(50)
    screen.fill((0,0,0))