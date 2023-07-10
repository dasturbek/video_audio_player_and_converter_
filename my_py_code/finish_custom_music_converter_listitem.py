from PyQt6 import uic, QtWidgets
from PyQt6.QtWidgets import QWidget
from my_py_code.music_listen import MusicListen


class FinishMusicConverterCustomQWidget(QWidget):
    def __init__(self, parent=None, name='Untitled', format='.mp3', size='0.0 Mb', filepath="", bool_color=True):
        super(FinishMusicConverterCustomQWidget, self).__init__(parent)
        self.filetype = None
        self.filepath = filepath
        self.formattype = format
        self.parent = parent

        self.format_audio = None
        uic.loadUi('./gui/finish_custom_music_converter_listitem.ui', self)
        self.name = self.findChild(QtWidgets.QPushButton, 'name')
        self.format = self.findChild(QtWidgets.QLabel, 'format')
        self.size = self.findChild(QtWidgets.QLabel, 'size')
        self.music_img = self.findChild(QtWidgets.QLabel, 'music_img')

        self.close_f = self.findChild(QtWidgets.QPushButton, 'close')
        self.name.clicked.connect(self.play_music)

        self.name.setText(name)
        self.format.setText(format)
        self.size.setText(size + ' Mb')
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

    def play_music(self):
        music_liste = MusicListen(self, self.filepath)
        music_liste.exec()
