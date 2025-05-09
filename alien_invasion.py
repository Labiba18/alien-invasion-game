"""alien_invasion.py
Author: Labiba Alam
Date: 4/1/25
Lab 14 - Option 2
Description: Main file for Alien Invasion.
"""

import sys
import pygame
from time import sleep
from settings import Settings
from ship import Ship
from arsenal import Arsenal
from alien_fleet import AlienFleet
from game_stats import GameStats
from button import Button
from hud import HUD

class AlienInvasion:
    """Main class to manage game behavior and main loop."""

    def __init__(self) -> None:
        """Initialize game window, settings, ship, aliens, and game components."""
        pygame.init()
        self.clock = pygame.time.Clock()

        self.settings = Settings()
        self.settings.initialize_dynamic_settings()

        self.bg_image = pygame.transform.scale(
            pygame.image.load(self.settings.bg_file),
            (self.settings.screen_w, self.settings.screen_h)
        )
        self.screen = pygame.display.set_mode(
            (self.settings.screen_w, self.settings.screen_h)
        )
        pygame.display.set_caption("Alien Invasion")

        self.game_stats = GameStats(self)
        self.HUD = HUD(self)

        self.ship = Ship(self, Arsenal(self))
        self.alien_fleet = AlienFleet(self)
        self.alien_fleet.create_fleet()

        self.laser_sound = pygame.mixer.Sound(self.settings.laser_sound)
        self.impact_sound = pygame.mixer.Sound(self.settings.impact_sound)

        self.play_button = Button(self, 'Play')
        self.game_active = False
        self.running = True

    def run_game(self) -> None:
        """Main loop to keep the game running."""
        while self.running:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self.alien_fleet.update_fleet()
                self._check_collisions()

            self._update_screen()
            self.clock.tick(self.settings.FPS)

    def _check_events(self) -> None:
        """Handle keypresses and quit events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.game_stats.save_scores()
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and self.game_active == True:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._check_button_clicked()

    def _check_keydown_events(self, event) -> None:
        """Handle keydown events for ship movement and shooting."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self.ship.fire_laser()
        elif event.key == pygame.K_q:
            self.running = False
            self.game_stats.save_scores()
            pygame.quit()
            sys.exit()

    def _check_keyup_events(self, event) -> None:
        """Handle key release events to stop ship movement."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self) -> None:
        """Redraw all game elements on screen."""
        self.screen.blit(self.bg_image, (0, 0))
        self.ship.draw()
        self.alien_fleet.draw()
        self.HUD.draw()

        if not self.game_active:
            self.play_button.draw()
            pygame.mouse.set_visible(True)
        else:
            pygame.mouse.set_visible(False)

        pygame.display.flip()

    def _check_collisions(self) -> None:
        """Check for all in-game collisions and responses."""
        if self.ship.check_collisions(self.alien_fleet.fleet):
            self._check_game_status()

        if self.alien_fleet.check_fleet_bottom():
            self._check_game_status()

        collisions = self.alien_fleet.check_collisions(self.ship.arsenal.arsenal)
        if collisions:
            self.impact_sound.play()
            self.impact_sound.fadeout(500)
            self.game_stats.update(collisions)
            self.HUD.update_scores()

        if self.alien_fleet.check_destroy_status():
            self._reset_level()
            self.settings.increase_difficulty()
            self.game_stats.update_level()
            self.HUD.update_level()

    def _reset_level(self) -> None:
        """Reset the level by respawning the alien fleet."""
        self.alien_fleet.reset_fleet_to_top()

    def _check_game_status(self) -> None:
        """Update game state depending on remaining ships."""
        if self.game_stats.ships_left > 0:
            self.game_stats.ships_left -= 1
            self._reset_level()
            sleep(0.5)
        else:
            self.game_active = False

    def _check_button_clicked(self) -> None:
        """Start game if Play button was clicked."""
        mouse_pos = pygame.mouse.get_pos()
        if self.play_button.check_clicked(mouse_pos):
            self.restart_game()

    def restart_game(self) -> None:
        """Restart the game from the beginning."""
        self.settings.initialize_dynamic_settings()
        self.game_stats.reset_stats()
        self.HUD.update_scores()
        self._reset_level()
        self.ship.center_ship()
        self.game_active = True
        pygame.mouse.set_visible(False)

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
