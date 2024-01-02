import pygame

class Ship():

    def __init__(self, screen):
        """Initialize the spaceship and defines your initial position"""
        self.screen = screen

        self.image = pygame.image.load('projetos/o_exterminador_de_autobots/images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the spaceship's position according to the moviment flag"""
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1

    def blitme(self):
        """Draw the spaceship in your current position"""
        self.screen.blit(self.image, self.rect)
