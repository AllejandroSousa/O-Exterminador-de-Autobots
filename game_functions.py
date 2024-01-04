import sys
from time import sleep
import pygame
from bullet import Bullet
from alien import Alien

def get_number_aliens_x(oea_settings, alien_width):
    """Determines the number of aliens that fit in a row."""
    available_space_x = oea_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(oea_settings, ship_height, alien_height):
    """Determines the number of rows with aliens that fit in the screen."""
    available_space_y = (oea_settings.screen_height - 
                         (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(oea_settings, screen, aliens, alien_number, row_number):
    """Creates an alien and places it in the row."""
    alien = Alien(oea_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(oea_settings, screen, ship, aliens):
    """Create a complete fleet of aliens."""
    alien = Alien(oea_settings, screen)
    number_aliens_x = get_number_aliens_x(oea_settings, alien.rect.width)
    number_rows = get_number_rows(oea_settings, ship.rect.height, alien.rect.height)

    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(oea_settings, screen, aliens, alien_number, row_number)

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

def update_bullets(oea_settings, screen, ship, aliens, bullets):
    """Update the projectile's position and remove the old projectiles."""
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    
    check_bullet_alien_collisions(oea_settings, screen, ship, aliens, bullets)

def check_bullet_alien_collisions(oea_settings, screen, ship, aliens, bullets):
    """Responds to collisions between projectiles and aliens."""
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if len(aliens) == 0:
        bullets.empty()
        create_fleet(oea_settings, screen, ship, aliens)

def check_fleet_edges(oea_settings, aliens):
    """Responds appropriately if some alien reachs an edge."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(oea_settings, aliens)
            break

def change_fleet_direction(oea_settings, aliens):
    """Makes the entire fleet descend and changes its direction."""
    for alien in aliens.sprites():
        alien.rect.y += oea_settings.fleet_drop_speed
    oea_settings.fleet_direction *= -1

def ship_hit(oea_settings, stats, screen, ship, aliens, bullets):
    """"Responds to the fact that the spaceship has been hit by an alien."""
    if stats.ships_left > 0:
        stats.ships_left -= 1
        aliens.empty()
        bullets.empty()
        create_fleet(oea_settings, screen, ship, aliens)
        ship.center_ship()
        sleep(0.5)
    else:
        stats.game_active = False

def check_aliens_bottom(oea_settings, stats, screen, ship, aliens, bullets):
    """Verify if any aliens reachs the bottom of the screen."""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(oea_settings, stats, screen, ship, aliens, bullets)
            break

def update_aliens(oea_settings, stats, screen, ship, aliens, bullets):
    """Updates the position of all the aliens of the fleet."""
    check_fleet_edges(oea_settings, aliens)
    aliens.update()

    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(oea_settings, stats, screen, ship, aliens, bullets)
    
    check_aliens_bottom(oea_settings, stats, screen, ship, aliens, bullets)
