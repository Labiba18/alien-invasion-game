import pygame
from typing import TYPE_CHECKING
from pygame.sprite import Sprite

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from ship import Ship

class Bullet(Sprite):
    def __init__(self, game: 'AlienInvasion', ship: 'Ship') -> None:
        super().__init__()

        self.screen = game.screen
        self.settings = game.settings

        self.image = pygame.image.load(self.settings.bullet_file)
        self.image = pygame.transform.scale(
            self.image,
            (self.settings.bullet_w, self.settings.bullet_h)
        )

        self.rect = self.image.get_rect()
        self.rect.midtop = ship.rect.midtop  # fixed: use ship.rect
        self.y = float(self.rect.y)

    def update(self) -> None:
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self) -> None:
        self.screen.blit(self.image, self.rect)