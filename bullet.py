"""bullet.py
Name: Bullet Class for Alien Invasion Game
Description: Defines the bullet behavior including appearance, position, movement, and drawing.
"""

import pygame
from typing import TYPE_CHECKING
from pygame.sprite import Sprite

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from ship import Ship

class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, game: 'AlienInvasion', ship: 'Ship') -> None:
        """Create a bullet object at the ship's current position.

        Parameters:
        game (AlienInvasion): Reference to the main game instance.
        ship (Ship): The player's ship instance.
        """
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        self.image = pygame.image.load(self.settings.bullet_file)
        self.image = pygame.transform.scale(
            self.image, (self.settings.bullet_w, self.settings.bullet_h)
        )
        self.rect = self.image.get_rect()

        self.rect.midtop = ship.rect.midtop

        self.y = float(self.rect.y)

    def update(self) -> None:
        """Move the bullet up the screen based on the bullet speed setting."""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self) -> None:
        """Draw the bullet on the screen at its current location."""
        self.screen.blit(self.image, self.rect)