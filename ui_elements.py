# ui_elements.py
import pygame

class Button:
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text

    def draw(self, screen):
        pygame.draw.rect(screen, (100, 100, 100), self.rect)  # Button color
        font = pygame.font.Font(None, 36)
        text_surf = font.render(self.text, True, (255, 255, 255))
        screen.blit(text_surf, (self.rect.x + 5, self.rect.y + 5))
