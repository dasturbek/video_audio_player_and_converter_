from PyQt6 import uic, QtWidgets
from PyQt6.QtCore import QFileInfo
from PyQt6.QtWidgets import QWidget


class MusicPlayerCustomQWidget(QWidget):
    def __init__(self, parent=None, filepath='Untitled', format='mp3', size='0.0 Mb', time='00:00:00', bool_color=True):
        super(MusicPlayerCustomQWidget, self).__init__(parent)

        uic.loadUi('./gui/custom_music_listitem.ui', self)
        self.name = self.findChild(QtWidgets.QLabel, 'name')
        self.format = self.findChild(QtWidgets.QLabel, 'format')
        self.size = self.findChild(QtWidgets.QLabel, 'size')
        self.time = self.findChild(QtWidgets.QLabel, 'time')
        self.music_img = self.findChild(QtWidgets.QLabel, 'music_img')
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

        filename = QFileInfo(filepath)
        self.name.setText(filename.fileName())
        self.format.setText(format)
        self.size.setText(size + ' Mb')
        self.time.setText(time)
