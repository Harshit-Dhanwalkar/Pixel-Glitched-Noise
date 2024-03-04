import pygame
import numpy as np
import sys

# Initialize Pygame
pygame.init()

# Load the input image
filename = 'golden-bengal-cat-black-wall.jpg'
src = pygame.image.load(filename)

# Get the original width and height of the image
original_width, original_height = src.get_size()

# Set the desired display width and height
display_width, display_height = 400, 300  # Adjust these values as needed

# Resize the input image
src = pygame.transform.scale(src, (display_width, display_height))

# Create a new surface with the same size as the resized input image
img = pygame.Surface((display_width, display_height))

# Copy the resized input image to the new surface
img.blit(src, (0, 0))

# Distortion parameters
distortion_amount = 70  # You can adjust this value to control the amount of distortion
distortion_direction = -1  # 1 for ascending order, -1 for descending order

# Convert the surface to a NumPy array
pixels = pygame.surfarray.array3d(img)

# Apply the pixel sort
sorted_pixels = np.sort(pixels, axis=2)[::distortion_direction]  # Apply distortion direction

# Explicitly cast the array to int32 before distortion
sorted_pixels = sorted_pixels.astype(np.int32)

# Add distortion to the sorted pixels
distortion = np.random.randint(-distortion_amount, distortion_amount + 1, sorted_pixels.shape)
sorted_pixels += distortion

# Clip the values to the valid range [0, 255]
sorted_pixels = np.clip(sorted_pixels, 0, 255).astype(np.uint8)

# Convert the sorted pixels back to a surface
sorted_img = pygame.surfarray.make_surface(sorted_pixels)

# Display the resized input and output images
window = pygame.display.set_mode((display_width * 2, display_height))
window.blit(src, (0, 0))
window.blit(sorted_img, (display_width, 0))
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
