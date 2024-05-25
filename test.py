import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((800, 600))

# Load the player image
player_image = pygame.image.load("assets/pack/default/window/images/player_new.png")
player_rect = player_image.get_rect()
player_rect.center = (400, 300)

# Load the block image
block_image = pygame.image.load("assets/pack/default/window/images/player.png")
block_rect = block_image.get_rect()
block_rect.center = (600, 300)

# Define the player movement speed
player_speed = 5

# Define the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_rect.x += player_speed
    if keys[pygame.K_UP]:
        player_rect.y -= player_speed
    if keys[pygame.K_DOWN]:
        player_rect.y += player_speed

    # Check for collision with blocks
    if player_rect.colliderect(block_rect):
        # Handle collision here
        pass

    # Update the screen
    screen.fill((0, 0, 0))
    screen.blit(player_image, player_rect)
    screen.blit(block_image, block_rect)
    pygame.display.flip()

# Quit the game
pygame.quit()