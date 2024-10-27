# ui_manager.py
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from web_wrapper import WebWrapper
import sys

class UIManager:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.window = QMainWindow()
        self.web_wrapper = WebWrapper()

        # Setup window
        self.window.setWindowTitle("Car Music Player")
        self.window.setGeometry(0, 0, 800, 480)

        # Setup layout and web wrapper
        layout = QVBoxLayout()
        layout.addWidget(self.web_wrapper)
        container = QWidget()
        container.setLayout(layout)
        self.window.setCentralWidget(container)

    def handle_navigation(self, action):
        # Logic to handle rotary encoder actions
        if action == "next":
            self.web_wrapper.next_song()
        elif action == "previous":
            self.web_wrapper.previous_song()

    def run(self):
        self.window.show()
        sys.exit(self.app.exec_())
