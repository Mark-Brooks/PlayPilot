# spotify_client.py
import requests

class SpotifyClient:
    def __init__(self, token):
        self.token = token
        self.headers = {"Authorization": f"Bearer {self.token}"}

    def play_track(self):
        requests.put("https://api.spotify.com/v1/me/player/play", headers=self.headers)

    def pause_track(self):
        requests.put("https://api.spotify.com/v1/me/player/pause", headers=self.headers)

    def next_track(self):
        requests.post("https://api.spotify.com/v1/me/player/next", headers=self.headers)

    def get_current_track(self):
        response = requests.get("https://api.spotify.com/v1/me/player/currently-playing", headers=self.headers)
        return response.json() if response.status_code == 200 else None
