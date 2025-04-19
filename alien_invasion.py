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
from alien_fleet import AlienFleet

class AlienInvasion:
    def __init__(self) -> None:
        pygame.init()
        self.clock = pygame.time.Clock()  # ← ADD THIS

        self.settings = Settings()
        self.bg_image = pygame.image.load(self.settings.bg_file)
        self.screen = pygame.display.set_mode(
            (self.settings.screen_w, self.settings.screen_h))
        pygame.display.set_caption("Alien Invasion")
    
        self.arsenal = Arsenal(self)
        self.ship = Ship(self, self.arsenal)
        self.alien_fleet = AlienFleet(self)

        self.laser_sound = pygame.mixer.Sound(self.settings.laser_sound)
        self.impact_sound = pygame.mixer.Sound(self.settings.impact_sound)
    def run_game(self) -> None:
        while True:
            self._check_events()
            self.ship.update()
            self.alien_fleet.update_fleet()
            self._check_collisions()
            self._update_screen()

            self.clock.tick(self.settings.FPS)

    def _check_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event) -> None:
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self.ship.fire_laser()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event) -> None:
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self) -> None:
        self.screen.blit(self.bg_image, (0, 0))
        self.ship.draw()
        self.ship.arsenal.draw()
        self.alien_fleet.draw()
        pygame.display.flip()

    def _check_collisions(self) -> None:
        if self.ship.check_collisions(self.alien_fleet.fleet):
            self.alien_fleet.reset_fleet_to_top()

        if self.alien_fleet.check_fleet_bottom():
            self.alien_fleet.reset_fleet_to_top()

        collisions = self.alien_fleet.check_collisions(self.ship.arsenal.arsenal)
        if collisions:
            self.impact_sound.play()
            self.impact_sound.fadeout(500)

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()