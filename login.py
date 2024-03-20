import sys
from PyQt5.QtCore import Qt
import time

from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtCore import QPropertyAnimation
from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit
from packages_import import *

class LoginWindow(QMainWindow):
    def __init__(self, widget):
        self.widget = widget
        super(LoginWindow, self).__init__()
        loadUi("login.ui", self)
        self.passwordIsHide = True
        # self.widget.setWindowTitle("Login")
        self.signup_page.setMaximumWidth(0)
        self.signin_btn.clicked.connect(self.logging_in_func)
        self.about_btn.clicked.connect(self.enter_register)
        self.cancel_btn.clicked.connect(self.exit_register)
        self.aboutus_info_label.setText(ABOUT_US_TEXT)
        self.hide_password_btn.clicked.connect(self.hiding_password)
    
    def hiding_password(self):
        self.passwordIsHide = not self.passwordIsHide
        if self.passwordIsHide:
            self.signin_password_input.setEchoMode(QLineEdit.Password)
        else:
            self.signin_password_input.setEchoMode(QLineEdit.Normal)

        
    
    def init_login(self):
        self.passwordIsHide = False
        self.hiding_password()
        self.signin_username_input.setText("")
        self.signin_password_input.setText("")

    def logging_in_func(self):
        if bool(logging_user(self.signin_username_input.text(),self.signin_password_input.text())):
            self.correct_user()
        else:
            self.wrong_user()
        

    def correct_user(self):
        print("CORRECT")
        success_login(self.signin_username_input.text())
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)
        self.widget.setWindowTitle(self.widget.currentWidget().objectName())
        self.widget.currentWidget().logging_in_func()
        self.signin_name_label.setStyleSheet("color: '#000'")

    def wrong_user(self):
        self.signin_name_label.setStyleSheet("color: '#ff0000'")
        print("WRONG")
        self.init_login()


    def enter_register(self):
        self.signup_page.setMaximumWidth(2000)

    def exit_register(self):
        self.signup_page.setMaximumWidth(0)