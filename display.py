# display.py
import pygame

class Display:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 480))  # Adjust to VNC resolution
        pygame.display.set_caption("Car Music Player")
        # Define button areas for playback controls
        self.play_button = pygame.Rect(50, 400, 100, 50)
        self.next_button = pygame.Rect(200, 400, 100, 50)
        self.prev_button = pygame.Rect(350, 400, 100, 50)

    def update(self, track_info=None):
        self.screen.fill((0, 0, 0))  # Clear screen with black
        font = pygame.font.Font(None, 36)
        if track_info:
            text = font.render(track_info.get("name", "No track"), True, (255, 255, 255))
            self.screen.blit(text, (10, 10))
        
        # Draw play/pause, next, and previous buttons
        pygame.draw.rect(self.screen, (100, 200, 100), self.play_button)   # Play button
        pygame.draw.rect(self.screen, (200, 100, 100), self.next_button)   # Next button
        pygame.draw.rect(self.screen, (100, 100, 200), self.prev_button)   # Previous button
        
        pygame.display.flip()
