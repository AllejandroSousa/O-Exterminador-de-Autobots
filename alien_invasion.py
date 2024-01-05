import pygame
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
    #Initialize the game and creates an object for the screen
    pygame.init()
    oea_settings = Settings()
    screen = pygame.display.set_mode((oea_settings.screen_width, oea_settings.screen_height))
    pygame.display.set_caption("O Exterminador de Autobots")

    play_button = Button(oea_settings, screen, "Play")
    stats = GameStats(oea_settings)
    sb = Scoreboard(oea_settings, screen, stats)

    ship = Ship(oea_settings ,screen)
    bullets = Group()
    aliens = Group()

    gf.create_fleet(oea_settings, screen, ship, aliens)

    #Initialize the principal loop of the game
    while True:
        gf.check_events(oea_settings, screen, stats, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(oea_settings, screen, ship, aliens, bullets)
            gf.update_aliens(oea_settings, stats, screen, ship, aliens, bullets)
            
        gf.update_screen(oea_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()
            