# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginaaVOND.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import resources.resources

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(591, 411)
        font = QFont()
        font.setFamily(u"Cambria")
        Login.setFont(font)
        self.login_window = QWidget(Login)
        self.login_window.setObjectName(u"login_window")
        self.window = QWidget(self.login_window)
        self.window.setObjectName(u"window")
        self.window.setGeometry(QRect(0, 0, 591, 411))
        self.window.setCursor(QCursor(Qt.ArrowCursor))
        self.window.setStyleSheet(u"QPushButton#sign_in_btn{\n"
"	background-color: rgba(85, 98, 112, 200);\n"
"	color: rgba(255,255,255,200);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#sign_in_btn:pressed{\n"
"	padding-left: 5px;\n"
"	padding-top: 5px;\n"
"	background-color: rgba(255,107,107, 255);\n"
"	background-position: calc(100% - 5px)center;\n"
"}\n"
"\n"
"QPushButton#sign_in_btn:hover{\n"
"	background-color: rgba(255,107,107, 255);\n"
"}\n"
"\n"
"")
        self.log_side = QLabel(self.window)
        self.log_side.setObjectName(u"log_side")
        self.log_side.setGeometry(QRect(290, 40, 260, 330))
        self.log_side.setFont(font)
        self.log_side.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.decor_side = QLabel(self.window)
        self.decor_side.setObjectName(u"decor_side")
        self.decor_side.setGeometry(QRect(40, 25, 270, 360))
        self.decor_side.setFont(font)
        self.decor_side.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(85, 98, 112, 255), stop:1 rgba(255, 107, 107, 255));\n"
"border-radius: 10px;")
        self.decor_side.setPixmap(QPixmap(u":/apps/apps/login_bg.png"))
        self.decor_side.setScaledContents(True)
        self.decor_side.setAlignment(Qt.AlignCenter)
        self.sign_in_title = QLabel(self.window)
        self.sign_in_title.setObjectName(u"sign_in_title")
        self.sign_in_title.setGeometry(QRect(360, 60, 141, 31))
        font1 = QFont()
        font1.setFamily(u"Cascadia Code")
        font1.setPointSize(13)
        font1.setBold(True)
        font1.setWeight(75)
        self.sign_in_title.setFont(font1)
        self.sign_in_title.setAlignment(Qt.AlignCenter)
        self.signin_username_input = QLineEdit(self.window)
        self.signin_username_input.setObjectName(u"signin_username_input")
        self.signin_username_input.setGeometry(QRect(322, 120, 190, 31))
        font2 = QFont()
        font2.setFamily(u"Cascadia Code")
        font2.setPointSize(9)
        self.signin_username_input.setFont(font2)
        self.signin_username_input.setStyleSheet(u"background-color: rgba(0,0,0,0);\n"
"border: 2px solid rgba(0,0,0,0);\n"
"border-bottom-color: rgba(46, 82, 101, 200);\n"
"color: rgb(0,0,0);\n"
"padding-bottom:7px;\n"
"")
        self.signin_password_input = QLineEdit(self.window)
        self.signin_password_input.setObjectName(u"signin_password_input")
        self.signin_password_input.setGeometry(QRect(320, 190, 191, 31))
        self.signin_password_input.setFont(font2)
        self.signin_password_input.setStyleSheet(u"background-color: rgba(0,0,0,0);\n"
"border: 2px solid rgba(0,0,0,0);\n"
"border-bottom-color: rgba(46, 82, 101, 200);\n"
"color: rgb(0,0,0);\n"
"padding-bottom:7px;\n"
"")
        self.signin_password_input.setEchoMode(QLineEdit.Password)
        self.signin_btn = QPushButton(self.window)
        self.signin_btn.setObjectName(u"signin_btn")
        self.signin_btn.setGeometry(QRect(390, 270, 93, 28))
        font3 = QFont()
        font3.setFamily(u"Cascadia Code")
        font3.setPointSize(8)
        font3.setBold(True)
        font3.setWeight(75)
        self.signin_btn.setFont(font3)
        self.signin_btn.setStyleSheet(u"")
        self.wrong_pass_label = QLabel(self.window)
        self.wrong_pass_label.setObjectName(u"wrong_pass_label")
        self.wrong_pass_label.setGeometry(QRect(380, 230, 131, 16))
        font4 = QFont()
        font4.setFamily(u"Cascadia Mono SemiBold")
        self.wrong_pass_label.setFont(font4)
        self.wrong_pass_label.setStyleSheet(u"color: rgb(255, 0, 4);")
        self.wrong_pass_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.signin_exit_btn = QPushButton(self.window)
        self.signin_exit_btn.setObjectName(u"signin_exit_btn")
        self.signin_exit_btn.setGeometry(QRect(45, 30, 25, 25))
        font5 = QFont()
        font5.setFamily(u"Cascadia Code")
        font5.setPointSize(8)
        font5.setBold(False)
        font5.setWeight(50)
        self.signin_exit_btn.setFont(font5)
        self.signin_exit_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.signin_exit_btn.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"border-radius: 10px;\n"
"\n"
"QPushButton #exit_btn:hover{\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icon-EC8482/EC8482/x-octagon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.signin_exit_btn.setIcon(icon)
        self.hide_password_btn = QPushButton(self.window)
        self.hide_password_btn.setObjectName(u"hide_password_btn")
        self.hide_password_btn.setGeometry(QRect(517, 195, 25, 25))
        self.hide_password_btn.setFont(font3)
        self.hide_password_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.hide_password_btn.setLayoutDirection(Qt.LeftToRight)
        self.hide_password_btn.setAutoFillBackground(False)
        self.hide_password_btn.setStyleSheet(u"border-radius: 12px;\n"
"background-color: rgb(2, 123, 199);")
        icon1 = QIcon()
        icon1.addFile(u":/icons/EC8482/alert-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.hide_password_btn.setIcon(icon1)
        Login.setCentralWidget(self.login_window)

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"MainWindow", None))
        self.log_side.setText("")
        self.decor_side.setText("")
        self.sign_in_title.setText(QCoreApplication.translate("Login", u"\u0110\u0102NG NH\u1eacP", None))
        self.signin_username_input.setPlaceholderText(QCoreApplication.translate("Login", u"T\u00ean \u0111\u0103ng nh\u1eadp", None))
        self.signin_password_input.setPlaceholderText(QCoreApplication.translate("Login", u"M\u1eadt kh\u1ea9u", None))
        self.signin_btn.setText(QCoreApplication.translate("Login", u"\u0110\u0103ng nh\u1eadp", None))
        self.wrong_pass_label.setText(QCoreApplication.translate("Login", u"Sai m\u1eadt kh\u1ea9u!", None))
        self.signin_exit_btn.setText("")
        self.hide_password_btn.setText("")
    # retranslateUi

