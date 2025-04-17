# settings.py
# Name: Alien Invasion Game Settings
# Description: Stores all settings and configuration for the Alien Invasion game.

from pathlib import Path

class Settings:
    def __init__(self) -> None:
        self.name: str = 'Alien Invasion'

        # Screen settings
        self.screen_w = 1200
        self.screen_h = 800
        self.FPS = 60

        # Background image
        self.bg_file = Path.cwd() / 'Assets' / 'images' / 'Starbasesnow.png'

        # Ship settings
        self.ship_file = Path.cwd() / 'Assets' / 'images' / 'ship2(no bg).png'
        self.ship_w = 40
        self.ship_h = 60
        self.ship_speed = 5

        # Bullet settings
        self.bullet_file = Path.cwd() / 'Assets' / 'images' / 'laserBlast.png'
        self.bullet_speed = 7
        self.bullet_w = 25
        self.bullet_h = 80
        self.bullet_amount = 5

        # Sound
        self.laser_sound = Path.cwd() / 'Assets' / 'sound' / 'laser.mp3'

        # Alien settings
        self.alien_file = Path.cwd() / 'Assets' / 'images' / 'enemy_4.png'
        self.alien_speed = 3
        self.fleet_direction = 1  # 1 for right, -1 for left
        self.fleet_drop_speed = 10  # can be any number, used later when moving fleet
        self.alien_w = 40
        self.alien_h = 40