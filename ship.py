# ship.py
# Name: Ship Class for Alien Invasion Game
# Description: Defines the spaceship’s behavior including loading the image,
#              starting position, movement (left and right), and firing bullets.

import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, game, arsenal) -> None:
        """Initialize the ship and its starting position."""
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.boundaries = self.screen.get_rect()

        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale(
            self.image, (self.settings.ship_w, self.settings.ship_h))
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.boundaries.midbottom
        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False

        self.arsenal = arsenal

    def center_ship(self) -> None:
        """Center the ship on the screen."""
        self.rect.midbottom = self.boundaries.midbottom
        self.x = float(self.rect.x)

    def update(self) -> None:
        """Update the ship’s position and arsenal."""
        self._update_ship_movement()
        self.arsenal.update_arsenal()

    def _update_ship_movement(self) -> None:
        """Move the ship left or right based on user input."""
        temp_speed = self.settings.ship_speed
        if self.moving_right and self.rect.right < self.boundaries.right:
            self.x += temp_speed
        if self.moving_left and self.rect.left > self.boundaries.left:
            self.x -= temp_speed
        self.rect.x = self.x

    def draw(self) -> None:
        """Draw the ship and its arsenal to the screen."""
        self.arsenal.draw()
        self.screen.blit(self.image, self.rect)

    def fire_laser(self) -> None:
        """Fire a bullet if under the allowed bullet limit."""
        self.arsenal.fire_bullet()

    def check_collisions(self, other_group) -> bool:
        """Check for collisions with another sprite group (e.g., aliens)."""
        if pygame.sprite.spritecollideany(self, other_group):
            self.center_ship()
            return True
        return False