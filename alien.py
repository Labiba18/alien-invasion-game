import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Alien(Sprite):
    """A class to represent a single alien moving up and down on the right side of the screen."""

    def __init__(self, game: 'AlienInvasion', x: float, y: float) -> None:
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = game.screen
        self.boundaries = game.screen.get_rect()
        self.settings = game.settings

        # Load, scale, and rotate the alien to face left
        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(
            self.image,
            (self.settings.alien_w, self.settings.alien_h)
        )
        self.image = pygame.transform.rotate(self.image, -90)  # Face left

        self.rect = self.image.get_rect()

        # Start at the right edge of the screen
        self.rect.right = self.boundaries.right
        self.rect.y = y

        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def update(self) -> None:
        """Move the alien vertically and bounce off top/bottom screen edges."""
        temp_speed = self.settings.fleet_speed

        if self.check_edges():
            self.settings.fleet_direction *= -1  # Reverse vertical direction

        self.y += temp_speed * self.settings.fleet_direction
        self.rect.y = self.y

    def check_edges(self) -> bool:
        """Return True if alien hits top or bottom of the screen."""
        return (self.rect.bottom >= self.boundaries.bottom or self.rect.top <= self.boundaries.top)

    def draw_alien(self) -> None:
        """Draw the alien to the screen."""
        self.screen.blit(self.image, self.rect)