import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Alien(Sprite):
    def __init__(self, game: 'AlienInvasion', x: float, y: float) -> None:
        super().__init__()

        self.screen = game.screen
        self.boundaries = game.screen.get_rect()
        self.settings = game.settings

        # Load the alien image and flip it to face left/right
        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(
            self.image,
            (self.settings.alien_w, self.settings.alien_h)
        )
        self.image = pygame.transform.rotate(self.image, -90)  # Rotate 90 degrees clockwise

        # Get the rect and move the alien to the right side of the screen
        self.rect = self.image.get_rect()
        self.rect.x = self.boundaries.right - self.rect.width - 10  # 10 pixels from the edge
        self.rect.y = y

    def update(self) -> None:
        pass

    def draw_alien(self) -> None:
        self.screen.blit(self.image, self.rect)