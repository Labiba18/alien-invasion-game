# alien.py
# Name: Alien Class for Alien Invasion Game
# Description: Defines the alien sprite's behavior including appearance, movement, edge detection, and resetting position.

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, game, x, y) -> None:
        """
        Initialize the alien and set its starting position.

        Parameters:
        game: Reference to the main game instance.
        x (int): The initial x-coordinate for the alien.
        y (int): The initial y-coordinate for the alien.
        """
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        # Load and scale the alien image
        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(
            self.image, (self.settings.alien_w, self.settings.alien_h)
        )
        self.rect = self.image.get_rect()

        # Position the alien at (x, y)
        self.rect.x = x
        self.rect.y = y

        # Store precise position for movement
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self, direction: int) -> None:
        """
        Move the alien left or right based on the direction.

        Parameters:
        direction (int): 1 to move right, -1 to move left.
        """
        self.x += direction * self.settings.fleet_speed
        self.rect.x = self.x

    def draw_alien(self) -> None:
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)

    def is_at_edge(self) -> bool:
        """
        Check if the alien has reached the edge of the screen.

        Returns:
        bool: True if at edge, False otherwise.
        """
        screen_rect = self.screen.get_rect()
        return self.rect.right >= screen_rect.right or self.rect.left <= 0

    def reset_position(self, x: int, y: int) -> None:
        """
        Reset the alien's position to (x, y).

        Parameters:
        x (int): New x-coordinate.
        y (int): New y-coordinate.
        """
        self.rect.x = x
        self.rect.y = y
        self.x = float(x)
        self.y = float(y)