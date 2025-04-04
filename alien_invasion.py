# alien_invasion.py
# Author: Labiba Alam
# Date: 4/1/25
# Lab 12 - Option 1: Reposition the Spaceship (Changing Gameplay)
# Description: This is the main game file. It initializes the game window,
# checks user inputs, updates object positions, and draws everything on screen.

import sys
import pygame
from settings import Settings
from ship import Ship
from arsenal import Arsenal


class AlienInvasion:
    """Main class to manage game behavior."""

    def __init__(self):
        """Initialize the game, settings, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_w, self.settings.screen_h))
        pygame.display.set_caption(self.settings.name)

        self.clock = pygame.time.Clock()
        self.running = True

        self.ship = Ship(self, Arsenal(self))
        self.laser_sound = pygame.mixer.Sound(self.settings.laser_sound)

    def run_game(self):
        """Start the main game loop."""
        while self.running:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(self.settings.FPS)

    def _check_events(self):
        """Respond to keypresses and other events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Handle keydown events."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            if self.ship.fire_laser():
                self.laser_sound.play()
                self.laser_sound.fadeout(250)
        elif event.key == pygame.K_q:
            self.running = False
            pygame.quit()
            sys.exit()

    def _check_keyup_events(self, event):
        """Handle keyup events."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _update_screen(self):
        """Redraw the screen during each pass through the loop."""
        self.screen.blit(self.settings.bg_file, (0, 0))
        self.ship.draw()
        self.ship.arsenal.draw()
        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
