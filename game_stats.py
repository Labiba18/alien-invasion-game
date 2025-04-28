# game_stats.py
# Name: GameStats Class for Alien Invasion Game
# Description: Tracks the number of ships the player has left in the game.

from pathlib import Path
import json
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

        self.init_saved_scores()
        self.reset_stats()

    def init_saved_scores(self) -> None:
        """Initialize saved high scores."""
        self.path = self.settings.scores_file
        if self.path.exists() and self.path.stat().st_size > 0:
            contents = self.path.read_text()
            if not contents:
                print('file empty')
            scores = json.loads(contents)
            self.hi_score = scores.get('hi_score', 0)
        else:
            self.hi_score = 0
            self.save_scores()

    def save_scores(self) -> None:
        """Save high scores to a file."""
        scores = {
            'hi_score': self.hi_score
        }
        contents = json.dumps(scores, indent=4)
        try:
            self.path.write_text(contents)
        except FileNotFoundError as e:
            print(f'File Not Found: {e.filename}')

    def reset_stats(self) -> None:
        """Reset statistics that can change during the game."""
        self.ships_left = self.settings.starting_ship_count
        self.score = 0
        self.level = 1

    def update(self, collisions) -> None:
        """Update stats based on collisions."""
        self._update_score(collisions)
        self._update_max_score()
        self._update_hi_score()

    def _update_score(self, collisions) -> None:
        """Update the score based on number of collisions."""
        for alien in collisions.values():
            self.score += self.settings.alien_points
        # print(f'Basic: {self.score}')

    def _update_max_score(self) -> None:
        """Update the max score."""
        if self.score > self.max_score:
            self.max_score = self.score
        # print(f'Max: {self.max_score}')

    def _update_hi_score(self) -> None:
        """Update the high score."""
        if self.score > self.hi_score:
            self.hi_score = self.score