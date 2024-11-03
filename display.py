# display.py
import pygame  # Assuming pygame is used for display handling

class Display:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 480))  # Adjust resolution
        pygame.display.set_caption("Car Music Player")

    def update(self, track_info=None):
        self.screen.fill((0, 0, 0))  # Clear screen with black
        if track_info:
            # Display track information (simple example)
            font = pygame.font.Font(None, 36)
            text = font.render(track_info.get("name", "No track"), True, (255, 255, 255))
            self.screen.blit(text, (10, 10))
        pygame.display.flip()
