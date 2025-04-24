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
        self.bg_image = pygame.image.load(self.bg_file)

        # Ship settings
        self.ship_file = Path.cwd() / 'Assets' / 'images' / 'white_ship.png'
        self.ship_w = 70                         # Ship width
        self.ship_h = 90                         # Ship height
        self.ship_speed = 5                      # Ship movement speed
        self.starting_ship_count = 3             # Number of lives the player starts with

        # Bullet settings
        self.bullet_file = Path.cwd() / 'Assets' / 'images' / 'laserBlast.png'
        self.bullet_speed = 15                   # Speed at which bullets travel
        self.bullet_w = 25                       # Bullet width
        self.bullet_h = 80                       # Bullet height
        self.bullet_amount = 5                   # Max bullets allowed on screen at a time

        # Sound settings
        self.laser_sound = Path.cwd() / 'Assets' / 'sound' / 'laser.mp3'
        self.impact_sound = Path.cwd() / 'Assets' / 'sound' / 'impactSound.mp3'

        # Alien settings
        self.alien_file = Path.cwd() / 'Assets' / 'images' / 'enemy_4.png'
        self.alien_speed = 2                     # Speed of alien movement
        self.fleet_direction = 1                 # 1 for right, -1 for left movement
        self.fleet_drop_speed = 40               # Pixels aliens drop when hitting an edge
        self.alien_w = 50                        # Alien width
        self.alien_h = 50                        # Alien height

        self.font_file = Path.cwd() / 'Assets' / 'Fonts' / 'Silkscreen' / 'Silkscreen-Bold.ttf'
        self.button_w = 200
        self.button_h = 50
        self.button_color = (0, 135, 50)
        self.text_color = (255, 255, 255)
        self.button_font_size = 48