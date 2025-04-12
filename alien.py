import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class Alien(Sprite):
    def __init__(self, game: 'AlienInvasion', x: float, y: float) -> None:
        super().__init__()

        self.screen = game.screen
        self.boundaries = game.screen.get_rect()
        self.settings = game.settings

        # Load, scale, and rotate the alien image to face left
        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(
            self.image,
            (self.settings.alien_w, self.settings.alien_h)
        )
        self.image = pygame.transform.rotate(self.image, -90)

        self.rect = self.image.get_rect()

        # Place the alien on the right side of the screen
        self.rect.right = self.boundaries.right
        self.rect.y = y

        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def update(self) -> None:
        """Move the alien downward and bounce back at edges."""
        temp_speed = self.settings.fleet_speed

        if self.check_edges():
            self.settings.fleet_direction *= -1
            self.x -= self.settings.fleet_drop_speed

        self.y += temp_speed * self.settings.fleet_direction
        self.rect.x = self.x
        self.rect.y = self.y

    def check_edges(self) -> bool:
        """Return True if alien has hit the top or bottom edge of screen."""
        return (
            self.rect.top <= self.boundaries.top or
            self.rect.bottom >= self.boundaries.bottom
        )

    def draw_alien(self) -> None:
        """Draw the alien on the screen."""
        self.screen.blit(self.image, self.rect)