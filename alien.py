import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class that represent a single alien of the fleet."""

    def __init__(self, oea_settings, screen):
        """Initialize the alien and sets its initial position."""
        super(Alien, self).__init__()
        self.screen = screen
        self.oea_settings = oea_settings

        self.image = pygame.image.load('projetos/o_exterminador_de_autobots/images/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the alien in its initial position"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """Return True if the alien is on the edge of the screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
    
    def update(self):
        """Move the alien to the right."""
        self.x += (self.oea_settings.alien_speed_factor * self.oea_settings.fleet_direction)
        self.rect.x = self.x
