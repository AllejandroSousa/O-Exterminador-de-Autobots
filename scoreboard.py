import pygame.font

class Scoreboard():
    """A class to show informations about the score."""

    def __init__(self, oea_settings, screen, stats):
        """Initialize the score attributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.oea_settings = oea_settings
        self.stats = stats

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()

    def prep_score(self):
        """Turns the score into a rendered image."""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.oea_settings.bg_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Draw the score on the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        