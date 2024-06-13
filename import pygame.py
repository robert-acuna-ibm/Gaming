import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sins of Valoria")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Player settings
player_size = 50
player_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT - 2 * player_size]
player_speed = 10

# Enemy settings
enemy_size = 50
enemy_pos = [SCREEN_WIDTH // 2, enemy_size]
enemy_speed = 10

# Clock
clock = pygame.time.Clock()

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
        enemy_pos[0] = pygame.randint(0, SCREEN_WIDTH - enemy_size)

    # Collision detection
    if (player_pos[0] < enemy_pos[0] < player_pos[0] + player_size or
        enemy_pos[0] < player_pos[0] < enemy_pos[0] + enemy_size) and \
       (player_pos[1] < enemy_pos[1] < player_pos[1] + player_size or
        enemy_pos[1] < player_pos[1] < enemy_pos[1] + enemy_size):
        game_over = True

    pygame.display.flip()
    clock.tick(30)
