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

        # Load, scale, and rotate the bullet image
        self.image = pygame.image.load(self.settings.bullet_file)
        self.image = pygame.transform.scale(
            self.image,
            (self.settings.bullet_w, self.settings.bullet_h)
        )
        self.image = pygame.transform.rotate(self.image, -90)  # Rotate to horizontal

        # Position bullet at the middle left of the ship
        self.rect = self.image.get_rect()
        self.rect.midleft = game.ship.rect.midleft
        self.x = float(self.rect.x)  # Track bullet x-position

    def update(self) -> None:
        """Move the bullet to the right on the screen."""
        self.x += self.settings.bullet_speed
        self.rect.x = self.x

    def draw_bullet(self) -> None:
        """Draw the bullet to the screen."""
        self.screen.blit(self.image, self.rect)