import pygame

class Enemy:
    def __init__(self, x, y):
        #position
        self.x = x
        self.y = y
        #größe
        self.width = 40
        self.height = 60
        #hitbox
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        #bewegung
        self.speed = 2


    def draw(self, screen):
        pygame.draw.rect(screen, (200, 0, 0), self.rect)

    def update(self):
        self.rect.x += self.speed