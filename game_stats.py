# game_stats.py
# Name: GameStats Class for Alien Invasion Game
# Description: Tracks the number of ships the player has left in the game.

class GameStats:
    """Track statistics for the Alien Invasion game."""

    def __init__(self, ship_limit: int) -> None:
        """
        Initialize the statistics.

        Parameters:
        ship_limit (int): The maximum number of ships the player starts with.
        """
        self.ship_limit = ship_limit      # Total number of ships player can use
        self.ships_left = ship_limit      # Remaining ships during gameplay