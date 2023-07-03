import sys

import pygame

from settings import Settings
from raindrop import Raindrop

class RaindropsGame:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
                (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Raindrops")

        self.raindrops = pygame.sprite.Group()
        self._create_drops()

    def run_game(self):
        """Start the game's main loop."""
        while True:
            self._check_events()
            self.raindrops.update()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
    
    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_q:
            sys.exit()
    
    def _create_drops(self):
        """Create a drop and find the number of drops in a row."""
        # Spacing betwen each star is equal to one drop width
        drop = Raindrop(self)
        drop_width, drop_height = drop.rect.size
        available_space_x = self.settings.screen_width - drop_width
        number_drops_x = available_space_x // (2 * drop_width)

        # Determine the number of rows of drops that fit on the screen
        available_space_y = self.settings.screen_height
        number_rows = available_space_y // (2 * drop_height)

        # Fill the sky with drops
        for row_number in range(number_rows):
            for drop_number in range(number_drops_x):
                self._create_drop(drop_number, row_number)

    def _create_drop(self, drop_number, row_number):
        """Create a drop and place it in the row."""
        drop = Raindrop(self)
        drop_width, drop_height = drop.rect.size
        drop.rect.x = drop_width + 2 * drop_width * drop_number
        drop.y = 2 * drop.rect.height * row_number
        drop.rect.y = drop.y
        self.raindrops.add(drop)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.raindrops.draw(self.screen)

        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game
    rd_game = RaindropsGame()
    rd_game.run_game()
