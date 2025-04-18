import pygame
from typing import TYPE_CHECKING
from alien import Alien

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class AlienFleet:
    def __init__(self, game: 'AlienInvasion') -> None:
        self.game = game
        self.settings = game.settings
        self.fleet = pygame.sprite.Group()
        self.direction = 1  # 1 = right, -1 = left

        self._create_fleet()

    def _create_fleet(self) -> None:
        alien_w = self.settings.alien_w
        alien_h = self.settings.alien_h
        screen_w = self.settings.screen_w
        screen_h = self.settings.screen_h

        # Set margins and spacing
        margin_x = 20
        margin_y = 20
        space_x = (screen_w - 2 * margin_x - (14 * alien_w)) // 13
        space_y = 20

        for row in range(4):
            for col in range(14):
                x = margin_x + col * (alien_w + space_x)
                y = margin_y + row * (alien_h + space_y)
                self._create_alien(x, y)

    def _create_alien(self, x: int, y: int) -> None:
        alien = Alien(self.game, x, y)
        self.fleet.add(alien)

    def update(self) -> None:
        self._check_edges()
        for alien in self.fleet.sprites():
            alien.rect.x += self.settings.alien_speed * self.direction

    def _check_edges(self) -> None:
        for alien in self.fleet.sprites():
            if alien.rect.right >= self.settings.screen_w or alien.rect.left <= 0:
                self.direction *= -1
                for a in self.fleet.sprites():
                    a.rect.y += self.settings.fleet_drop_speed
                break

    def draw(self) -> None:
        for alien in self.fleet:
            alien.draw_alien()

