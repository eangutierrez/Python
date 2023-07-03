from random import randint

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""
    
    def __init__(self, ss_game):
        """Initialize the alien and set its starting placement."""
        super().__init__()
        self.screen = ss_game.screen
        self.settings = ss_game.settings

        # Load the alien image and set its rect
        self.image = pygame.image.load('images/alien_ship.png')
        self.rect = self.image.get_rect()

        # Start each new alien at a random position on the right side
        self.rect.left = self.screen.get_rect().right
        # The farthest alien position is screen height - alien height
        alien_top_max = self.settings.screen_height - self.rect.height
        self.rect.top = randint(0, alien_top_max)

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)

    def update(self):
        """Move the alien steadily to the left."""
        self.x -= self.settings.alien_speed
        self.rect.x = self.x