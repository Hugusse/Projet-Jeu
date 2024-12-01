import sys, pygame,os
print("Répertoire courant :", os.getcwd())
pygame.init()

import enemies


screen = pygame.display.set_mode((640,480))
player = pygame.image.load( os.path.join("Ressources", "Joueur.png")).convert()
background = pygame.image.load( os.path.join("Ressources", "BG.png")).convert()
screen.blit(background,(0,0))

aliveenemies = []

eimage = pygame.image.load(os.path.join("Ressources", "Rat.png")).convert()

for i in range(10) : #Initialise 10 mobs
    e = enemies.Mob1(i,20*i, eimage)
    aliveenemies.append(e)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    for e in aliveenemies:
        screen.blit(background,(0,0))
    for e in aliveenemies:
        e.move()
        screen.blit(e.image, e.pos)
    pygame.display.update()
    pygame.time.delay(100)
    screen.fill((0,0,0))