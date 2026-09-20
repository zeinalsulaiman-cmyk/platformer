import pygame

import settings
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
    pygame.display.set_caption("Platformer")
    clock = pygame.time.Clock()

    player = Player(100, settings.HEIGHT - 100)
    all_sprites = pygame.sprite.Group(player)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        all_sprites.update(keys)

        screen.fill(settings.COLORS["sky"])
        pygame.draw.rect(
            screen,
            settings.COLORS["ground"],
            (0, settings.HEIGHT - 40, settings.WIDTH, 40),
        )
        all_sprites.draw(screen)

        pygame.display.flip()
        clock.tick(settings.FPS)

    pygame.quit()


if __name__ == "__main__":
    main()