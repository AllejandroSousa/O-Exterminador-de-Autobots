class Settings():
    """A class to store all the settings of O Exterminador de Autobots."""

    def __init__(self):
        """Initialize the game's settings."""
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.ship_limit = 3

        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 255, 0, 0
        self.bullets_allowed = 3

        self.fleet_drop_speed = 10
        
        self.speed_up_scale = 1.1
        
    def initialize_dynamic_settings(self):
        """Initialize the settings that change during the game."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 1
        self.alien_speed_factor = 1

        #fleet_direction equals to 1 represents the right; -1 represents the left
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase the speed's settings."""
        self.ship_speed_factor *= self.speed_up_scale
        self.bullet_speed_factor *= self.speed_up_scale
        self.alien_speed_factor *= self.speed_up_scale
