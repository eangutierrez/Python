import pygame

class Bird:
    """A class to manage the bird character."""

    def __init__(self, bb_game):
        """Initialize bird and set its position."""
        self.screen = bb_game.screen
        self.screen_rect = bb_game.screen.get_rect()

        # Load the bird sprite and get its rectangle
        # bird image from: https://opengameart.org/content/game-character-blue-flappy-bird-sprite-sheets
        self.image = pygame.image.load('images/bird.bmp')
        self.rect = self.image.get_rect()
        
        # Position bird at the center of the screen
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Set the bird sprite at its current location."""
        self.screen.blit(self.image, self.rect)