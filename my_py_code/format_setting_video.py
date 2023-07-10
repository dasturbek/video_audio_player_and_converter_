from PyQt6 import uic, QtWidgets
from PyQt6.QtWidgets import QDialog
from PyQt6 import QtCore as qtc


class FormatSettingVideo(QDialog):
    submitClicked = qtc.pyqtSignal(str, str, str)

    def __init__(self, parent=None):
        super(FormatSettingVideo, self).__init__(parent)
        self.format_out = None
        uic.loadUi('./gui/format_setting_video.ui', self)
        self.buttonbox = self.findChild(QtWidgets.QDialogButtonBox, "buttonBox")
        self.type_con = self.findChild(QtWidgets.QComboBox, "type_con")
        self.rate = self.findChild(QtWidgets.QComboBox, "rate")
        self.resolution = self.findChild(QtWidgets.QComboBox, "resolution")

        self.buttonbox.accepted.connect(self.onAccepted)
        self.buttonbox.rejected.connect(self.onRejected)
        self.type_con.activated.connect(self.format_enabled)

    def onAccepted(self):
        type_c = self.type_con.currentText()
        rate = self.rate.currentText()
        resolution = self.resolution.currentText()

        self.submitClicked.emit(type_c, resolution, rate)
        self.close()

    def onRejected(self):
        self.close()

    def format_enabled(self):
        format_out = self.type_con.currentText()
        if (format_out == ".mp3" or format_out == ".mpa" or
                format_out == ".m4a" or format_out == ".ogg" or
                format_out == ".m3u" or format_out == "wav"):
            self.resolution.setEnabled(False)
            self.rate.setEnabled(False)
        else:
            self.resolution.setEnabled(True)
            self.rate.setEnabled(True)



