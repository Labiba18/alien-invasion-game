import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, game, x, y) -> None:
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(
            self.image, (self.settings.alien_w, self.settings.alien_h)
        )
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
        self.x = float(self.rect.x)

        # Direction: 1 is right, -1 is left
        self.direction = 1

    def update(self):
        self.x += self.direction * self.settings.alien_speed
        self.rect.x = self.x

        # Change direction if hitting edge
        if self.rect.right >= self.screen.get_rect().right:
            self.direction = -1
        elif self.rect.left <= 0:
            self.direction = 1

    def draw_alien(self):
        self.screen.blit(self.image, self.rect)