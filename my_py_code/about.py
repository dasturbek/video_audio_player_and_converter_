from PyQt6 import uic, QtWidgets
from PyQt6.QtWidgets import QDialog


class About(QDialog):
    def __init__(self, parent=None):
        super(About, self).__init__(parent)

        uic.loadUi('./gui/about.ui', self)
        self.cancel = self.findChild(QtWidgets.QPushButton, 'cancel')
        self.cancel.clicked.connect(self.close)
