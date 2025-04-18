# ship.py
# Name: Ship Class for Alien Invasion Game
# Description: Defines the spaceship's behavior including loading the image,
# starting position, movement (up and down), and firing bullets.


import pygame

class Ship:
    def __init__(self, game, arsenal):
        self.screen = game.screen
        self.settings = game.settings

        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale(
            self.image, (self.settings.ship_w, self.settings.ship_h)
        )
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Start at bottom center
        self.rect.midbottom = self.screen_rect.midbottom
        self.y = float(self.rect.y)

        # Arsenal (like bullets, etc.)
        self.arsenal = arsenal

    def update(self):
        # If needed, update movement logic here
        pass

    def draw(self):
        self.screen.blit(self.image, self.rect)