import ffmpeg
from PyQt6 import uic, QtWidgets
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget, QMessageBox
from my_py_code.format_setting_video import FormatSettingVideo
from my_py_code.music_listen import MusicListen
from my_py_code.video_watch import VideoWatch


class VideoConverterPlayerCustomQWidget(QWidget):
    def __init__(self, parent=None, name='Untitled', format='.mp4', size='0.0 Mb', filepath="", bool_color=True):
        super(VideoConverterPlayerCustomQWidget, self).__init__(parent)
        self.rate = None
        self.resolution = None
        self.filetype = format
        self.filepath = filepath
        self.format_out = ".mp4"
        self.format_video = None

        uic.loadUi('./gui/custom_video_converter_listitem.ui', self)
        self.name = self.findChild(QtWidgets.QPushButton, 'name')
        self.format = self.findChild(QtWidgets.QLabel, 'format')
        self.w_h_size = self.findChild(QtWidgets.QLabel, 'w_h_size')
        self.size = self.findChild(QtWidgets.QLabel, 'size')
        self.music_img = self.findChild(QtWidgets.QLabel, 'music_img')
        self.result = self.findChild(QtWidgets.QLabel, 'result')
        self.result.setHidden(True)

        self.con_format = self.findChild(QtWidgets.QLabel, 'con_format')
        self.con_format.setText(self.format_out)
        self.con_w_h_size = self.findChild(QtWidgets.QLabel, 'con_w_h_size')

        probe = ffmpeg.probe(self.filepath)
        video_streams = [stream for stream in probe["streams"] if stream["codec_type"] == "video"]
        width = str(video_streams[0]['width'])
        height = str(video_streams[0]['height'])
        self.w_h_size.setText(width + "x" + height)
        self.con_w_h_size.setText(width + "x" + height)
        self.resolution = self.con_w_h_size.text()
        self.con_fps = self.findChild(QtWidgets.QLabel, 'con_fps')
        self.con_fps.setText("30 fps")
        self.rate = "30 fps"

        self.video_converter_setting = self.findChild(QtWidgets.QPushButton, 'video_converter_setting')
        self.video_converter_setting.clicked.connect(self.video_setting)
        self.video_converter_start = self.findChild(QtWidgets.QPushButton, 'video_converter_start')

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

    def video_setting(self):
        self.format_video = FormatSettingVideo()
        self.format_video.submitClicked.connect(self.on_sub_window_confirm)
        self.format_video.exec()

    def on_sub_window_confirm(self, type_c, resolution, rate):  # <-- This is the main window's slot
        self.con_format.setText(type_c)
        self.format_out = type_c
        format_out = type_c
        if (format_out == ".mp3" or format_out == ".mpa" or
                format_out == ".m4a" or format_out == ".wav"):
            self.con_w_h_size.setText("")
            self.con_fps.setText("")

        else:
            if resolution == "Avto":
                self.con_w_h_size.setText(self.w_h_size.text())
                resolution = self.w_h_size.text()
            else:
                self.con_w_h_size.setText(resolution)
            if rate == "Avto":
                self.con_fps.setText("30 fps")
                rate = "30 fps"
            else:
                self.con_fps.setText(rate)

        self.filetype = type_c
        self.resolution = resolution
        self.rate = rate

    def play_video(self):
        self.formattype = self.filetype
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
