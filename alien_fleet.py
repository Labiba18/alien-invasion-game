import pygame
from alien import Alien
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class AlienFleet:
    def __init__(self, game: 'AlienInvasion') -> None:
        self.game = game
        self.settings = game.settings
        self.fleet = pygame.sprite.Group()

        self._create_fleet()

    def _create_fleet(self) -> None:
        alien_w = self.settings.alien_w
        alien_h = self.settings.alien_h
        screen_w = self.settings.screen_w
        screen_h = self.settings.screen_h

        cols = 14  # 14 aliens per row
        rows = 4   # 4 rows

        # Calculate total width and height of fleet
        total_w = cols * alien_w
        total_h = rows * alien_h

        # Calculate even horizontal and vertical spacing
        x_margin = (screen_w - total_w) // (cols + 1)
        y_margin = (screen_h // 2 - total_h) // (rows + 1)

        for row in range(rows):
            for col in range(cols):
                x = x_margin + col * (alien_w + x_margin)
                y = y_margin + row * (alien_h + y_margin)
                self._create_alien(x, y)

    def _create_alien(self, x: int, y: int) -> None:
        new_alien = Alien(self.game, x, y)
        self.fleet.add(new_alien)

    def update(self) -> None:
        self.fleet.update()

    def draw(self) -> None:
        for alien in self.fleet:
            alien.draw_alien()
