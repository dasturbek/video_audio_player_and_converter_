from PyQt6 import uic, QtWidgets
from PyQt6.QtWidgets import QDialog
from PyQt6 import QtCore as qtc


class FormatSettingAudio(QDialog):
    submitClicked = qtc.pyqtSignal(str)

    def __init__(self, parent=None):
        super(FormatSettingAudio, self).__init__(parent)
        uic.loadUi('./gui/format_setting_audio.ui', self)
        self.buttonbox = self.findChild(QtWidgets.QDialogButtonBox, "buttonBox")
        self.type_audio = self.findChild(QtWidgets.QComboBox, "type_audio")

        self.buttonbox.accepted.connect(self.onAccepted)
        self.buttonbox.rejected.connect(self.onRejected)

    def onAccepted(self):
        data = self.type_audio.currentText()
        self.submitClicked.emit(data)
        self.close()

    def onRejected(self):
        self.close()
