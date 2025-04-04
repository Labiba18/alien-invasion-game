# arsenal.py
# Name: Arsenal Class for Alien Invasion Game
# Description: Manages the group of bullets (arsenal) in the Alien Invasion game. Responsible for updating, drawing, and firing bullets.


import pygame
from bullet import Bullet
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Arsenal:
    def __init__(self, game: 'AlienInvasion') -> None:
        """Initialize the arsenal which holds and manages all active bullets."""
        self.game = game
        self.settings = game.settings
        self.arsenal = pygame.sprite.Group()

    def update_arsenal(self) -> None:
        """Update bullet positions and remove bullets that are off screen."""
        self.arsenal.update()
        self._remove_bullets_offscreen()

    def _remove_bullets_offscreen(self) -> None:
        """Remove bullets that have moved off the top of the screen."""
        for bullet in self.arsenal.copy():
            if bullet.rect.bottom <= 0:
                self.arsenal.remove(bullet)

    def draw(self) -> None:
        """Draw all bullets currently in the arsenal."""
        for bullet in self.arsenal:
            bullet.draw_bullet()

    def fire_bullet(self) -> bool:
        """Fire a bullet if the current number of bullets is less than the allowed maximum.
        Returns True if a bullet was fired, otherwise False.
        """
        if len(self.arsenal) < self.settings.bullet_amount:
            new_bullet = Bullet(self.game)
            self.arsenal.add(new_bullet)
            return True
        return False
    




    