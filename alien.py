import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, game, x, y) -> None:
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(
            self.image, (self.settings.alien_w, self.settings.alien_h))
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self, direction: int) -> None:
        self.x += direction * self.settings.alien_speed
        self.rect.x = self.x

    def draw_alien(self) -> None:
        self.screen.blit(self.image, self.rect)

    def is_at_edge(self) -> bool:
        screen_rect = self.screen.get_rect()
        return self.rect.right >= screen_rect.right or self.rect.left <= 0

    def reset_position(self, x: int, y: int) -> None:
        self.rect.x = x
        self.rect.y = y
        self.x = float(x)
        self.y = float(y)