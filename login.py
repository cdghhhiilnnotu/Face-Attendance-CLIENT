import sys
from PyQt5.QtCore import Qt

from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtCore import QPropertyAnimation
from PyQt5.QtWidgets import QMainWindow, QApplication


class LoginWindow(QMainWindow):
    def __init__(self, widget):
        self.widget = widget
        super(LoginWindow, self).__init__()
        loadUi("login.ui", self)
        # self.widget.setWindowTitle("Login")
        self.signup.setMaximumWidth(0)
        self.signin_btn.clicked.connect(self.logging_in)
        self.register_btn.clicked.connect(self.enter_register)
        self.cancel_register_btn.clicked.connect(self.exit_register)

    def logging_in(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)
        self.widget.setWindowTitle(self.widget.currentWidget().objectName())

    def enter_register(self):
        self.signup.setMaximumWidth(2000)

    def exit_register(self):
        self.signup.setMaximumWidth(0)