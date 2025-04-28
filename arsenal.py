"""arsenal.py
Name: Arsenal Class for Alien Invasion Game
Description: Manages the group of bullets (arsenal) in the Alien Invasion game.
Handles updating bullet positions, removing off-screen bullets,
drawing bullets, and firing new bullets based on settings.
"""

import pygame
from bullet import Bullet
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Arsenal:
    def __init__(self, game: 'AlienInvasion') -> None:
        """Initialize the Arsenal with game settings and laser sound."""
        self.game = game
        self.settings = game.settings
        self.arsenal = pygame.sprite.Group()
        self.laser_sound = pygame.mixer.Sound(self.settings.laser_sound)

    def update_arsenal(self) -> None:
        """Update the bullets in the arsenal and remove off-screen bullets."""
        self.arsenal.update()
        self._remove_bullets_offscreen()

    def _remove_bullets_offscreen(self) -> None:
        """Remove bullets that have moved off the top of the screen."""
        for bullet in self.arsenal.copy():
            if bullet.rect.bottom <= 0:
                self.arsenal.remove(bullet)

    def draw(self) -> None:
        """Draw all bullets in the arsenal to the screen."""
        for bullet in self.arsenal:
            bullet.draw_bullet()

    def fire_bullet(self) -> bool:
        """Fire a new bullet if under the bullet limit. Return True if fired."""
        if len(self.arsenal) < self.settings.bullet_amount:
            new_bullet = Bullet(self.game, self.game.ship)
            self.arsenal.add(new_bullet)
            self.laser_sound.play()
            return True
        return False

    