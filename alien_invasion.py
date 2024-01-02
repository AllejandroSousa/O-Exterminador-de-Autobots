import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    #Initialize the game and creates an object for the screen
    pygame.init()
    oea_settings = Settings()
    screen = pygame.display.set_mode((oea_settings.screen_width, oea_settings.screen_height))
    pygame.display.set_caption("O Exterminador de Autobots")

    ship = Ship(oea_settings ,screen)

    #Initialize the principal loop of the game
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(oea_settings, screen, ship)

run_game()
            