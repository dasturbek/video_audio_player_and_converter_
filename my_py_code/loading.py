import threading

from PyQt6 import QtCore
from PyQt6.QtCore import QTimer, Qt, pyqtProperty
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import (QVBoxLayout, QWidget, QLabel, QSizePolicy)


class Loading(QWidget):
    bg_color1 = pyqtProperty(
        str, lambda self: QColor(self._bg_color1).name(), lambda self, col:
        setattr(self, "_bg_color1", col), )
    bg_color2 = pyqtProperty(
        str, lambda self: QColor(self._bg_color2).name(), lambda self, col:
        setattr(self, "_bg_color2", col), )
    mask_color = pyqtProperty(
        str, lambda self: QColor(self._mask_color).name(), lambda self, col:
        setattr(self, "_mask_color", col), )
    text_color = pyqtProperty(
        str, lambda self: QColor(self._text_color).name(), lambda self, col:
        setattr(self, "_text_color", col), )
    text_bg_color = pyqtProperty(
        str, lambda self: QColor(self._text_bg_color).name(), lambda self, col:
        setattr(self, "_text_bg_color", col), )

    def __init__(self, parent=None):
        super().__init__()

        self.timer = QTimer()
        self.timer.timeout.connect(self.rotate)
        self.timer.start(1)  # ~60 FPS
        self.angle = 0
        self.current_value = 0

        self._bg_color1 = "rgb(0, 255, 255)"
        self._bg_color2 = "rgb(0, 69, 142)"
        self._mask_color = "rgb(227, 227, 227)"
        self._text_color = "rgb(0, 0, 0)"
        self._text_bg_color = "rgb(255, 255, 255)"

        self.Circle_size = 200  # Widget Size
        chunk_size = int(self.Circle_size * 0.08)
        self.center_radius = int(
            self.Circle_size * 0.42)  # Center Circle Size (0.43 + 0.07 = 0.5)
        self.percent_size = int(self.Circle_size * 0.25)  # Percentil Size
        self.text_size = int(self.Circle_size * 0.12)

        self.alignment = None
        self.description = " "
        self.indicator = None
        self.progress = None

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        self.ProgressBack = QWidget(parent)
        self.ProgressBack.setObjectName("ProgressBack")
        self.ProgressBack.setMinimumSize(
            QtCore.QSize(self.Circle_size, self.Circle_size))
        size_policy = QSizePolicy(QSizePolicy.Policy.Fixed,
                                  QSizePolicy.Policy.Fixed)
        self.ProgressBack.setSizePolicy(size_policy)
        self.ProgressBack_2 = QVBoxLayout(self.ProgressBack)
        self.ProgressBack_2.setObjectName("ProgressBack_2")
        self.ProgressBack_2.setContentsMargins(0, 0, 0, 0)

        self.ProgressIndicator = QWidget(self.ProgressBack)
        self.ProgressIndicator.setObjectName("ProgressIndicator")

        self.ProgressIndicator_2 = QVBoxLayout(self.ProgressIndicator)
        self.ProgressIndicator_2.setObjectName("ProgressIndicator_2")
        self.ProgressIndicator_2.setContentsMargins(
            chunk_size, chunk_size, chunk_size, chunk_size)

        self.ProgressLabel = QLabel(self.ProgressIndicator)
        self.ProgressLabel.setObjectName("ProgressLabel")

        self.ProgressIndicator_2.addWidget(self.ProgressLabel)
        self.ProgressBack_2.addWidget(self.ProgressIndicator)
        self.layout.addWidget(self.ProgressBack,
                              alignment=Qt.AlignmentFlag.AlignCenter)

    def setValue(self, value):
        self.current_value = value

    def setFormat(self, text):
        self.description = text
        self.update_font_size()

    def setLabelStyleSheet(self):
        style = (
                "border-radius:" + str(self.center_radius) +
                "px; background-color:" + self._text_bg_color + ";")
        self.ProgressLabel.setStyleSheet(style)

    def update_label(self):
        if self.description is None:
            text = ""
            self.percent_size = int(self.Circle_size * 0.25)
        else:
            text = self.description

        percentage = str(round(self.current_value, None))

        sup_size = int(self.percent_size * 0.75)

        self.progress = self.current_value / 100
        self.indicator = 270 - (self.current_value * 3.6)

        f_text = (
                '<br><span style="color:' + self.text_color
                + ";font-size:" + str(self.text_size) + 'px;">'
                + "" + "</span>")

        style = ('<p align="center">' + f_text + "</p>")
        self.ProgressLabel.setText(style)

    def update_font_size(self):
        max_characters = 11
        text_length = len(self.description)
        if text_length > max_characters:
            shrink_factor = max_characters / text_length
            self.text_size = int((self.Circle_size * 0.14) * shrink_factor)
        else:
            self.text_size = int(self.Circle_size * 0.12)

    def rotate(self):
        self.angle -= 1
        radius = int(self.Circle_size / 2)
        base_style = (
                "border: 0px; background-color: qconicalgradient(cx:0.5,cy:0.5,"
                " angle:" + str(self.angle) + ", stop:0 " + self._bg_color1 +
                ", stop:0.5 " + self._bg_color2 + ", stop:1 " + self._bg_color1
                + "); border-radius:" + str(radius) + "px")
        self.ProgressBack.setStyleSheet(base_style)
        self.setLabelStyleSheet()
        self.update_label()

    def setAlignment(self, alignment):
        self.alignment = alignment

    def setMinimumWidth(self, width):
        self.ProgressBack.setMinimumWidth(width)


