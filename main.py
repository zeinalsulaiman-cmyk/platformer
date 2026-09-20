import pygame
import settings

#player.py und enemy.py importieren
from player import Player
from enemy import Enemy

#pygame starten
pygame.init()


#Spiel Fenster
screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
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
    screen.fill((settings.COLORS["sky"]))
    pygame.display.flip()

#FPS
    clock.tick(settings.FPS)

##



pygame.quit()
