import sys
import pygame
from bullet import Bullet

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
  
def update_screen(oea_settings, screen, ship, bullets):
    """Update the images on the screen and changes to the new screen."""
    screen.fill(oea_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()

    pygame.display.flip()

def update_bullets(bullets):
    """Update the projectile's position and remove the old projectiles."""
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    