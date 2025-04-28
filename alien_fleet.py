"""alien_fleet.py
Name: AlienFleet Class for Alien Invasion Game
Description: Manages the alien fleet's creation, movement, edge detection,
             collision detection, reset, and destruction checks.
             Includes custom formation logic (X-shaped pattern).
"""

import pygame
from pygame.sprite import Group
from alien import Alien

class AlienFleet:
    """Manages a fleet of alien enemies in the game."""

    def __init__(self, game) -> None:
        """Initialize the fleet with game settings and create the initial fleet."""
        self.screen = game.screen
        self.settings = game.settings
        self.fleet = Group()
        self._create_fleet()

    def _create_fleet(self) -> None:
        """Create an X-shaped alien fleet formation."""
        self.fleet.empty()

        alien_w = self.settings.alien_w
        alien_h = self.settings.alien_h
        screen_w = self.settings.screen_w
        screen_h = self.settings.screen_h

        cols = 7
        rows = 7
        spacing_x = 20
        spacing_y = 20

        offset_x = (screen_w - (cols * (alien_w + spacing_x))) // 2
        offset_y = 50

        for row in range(rows):
            for col in range(cols):
                if col == row or col == (cols - 1 - row):
                    x = offset_x + col * (alien_w + spacing_x)
                    y = offset_y + row * (alien_h + spacing_y)
                    alien = Alien(self, x, y)
                    self.fleet.add(alien)

    def _check_fleet_edges(self) -> None:
        """Check if any alien has hit the screen edge and reverse fleet direction."""
        for alien in self.fleet:
            if alien.is_at_edge():
                self._drop_alien_fleet()
                self.settings.fleet_direction *= -1
                break

    def _drop_alien_fleet(self) -> None:
        """Move the fleet downward when edge is reached."""
        for alien in self.fleet:
            alien.y += self.settings.fleet_drop_speed
            alien.rect.y = alien.y

    def update_fleet(self) -> None:
        """Update position of all aliens in the fleet."""
        self._check_fleet_edges()
        for alien in self.fleet:
            alien.update(self.settings.fleet_direction)

    def draw(self) -> None:
        """Draw all aliens to the screen."""
        for alien in self.fleet:
            alien.draw_alien()

    def check_collisions(self, other_group) -> dict:
        """Check for collisions between aliens and another group (e.g., bullets)."""
        return pygame.sprite.groupcollide(self.fleet, other_group, True, True)

    def check_fleet_bottom(self) -> bool:
        """Return True if any alien has reached the bottom of the screen."""
        for alien in self.fleet:
            if alien.rect.bottom >= self.settings.screen_h:
                return True
        return False

    def create_fleet(self) -> None:
        """Public method to create a new fleet."""
        self._create_fleet()

    def reset_fleet_to_top(self) -> None:
        """Reset all aliens to their starting positions at the top of the screen."""
        self._create_fleet()

    def check_destroy_status(self) -> bool:
        """Return True if the fleet is empty (all aliens destroyed)."""
        return not self.fleet