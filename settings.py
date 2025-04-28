"""settings.py
Name: Alien Invasion Game Settings
Description: Stores all settings and configuration for the Alien Invasion game,
including screen size, image files, speeds, bullet amounts, and more.
"""

from pathlib import Path
import pygame

class Settings:
    """Settings class to store all game configuration."""

    def __init__(self) -> None:
        """Initialize all static settings."""
        self.name: str = 'Alien Invasion'

        self.screen_w = 1200
        self.screen_h = 800
        self.FPS = 60
        self.bg_color = (0, 0, 0)

        self.bg_file = Path.cwd() / 'Assets' / 'images' / 'Outerspace.png'
        self.difficulty_scale = 1.1
        self.scores_file = Path.cwd() / 'Assets' / 'file' / 'scores.json'
        self.HUD_font_size = 25
        self.bg_image = pygame.image.load(self.bg_file)

        self.ship_file = Path.cwd() / 'Assets' / 'images' / 'white_ship.png'
        self.ship_w = 70
        self.ship_h = 90

        self.bullet_file = Path.cwd() / 'Assets' / 'images' / 'Laserorb.png'

        self.laser_sound = Path.cwd() / 'Assets' / 'sound' / 'Laserzap.mp3'
        self.impact_sound = Path.cwd() / 'Assets' / 'sound' / 'Blast1.mp3'

        self.alien_file = Path.cwd() / 'Assets' / 'images' / 'Enemy.png'
        self.fleet_direction = 1
        self.alien_w = 50
        self.alien_h = 50

        self.font_file = Path.cwd() / 'Assets' / 'Fonts' / 'Silkscreen' / 'KaushanScript-Regular.ttf'
        self.button_w = 200
        self.button_h = 50
        self.button_color = (0, 135, 50)
        self.text_color = (255, 255, 255)
        self.button_font_size = 48

    def initialize_dynamic_settings(self) -> None:
        """Initialize settings that change throughout the game."""
        self.ship_speed = 5
        self.starting_ship_count = 3

        self.bullet_w = 25
        self.bullet_h = 80
        self.bullet_speed = 7
        self.bullet_amount = 5

        self.fleet_speed = 2
        self.fleet_drop_speed = 40
        self.alien_points = 50

    def increase_difficulty(self) -> None:
        """Increase speed settings and alien point values."""
        self.ship_speed *= self.difficulty_scale
        self.bullet_speed *= self.difficulty_scale
        self.fleet_speed *= self.difficulty_scale