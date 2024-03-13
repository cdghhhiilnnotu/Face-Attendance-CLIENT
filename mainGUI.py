import sys
from PyQt5.QtCore import Qt

from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication

from attendance import AttendanceWindow
from login import LoginWindow

app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
loginWin = LoginWindow(widget)
attendanceWin = AttendanceWindow(widget)

widget.setFixedWidth(800)
widget.setFixedHeight(500)

widget.addWidget(loginWin)
widget.addWidget(attendanceWin)
widget.setWindowTitle(widget.currentWidget().objectName())
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("Exiting")


