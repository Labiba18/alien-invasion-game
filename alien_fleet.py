import pygame
from pygame.sprite import Group
from alien import Alien

class AlienFleet:
    def __init__(self, game) -> None:
        self.screen = game.screen
        self.settings = game.settings
        self.fleet = Group()
        self._create_fleet()

    def _create_fleet(self) -> None:
        self.fleet.empty()
        alien_w = self.settings.alien_w
        alien_h = self.settings.alien_h
        screen_w = self.settings.screen_w
        screen_h = self.settings.screen_h

        cols = 14
        rows = 4
        spacing_x = 20
        spacing_y = 20

        offset_x = (screen_w - (cols * (alien_w + spacing_x))) // 2
        offset_y = 50

        for row in range(rows):
            for col in range(cols):
                x = offset_x + col * (alien_w + spacing_x)
                y = offset_y + row * (alien_h + spacing_y)
                alien = Alien(self, x, y)
                self.fleet.add(alien)

    def _check_fleet_edges(self) -> None:
        for alien in self.fleet:
            if alien.is_at_edge():
                self._drop_alien_fleet()
                self.settings.fleet_direction *= -1
                break

    def _drop_alien_fleet(self) -> None:
        for alien in self.fleet:
            alien.y += self.settings.fleet_drop_speed
            alien.rect.y = alien.y

    def update_fleet(self) -> None:
        self._check_fleet_edges()
        for alien in self.fleet:
            alien.update(self.settings.fleet_direction)

    def draw(self) -> None:
        for alien in self.fleet:
            alien.draw_alien()

    def check_collisions(self, other_group) -> dict:
        return pygame.sprite.groupcollide(self.fleet, other_group, True, True)

    def check_fleet_bottom(self) -> bool:
        for alien in self.fleet:
            if alien.rect.bottom >= self.settings.screen_h:
                return True
        return False

    def create_fleet(self) -> None:
        self._create_fleet()

    def reset_fleet_to_top(self) -> None:
        """Reset all aliens to their starting positions at the top of the screen."""
        self._create_fleet()

    def check_destroy_status(self) -> bool:
        """Return True if the fleet is empty (all aliens destroyed)."""
        return not self.fleet
