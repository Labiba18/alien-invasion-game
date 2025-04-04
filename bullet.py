# bullet.py
# Name: Bullet Class for Alien Invasion Game
# Description: Defines the bullet behavior including appearance, position, movement, and drawing.


import pygame
from typing import TYPE_CHECKING
from pygame.sprite import Sprite

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Bullet(Sprite):
    """Represents a laser bullet fired from the spaceship."""

    def __init__(self, game: 'AlienInvasion') -> None:
        """Initialize the bullet and set its position based on the ship."""
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        # Load and scale the bullet image
        self.image = pygame.image.load(self.settings.bullet_file)
        self.image = pygame.transform.scale(
            self.image,
            (self.settings.bullet_w, self.settings.bullet_h)
        )

        # Position bullet at the top center of the ship
        self.rect = self.image.get_rect()
        self.rect.midtop = game.ship.rect.midtop
        self.y = float(self.rect.y)

    def update(self) -> None:
        """Move the bullet upward on the screen."""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self) -> None:
        """Draw the bullet to the screen."""
        self.screen.blit(self.image, self.rect)