import sys

from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QDialog

from my_py_code.custom_progress import QCircularProgressBar
from my_py_code.mainwindow import MainWindow
from my_py_code.music_player import MusicPlayer
from my_py_code.video_player import VideoPlayer


class SplashWindow(QDialog):
    def __init__(self, parent=None):
        super(SplashWindow, self).__init__(parent)

        self.window = None
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)

        self.setWindowTitle(" ")

        self.progress_bar = QCircularProgressBar()
        self.progress_bar.setStyleSheet(
            "QCircularProgressBar {"
            "qproperty-bg_color1: #002855;"
            "qproperty-bg_color2: #64b5f6;"
            "qproperty-mask_color: #90caf9;"
            "qproperty-text_color: #0b506b;"
            "qproperty-text_bg_color: #e3f2fd;}"
        )
        self.progress_bar.setFormat("Loading...")
        layout = QVBoxLayout()
        layout.addWidget(self.progress_bar)

        self.setLayout(layout)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_progress_bar)
        self.timer.start(1)

    def update_progress_bar(self):
        if self.progress_bar.current_value < 100:
            self.progress_bar.setValue(self.progress_bar.current_value + 0.2)
        else:
            self.timer.stop()
            self.close()
            # main window show
            self.window = MainWindow()
            self.window.show()
