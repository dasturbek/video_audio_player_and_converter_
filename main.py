from PyQt6 import QtWidgets
import sys

from my_py_code.splash_window import SplashWindow

app = QtWidgets.QApplication(sys.argv)

# splash window
window = SplashWindow()
window.show()

app.exec()
