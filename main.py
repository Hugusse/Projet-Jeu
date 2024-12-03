import sys, pygame,os
from pygame.locals import *
print("Répertoire courant :", os.getcwd())
pygame.init()

import entities


screen = pygame.display.set_mode((640,480))
playerimage = pygame.image.load( os.path.join("Ressources", "Joueur.png")).convert()
background = pygame.image.load( os.path.join("Ressources", "BG.png")).convert()
eimage = pygame.image.load(os.path.join("Ressources", "Rat.png")).convert()
screen.blit(background,(0,0))

aliveenemies = []

clock = pygame.time.Clock()
fps = 10

player = entities.Player((320,240),playerimage,2)

for i in range(10) : #Initialise 10 rats
    e = entities.Rat(i,20*i, eimage)
    aliveenemies.append(e)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == KEYUP:
            keys = pygame.key.get_pressed()
            if not (keys[K_UP] or keys[K_DOWN] or keys[K_LEFT] or keys[K_RIGHT]):
                player.state = "still"

    keys = pygame.key.get_pressed()
    if keys[K_UP]:
        player.move_u()
    if keys[K_DOWN]:
        player.move_d()
    if keys[K_LEFT]:
        player.move_l()
    if keys[K_RIGHT]:
        player.move_r()


    screen.blit(background,(0,0))     
    for enemy in aliveenemies:
        enemy.move()
        screen.blit(enemy.image, enemy.pos)
    
    screen.blit(player.image,player.pos)
    pygame.display.update()
    screen.fill((0,0,0))
    clock.tick(fps)