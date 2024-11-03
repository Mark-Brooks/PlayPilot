import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 480))
pygame.display.set_caption("Pygame Test")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((255, 0, 0))  # Fill the screen with red
    pygame.display.flip()  # Update the display
