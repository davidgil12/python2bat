import pygame

# Initialize Pygame
pygame.init()

# Define window size
win_width = 800
win_height = 600

# Create window surface
win = pygame.display.set_mode((win_width, win_height))

# Set window title
pygame.display.set_caption("Move Circle with Keyboard")

# Define circle properties
circle_color = (255, 0, 0)  # Red
circle_radius = 10
circle_x = win_width // 2
circle_y = win_height // 2
circle_speed = 5

reloj = pygame.time.Clock()

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move circle based on keyboard input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        circle_x -= circle_speed
    elif keys[pygame.K_RIGHT]:
        circle_x += circle_speed
    elif keys[pygame.K_UP]:
        circle_y -= circle_speed
    elif keys[pygame.K_DOWN]:
        circle_y += circle_speed

    # Clear screen
    win.fill((255, 255, 255))  # White

    # Draw circle
    pygame.draw.circle(win, circle_color, (circle_x, circle_y), circle_radius)

    # Update display
    pygame.display.update()

    reloj.tick(30)

# Quit Pygame
pygame.quit()
