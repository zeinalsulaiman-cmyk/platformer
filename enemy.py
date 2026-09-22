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
