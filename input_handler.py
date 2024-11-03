# input_handler.py
import pygame
from auth import authorize_user

class InputHandler:
    def __init__(self, spotify_client, display):
        self.spotify = spotify_client
        self.display = display

    def listen(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.display.login_button.collidepoint(event.pos):
                    authorize_user()  # Trigger login on button click
                elif self.display.play_button.collidepoint(event.pos):
                    self.spotify.pause_track() if self.spotify.is_playing() else self.spotify.play_track()
                elif self.display.next_button.collidepoint(event.pos):
                    self.spotify.next_track()
                elif self.display.prev_button.collidepoint(event.pos):
                    self.spotify.previous_track()
