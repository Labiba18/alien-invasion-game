# settings.py
# Name: Alien Invasion Game Settings
# Description: Stores all settings and configuration for the Alien Invasion game.


import pygame
from pathlib import Path

class Settings:
    def __init__(self) -> None:
        """Initialize game settings including screen, ship, bullet, background, and sound."""
        # Game title
        self.name: str = 'Alien Invasion'

        # Screen settings
        self.screen_w = 1200
        self.screen_h = 800
        self.FPS = 60

        # Background image
        self.bg_file = pygame.image.load(Path.cwd() / 'Assets' / 'images' / 'Starbasesnow.png')

        # Ship settings (uses sprite from assets)
        self.ship_file = Path.cwd() / 'Assets' / 'images' / 'ship2(no bg).png'
        self.ship_w = 40
        self.ship_h = 60
        self.ship_speed = 5

        # Bullet settings
        self.bullet_file = Path.cwd() / 'Assets' / 'images' / 'laserBlast.png'
        self.laser_sound = Path.cwd() / 'Assets' / 'sound' / 'laser.mp3'
        self.bullet_speed = 7
        self.bullet_w = 25
        self.bullet_h = 80
        self.bullet_amount = 5

        self.alien_file = Path.cwd() / 'Assets' / 'images' / 'enemy_4.png'
        self.alien_w = 40
        self.alien_h = 40
        self.fleet_speed = 5
        self.fleet_direction = 1
        self.fleet_drop_speed = 40