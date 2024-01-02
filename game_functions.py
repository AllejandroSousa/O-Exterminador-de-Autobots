import sys
import pygame

def check_events(ship):
    """Responds to keyboard and mouse input events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True
        
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False
    
def update_screen(oea_settings, screen, ship):
    """Update the images on the screen and changes to the new screen"""
    screen.fill(oea_settings.bg_color)
    ship.blitme()

    pygame.display.flip()
