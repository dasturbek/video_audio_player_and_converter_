from PyQt6 import uic, QtWidgets
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget, QMessageBox

from my_py_code.music_listen import MusicListen
from my_py_code.video_watch import VideoWatch


class FinishVideoConverterPlayerCustomQWidget(QWidget):
    def __init__(self, parent=None, name='Untitled', format='.mp4', size='0.0 Mb', filepath="", bool_color=True):
        super(FinishVideoConverterPlayerCustomQWidget, self).__init__(parent)
        self.filetype = None
        self.filepath = filepath
        self.formattype = format

        uic.loadUi('./gui/finish_custom_video_converter_listitem.ui', self)
        self.name = self.findChild(QtWidgets.QPushButton, 'name')
        self.format = self.findChild(QtWidgets.QLabel, 'format')
        self.size = self.findChild(QtWidgets.QLabel, 'size')
        self.music_img = self.findChild(QtWidgets.QLabel, 'music_img')

        self.close_f = self.findChild(QtWidgets.QPushButton, 'close')
        self.name.clicked.connect(self.play_video)

        self.name.setText(name)
        self.format.setText(format)
        self.size.setText(size + ' Mb')

        self.frame = self.findChild(QtWidgets.QFrame, 'frame')
        if bool_color:
            self.frame.setStyleSheet("#frame{"
                                     "border:none;"
                                     "background-color: rgb(234, 234, 234);"
                                     "}"
                                     "#frame:hover{"
                                     "background-color:rgb(176, 227, 227);"
                                     "}")
        else:
            self.frame.setStyleSheet("#frame{"
                                     "border:none;"
                                     "background-color:rgb(250, 250, 250);"
                                     "}"
                                     "#frame:hover{"
                                     "background-color:rgb(176, 227, 227);"
                                     "}")

    def play_video(self):
        if (self.formattype == "mp3" or self.formattype == "mpa" or
                self.formattype == "m4a" or self.formattype == "wav"):
            music = MusicListen(self, self.filepath)
            music.exec()
        else:
            if self.formattype == "mp4" or self.formattype == "avi":
                video = VideoWatch(self, self.filepath)
                video.exec()
            else:
                close = QMessageBox()
                close.setWindowTitle("Warning")
                close.setIcon(QMessageBox.Icon.Warning)
                close.setWindowIcon(QIcon("./gui/qrc/dasturbek.png"))
                close.setText("Video type unsupported")
                close.setStandardButtons(QMessageBox.StandardButton.Yes)
                close.exec()
