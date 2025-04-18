# alien_invasion.py
# Author: Labiba Alam
# Date: 4/1/25
# Lab 12 - Option 1: Reposition the Spaceship (Changing Gameplay)
# Description: This is the main game file. It initializes the game window,
# checks user inputs, updates object positions, and draws everything on screen.

import pygame
from settings import Settings
from ship import Ship
from arsenal import Arsenal
from alien_fleet import AlienFleet

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_w, self.settings.screen_h))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self, Arsenal(self))
        self.aliens = AlienFleet(self)  # fleet now managed in alien_fleet.py

        self.clock = pygame.time.Clock()
        self.running = True

    def run_game(self):
        while self.running:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.ship.handle_keydown(event.key)
            elif event.type == pygame.KEYUP:
                self.ship.handle_keyup(event.key)

    def _update_screen(self):
        self.screen.blit(self.settings.bg_image, (0, 0))
        self.ship.update()
        self.ship.draw()
        self.aliens.update()  # <-- Update alien movement
        self.aliens.draw()

        pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()