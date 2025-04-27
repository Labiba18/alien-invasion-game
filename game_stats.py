# game_stats.py
# Name: GameStats Class for Alien Invasion Game
# Description: Tracks the number of ships the player has left in the game.

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class GameStats:
    """Track statistics for the Alien Invasion game."""

    def __init__(self, game: 'AlienInvasion') -> None:
        """Initialize the statistics."""
        self.game = game
        self.settings = game.settings
        self.max_score = 0
        self.reset_stats()

    def reset_stats(self) -> None:
        """Reset statistics that can change during the game."""
        self.ships_left = self.settings.starting_ship_count
        self.score = 0
        self.level = 1

    def update(self, collisions) -> None:
        """Update game statistics."""
        self._update_score(collisions)
        self._update_max_score()
        # update hi_score

    def _update_max_score(self) -> None:
        """Update the maximum score if the current score is higher."""
        if self.score > self.max_score:
            self.max_score = self.score
        #print(f'Max: {self.max_score}')

    def _update_score(self, collisions) -> None:
        """Update the score based on collisions."""
        for alien in collisions.values():
            self.score += self.settings.alien_points
        #print(f'Basic: {self.score}')

    def update_level(self) -> None:
        """Increase the level."""
        self.level += 1
        #print(self.level)