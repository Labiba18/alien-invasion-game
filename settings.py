# settings.py
# Name: Alien Invasion Game Settings
# Description: Stores all settings and configuration for the Alien Invasion game,
# including screen size, image files, speeds, bullet amounts, and more.

from pathlib import Path
import pygame

class Settings:
    def __init__(self) -> None:
        # Game name
        self.name: str = 'Alien Invasion'

        # Screen settings
        self.screen_w = 1200                     # Width of the game screen
        self.screen_h = 800                      # Height of the game screen
        self.FPS = 60                            # Frames per second
        self.bg_color = (0, 0, 0)                # Default background color (black)

        # Background image
        self.bg_file = Path.cwd() / 'Assets' / 'images' / 'Starbasesnow.png'
        self.difficulty_scale = 1.1
        self.scores_file = Path.cwd() / 'Assets' / 'file' / 'scores.json'
        self.bg_image = pygame.image.load(self.bg_file)

        # Ship settings
        self.ship_file = Path.cwd() / 'Assets' / 'images' / 'white_ship.png'
        self.ship_w = 70                         # Ship width
        self.ship_h = 90                         # Ship height

        # Bullet settings
        self.bullet_file = Path.cwd() / 'Assets' / 'images' / 'laserBlast.png'

        # Sound settings
        self.laser_sound = Path.cwd() / 'Assets' / 'sound' / 'laser.mp3'
        self.impact_sound = Path.cwd() / 'Assets' / 'sound' / 'impactSound.mp3'

        # Alien settings
        self.alien_file = Path.cwd() / 'Assets' / 'images' / 'enemy_4.png'
        self.fleet_direction = 1                 # 1 for right, -1 for left movement
        self.alien_w = 50                        # Alien width
        self.alien_h = 50                        # Alien height

        self.font_file = Path.cwd() / 'Assets' / 'Fonts' / 'Silkscreen' / 'Silkscreen-Bold.ttf'
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
        self.ship_speed *= self.difficulty_scale
        self.bullet_speed *= self.difficulty_scale
        self.fleet_speed *= self.difficulty_scale