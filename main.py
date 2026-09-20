import pygame

#player.py und enemy.py importieren
from player import Player
from enemy import Enemy

#pygame starten
pygame.init()


#Spiel Fenster
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Dark Fantasy")

#FPS / Spiel Uhr
clock = pygame.time.Clock()

#player und enemy erstellen
player = Player()
enemy = Enemy()

#Spiel Schleife

running=True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#Hintergrund grau
    screen.fill((30, 30, 30))
    pygame.display.flip()

#FPS
    clock.tick(60)

##



pygame.quit()
