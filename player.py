import pygame

import settings


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((24, 32))
        self.image.fill(settings.COLORS["player"])
        self.rect = self.image.get_rect(topleft=(x, y))
        self.vel_y = 0

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= settings.PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            self.rect.x += settings.PLAYER_SPEED
        if keys[pygame.K_SPACE] and self.on_ground():
            self.vel_y = -settings.PLAYER_JUMP

        self.vel_y += settings.GRAVITY
        self.rect.y += self.vel_y

        if self.on_ground():
            self.vel_y = 0
            self.rect.bottom = settings.HEIGHT - 40

        self.rect.x = max(0, min(self.rect.x, settings.WIDTH - self.rect.width))

    def on_ground(self):
        return self.rect.bottom >= settings.HEIGHT - 40