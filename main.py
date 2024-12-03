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
fps = 30

player = entities.Player((320,240),playerimage,2)

platforms = [
    entities.Platform(0, 300, 400, 20, (0, 255, 0)),  # Plateforme verte
    entities.Platform(0, 200, 640, 20, (255, 0, 0)),  # Plateforme rouge
]

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
    player.move(keys, platforms)


    screen.blit(background,(0,0))     
    for enemy in aliveenemies:
        enemy.move(player.pos,platforms)
        screen.blit(enemy.image, enemy.pos)
    
    for platform in platforms:
        platform.draw(screen)
    screen.blit(player.image,player.pos)
    pygame.display.update()
    screen.fill((0,0,0))
    clock.tick(fps)