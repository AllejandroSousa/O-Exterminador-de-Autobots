import pygame

class Ship():

    def __init__(self, oea_settings, screen):
        """Initialize the spaceship and defines your initial position"""
        self.screen = screen
        self.oea_settings = oea_settings

        self.image = pygame.image.load('projetos/o_exterminador_de_autobots/images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the spaceship's position according to the moviment flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.oea_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.oea_settings.ship_speed_factor

        self.rect.centerx = self.center

    def blitme(self):
        """Draw the spaceship in your current position"""
        self.screen.blit(self.image, self.rect)
