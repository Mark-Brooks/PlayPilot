# web_wrapper.py
from PyQt5.QtWebEngineWidgets import QWebEngineView

class WebWrapper(QWebEngineView):
    def __init__(self):
        super().__init__()
        # Load a car-friendly web page
        self.load_url("https://open.spotify.com/")  # Modify with the appropriate login URL

    def load_url(self, url):
        self.setUrl(url)

    def next_song(self):
        # Implement control to go to the next song if possible
        pass

    def previous_song(self):
        # Implement control to go to the previous song if possible
        pass
