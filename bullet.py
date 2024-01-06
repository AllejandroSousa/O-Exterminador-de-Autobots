import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """"A class that manages projectiles fired by the spaceship."""

    def __init__(self, oea_settings, screen, ship):
        """Create an object to the projectile in the spaceship current position."""
        pygame.mixer.init()
        super(Bullet, self).__init__()
        self.laser_sound = pygame.mixer.music.load('projetos/o_exterminador_de_autobots/sounds/laser.mp3')
        self.screen = screen

        self.rect = pygame.Rect(0, 0, oea_settings.bullet_width, oea_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)

        self.color = oea_settings.bullet_color
        self.speed_factor = oea_settings.bullet_speed_factor

    def update(self):
        """Move up the projectile on the screen."""
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the projectile on the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
    
    def play_fire_sound(self):
        pygame.mixer.music.play()
