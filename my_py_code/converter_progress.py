import datetime
import threading

from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QVBoxLayout
from PyQt6 import QtCore as qtc

from my_py_code.converter_audio import ConverterAudio
from my_py_code.converter_video import ConverterVideo
from my_py_code.loading import Loading


class ConverterProgress(QtWidgets.QDialog):
    submitClicked = qtc.pyqtSignal(str, str)

    def __init__(self, parent=None, inp="", path="", format_out="", finish="", resolution="", rate=""):
        super(ConverterProgress, self).__init__(parent)
        self.setMaximumSize(270, 270)
        self.setMinimumSize(270, 270)
        self.setWindowTitle("Converter Start")
        self.setWindowIcon(QIcon("./gui/qrc/dasturbek.png"))

        self.timer = None
        self.format_out = format_out
        self.out = None
        self.inp = inp
        self.path = path
        self.finish = finish
        self.resolution = resolution
        self.rate = rate

        self.progress_bar = Loading()
        self.progress_bar.setStyleSheet(
            "QCircularProgressBar {"
            "qproperty-bg_color1: #b30000;"
            "qproperty-bg_color2: #ff6666;"
            "qproperty-mask_color: #ff8080;"
            "qproperty-text_color: #ff6700;"
            "qproperty-text_bg_color: rgba(255,255,255,0);}"
        )
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(self.progress_bar)
        self.button = QtWidgets.QPushButton("Start")
        self.button.setMinimumHeight(30)
        self.button.setMaximumHeight(30)
        layout.addWidget(self.button)
        self.setLayout(layout)
        self.button.clicked.connect(self.converter)

    def converter(self):
        # fileinfo = QFileInfo(self.inp)
        # basename = fileinfo.baseName()
        now = datetime.datetime.now().strftime('%Y_%m_%d__%H_%M_%S')
        basename = "dasturbek"
        self.out = self.path + "/" + basename + f"({now})" + self.format_out

        if self.finish == "video":
            video_con = ConverterVideo(self.inp, self.out, self.format_out, self.resolution, self.rate)
            video_con.converter_run()
        elif self.finish == "audio":
            audio_con = ConverterAudio(self.inp, self.out)
            audio_con.converter_run()
        self.submitClicked.emit(self.out, self.finish)
        self.close()
