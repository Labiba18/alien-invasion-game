# ship.py
# Name: Ship Class for Alien Invasion Game
# Description: Defines the spaceship's behavior including loading the image,
# starting position, movement (up and down), and firing bullets.


import pygame
from typing import TYPE_CHECKING
from pathlib import Path
from arsenal import Arsenal

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Ship:
    """A class to manage the player's spaceship."""

    def __init__(self, game: 'AlienInvasion', arsenal: 'Arsenal') -> None:
        """Initialize the ship and set its starting position."""
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()

        # Load and scale the ship image
        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale(
            self.image, (self.settings.ship_w, self.settings.ship_h)
        )

        self.image = pygame.transform.rotate(self.image, -90)

        # Start the ship at the left-center of the screen
        self.rect = self.image.get_rect()
        self.rect.midleft = self.boundaries.midleft

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_up = False
        self.moving_down = False

        self.arsenal = arsenal

    def update(self) -> None:
        """Update the ship's position based on movement flags."""
        self._update_ship_movement()
        self.arsenal.update_arsenal()

    def _update_ship_movement(self) -> None:
        """Move the ship up or down if the movement flags are set."""
        temp_speed = self.settings.ship_speed
        if self.moving_up and self.rect.top > self.boundaries.top:
            self.y -= temp_speed
        if self.moving_down and self.rect.bottom < self.boundaries.bottom:
            self.y += temp_speed
        self.rect.y = self.y

    def draw(self) -> None:
        """Draw the ship and its bullets on the screen."""
        self.arsenal.draw()
        self.screen.blit(self.image, self.rect)

    def fire_laser(self) -> bool:
        """Command the arsenal to fire a bullet."""
        return self.arsenal.fire_bullet()

        