import pygame
import sys

# Initialize pygame
pygame.init()

# Set up display
window_width = 800
window_height = 600
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Estéreo Picnic Festival Simulation")

# Colors
background_color = (34, 139, 34)  # Green for grass
stage_color = (139, 0, 0)          # Dark red for the stage area
bar_color = (255, 215, 0)          # Gold for the bar areas

# Positions and sizes
stage_rect = pygame.Rect(100, 50, 600, 100)  # x, y, width, height
bar1_rect = pygame.Rect(100, 200, 100, 50)
bar2_rect = pygame.Rect(600, 200, 100, 50)

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the screen with the background color
    screen.fill(background_color)

    # Draw the stage area
    pygame.draw.rect(screen, stage_color, stage_rect)

    # Draw the bar areas
    pygame.draw.rect(screen, bar_color, bar1_rect)
    pygame.draw.rect(screen, bar_color, bar2_rect)

    # Update the display
    pygame.display.flip()
