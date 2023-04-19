# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 23:13:28 2023

@author: josia
"""

import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Image Movement')

# Load images
image1 = pygame.image.load('image1.jpg')
image2 = pygame.image.load('image2.jpg')

# Set initial positions
image1_x = 0
image1_y = window_height // 2 - image1.get_height() // 2
image2_x = window_width // 2 - image2.get_width() // 2
image2_y = 0

# Set initial velocities
image1_velocity = 2
image2_velocity_x = 1
image2_velocity_y = 1

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update image1 position
    image1_x += image1_velocity
    if image1_x > window_width:
        image1_x = -image1.get_width()

    # Update image2 position
    image2_x += image2_velocity_x
    image2_y += image2_velocity_y

    if image2_x < 0 or image2_x > window_width - image2.get_width():
        image2_velocity_x = -image2_velocity_x

    if image2_y < 0 or image2_y > window_height - image2.get_height():
        image2_velocity_y = -image2_velocity_y

    # Fill window with white color
    window.fill((255, 255, 255))

    # Draw images on the window
    window.blit(image1, (image1_x, image1_y))
    window.blit(image2, (image2_x, image2_y))

    # Update display
    pygame.display.update()




