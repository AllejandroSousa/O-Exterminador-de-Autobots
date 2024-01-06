class GameStats():
    """Store statistical data of O Exterminador de Autobots"""

    def __init__(self, oea_settings):
        """Initialize the statitical data"""
        self.oea_settings = oea_settings
        self.reset_stats()
        self.game_active = False

        self.high_score = 0

    def reset_stats(self):
        """Initialize the statistical data that may change during the game."""
        self.ships_left = self.oea_settings.ship_limit
        self.score = 0
        self.level = 1
        