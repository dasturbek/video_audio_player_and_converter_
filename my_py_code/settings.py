from PyQt6 import uic, QtWidgets
from PyQt6.QtWidgets import QDialog


class Settings(QDialog):
    def __init__(self, parent=None):
        super(Settings, self).__init__(parent)

        uic.loadUi('./gui/settings.ui', self)
