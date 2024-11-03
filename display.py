# display.py
import pygame

class Display:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 480))
        pygame.display.set_caption("Car Music Player")
        
        # Define button areas
        self.login_button = pygame.Rect(50, 50, 150, 50)  # New Login button
        self.play_button = pygame.Rect(50, 400, 100, 50)
        self.next_button = pygame.Rect(200, 400, 100, 50)
        self.prev_button = pygame.Rect(350, 400, 100, 50)

    def update(self, track_info=None):
        self.screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 36)

        # Draw login button
        pygame.draw.rect(self.screen, (150, 150, 0), self.login_button)
        login_text = font.render("Login", True, (255, 255, 255))
        self.screen.blit(login_text, (self.login_button.x + 10, self.login_button.y + 10))

        # Draw playback buttons
        pygame.draw.rect(self.screen, (100, 200, 100), self.play_button)
        pygame.draw.rect(self.screen, (200, 100, 100), self.next_button)
        pygame.draw.rect(self.screen, (100, 100, 200), self.prev_button)

        pygame.display.flip()
