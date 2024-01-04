import sys
import pygame
from bullet import Bullet
from alien import Alien

def create_fleet(oea_settings, screen, aliens):
    """Create a complete fleet of aliens."""
    #The spacing between the aliens is equal to the width of one alien.
    alien = Alien(oea_settings, screen)
    alien_width = alien.rect.width
    available_space_x = oea_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))

    for alien_number in range(number_aliens_x):
        alien = Alien(oea_settings, screen)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)

def fire_bullet(oea_settings, screen, ship, bullets):
    """Fire a projectile if the limit has not been reached."""
    if len(bullets) < oea_settings.bullets_allowed:
        new_bullet = Bullet(oea_settings, screen, ship)
        bullets.add(new_bullet)

def check_keydown_events(event, oea_settings, screen, ship, bullets):
    """Responds to key presses."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(oea_settings, screen, ship, bullets)

def check_keyup_events(event, ship):
    """Responds to key releases."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(oea_settings, screen, ship, bullets):
    """Responds to keyboard and mouse input events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, oea_settings, screen, ship, bullets)
        
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
  
def update_screen(oea_settings, screen, ship, aliens, bullets):
    """Update the images on the screen and changes to the new screen."""
    screen.fill(oea_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    pygame.display.flip()

def update_bullets(bullets):
    """Update the projectile's position and remove the old projectiles."""
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    