import pygame
import numpy as np
import sys

# Initialize Pygame
pygame.init()

# Load the image
filename = 'golden-bengal-cat-black-wall.jpg'
src = pygame.image.load(filename)

# Get the width and height of the image
width, height = src.get_size()

# Create a new surface with the same size as the image
img = pygame.Surface((width, height))

# Copy the image to the new surface
img.blit(src, (0, 0))

# Distortion parameters
distortion_amount = 7  # You can adjust this value to control the amount of distortion
distortion_direction = 1  # 1 for ascending order, -1 for descending order

# Convert the surface to a NumPy array
pixels = pygame.surfarray.array3d(img)

# Apply the pixel sort
sorted_pixels = np.sort(pixels, axis=0)[::distortion_direction]  # Apply distortion direction

# Explicitly cast the array to int32 before distortion
sorted_pixels = sorted_pixels.astype(np.int32)

# Add distortion to the sorted pixels
distortion = np.random.randint(-distortion_amount, distortion_amount + 1, sorted_pixels.shape)
sorted_pixels += distortion

# Clip the values to the valid range [0, 255]
sorted_pixels = np.clip(sorted_pixels, 0, 255).astype(np.uint8)

# Convert the sorted pixels back to a surface
sorted_img = pygame.surfarray.make_surface(sorted_pixels)

# Display the sorted image
window = pygame.display.set_mode((width, height))
window.blit(sorted_img, (0, 0))
pygame.display.flip()

# Wait for the user to close the window
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:  # If 'q' is pressed
                pygame.quit()
                sys.exit()
