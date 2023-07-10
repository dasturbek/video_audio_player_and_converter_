from PyQt6 import uic, QtWidgets
from PyQt6.QtWidgets import QWidget
from my_py_code.format_setting_audio import FormatSettingAudio
from my_py_code.music_listen import MusicListen


class MusicConverterCustomQWidget(QWidget):
    def __init__(self, parent=None, name='Untitled', format='.mp3', size='0.0 Mb', filepath="", bool_color=True):
        super(MusicConverterCustomQWidget, self).__init__(parent)
        self.filetype = ".mp3"
        self.filepath = filepath
        self.formattype = format

        self.format_audio = None
        uic.loadUi('./gui/custom_music_converter_listitem.ui', self)
        self.name = self.findChild(QtWidgets.QPushButton, 'name')
        self.format = self.findChild(QtWidgets.QLabel, 'format')
        self.size = self.findChild(QtWidgets.QLabel, 'size')
        self.music_img = self.findChild(QtWidgets.QLabel, 'music_img')
        self.result = self.findChild(QtWidgets.QLabel, 'result')
        self.result.setHidden(True)

        self.con_format = self.findChild(QtWidgets.QLabel, 'con_format')
        self.con_format.setText(self.filetype)
        self.con_size = self.findChild(QtWidgets.QLabel, 'con_size')

        self.music_converter_setting = self.findChild(QtWidgets.QPushButton, 'music_converter_setting')
        self.music_converter_setting.clicked.connect(self.audio_setting)
        self.name.clicked.connect(self.play_music)

        self.close_f = self.findChild(QtWidgets.QPushButton, 'close')

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

    def audio_setting(self):
        self.format_audio = FormatSettingAudio()
        self.format_audio.submitClicked.connect(self.on_sub_window_confirm)
        self.format_audio.exec()

    def on_sub_window_confirm(self, url):  # <-- This is the main window's slot
        self.con_format.setText(url)
        self.filetype = url

    def play_music(self):
        music_liste = MusicListen(self, self.filepath)
        music_liste.exec()
