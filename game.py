import pygame
import sys
import os
import random

# Initialize Pygame
pygame.init()

# Screen dimensions and full screen option
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FULLSCREEN = False

# Screen initialization
if FULLSCREEN:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
else:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sins of Valoria")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Fonts
font_large = pygame.font.SysFont("arial", 72)
font_small = pygame.font.SysFont("arial", 36)
font_credits = pygame.font.SysFont("arial", 24)

# Load image
image = pygame.image.load('ValoriaHomePage.png')
image = pygame.transform.scale(image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Sound files
sound_files = [os.path.join('sounds', file) for file in os.listdir('sounds') if file.endswith('.wav')]

# Function to play a random scary sound
def play_random_sound():
    if sound_files:
        sound = random.choice(sound_files)
        pygame.mixer.Sound(sound).play()

def show_splash_screen():
    screen.blit(image, (0, 0))
    credits_text = font_credits.render("Powered by RHUD Software - Games Division - copyright RHUDSoftware, Inc 2024", True, WHITE)
    screen.blit(credits_text, (SCREEN_WIDTH // 2 - credits_text.get_width() // 2, SCREEN_HEIGHT - credits_text.get_height() - 20))
    pygame.display.flip()
    
    # Wait for a key press
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                play_random_sound()
                waiting = False

# Show splash screen
show_splash_screen()

# Main game loop
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT] and player_pos[0] < SCREEN_WIDTH - player_size:
        player_pos[0] += player_speed
    if keys[pygame.K_UP] and player_pos[1] > 0:
        player_pos[1] -= player_speed
    if keys[pygame.K_DOWN] and player_pos[1] < SCREEN_HEIGHT - player_size:
        player_pos[1] += player_speed

    screen.fill(BLACK)

    pygame.draw.rect(screen, RED, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))
    pygame.draw.rect(screen, WHITE, (player_pos[0], player_pos[1], player_size, player_size))

    enemy_pos[1] += enemy_speed
    if enemy_pos[1] > SCREEN_HEIGHT:
        enemy_pos[1] = 0 - enemy_size
        enemy_pos[0] = random.randint(0, SCREEN_WIDTH - enemy_size)

    # Collision detection
    if (player_pos[0] < enemy_pos[0] < player_pos[0] + player_size or
        enemy_pos[0] < player_pos[0] < enemy_pos[0] + enemy_size) and \
       (player_pos[1] < enemy_pos[1] < player_pos[1] + player_size or
        enemy_pos[1] < player_pos[1] < player_pos[1] + enemy_size):
        game_over = True

    pygame.display.flip()
    clock.tick(30)

print("Game Over")