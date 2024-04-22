# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'adminfNVRFc.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import resources.resources

class Ui_Admin(object):
    def setupUi(self, Admin):
        if not Admin.objectName():
            Admin.setObjectName(u"Admin")
        Admin.resize(1280, 720)
        font = QFont()
        font.setFamily(u"Cambria")
        Admin.setFont(font)
        Admin.setWindowTitle(u"Attendance")
        self.adminWidget = QWidget(Admin)
        self.adminWidget.setObjectName(u"adminWidget")
        self.adminWidget.setMaximumSize(QSize(16777215, 820))
        self.verticalLayout_16 = QVBoxLayout(self.adminWidget)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.panel_window = QWidget(self.adminWidget)
        self.panel_window.setObjectName(u"panel_window")
        self.panel_window.setMinimumSize(QSize(0, 40))
        self.panel_window.setMaximumSize(QSize(16777215, 40))
        self.panel_window.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"border-top-right-radius: 5px;\n"
"border-top-left-radius: 5px;")
        self.horizontalLayout_2 = QHBoxLayout(self.panel_window)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.icon_admin = QLabel(self.panel_window)
        self.icon_admin.setObjectName(u"icon_admin")
        self.icon_admin.setMinimumSize(QSize(30, 30))
        self.icon_admin.setMaximumSize(QSize(30, 30))
        self.icon_admin.setPixmap(QPixmap(u":/apps/apps/logo_app.png"))
        self.icon_admin.setScaledContents(True)
        self.icon_admin.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.icon_admin)

        self.name_admin = QLabel(self.panel_window)
        self.name_admin.setObjectName(u"name_admin")
        font1 = QFont()
        font1.setFamily(u"Cascadia Code")
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setWeight(75)
        self.name_admin.setFont(font1)
        self.name_admin.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.name_admin.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.name_admin)

        self.horizontalSpacer_2 = QSpacerItem(1017, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.admin_minimize_btn = QPushButton(self.panel_window)
        self.admin_minimize_btn.setObjectName(u"admin_minimize_btn")
        self.admin_minimize_btn.setMinimumSize(QSize(25, 25))
        self.admin_minimize_btn.setMaximumSize(QSize(25, 25))
        icon = QIcon()
        icon.addFile(u":/icon-EC8482/EC8482/minus-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.admin_minimize_btn.setIcon(icon)
        self.admin_minimize_btn.setIconSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.admin_minimize_btn)

        self.admin_expand_btn = QPushButton(self.panel_window)
        self.admin_expand_btn.setObjectName(u"admin_expand_btn")
        self.admin_expand_btn.setMinimumSize(QSize(25, 25))
        self.admin_expand_btn.setMaximumSize(QSize(25, 25))
        icon1 = QIcon()
        icon1.addFile(u":/icon-EC8482/EC8482/octagon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.admin_expand_btn.setIcon(icon1)
        self.admin_expand_btn.setIconSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.admin_expand_btn)

        self.admin_exit_btn = QPushButton(self.panel_window)
        self.admin_exit_btn.setObjectName(u"admin_exit_btn")
        self.admin_exit_btn.setMinimumSize(QSize(25, 25))
        self.admin_exit_btn.setMaximumSize(QSize(25, 25))
        icon2 = QIcon()
        icon2.addFile(u":/icon-EC8482/EC8482/x-octagon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.admin_exit_btn.setIcon(icon2)
        self.admin_exit_btn.setIconSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.admin_exit_btn)


        self.verticalLayout_16.addWidget(self.panel_window)

        self.container = QWidget(self.adminWidget)
        self.container.setObjectName(u"container")
        self.container.setLayoutDirection(Qt.LeftToRight)
        self.container.setAutoFillBackground(False)
        self.container.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.horizontalLayout = QHBoxLayout(self.container)
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(4, 4, 4, 4)
        self.menu = QWidget(self.container)
        self.menu.setObjectName(u"menu")
        self.menu.setMinimumSize(QSize(50, 0))
        self.menu.setMaximumSize(QSize(200, 16777215))
        self.menu.setStyleSheet(u"background-color:rgb(223,229,219);\n"
"border-radius: 9px;\n"
"")
        self.verticalLayout_11 = QVBoxLayout(self.menu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(1, 1, 1, 1)
        self.menu_btn = QPushButton(self.menu)
        self.menu_btn.setObjectName(u"menu_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menu_btn.sizePolicy().hasHeightForWidth())
        self.menu_btn.setSizePolicy(sizePolicy)
        self.menu_btn.setMinimumSize(QSize(0, 50))
        font2 = QFont()
        font2.setFamily(u"Cascadia Code")
        font2.setPointSize(12)
        self.menu_btn.setFont(font2)
        self.menu_btn.setLayoutDirection(Qt.LeftToRight)
        self.menu_btn.setStyleSheet(u"margin: 4px 4px 4px 4px;\n"
"background-color:rgb(188,203,234);\n"
"border-radius:9px;\n"
"border: 2px solid #000;\n"
"font-size: 12pt;\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/icon-dark/icon-dark/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_btn.setIcon(icon3)
        self.menu_btn.setIconSize(QSize(25, 25))
        self.menu_btn.setAutoRepeatDelay(300)
        self.menu_btn.setAutoRepeatInterval(100)

        self.verticalLayout_11.addWidget(self.menu_btn)

        self.verticalSpacer = QSpacerItem(20, 160, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_11.addItem(self.verticalSpacer)

        self.remote_controllers = QWidget(self.menu)
        self.remote_controllers.setObjectName(u"remote_controllers")
        self.remote_controllers.setMinimumSize(QSize(0, 300))
        self.verticalLayout = QVBoxLayout(self.remote_controllers)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.admins_btn = QPushButton(self.remote_controllers)
        self.admins_btn.setObjectName(u"admins_btn")
        self.admins_btn.setMinimumSize(QSize(0, 50))
        font3 = QFont()
        font3.setFamily(u"Cascadia Code")
        font3.setPointSize(10)
        self.admins_btn.setFont(font3)
        self.admins_btn.setStyleSheet(u"margin: 4px 4px 4px 4px;\n"
"background-color:rgb(188,203,234);\n"
"border-radius:9px;\n"
"border: 2px solid #000;\n"
"font-size: 10pt;\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/icon-dark/icon-dark/award.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.admins_btn.setIcon(icon4)
        self.admins_btn.setIconSize(QSize(25, 25))

        self.verticalLayout.addWidget(self.admins_btn)

        self.teachers_btn = QPushButton(self.remote_controllers)
        self.teachers_btn.setObjectName(u"teachers_btn")
        self.teachers_btn.setMinimumSize(QSize(0, 50))
        self.teachers_btn.setFont(font3)
        self.teachers_btn.setStyleSheet(u"margin: 4px 4px 4px 4px;\n"
"background-color:rgb(188,203,234);\n"
"border-radius:9px;\n"
"border: 2px solid #000;\n"
"font-size: 10pt;\n"
"")
        icon5 = QIcon()
        icon5.addFile(u":/icon-dark/icon-dark/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.teachers_btn.setIcon(icon5)
        self.teachers_btn.setIconSize(QSize(25, 25))

        self.verticalLayout.addWidget(self.teachers_btn)

        self.students_btn = QPushButton(self.remote_controllers)
        self.students_btn.setObjectName(u"students_btn")
        self.students_btn.setMinimumSize(QSize(0, 50))
        self.students_btn.setFont(font3)
        self.students_btn.setStyleSheet(u"margin: 4px 4px 4px 4px;\n"
"background-color:rgb(188,203,234);\n"
"border-radius:9px;\n"
"border: 2px solid #000;\n"
"font-size: 10pt;\n"
"")
        icon6 = QIcon()
        icon6.addFile(u":/icon-dark/icon-dark/users.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.students_btn.setIcon(icon6)
        self.students_btn.setIconSize(QSize(25, 25))

        self.verticalLayout.addWidget(self.students_btn)

        self.rooms_btn = QPushButton(self.remote_controllers)
        self.rooms_btn.setObjectName(u"rooms_btn")
        self.rooms_btn.setMinimumSize(QSize(0, 50))
        self.rooms_btn.setFont(font3)
        self.rooms_btn.setStyleSheet(u"margin: 4px 4px 4px 4px;\n"
"background-color:rgb(188,203,234);\n"
"border-radius:9px;\n"
"border: 2px solid #000;\n"
"font-size: 10pt;\n"
"")
        icon7 = QIcon()
        icon7.addFile(u":/icon-dark/icon-dark/folder.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.rooms_btn.setIcon(icon7)
        self.rooms_btn.setIconSize(QSize(25, 25))

        self.verticalLayout.addWidget(self.rooms_btn)

        self.reports_btn = QPushButton(self.remote_controllers)
        self.reports_btn.setObjectName(u"reports_btn")
        self.reports_btn.setMinimumSize(QSize(0, 50))
        self.reports_btn.setFont(font3)
        self.reports_btn.setStyleSheet(u"margin: 4px 4px 4px 4px;\n"
"background-color:rgb(188,203,234);\n"
"border-radius:9px;\n"
"border: 2px solid #000;\n"
"font-size: 10pt;\n"
"")
        icon8 = QIcon()
        icon8.addFile(u":/icon-dark/icon-dark/message-square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.reports_btn.setIcon(icon8)
        self.reports_btn.setIconSize(QSize(25, 25))

        self.verticalLayout.addWidget(self.reports_btn)

        self.reports_list_btn = QPushButton(self.remote_controllers)
        self.reports_list_btn.setObjectName(u"reports_list_btn")
        self.reports_list_btn.setMinimumSize(QSize(0, 50))
        self.reports_list_btn.setFont(font3)
        self.reports_list_btn.setStyleSheet(u"margin: 4px 4px 4px 4px;\n"
"background-color:rgb(188,203,234);\n"
"border-radius:9px;\n"
"border: 2px solid #000;\n"
"font-size: 10pt;\n"
"")
        icon9 = QIcon()
        icon9.addFile(u":/icon-dark/icon-dark/file-text.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.reports_list_btn.setIcon(icon9)
        self.reports_list_btn.setIconSize(QSize(25, 25))

        self.verticalLayout.addWidget(self.reports_list_btn)


        self.verticalLayout_11.addWidget(self.remote_controllers)

        self.verticalSpacer_2 = QSpacerItem(20, 200, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_2)

        self.logout_btn = QPushButton(self.menu)
        self.logout_btn.setObjectName(u"logout_btn")
        self.logout_btn.setMinimumSize(QSize(0, 50))
        self.logout_btn.setFont(font2)
        self.logout_btn.setStyleSheet(u"margin: 4px 4px 4px 4px;\n"
"background-color:rgb(188,203,234);\n"
"border-radius:9px;\n"
"border: 2px solid #000;\n"
"font-size: 12pt;\n"
"")
        icon10 = QIcon()
        icon10.addFile(u":/icon-dark/icon-dark/log-out.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.logout_btn.setIcon(icon10)
        self.logout_btn.setIconSize(QSize(25, 25))

        self.verticalLayout_11.addWidget(self.logout_btn)


        self.horizontalLayout.addWidget(self.menu)

        self.main = QWidget(self.container)
        self.main.setObjectName(u"main")
        self.main.setMaximumSize(QSize(16777215, 16777215))
        self.main.setStyleSheet(u"background-color:rgb(223,228,219);\n"
"border-radius: 9px;")
        self.verticalLayout_2 = QVBoxLayout(self.main)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.main_pages = QStackedWidget(self.main)
        self.main_pages.setObjectName(u"main_pages")
        self.admins_page = QWidget()
        self.admins_page.setObjectName(u"admins_page")
        self.verticalLayout_3 = QVBoxLayout(self.admins_page)
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(1, 1, 1, 1)
        self.admins_controllers = QWidget(self.admins_page)
        self.admins_controllers.setObjectName(u"admins_controllers")
        self.admins_controllers.setMaximumSize(QSize(16777215, 200))
        self.admins_controllers.setAutoFillBackground(False)
        self.verticalLayout_28 = QVBoxLayout(self.admins_controllers)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(-1, -1, -1, 0)
        self.admins_label = QLabel(self.admins_controllers)
        self.admins_label.setObjectName(u"admins_label")
        self.admins_label.setMinimumSize(QSize(0, 30))
        self.admins_label.setMaximumSize(QSize(16777215, 30))
        font4 = QFont()
        font4.setFamily(u"Cascadia Mono SemiBold")
        font4.setPointSize(15)
        font4.setBold(True)
        font4.setUnderline(False)
        font4.setWeight(75)
        font4.setStrikeOut(False)
        self.admins_label.setFont(font4)
        self.admins_label.setLayoutDirection(Qt.LeftToRight)
        self.admins_label.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"padding-left: 10px;\n"
"font-weight: bold;\n"
"font-size: 15pt;")
        self.admins_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_28.addWidget(self.admins_label)

        self.widget_16 = QWidget(self.admins_controllers)
        self.widget_16.setObjectName(u"widget_16")
        self.widget_16.setMinimumSize(QSize(0, 150))
        self.horizontalLayout_13 = QHBoxLayout(self.widget_16)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(-1, -1, -1, 0)
        self.widget_17 = QWidget(self.widget_16)
        self.widget_17.setObjectName(u"widget_17")
        self.verticalLayout_30 = QVBoxLayout(self.widget_17)
        self.verticalLayout_30.setSpacing(5)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(7, 7, 7, 7)
        self.admins_input = QLineEdit(self.widget_17)
        self.admins_input.setObjectName(u"admins_input")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.admins_input.sizePolicy().hasHeightForWidth())
        self.admins_input.setSizePolicy(sizePolicy1)
        self.admins_input.setMinimumSize(QSize(300, 30))
        self.admins_input.setFont(font3)
        self.admins_input.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 7px;\n"
"border: 2px solid #000;")

        self.verticalLayout_30.addWidget(self.admins_input)

        self.verticalSpacer_10 = QSpacerItem(20, 46, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_30.addItem(self.verticalSpacer_10)


        self.horizontalLayout_13.addWidget(self.widget_17)

        self.widget_18 = QWidget(self.widget_16)
        self.widget_18.setObjectName(u"widget_18")
        self.widget_18.setMinimumSize(QSize(150, 0))
        self.verticalLayout_31 = QVBoxLayout(self.widget_18)
        self.verticalLayout_31.setSpacing(5)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(7, 7, 7, 7)
        self.admins_search_btn = QPushButton(self.widget_18)
        self.admins_search_btn.setObjectName(u"admins_search_btn")
        self.admins_search_btn.setMinimumSize(QSize(150, 30))
        self.admins_search_btn.setMaximumSize(QSize(10, 30))
        font5 = QFont()
        font5.setFamily(u"Cascadia Code")
        font5.setPointSize(12)
        font5.setBold(True)
        font5.setWeight(75)
        self.admins_search_btn.setFont(font5)
        self.admins_search_btn.setStyleSheet(u"background-color: rgb(190,207,187);\n"
"color: rgb(0,0,0);\n"
"border-radius: 5px;\n"
"border: 2px solid #000;\n"
"font-weight: bold;\n"
"font-size: 12pt;")
        self.admins_search_btn.setIconSize(QSize(25, 25))

        self.verticalLayout_31.addWidget(self.admins_search_btn)

        self.admins_add_btn = QPushButton(self.widget_18)
        self.admins_add_btn.setObjectName(u"admins_add_btn")
        self.admins_add_btn.setMinimumSize(QSize(150, 30))
        self.admins_add_btn.setMaximumSize(QSize(150, 30))
        self.admins_add_btn.setFont(font5)
        self.admins_add_btn.setStyleSheet(u"background-color: rgb(190,207,187);\n"
"color: rgb(0,0,0);\n"
"border-radius: 5px;\n"
"border: 2px solid #000;\n"
"font-weight: bold;\n"
"font-size: 12pt;")
        icon11 = QIcon()
        icon11.addFile(u":/icons/zap.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.admins_add_btn.setIcon(icon11)
        self.admins_add_btn.setIconSize(QSize(25, 25))

        self.verticalLayout_31.addWidget(self.admins_add_btn)

        self.admins_edit_btn = QPushButton(self.widget_18)
        self.admins_edit_btn.setObjectName(u"admins_edit_btn")
        self.admins_edit_btn.setMinimumSize(QSize(150, 30))
        self.admins_edit_btn.setMaximumSize(QSize(150, 30))
        self.admins_edit_btn.setFont(font5)
        self.admins_edit_btn.setStyleSheet(u"background-color: rgb(190,207,187);\n"
"color: rgb(0,0,0);\n"
"border-radius: 5px;\n"
"border: 2px solid #000;\n"
"font-weight: bold;\n"
"font-size: 12pt;")
        self.admins_edit_btn.setIcon(icon11)
        self.admins_edit_btn.setIconSize(QSize(25, 25))

        self.verticalLayout_31.addWidget(self.admins_edit_btn)

        self.admins_del_btn = QPushButton(self.widget_18)
        self.admins_del_btn.setObjectName(u"admins_del_btn")
        self.admins_del_btn.setMinimumSize(QSize(150, 30))
        self.admins_del_btn.setMaximumSize(QSize(150, 30))
        self.admins_del_btn.setFont(font5)
        self.admins_del_btn.setStyleSheet(u"background-color: rgb(190,207,187);\n"
"color: rgb(0,0,0);\n"
"border-radius: 5px;\n"
"border: 2px solid #000;\n"
"font-weight: bold;\n"
"font-size: 12pt;")
        self.admins_del_btn.setIcon(icon11)
        self.admins_del_btn.setIconSize(QSize(25, 25))

        self.verticalLayout_31.addWidget(self.admins_del_btn)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_31.addItem(self.verticalSpacer_11)


        self.horizontalLayout_13.addWidget(self.widget_18)


        self.verticalLayout_28.addWidget(self.widget_16)


        self.verticalLayout_3.addWidget(self.admins_controllers)

        self.admins_view = QWidget(self.admins_page)
        self.admins_view.setObjectName(u"admins_view")
        font6 = QFont()
        font6.setFamily(u"Cascadia Code")
        self.admins_view.setFont(font6)
        self.admins_view.setStyleSheet(u"border-radius: 5px;\n"
"background-color:rgb(54, 71, 107); \n"
"border-radius: 5px;\n"
"border: 2px solid #000;\n"
"")
        self.verticalLayout_32 = QVBoxLayout(self.admins_view)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(11, 11, 11, 11)
        self.admins_table = QTableWidget(self.admins_view)
        self.admins_table.setObjectName(u"admins_table")
        self.admins_table.setFont(font6)
        self.admins_table.setStyleSheet(u"border-radius: 5px;\n"
"border: 0px;\n"
"background-color: rgb(255, 255, 255);")
        self.admins_table.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.admins_table.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)

        self.verticalLayout_32.addWidget(self.admins_table)


        self.verticalLayout_3.addWidget(self.admins_view)

        self.main_pages.addWidget(self.admins_page)
        self.teachers_page = QWidget()
        self.teachers_page.setObjectName(u"teachers_page")
        self.verticalLayout_4 = QVBoxLayout(self.teachers_page)
        self.verticalLayout_4.setSpacing(3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(1, 1, 1, 1)
        self.teachers_controllers = QWidget(self.teachers_page)
        self.teachers_controllers.setObjectName(u"teachers_controllers")
        self.teachers_controllers.setMaximumSize(QSize(16777215, 200))
        self.teachers_controllers.setAutoFillBackground(False)
        self.verticalLayout_33 = QVBoxLayout(self.teachers_controllers)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(-1, -1, -1, 0)
        self.teachers_name_label = QLabel(self.teachers_controllers)
        self.teachers_name_label.setObjectName(u"teachers_name_label")
        self.teachers_name_label.setMinimumSize(QSize(0, 30))
        self.teachers_name_label.setMaximumSize(QSize(16777215, 30))
        self.teachers_name_label.setFont(font4)
        self.teachers_name_label.setLayoutDirection(Qt.LeftToRight)
        self.teachers_name_label.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"padding-left: 10px;\n"
"font-weight: bold;\n"
"font-size: 15pt;")
        self.teachers_name_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_33.addWidget(self.teachers_name_label)

        self.widget_19 = QWidget(self.teachers_controllers)
        self.widget_19.setObjectName(u"widget_19")
        self.widget_19.setMinimumSize(QSize(0, 150))
        self.horizontalLayout_14 = QHBoxLayout(self.widget_19)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(-1, -1, -1, 0)
        self.widget_20 = QWidget(self.widget_19)
        self.widget_20.setObjectName(u"widget_20")
        self.verticalLayout_34 = QVBoxLayout(self.widget_20)
        self.verticalLayout_34.setSpacing(5)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(7, 7, 7, 7)
        self.teachers_input = QLineEdit(self.widget_20)
        self.teachers_input.setObjectName(u"teachers_input")
        sizePolicy1.setHeightForWidth(self.teachers_input.sizePolicy().hasHeightForWidth())
        self.teachers_input.setSizePolicy(sizePolicy1)
        self.teachers_input.setMinimumSize(QSize(300, 30))
        self.teachers_input.setFont(font3)
        self.teachers_input.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 7px;\n"
"border: 2px solid #000;")

        self.verticalLayout_34.addWidget(self.teachers_input)

        self.verticalSpacer_12 = QSpacerItem(20, 46, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_34.addItem(self.verticalSpacer_12)


        self.horizontalLayout_14.addWidget(self.widget_20)

        self.widget_21 = QWidget(self.widget_19)
        self.widget_21.setObjectName(u"widget_21")
        self.widget_21.setMinimumSize(QSize(150, 0))
        self.verticalLayout_35 = QVBoxLayout(self.widget_21)
        self.verticalLayout_35.setSpacing(5)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(7, 7, 7, 7)
        self.teachers_search_btn = QPushButton(self.widget_21)
        self.teachers_search_btn.setObjectName(u"teachers_search_btn")
        self.teachers_search_btn.setMinimumSize(QSize(150, 30))
        self.teachers_search_btn.setMaximumSize(QSize(10, 30))
        self.teachers_search_btn.setFont(font5)
        self.teachers_search_btn.setStyleSheet(u"background-color: rgb(190,207,187);\n"
"color: rgb(0,0,0);\n"
"border-radius: 5px;\n"
"border: 2px solid #000;\n"
"font-weight: bold;\n"
"font-size: 12pt;")
        self.teachers_search_btn.setIconSize(QSize(25, 25))

        self.verticalLayout_35.addWidget(self.teachers_search_btn)

        self.teachers_add_btn = QPushButton(self.widget_21)
        self.teachers_add_btn.setObjectName(u"teachers_add_btn")
        self.teachers_add_btn.setMinimumSize(QSize(150, 30))
        self.teachers_add_btn.setMaximumSize(QSize(150, 30))
        self.teachers_add_btn.setFont(font5)
        self.teachers_add_btn.setStyleSheet(u"background-color: rgb(190,207,187);\n"
"color: rgb(0,0,0);\n"
"border-radius: 5px;\n"
"border: 2px solid #000;\n"
"font-weight: bold;\n"
"font-size: 12pt;")
        self.teachers_add_btn.setIcon(icon11)
        self.teachers_add_btn.setIconSize(QSize(25, 25))

        self.verticalLayout_35.addWidget(self.teachers_add_btn)

        self.teachers_edit_btn = QPushButton(self.widget_21)
        self.teachers_edit_btn.setObjectName(u"teachers_edit_btn")
        self.teachers_edit_btn.setMinimumSize(QSize(150, 30))
        self.teachers_edit_btn.setMaximumSize(QSize(150, 30))
        self.teachers_edit_btn.setFont(font5)
        self.teachers_edit_btn.setStyleSheet(u"background-color: rgb(190,207,187);\n"
"color: rgb(0,0,0);\n"
"border-radius: 5px;\n"
"border: 2px solid #000;\n"
"font-weight: bold;\n"
"font-size: 12pt;")
        self.teachers_edit_btn.setIcon(icon11)
        self.teachers_edit_btn.setIconSize(QSize(25, 25))

        self.verticalLayout_35.addWidget(self.teachers_edit_btn)

        self.teachers_del_btn = QPushButton(self.widget_21)
        self.teachers_del_btn.setObjectName(u"teachers_del_btn")
        self.teachers_del_btn.setMinimumSize(QSize(150, 30))
        self.teachers_del_btn.setMaximumSize(QSize(150, 30))
        self.teachers_del_btn.setFont(font5)
        self.teachers_del_btn.setStyleSheet(u"background-color: rgb(190,207,187);\n"
"color: rgb(0,0,0);\n"
"border-radius: 5px;\n"
"border: 2px solid #000;\n"
"font-weight: bold;\n"
"font-size: 12pt;")
        self.teachers_del_btn.setIcon(icon11)
        self.teachers_del_btn.setIconSize(QSize(25, 25))

        self.verticalLayout_35.addWidget(self.teachers_del_btn)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_35.addItem(self.verticalSpacer_13)


        self.horizontalLayout_14.addWidget(self.widget_21)


        self.verticalLayout_33.addWidget(self.widget_19)


        self.verticalLayout_4.addWidget(self.teachers_controllers)

        self.teachers_view = QWidget(self.teachers_page)
        self.teachers_view.setObjectName(u"teachers_view")
        self.teachers_view.setFont(font6)
        self.teachers_view.setStyleSheet(u"border-radius: 5px;\n"
"background-color:rgb(54, 71, 107); \n"
"border-radius: 5px;\n"
"border: 2px solid #000;\n"
"")
        self.verticalLayout_36 = QVBoxLayout(self.teachers_view)
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(11, 11, 11, 11)
        self.teachers_table = QTableWidget(self.teachers_view)
        self.teachers_table.setObjectName(u"teachers_table")
        self.teachers_table.setFont(font6)
        self.teachers_table.setStyleSheet(u"border-radius: 5px;\n"
"border: 0px;\n"
"background-color: rgb(255, 255, 255);")
        self.teachers_table.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.teachers_table.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)

        self.verticalLayout_36.addWidget(self.teachers_table)


        self.verticalLayout_4.addWidget(self.teachers_view)

        self.main_pages.addWidget(self.teachers_page)
        self.students_page = QWidget()
        self.students_page.setObjectName(u"students_page")
        self.verticalLayout_5 = QVBoxLayout(self.students_page)
        self.verticalLayout_5.setSpacing(3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(1, 1, 1, 1)
        self.students_controllers = QWidget(self.students_page)
        self.students_controllers.setObjectName(u"students_controllers")
        self.students_controllers.setMaximumSize(QSize(16777215, 200))
        self.students_controllers.setAutoFillBackground(False)
        self.verticalLayout_37 = QVBoxLayout(self.students_controllers)
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(-1, -1, -1, 0)
        self.students_name_label = QLabel(self.students_controllers)
        self.students_name_label.setObjectName(u"students_name_label")
        self.students_name_label.setMinimumSize(QSize(0, 30))
        self.students_name_label.setMaximumSize(QSize(16777215, 30))
        self.students_name_label.setFont(font4)
        self.students_name_label.setLayoutDirection(Qt.LeftToRight)
        self.students_name_label.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"padding-left: 10px;\n"
"font-weight: bold;\n"
"font-size: 15pt;")
        self.students_name_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_37.addWidget(self.students_name_label)

        self.widget_22 = QWidget(self.students_controllers)
        self.widget_22.setObjectName(u"widget_22")
        self.widget_22.setMinimumSize(QSize(0, 150))
        self.horizontalLayout_15 = QHBoxLayout(self.widget_22)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(-1, -1, -1, 0)
        self.widget_23 = QWidget(self.widget_22)
        self.widget_23.setObjectName(u"widget_23")
        self.verticalLayout_38 = QVBoxLayout(self.widget_23)
        self.verticalLayout_38.setSpacing(5)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(7, 7, 7, 7)
        self.students_input = QLineEdit(self.widget_23)
        self.students_input.setObjectName(u"students_input")
        sizePolicy1.setHeightForWidth(self.students_input.sizePolicy().hasHeightForWidth())
        self.students_input.setSizePolicy(sizePolicy1)
        self.students_input.setMinimumSize(QSize(300, 30))
        self.students_input.setFont(font3)
        self.students_input.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 7px;\n"
"border: 2px solid #000;")

        self.verticalLayout_38.addWidget(self.students_input)

        self.verticalSpacer_14 = QSpacerItem(20, 46, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_38.addItem(self.verticalSpacer_14)


        self.horizontalLayout_15.addWidget(self.widget_23)

        self.widget_24 = QWidget(self.widget_22)
        self.widget_24.setObjectName(u"widget_24")
        self.widget_24.setMinimumSize(QSize(150, 0))
        self.verticalLayout_39 = QVBoxLayout(self.widget_24)
        self.verticalLayout_39.setSpacing(5)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(7, 7, 7, 7)
        self.students_search_btn = QPushButton(self.widget_24)
        self.students_search_btn.setObjectName(u"students_search_btn")
        self.students_search_btn.setMinimumSize(QSize(150, 30))
        self.students_search_btn.setMaximumSize(QSize(10, 30))
        self.students_search_btn.setFont(font5)
        self.students_search_btn.setStyleSheet(u"background-color: rgb(190,207,187);\n"
"color: rgb(0,0,0);\n"
"border-radius: 5px;\n"
"border: 2px solid #000;\n"
"font-weight: bold;\n"
"font-size: 12pt;")
        self.students_search_btn.setIconSize(QSize(25, 25))

        self.verticalLayout_39.addWidget(self.students_search_btn)

        self.students_add_btn = QPushButton(self.widget_24)
        self.students_add_btn.setObjectName(u"students_add_btn")
        self.students_add_btn.setMinimumSize(QSize(150, 30))
        self.students_add_btn.setMaximumSize(QSize(150, 30))
        self.students_add_btn.setFont(font5)
        self.students_add_btn.setStyleSheet(u"background-color: rgb(190,207,187);\n"
"color: rgb(0,0,0);\n"
"border-radius: 5px;\n"
"border: 2px solid #000;\n"
"font-weight: bold;\n"
"font-size: 12pt;")
        self.students_add_btn.setIcon(icon11)
        self.students_add_btn.setIconSize(QSize(25, 25))

        self.verticalLayout_39.addWidget(self.students_add_btn)

        self.students_edit_btn = QPushButton(self.widget_24)
        self.students_edit_btn.setObjectName(u"students_edit_btn")
        self.students_edit_btn.setMinimumSize(QSize(150, 30))
        self.students_edit_btn.setMaximumSize(QSize(150, 30))
        self.students_edit_btn.setFont(font5)
        self.students_edit_btn.setStyleSheet(u"background-color: rgb(190,207,187);\n"
"color: rgb(0,0,0);\n"
"border-radius: 5px;\n"
"border: 2px solid #000;\n"
"font-weight: bold;\n"
"font-size: 12pt;")
        self.students_edit_btn.setIcon(icon11)
        self.students_edit_btn.setIconSize(QSize(25, 25))

        self.verticalLayout_39.addWidget(self.students_edit_btn)

        self.students_del_btn = QPushButton(self.widget_24)
        self.students_del_btn.setObjectName(u"students_del_btn")
        self.students_del_btn.setMinimumSize(QSize(150, 30))
        self.students_del_btn.setMaximumSize(QSize(150, 30))
        self.students_del_btn.setFont(font5)
        self.students_del_btn.setStyleSheet(u"background-color: rgb(190,207,187);\n"
"color: rgb(0,0,0);\n"
"border-radius: 5px;\n"
"border: 2px solid #000;\n"
"font-weight: bold;\n"
"font-size: 12pt;")
        self.students_del_btn.setIcon(icon11)
        self.students_del_btn.setIconSize(QSize(25, 25))

        self.verticalLayout_39.addWidget(self.students_del_btn)

        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_39.addItem(self.verticalSpacer_15)


        self.horizontalLayout_15.addWidget(self.widget_24)


        self.verticalLayout_37.addWidget(self.widget_22)


        self.verticalLayout_5.addWidget(self.students_controllers)

        self.students_view = QWidget(self.students_page)
        self.students_view.setObjectName(u"students_view")
        self.students_view.setFont(font6)
        self.students_view.setStyleSheet(u"border-radius: 5px;\n"
"background-color:rgb(54, 71, 107); \n"
"border-radius: 5px;\n"
"border: 2px solid #000;\n"
"")
        self.verticalLayout_40 = QVBoxLayout(self.students_view)
        self.verticalLayout_40.setSpacing(0)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(11, 11, 11, 11)
        self.students_table = QTableWidget(self.students_view)
        self.students_table.setObjectName(u"students_table")
        self.students_table.setFont(font6)
        self.students_table.setStyleSheet(u"border-radius: 5px;\n"
"border: 0px;\n"
"background-color: rgb(255, 255, 255);")
        self.students_table.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.students_table.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)

        self.verticalLayout_40.addWidget(self.students_table)


        self.verticalLayout_5.addWidget(self.students_view)

        self.main_pages.addWidget(self.students_page)
        self.rooms_page = QWidget()
        self.rooms_page.setObjectName(u"rooms_page")
        self.verticalLayout_6 = QVBoxLayout(self.rooms_page)
        self.verticalLayout_6.setSpacing(3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(1, 1, 1, 1)
        self.reports_list_controllers_5 = QWidget(self.rooms_page)
        self.reports_list_controllers_5.setObjectName(u"reports_list_controllers_5")
        self.reports_list_controllers_5.setMaximumSize(QSize(16777215, 200))
        self.reports_list_controllers_5.setAutoFillBackground(False)
        self.verticalLayout_41 = QVBoxLayout(self.reports_list_controllers_5)
        self.verticalLayout_41.setSpacing(0)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(-1, -1, -1, 0)
        self.reports_list_name_label_5 = QLabel(self.reports_list_controllers_5)
        self.reports_list_name_label_5.setObjectName(u"reports_list_name_label_5")
        self.reports_list_name_label_5.setMinimumSize(QSize(0, 30))
        self.reports_list_name_label_5.setMaximumSize(QSize(16777215, 30))
        self.reports_list_name_label_5.setFont(font4)
        self.reports_list_name_label_5.setLayoutDirection(Qt.LeftToRight)
        self.reports_list_name_label_5.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"padding-left: 10px;\n"
"font-weight: bold;\n"
"font-size: 15pt;")
        self.reports_list_name_label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_41.addWidget(self.reports_list_name_label_5)

        self.widget_25 = QWidget(self.reports_list_controllers_5)
        self.widget_25.setObjectName(u"widget_25")
        self.widget_25.setMinimumSize(QSize(0, 150))
        self.horizontalLayout_16 = QHBoxLayout(self.widget_25)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(-1, -1, -1, 0)
        self.widget_26 = QWidget(self.widget_25)
        self.widget_26.setObjectName(u"widget_26")
        self.verticalLayout_42 = QVBoxLayout(self.widget_26)
        self.verticalLayout_42.setSpacing(5)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(7, 7, 7, 7)
        self.reports_list_input_5 = QLineEdit(self.widget_26)
        self.reports_list_input_5.setObjectName(u"reports_list_input_5")
        sizePolicy1.setHeightForWidth(self.reports_list_input_5.sizePolicy().hasHeightForWidth())
        self.reports_list_input_5.setSizePolicy(sizePolicy1)
        self.reports_list_input_5.setMinimumSize(QSize(300, 30))
        self.reports_list_input_5.setFont(font3)
        self.reports_list_input_5.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 7px;\n"
"border: 2px solid #000;")

        self.verticalLayout_42.addWidget(self.reports_list_input_5)

        self.verticalSpacer_16 = QSpacerItem(20, 46, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_42.addItem(self.verticalSpacer_16)


        self.horizontalLayout_16.addWidget(self.widget_26)

        self.widget_27 = QWidget(self.widget_25)
        self.widget_27.setObjectName(u"widget_27")
        self.widget_27.setMinimumSize(QSize(150, 0))
        self.verticalLayout_43 = QVBoxLayout(self.widget_27)
        self.verticalLayout_43.setSpacing(5)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(7, 7, 7, 7)
        self.reports_list_search_btn_5 = QPushButton(self.widget_27)
        self.reports_list_search_btn_5.setObjectName(u"reports_list_search_btn_5")
        self.reports_list_search_btn_5.setMinimumSize(QSize(150, 30))
        self.reports_list_search_btn_5.setMaximumSize(QSize(10, 30))
        self.reports_list_search_btn_5.setFont(font5)
        self.reports_list_search_btn_5.setStyleSheet(u"background-color: rgb(190,207,187);\n"
"color: rgb(0,0,0);\n"
"border-radius: 5px;\n"
"border: 2px solid #000;\n"
"font-weight: bold;\n"
"font-size: 12pt;")
        self.reports_list_search_btn_5.setIconSize(QSize(25, 25))

        self.verticalLayout_43.addWidget(self.reports_list_search_btn_5)

        self.reports_list_add_btn_5 = QPushButton(self.widget_27)
        self.reports_list_add_btn_5.setObjectName(u"reports_list_add_btn_5")
        self.reports_list_add_btn_5.setMinimumSize(QSize(150, 30))
        self.reports_list_add_btn_5.setMaximumSize(QSize(150, 30))
        self.reports_list_add_btn_5.setFont(font5)
        self.reports_list_add_btn_5.setStyleSheet(u"background-color: rgb(190,207,187);\n"
"color: rgb(0,0,0);\n"
"border-radius: 5px;\n"
"border: 2px solid #000;\n"
"font-weight: bold;\n"
"font-size: 12pt;")
        self.reports_list_add_btn_5.setIcon(icon11)
        self.reports_list_add_btn_5.setIconSize(QSize(25, 25))

        self.verticalLayout_43.addWidget(self.reports_list_add_btn_5)

        self.reports_list_edit_btn_5 = QPushButton(self.widget_27)
        self.reports_list_edit_btn_5.setObjectName(u"reports_list_edit_btn_5")
        self.reports_list_edit_btn_5.setMinimumSize(QSize(150, 30))
        self.reports_list_edit_btn_5.setMaximumSize(QSize(150, 30))
        self.reports_list_edit_btn_5.setFont(font5)
        self.reports_list_edit_btn_5.setStyleSheet(u"background-color: rgb(190,207,187);\n"
"color: rgb(0,0,0);\n"
"border-radius: 5px;\n"
"border: 2px solid #000;\n"
"font-weight: bold;\n"
"font-size: 12pt;")
        self.reports_list_edit_btn_5.setIcon(icon11)
        self.reports_list_edit_btn_5.setIconSize(QSize(25, 25))

        self.verticalLayout_43.addWidget(self.reports_list_edit_btn_5)

        self.reports_list_del_btn_5 = QPushButton(self.widget_27)
        self.reports_list_del_btn_5.setObjectName(u"reports_list_del_btn_5")
        self.reports_list_del_btn_5.setMinimumSize(QSize(150, 30))
        self.reports_list_del_btn_5.setMaximumSize(QSize(150, 30))
        self.reports_list_del_btn_5.setFont(font5)
        self.reports_list_del_btn_5.setStyleSheet(u"background-color: rgb(190,207,187);\n"
"color: rgb(0,0,0);\n"
"border-radius: 5px;\n"
"border: 2px solid #000;\n"
"font-weight: bold;\n"
"font-size: 12pt;")
        self.reports_list_del_btn_5.setIcon(icon11)
        self.reports_list_del_btn_5.setIconSize(QSize(25, 25))

        self.verticalLayout_43.addWidget(self.reports_list_del_btn_5)

        self.verticalSpacer_17 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_43.addItem(self.verticalSpacer_17)


        self.horizontalLayout_16.addWidget(self.widget_27)


        self.verticalLayout_41.addWidget(self.widget_25)


        self.verticalLayout_6.addWidget(self.reports_list_controllers_5)

        self.reports_list_view_5 = QWidget(self.rooms_page)
        self.reports_list_view_5.setObjectName(u"reports_list_view_5")
        self.reports_list_view_5.setFont(font6)
        self.reports_list_view_5.setStyleSheet(u"border-radius: 5px;\n"
"background-color:rgb(54, 71, 107); \n"
"border-radius: 5px;\n"
"border: 2px solid #000;\n"
"")
        self.verticalLayout_44 = QVBoxLayout(self.reports_list_view_5)
        self.verticalLayout_44.setSpacing(0)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(11, 11, 11, 11)
        self.reports_list_table_5 = QTableWidget(self.reports_list_view_5)
        self.reports_list_table_5.setObjectName(u"reports_list_table_5")
        self.reports_list_table_5.setFont(font6)
        self.reports_list_table_5.setStyleSheet(u"border-radius: 5px;\n"
"border: 0px;\n"
"background-color: rgb(255, 255, 255);")
        self.reports_list_table_5.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.reports_list_table_5.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)

        self.verticalLayout_44.addWidget(self.reports_list_table_5)


        self.verticalLayout_6.addWidget(self.reports_list_view_5)

        self.main_pages.addWidget(self.rooms_page)
        self.reports_page = QWidget()
        self.reports_page.setObjectName(u"reports_page")
        self.verticalLayout_7 = QVBoxLayout(self.reports_page)
        self.verticalLayout_7.setSpacing(3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(1, 1, 1, 1)
        self.reports_list_controllers_6 = QWidget(self.reports_page)
        self.reports_list_controllers_6.setObjectName(u"reports_list_controllers_6")
        self.reports_list_controllers_6.setMaximumSize(QSize(16777215, 200))
        self.reports_list_controllers_6.setAutoFillBackground(False)
        self.verticalLayout_45 = QVBoxLayout(self.reports_list_controllers_6)
        self.verticalLayout_45.setSpacing(0)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(-1, -1, -1, 0)
        self.reports_list_name_label_6 = QLabel(self.reports_list_controllers_6)
        self.reports_list_name_label_6.setObjectName(u"reports_list_name_label_6")
        self.reports_list_name_label_6.setMinimumSize(QSize(0, 30))
        self.reports_list_name_label_6.setMaximumSize(QSize(16777215, 30))
        self.reports_list_name_label_6.setFont(font4)
        self.reports_list_name_label_6.setLayoutDirection(Qt.LeftToRight)
        self.reports_list_name_label_6.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"padding-left: 10px;\n"
"font-weight: bold;\n"
"font-size: 15pt;")
        self.reports_list_name_label_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_45.addWidget(self.reports_list_name_label_6)

        self.widget_28 = QWidget(self.reports_list_controllers_6)
        self.widget_28.setObjectName(u"widget_28")
        self.widget_28.setMinimumSize(QSize(0, 150))
        self.horizontalLayout_17 = QHBoxLayout(self.widget_28)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(-1, -1, -1, 0)
        self.widget_29 = QWidget(self.widget_28)
        self.widget_29.setObjectName(u"widget_29")
        self.verticalLayout_46 = QVBoxLayout(self.widget_29)
        self.verticalLayout_46.setSpacing(5)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(7, 7, 7, 7)
        self.reports_list_input_6 = QLineEdit(self.widget_29)
        self.reports_list_input_6.setObjectName(u"reports_list_input_6")
        sizePolicy1.setHeightForWidth(self.reports_list_input_6.sizePolicy().hasHeightForWidth())
        self.reports_list_input_6.setSizePolicy(sizePolicy1)
        self.reports_list_input_6.setMinimumSize(QSize(300, 30))
        self.reports_list_input_6.setFont(font3)
        self.reports_list_input_6.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 7px;\n"
"border: 2px solid #000;")

        self.verticalLayout_46.addWidget(self.reports_list_input_6)

        self.verticalSpacer_18 = QSpacerItem(20, 46, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_46.addItem(self.verticalSpacer_18)


        self.horizontalLayout_17.addWidget(self.widget_29)

        self.widget_30 = QWidget(self.widget_28)
        self.widget_30.setObjectName(u"widget_30")
        self.widget_30.setMinimumSize(QSize(150, 0))
        self.verticalLayout_47 = QVBoxLayout(self.widget_30)
        self.verticalLayout_47.setSpacing(5)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(7, 7, 7, 7)
        self.reports_list_search_btn_6 = QPushButton(self.widget_30)
        self.reports_list_search_btn_6.setObjectName(u"reports_list_search_btn_6")
        self.reports_list_search_btn_6.setMinimumSize(QSize(150, 30))
        self.reports_list_search_btn_6.setMaximumSize(QSize(10, 30))
        self.reports_list_search_btn_6.setFont(font5)
        self.reports_list_search_btn_6.setStyleSheet(u"background-color: rgb(190,207,187);\n"
"color: rgb(0,0,0);\n"
"border-radius: 5px;\n"
"border: 2px solid #000;\n"
"font-weight: bold;\n"
"font-size: 12pt;")
        self.reports_list_search_btn_6.setIconSize(QSize(25, 25))

        self.verticalLayout_47.addWidget(self.reports_list_search_btn_6)

        self.reports_list_add_btn_6 = QPushButton(self.widget_30)
        self.reports_list_add_btn_6.setObjectName(u"reports_list_add_btn_6")
        self.reports_list_add_btn_6.setMinimumSize(QSize(150, 30))
        self.reports_list_add_btn_6.setMaximumSize(QSize(150, 30))
        self.reports_list_add_btn_6.setFont(font5)
        self.reports_list_add_btn_6.setStyleSheet(u"background-color: rgb(190,207,187);\n"
"color: rgb(0,0,0);\n"
"border-radius: 5px;\n"
"border: 2px solid #000;\n"
"font-weight: bold;\n"
"font-size: 12pt;")
        self.reports_list_add_btn_6.setIcon(icon11)
        self.reports_list_add_btn_6.setIconSize(QSize(25, 25))

        self.verticalLayout_47.addWidget(self.reports_list_add_btn_6)

        self.reports_list_edit_btn_6 = QPushButton(self.widget_30)
        self.reports_list_edit_btn_6.setObjectName(u"reports_list_edit_btn_6")
        self.reports_list_edit_btn_6.setMinimumSize(QSize(150, 30))
        self.reports_list_edit_btn_6.setMaximumSize(QSize(150, 30))
        self.reports_list_edit_btn_6.setFont(font5)
        self.reports_list_edit_btn_6.setStyleSheet(u"background-color: rgb(190,207,187);\n"
"color: rgb(0,0,0);\n"
"border-radius: 5px;\n"
"border: 2px solid #000;\n"
"font-weight: bold;\n"
"font-size: 12pt;")
        self.reports_list_edit_btn_6.setIcon(icon11)
        self.reports_list_edit_btn_6.setIconSize(QSize(25, 25))

        self.verticalLayout_47.addWidget(self.reports_list_edit_btn_6)

        self.reports_list_del_btn_6 = QPushButton(self.widget_30)
        self.reports_list_del_btn_6.setObjectName(u"reports_list_del_btn_6")
        self.reports_list_del_btn_6.setMinimumSize(QSize(150, 30))
        self.reports_list_del_btn_6.setMaximumSize(QSize(150, 30))
        self.reports_list_del_btn_6.setFont(font5)
        self.reports_list_del_btn_6.setStyleSheet(u"background-color: rgb(190,207,187);\n"
"color: rgb(0,0,0);\n"
"border-radius: 5px;\n"
"border: 2px solid #000;\n"
"font-weight: bold;\n"
"font-size: 12pt;")
        self.reports_list_del_btn_6.setIcon(icon11)
        self.reports_list_del_btn_6.setIconSize(QSize(25, 25))

        self.verticalLayout_47.addWidget(self.reports_list_del_btn_6)

        self.verticalSpacer_19 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_47.addItem(self.verticalSpacer_19)


        self.horizontalLayout_17.addWidget(self.widget_30)


        self.verticalLayout_45.addWidget(self.widget_28)


        self.verticalLayout_7.addWidget(self.reports_list_controllers_6)

        self.reports_list_view_6 = QWidget(self.reports_page)
        self.reports_list_view_6.setObjectName(u"reports_list_view_6")
        self.reports_list_view_6.setFont(font6)
        self.reports_list_view_6.setStyleSheet(u"border-radius: 5px;\n"
"background-color:rgb(54, 71, 107); \n"
"border-radius: 5px;\n"
"border: 2px solid #000;\n"
"")
        self.verticalLayout_48 = QVBoxLayout(self.reports_list_view_6)
        self.verticalLayout_48.setSpacing(0)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(11, 11, 11, 11)
        self.reports_list_table_6 = QTableWidget(self.reports_list_view_6)
        self.reports_list_table_6.setObjectName(u"reports_list_table_6")
        self.reports_list_table_6.setFont(font6)
        self.reports_list_table_6.setStyleSheet(u"border-radius: 5px;\n"
"border: 0px;\n"
"background-color: rgb(255, 255, 255);")
        self.reports_list_table_6.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.reports_list_table_6.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)

        self.verticalLayout_48.addWidget(self.reports_list_table_6)


        self.verticalLayout_7.addWidget(self.reports_list_view_6)

        self.main_pages.addWidget(self.reports_page)
        self.reports_list_page = QWidget()
        self.reports_list_page.setObjectName(u"reports_list_page")
        self.verticalLayout_29 = QVBoxLayout(self.reports_list_page)
        self.verticalLayout_29.setSpacing(3)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(1, 1, 1, 1)
        self.reports_list_controllers = QWidget(self.reports_list_page)
        self.reports_list_controllers.setObjectName(u"reports_list_controllers")
        self.reports_list_controllers.setMaximumSize(QSize(16777215, 200))
        self.reports_list_controllers.setAutoFillBackground(False)
        self.verticalLayout_25 = QVBoxLayout(self.reports_list_controllers)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(-1, -1, -1, 0)
        self.reports_list_name_label = QLabel(self.reports_list_controllers)
        self.reports_list_name_label.setObjectName(u"reports_list_name_label")
        self.reports_list_name_label.setMinimumSize(QSize(0, 30))
        self.reports_list_name_label.setMaximumSize(QSize(16777215, 30))
        self.reports_list_name_label.setFont(font4)
        self.reports_list_name_label.setLayoutDirection(Qt.LeftToRight)
        self.reports_list_name_label.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"padding-left: 10px;\n"
"font-weight: bold;\n"
"font-size: 15pt;")
        self.reports_list_name_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_25.addWidget(self.reports_list_name_label)

        self.widget_13 = QWidget(self.reports_list_controllers)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setMinimumSize(QSize(0, 150))
        self.horizontalLayout_12 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(-1, -1, -1, 0)
        self.widget_14 = QWidget(self.widget_13)
        self.widget_14.setObjectName(u"widget_14")
        self.verticalLayout_26 = QVBoxLayout(self.widget_14)
        self.verticalLayout_26.setSpacing(5)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(7, 7, 7, 7)
        self.reports_list_input = QLineEdit(self.widget_14)
        self.reports_list_input.setObjectName(u"reports_list_input")
        sizePolicy1.setHeightForWidth(self.reports_list_input.sizePolicy().hasHeightForWidth())
        self.reports_list_input.setSizePolicy(sizePolicy1)
        self.reports_list_input.setMinimumSize(QSize(300, 30))
        self.reports_list_input.setFont(font3)
        self.reports_list_input.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 7px;\n"
"border: 2px solid #000;")

        self.verticalLayout_26.addWidget(self.reports_list_input)

        self.verticalSpacer_8 = QSpacerItem(20, 46, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_26.addItem(self.verticalSpacer_8)


        self.horizontalLayout_12.addWidget(self.widget_14)

        self.widget_15 = QWidget(self.widget_13)
        self.widget_15.setObjectName(u"widget_15")
        self.widget_15.setMinimumSize(QSize(150, 0))
        self.verticalLayout_27 = QVBoxLayout(self.widget_15)
        self.verticalLayout_27.setSpacing(5)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(7, 7, 7, 7)
        self.reports_list_search_btn = QPushButton(self.widget_15)
        self.reports_list_search_btn.setObjectName(u"reports_list_search_btn")
        self.reports_list_search_btn.setMinimumSize(QSize(150, 30))
        self.reports_list_search_btn.setMaximumSize(QSize(10, 30))
        self.reports_list_search_btn.setFont(font5)
        self.reports_list_search_btn.setStyleSheet(u"background-color: rgb(190,207,187);\n"
"color: rgb(0,0,0);\n"
"border-radius: 5px;\n"
"border: 2px solid #000;\n"
"font-weight: bold;\n"
"font-size: 12pt;")
        self.reports_list_search_btn.setIconSize(QSize(25, 25))

        self.verticalLayout_27.addWidget(self.reports_list_search_btn)

        self.reports_list_add_btn = QPushButton(self.widget_15)
        self.reports_list_add_btn.setObjectName(u"reports_list_add_btn")
        self.reports_list_add_btn.setMinimumSize(QSize(150, 30))
        self.reports_list_add_btn.setMaximumSize(QSize(150, 30))
        self.reports_list_add_btn.setFont(font5)
        self.reports_list_add_btn.setStyleSheet(u"background-color: rgb(190,207,187);\n"
"color: rgb(0,0,0);\n"
"border-radius: 5px;\n"
"border: 2px solid #000;\n"
"font-weight: bold;\n"
"font-size: 12pt;")
        self.reports_list_add_btn.setIcon(icon11)
        self.reports_list_add_btn.setIconSize(QSize(25, 25))

        self.verticalLayout_27.addWidget(self.reports_list_add_btn)

        self.reports_list_edit_btn = QPushButton(self.widget_15)
        self.reports_list_edit_btn.setObjectName(u"reports_list_edit_btn")
        self.reports_list_edit_btn.setMinimumSize(QSize(150, 30))
        self.reports_list_edit_btn.setMaximumSize(QSize(150, 30))
        self.reports_list_edit_btn.setFont(font5)
        self.reports_list_edit_btn.setStyleSheet(u"background-color: rgb(190,207,187);\n"
"color: rgb(0,0,0);\n"
"border-radius: 5px;\n"
"border: 2px solid #000;\n"
"font-weight: bold;\n"
"font-size: 12pt;")
        self.reports_list_edit_btn.setIcon(icon11)
        self.reports_list_edit_btn.setIconSize(QSize(25, 25))

        self.verticalLayout_27.addWidget(self.reports_list_edit_btn)

        self.reports_list_del_btn = QPushButton(self.widget_15)
        self.reports_list_del_btn.setObjectName(u"reports_list_del_btn")
        self.reports_list_del_btn.setMinimumSize(QSize(150, 30))
        self.reports_list_del_btn.setMaximumSize(QSize(150, 30))
        self.reports_list_del_btn.setFont(font5)
        self.reports_list_del_btn.setStyleSheet(u"background-color: rgb(190,207,187);\n"
"color: rgb(0,0,0);\n"
"border-radius: 5px;\n"
"border: 2px solid #000;\n"
"font-weight: bold;\n"
"font-size: 12pt;")
        self.reports_list_del_btn.setIcon(icon11)
        self.reports_list_del_btn.setIconSize(QSize(25, 25))

        self.verticalLayout_27.addWidget(self.reports_list_del_btn)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_27.addItem(self.verticalSpacer_9)


        self.horizontalLayout_12.addWidget(self.widget_15)


        self.verticalLayout_25.addWidget(self.widget_13)


        self.verticalLayout_29.addWidget(self.reports_list_controllers)

        self.reports_list_view = QWidget(self.reports_list_page)
        self.reports_list_view.setObjectName(u"reports_list_view")
        self.reports_list_view.setFont(font6)
        self.reports_list_view.setStyleSheet(u"border-radius: 5px;\n"
"background-color:rgb(54, 71, 107); \n"
"border-radius: 5px;\n"
"border: 2px solid #000;\n"
"")
        self.verticalLayout_24 = QVBoxLayout(self.reports_list_view)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(11, 11, 11, 11)
        self.reports_list_table = QTableWidget(self.reports_list_view)
        self.reports_list_table.setObjectName(u"reports_list_table")
        self.reports_list_table.setFont(font6)
        self.reports_list_table.setStyleSheet(u"border-radius: 5px;\n"
"border: 0px;\n"
"background-color: rgb(255, 255, 255);")
        self.reports_list_table.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.reports_list_table.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)

        self.verticalLayout_24.addWidget(self.reports_list_table)


        self.verticalLayout_29.addWidget(self.reports_list_view)

        self.main_pages.addWidget(self.reports_list_page)

        self.verticalLayout_2.addWidget(self.main_pages)


        self.horizontalLayout.addWidget(self.main)


        self.verticalLayout_16.addWidget(self.container)

        self.popupWidget = QWidget(self.adminWidget)
        self.popupWidget.setObjectName(u"popupWidget")
        self.popupWidget.setMinimumSize(QSize(800, 0))
        self.popupWidget.setMaximumSize(QSize(800, 0))
        self.popupWidget.setStyleSheet(u"border: 3px solid rgb(0,0,0);\n"
"border-radius: 5px;\n"
"background-color: rgb(223, 228, 219);")
        self.verticalLayout_8 = QVBoxLayout(self.popupWidget)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(4, 4, 4, 4)
        self.popupPages = QStackedWidget(self.popupWidget)
        self.popupPages.setObjectName(u"popupPages")
        self.popupPages.setStyleSheet(u"border: 1px;\n"
"background-color: rgb(54, 71, 107);\n"
"border-radius: 3px;")
        self.admins_popup = QWidget()
        self.admins_popup.setObjectName(u"admins_popup")
        self.admins_popup.setStyleSheet(u"")
        self.verticalLayout_9 = QVBoxLayout(self.admins_popup)
        self.verticalLayout_9.setSpacing(5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(1, 1, 1, 1)
        self.head_admins = QWidget(self.admins_popup)
        self.head_admins.setObjectName(u"head_admins")
        self.head_admins.setMaximumSize(QSize(16777215, 35))
        self.head_admins.setStyleSheet(u"")
        self.horizontalLayout_3 = QHBoxLayout(self.head_admins)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, 0, 5, 0)
        self.admin_label = QLabel(self.head_admins)
        self.admin_label.setObjectName(u"admin_label")
        self.admin_label.setFont(font1)

        self.horizontalLayout_3.addWidget(self.admin_label)

        self.horizontalSpacer = QSpacerItem(484, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(self.head_admins)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(30, 30))
        self.pushButton.setIcon(icon2)
        self.pushButton.setIconSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.pushButton)


        self.verticalLayout_9.addWidget(self.head_admins)

        self.body_admins = QWidget(self.admins_popup)
        self.body_admins.setObjectName(u"body_admins")
        self.body_admins.setStyleSheet(u"")
        self.admin_id_text = QLineEdit(self.body_admins)
        self.admin_id_text.setObjectName(u"admin_id_text")
        self.admin_id_text.setEnabled(False)
        self.admin_id_text.setGeometry(QRect(30, 100, 351, 31))
        font7 = QFont()
        font7.setFamily(u"Cascadia Code")
        font7.setPointSize(11)
        font7.setBold(False)
        font7.setWeight(50)
        self.admin_id_text.setFont(font7)
        self.admin_id_text.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.admin_username_text = QLineEdit(self.body_admins)
        self.admin_username_text.setObjectName(u"admin_username_text")
        self.admin_username_text.setGeometry(QRect(30, 200, 351, 31))
        self.admin_username_text.setFont(font7)
        self.admin_username_text.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.admin_password_text = QLineEdit(self.body_admins)
        self.admin_password_text.setObjectName(u"admin_password_text")
        self.admin_password_text.setGeometry(QRect(30, 300, 351, 31))
        self.admin_password_text.setFont(font7)
        self.admin_password_text.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.admin_id_label = QLabel(self.body_admins)
        self.admin_id_label.setObjectName(u"admin_id_label")
        self.admin_id_label.setGeometry(QRect(40, 60, 201, 31))
        self.admin_id_label.setFont(font1)
        self.admin_username_label = QLabel(self.body_admins)
        self.admin_username_label.setObjectName(u"admin_username_label")
        self.admin_username_label.setGeometry(QRect(40, 160, 201, 31))
        self.admin_username_label.setFont(font1)
        self.admin_password_label = QLabel(self.body_admins)
        self.admin_password_label.setObjectName(u"admin_password_label")
        self.admin_password_label.setGeometry(QRect(40, 260, 201, 31))
        self.admin_password_label.setFont(font1)
        self.admin_save_btn = QPushButton(self.body_admins)
        self.admin_save_btn.setObjectName(u"admin_save_btn")
        self.admin_save_btn.setGeometry(QRect(520, 390, 93, 28))
        font8 = QFont()
        font8.setFamily(u"Cascadia Code")
        font8.setPointSize(11)
        self.admin_save_btn.setFont(font8)
        self.admin_save_btn.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.admin_refesh_btn = QPushButton(self.body_admins)
        self.admin_refesh_btn.setObjectName(u"admin_refesh_btn")
        self.admin_refesh_btn.setGeometry(QRect(650, 390, 93, 28))
        self.admin_refesh_btn.setFont(font8)
        self.admin_refesh_btn.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_9.addWidget(self.body_admins)

        self.popupPages.addWidget(self.admins_popup)
        self.teachers_popup = QWidget()
        self.teachers_popup.setObjectName(u"teachers_popup")
        self.verticalLayout_10 = QVBoxLayout(self.teachers_popup)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.head_admins_2 = QWidget(self.teachers_popup)
        self.head_admins_2.setObjectName(u"head_admins_2")
        self.head_admins_2.setMaximumSize(QSize(16777215, 35))
        self.head_admins_2.setStyleSheet(u"")
        self.horizontalLayout_4 = QHBoxLayout(self.head_admins_2)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(5, 0, 5, 0)
        self.admin_label_2 = QLabel(self.head_admins_2)
        self.admin_label_2.setObjectName(u"admin_label_2")
        self.admin_label_2.setFont(font1)

        self.horizontalLayout_4.addWidget(self.admin_label_2)

        self.horizontalSpacer_3 = QSpacerItem(484, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.pushButton_2 = QPushButton(self.head_admins_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMaximumSize(QSize(30, 30))
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QSize(30, 30))

        self.horizontalLayout_4.addWidget(self.pushButton_2)


        self.verticalLayout_10.addWidget(self.head_admins_2)

        self.body_admins_2 = QWidget(self.teachers_popup)
        self.body_admins_2.setObjectName(u"body_admins_2")
        self.body_admins_2.setStyleSheet(u"")
        self.admin_id_text_2 = QLineEdit(self.body_admins_2)
        self.admin_id_text_2.setObjectName(u"admin_id_text_2")
        self.admin_id_text_2.setEnabled(False)
        self.admin_id_text_2.setGeometry(QRect(20, 100, 351, 31))
        self.admin_id_text_2.setFont(font7)
        self.admin_id_text_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.admin_username_text_2 = QLineEdit(self.body_admins_2)
        self.admin_username_text_2.setObjectName(u"admin_username_text_2")
        self.admin_username_text_2.setGeometry(QRect(20, 200, 351, 31))
        self.admin_username_text_2.setFont(font7)
        self.admin_username_text_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.admin_password_text_2 = QLineEdit(self.body_admins_2)
        self.admin_password_text_2.setObjectName(u"admin_password_text_2")
        self.admin_password_text_2.setGeometry(QRect(20, 300, 351, 31))
        self.admin_password_text_2.setFont(font7)
        self.admin_password_text_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.admin_id_label_2 = QLabel(self.body_admins_2)
        self.admin_id_label_2.setObjectName(u"admin_id_label_2")
        self.admin_id_label_2.setGeometry(QRect(30, 60, 201, 31))
        self.admin_id_label_2.setFont(font1)
        self.admin_username_label_2 = QLabel(self.body_admins_2)
        self.admin_username_label_2.setObjectName(u"admin_username_label_2")
        self.admin_username_label_2.setGeometry(QRect(30, 160, 201, 31))
        self.admin_username_label_2.setFont(font1)
        self.admin_password_label_2 = QLabel(self.body_admins_2)
        self.admin_password_label_2.setObjectName(u"admin_password_label_2")
        self.admin_password_label_2.setGeometry(QRect(30, 260, 201, 31))
        self.admin_password_label_2.setFont(font1)
        self.admin_save_btn_2 = QPushButton(self.body_admins_2)
        self.admin_save_btn_2.setObjectName(u"admin_save_btn_2")
        self.admin_save_btn_2.setGeometry(QRect(520, 390, 93, 28))
        self.admin_save_btn_2.setFont(font8)
        self.admin_save_btn_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.admin_refesh_btn_2 = QPushButton(self.body_admins_2)
        self.admin_refesh_btn_2.setObjectName(u"admin_refesh_btn_2")
        self.admin_refesh_btn_2.setGeometry(QRect(650, 390, 93, 28))
        self.admin_refesh_btn_2.setFont(font8)
        self.admin_refesh_btn_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.admin_password_label_3 = QLabel(self.body_admins_2)
        self.admin_password_label_3.setObjectName(u"admin_password_label_3")
        self.admin_password_label_3.setGeometry(QRect(410, 60, 201, 31))
        self.admin_password_label_3.setFont(font1)
        self.admin_password_text_3 = QLineEdit(self.body_admins_2)
        self.admin_password_text_3.setObjectName(u"admin_password_text_3")
        self.admin_password_text_3.setGeometry(QRect(400, 100, 351, 31))
        self.admin_password_text_3.setFont(font7)
        self.admin_password_text_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.admin_password_label_4 = QLabel(self.body_admins_2)
        self.admin_password_label_4.setObjectName(u"admin_password_label_4")
        self.admin_password_label_4.setGeometry(QRect(410, 160, 201, 31))
        self.admin_password_label_4.setFont(font1)
        self.admin_password_text_4 = QLineEdit(self.body_admins_2)
        self.admin_password_text_4.setObjectName(u"admin_password_text_4")
        self.admin_password_text_4.setGeometry(QRect(400, 200, 351, 31))
        self.admin_password_text_4.setFont(font7)
        self.admin_password_text_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_10.addWidget(self.body_admins_2)

        self.popupPages.addWidget(self.teachers_popup)
        self.students_popup = QWidget()
        self.students_popup.setObjectName(u"students_popup")
        self.verticalLayout_12 = QVBoxLayout(self.students_popup)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.head_admins_3 = QWidget(self.students_popup)
        self.head_admins_3.setObjectName(u"head_admins_3")
        self.head_admins_3.setMaximumSize(QSize(16777215, 35))
        self.head_admins_3.setStyleSheet(u"")
        self.horizontalLayout_5 = QHBoxLayout(self.head_admins_3)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(5, 0, 5, 0)
        self.admin_label_3 = QLabel(self.head_admins_3)
        self.admin_label_3.setObjectName(u"admin_label_3")
        self.admin_label_3.setFont(font1)

        self.horizontalLayout_5.addWidget(self.admin_label_3)

        self.horizontalSpacer_4 = QSpacerItem(484, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.pushButton_3 = QPushButton(self.head_admins_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMaximumSize(QSize(30, 30))
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QSize(30, 30))

        self.horizontalLayout_5.addWidget(self.pushButton_3)


        self.verticalLayout_12.addWidget(self.head_admins_3)

        self.body_admins_3 = QWidget(self.students_popup)
        self.body_admins_3.setObjectName(u"body_admins_3")
        self.body_admins_3.setStyleSheet(u"")
        self.admin_id_text_3 = QLineEdit(self.body_admins_3)
        self.admin_id_text_3.setObjectName(u"admin_id_text_3")
        self.admin_id_text_3.setEnabled(False)
        self.admin_id_text_3.setGeometry(QRect(20, 100, 351, 31))
        self.admin_id_text_3.setFont(font7)
        self.admin_id_text_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.admin_username_text_3 = QLineEdit(self.body_admins_3)
        self.admin_username_text_3.setObjectName(u"admin_username_text_3")
        self.admin_username_text_3.setGeometry(QRect(20, 200, 351, 31))
        self.admin_username_text_3.setFont(font7)
        self.admin_username_text_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.admin_password_text_5 = QLineEdit(self.body_admins_3)
        self.admin_password_text_5.setObjectName(u"admin_password_text_5")
        self.admin_password_text_5.setGeometry(QRect(20, 300, 351, 31))
        self.admin_password_text_5.setFont(font7)
        self.admin_password_text_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.admin_id_label_3 = QLabel(self.body_admins_3)
        self.admin_id_label_3.setObjectName(u"admin_id_label_3")
        self.admin_id_label_3.setGeometry(QRect(30, 60, 201, 31))
        self.admin_id_label_3.setFont(font1)
        self.admin_username_label_3 = QLabel(self.body_admins_3)
        self.admin_username_label_3.setObjectName(u"admin_username_label_3")
        self.admin_username_label_3.setGeometry(QRect(30, 160, 201, 31))
        self.admin_username_label_3.setFont(font1)
        self.admin_password_label_5 = QLabel(self.body_admins_3)
        self.admin_password_label_5.setObjectName(u"admin_password_label_5")
        self.admin_password_label_5.setGeometry(QRect(30, 260, 201, 31))
        self.admin_password_label_5.setFont(font1)
        self.admin_save_btn_3 = QPushButton(self.body_admins_3)
        self.admin_save_btn_3.setObjectName(u"admin_save_btn_3")
        self.admin_save_btn_3.setGeometry(QRect(520, 390, 93, 28))
        self.admin_save_btn_3.setFont(font8)
        self.admin_save_btn_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.admin_refesh_btn_3 = QPushButton(self.body_admins_3)
        self.admin_refesh_btn_3.setObjectName(u"admin_refesh_btn_3")
        self.admin_refesh_btn_3.setGeometry(QRect(650, 390, 93, 28))
        self.admin_refesh_btn_3.setFont(font8)
        self.admin_refesh_btn_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.admin_password_label_6 = QLabel(self.body_admins_3)
        self.admin_password_label_6.setObjectName(u"admin_password_label_6")
        self.admin_password_label_6.setGeometry(QRect(410, 60, 201, 31))
        self.admin_password_label_6.setFont(font1)
        self.admin_password_text_6 = QLineEdit(self.body_admins_3)
        self.admin_password_text_6.setObjectName(u"admin_password_text_6")
        self.admin_password_text_6.setGeometry(QRect(400, 100, 351, 31))
        self.admin_password_text_6.setFont(font7)
        self.admin_password_text_6.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.admin_password_label_7 = QLabel(self.body_admins_3)
        self.admin_password_label_7.setObjectName(u"admin_password_label_7")
        self.admin_password_label_7.setGeometry(QRect(410, 160, 201, 31))
        self.admin_password_label_7.setFont(font1)
        self.admin_password_text_7 = QLineEdit(self.body_admins_3)
        self.admin_password_text_7.setObjectName(u"admin_password_text_7")
        self.admin_password_text_7.setGeometry(QRect(400, 200, 351, 31))
        self.admin_password_text_7.setFont(font7)
        self.admin_password_text_7.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.admin_password_text_8 = QLineEdit(self.body_admins_3)
        self.admin_password_text_8.setObjectName(u"admin_password_text_8")
        self.admin_password_text_8.setGeometry(QRect(400, 300, 351, 31))
        self.admin_password_text_8.setFont(font7)
        self.admin_password_text_8.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.admin_password_label_8 = QLabel(self.body_admins_3)
        self.admin_password_label_8.setObjectName(u"admin_password_label_8")
        self.admin_password_label_8.setGeometry(QRect(410, 260, 201, 31))
        self.admin_password_label_8.setFont(font1)

        self.verticalLayout_12.addWidget(self.body_admins_3)

        self.popupPages.addWidget(self.students_popup)
        self.rooms_popup = QWidget()
        self.rooms_popup.setObjectName(u"rooms_popup")
        self.verticalLayout_13 = QVBoxLayout(self.rooms_popup)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.head_admins_4 = QWidget(self.rooms_popup)
        self.head_admins_4.setObjectName(u"head_admins_4")
        self.head_admins_4.setMaximumSize(QSize(16777215, 35))
        self.head_admins_4.setStyleSheet(u"")
        self.horizontalLayout_6 = QHBoxLayout(self.head_admins_4)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 0, 5, 0)
        self.admin_label_4 = QLabel(self.head_admins_4)
        self.admin_label_4.setObjectName(u"admin_label_4")
        self.admin_label_4.setFont(font1)

        self.horizontalLayout_6.addWidget(self.admin_label_4)

        self.horizontalSpacer_5 = QSpacerItem(484, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)

        self.pushButton_4 = QPushButton(self.head_admins_4)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMaximumSize(QSize(30, 30))
        self.pushButton_4.setIcon(icon2)
        self.pushButton_4.setIconSize(QSize(30, 30))

        self.horizontalLayout_6.addWidget(self.pushButton_4)


        self.verticalLayout_13.addWidget(self.head_admins_4)

        self.body_admins_4 = QWidget(self.rooms_popup)
        self.body_admins_4.setObjectName(u"body_admins_4")
        self.body_admins_4.setStyleSheet(u"")
        self.admin_id_text_4 = QLineEdit(self.body_admins_4)
        self.admin_id_text_4.setObjectName(u"admin_id_text_4")
        self.admin_id_text_4.setEnabled(False)
        self.admin_id_text_4.setGeometry(QRect(20, 40, 351, 31))
        self.admin_id_text_4.setFont(font7)
        self.admin_id_text_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.admin_username_text_4 = QLineEdit(self.body_admins_4)
        self.admin_username_text_4.setObjectName(u"admin_username_text_4")
        self.admin_username_text_4.setGeometry(QRect(20, 140, 351, 31))
        self.admin_username_text_4.setFont(font7)
        self.admin_username_text_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.admin_password_text_9 = QLineEdit(self.body_admins_4)
        self.admin_password_text_9.setObjectName(u"admin_password_text_9")
        self.admin_password_text_9.setGeometry(QRect(20, 240, 351, 131))
        self.admin_password_text_9.setFont(font7)
        self.admin_password_text_9.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.admin_id_label_4 = QLabel(self.body_admins_4)
        self.admin_id_label_4.setObjectName(u"admin_id_label_4")
        self.admin_id_label_4.setGeometry(QRect(30, 0, 201, 31))
        self.admin_id_label_4.setFont(font1)
        self.admin_username_label_4 = QLabel(self.body_admins_4)
        self.admin_username_label_4.setObjectName(u"admin_username_label_4")
        self.admin_username_label_4.setGeometry(QRect(30, 100, 201, 31))
        self.admin_username_label_4.setFont(font1)
        self.admin_password_label_9 = QLabel(self.body_admins_4)
        self.admin_password_label_9.setObjectName(u"admin_password_label_9")
        self.admin_password_label_9.setGeometry(QRect(30, 200, 201, 31))
        self.admin_password_label_9.setFont(font1)
        self.admin_save_btn_4 = QPushButton(self.body_admins_4)
        self.admin_save_btn_4.setObjectName(u"admin_save_btn_4")
        self.admin_save_btn_4.setGeometry(QRect(520, 390, 93, 28))
        self.admin_save_btn_4.setFont(font8)
        self.admin_save_btn_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.admin_refesh_btn_4 = QPushButton(self.body_admins_4)
        self.admin_refesh_btn_4.setObjectName(u"admin_refesh_btn_4")
        self.admin_refesh_btn_4.setGeometry(QRect(650, 390, 93, 28))
        self.admin_refesh_btn_4.setFont(font8)
        self.admin_refesh_btn_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.admin_password_label_10 = QLabel(self.body_admins_4)
        self.admin_password_label_10.setObjectName(u"admin_password_label_10")
        self.admin_password_label_10.setGeometry(QRect(410, 100, 201, 31))
        self.admin_password_label_10.setFont(font1)
        self.admin_password_text_10 = QLineEdit(self.body_admins_4)
        self.admin_password_text_10.setObjectName(u"admin_password_text_10")
        self.admin_password_text_10.setGeometry(QRect(400, 140, 351, 31))
        self.admin_password_text_10.setFont(font7)
        self.admin_password_text_10.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.admin_password_label_11 = QLabel(self.body_admins_4)
        self.admin_password_label_11.setObjectName(u"admin_password_label_11")
        self.admin_password_label_11.setGeometry(QRect(410, 200, 201, 31))
        self.admin_password_label_11.setFont(font1)
        self.admin_password_text_11 = QLineEdit(self.body_admins_4)
        self.admin_password_text_11.setObjectName(u"admin_password_text_11")
        self.admin_password_text_11.setGeometry(QRect(400, 240, 351, 31))
        self.admin_password_text_11.setFont(font7)
        self.admin_password_text_11.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.admin_password_text_12 = QLineEdit(self.body_admins_4)
        self.admin_password_text_12.setObjectName(u"admin_password_text_12")
        self.admin_password_text_12.setGeometry(QRect(400, 340, 351, 31))
        self.admin_password_text_12.setFont(font7)
        self.admin_password_text_12.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.admin_password_label_12 = QLabel(self.body_admins_4)
        self.admin_password_label_12.setObjectName(u"admin_password_label_12")
        self.admin_password_label_12.setGeometry(QRect(410, 300, 201, 31))
        self.admin_password_label_12.setFont(font1)
        self.admin_password_text_13 = QLineEdit(self.body_admins_4)
        self.admin_password_text_13.setObjectName(u"admin_password_text_13")
        self.admin_password_text_13.setGeometry(QRect(400, 40, 351, 31))
        self.admin_password_text_13.setFont(font7)
        self.admin_password_text_13.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.admin_password_label_13 = QLabel(self.body_admins_4)
        self.admin_password_label_13.setObjectName(u"admin_password_label_13")
        self.admin_password_label_13.setGeometry(QRect(410, 0, 201, 31))
        self.admin_password_label_13.setFont(font1)

        self.verticalLayout_13.addWidget(self.body_admins_4)

        self.popupPages.addWidget(self.rooms_popup)
        self.reports_popup = QWidget()
        self.reports_popup.setObjectName(u"reports_popup")
        self.verticalLayout_14 = QVBoxLayout(self.reports_popup)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.head_admins_5 = QWidget(self.reports_popup)
        self.head_admins_5.setObjectName(u"head_admins_5")
        self.head_admins_5.setMaximumSize(QSize(16777215, 35))
        self.head_admins_5.setStyleSheet(u"")
        self.horizontalLayout_7 = QHBoxLayout(self.head_admins_5)
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(5, 0, 5, 0)
        self.admin_label_5 = QLabel(self.head_admins_5)
        self.admin_label_5.setObjectName(u"admin_label_5")
        self.admin_label_5.setFont(font1)

        self.horizontalLayout_7.addWidget(self.admin_label_5)

        self.horizontalSpacer_6 = QSpacerItem(484, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_6)

        self.pushButton_5 = QPushButton(self.head_admins_5)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMaximumSize(QSize(30, 30))
        self.pushButton_5.setIcon(icon2)
        self.pushButton_5.setIconSize(QSize(30, 30))

        self.horizontalLayout_7.addWidget(self.pushButton_5)


        self.verticalLayout_14.addWidget(self.head_admins_5)

        self.body_admins_5 = QWidget(self.reports_popup)
        self.body_admins_5.setObjectName(u"body_admins_5")
        self.body_admins_5.setStyleSheet(u"")
        self.admin_id_text_5 = QLineEdit(self.body_admins_5)
        self.admin_id_text_5.setObjectName(u"admin_id_text_5")
        self.admin_id_text_5.setEnabled(False)
        self.admin_id_text_5.setGeometry(QRect(30, 100, 351, 31))
        self.admin_id_text_5.setFont(font7)
        self.admin_id_text_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.admin_username_text_5 = QLineEdit(self.body_admins_5)
        self.admin_username_text_5.setObjectName(u"admin_username_text_5")
        self.admin_username_text_5.setGeometry(QRect(30, 200, 351, 31))
        self.admin_username_text_5.setFont(font7)
        self.admin_username_text_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.admin_password_text_14 = QLineEdit(self.body_admins_5)
        self.admin_password_text_14.setObjectName(u"admin_password_text_14")
        self.admin_password_text_14.setGeometry(QRect(30, 300, 351, 31))
        self.admin_password_text_14.setFont(font7)
        self.admin_password_text_14.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.admin_id_label_5 = QLabel(self.body_admins_5)
        self.admin_id_label_5.setObjectName(u"admin_id_label_5")
        self.admin_id_label_5.setGeometry(QRect(40, 60, 201, 31))
        self.admin_id_label_5.setFont(font1)
        self.admin_username_label_5 = QLabel(self.body_admins_5)
        self.admin_username_label_5.setObjectName(u"admin_username_label_5")
        self.admin_username_label_5.setGeometry(QRect(40, 160, 201, 31))
        self.admin_username_label_5.setFont(font1)
        self.admin_password_label_14 = QLabel(self.body_admins_5)
        self.admin_password_label_14.setObjectName(u"admin_password_label_14")
        self.admin_password_label_14.setGeometry(QRect(40, 260, 201, 31))
        self.admin_password_label_14.setFont(font1)
        self.admin_save_btn_5 = QPushButton(self.body_admins_5)
        self.admin_save_btn_5.setObjectName(u"admin_save_btn_5")
        self.admin_save_btn_5.setGeometry(QRect(520, 390, 93, 28))
        self.admin_save_btn_5.setFont(font8)
        self.admin_save_btn_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.admin_refesh_btn_5 = QPushButton(self.body_admins_5)
        self.admin_refesh_btn_5.setObjectName(u"admin_refesh_btn_5")
        self.admin_refesh_btn_5.setGeometry(QRect(650, 390, 93, 28))
        self.admin_refesh_btn_5.setFont(font8)
        self.admin_refesh_btn_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.admin_username_text_6 = QLineEdit(self.body_admins_5)
        self.admin_username_text_6.setObjectName(u"admin_username_text_6")
        self.admin_username_text_6.setGeometry(QRect(400, 200, 351, 31))
        self.admin_username_text_6.setFont(font7)
        self.admin_username_text_6.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.admin_id_label_6 = QLabel(self.body_admins_5)
        self.admin_id_label_6.setObjectName(u"admin_id_label_6")
        self.admin_id_label_6.setGeometry(QRect(410, 60, 201, 31))
        self.admin_id_label_6.setFont(font1)
        self.admin_username_label_6 = QLabel(self.body_admins_5)
        self.admin_username_label_6.setObjectName(u"admin_username_label_6")
        self.admin_username_label_6.setGeometry(QRect(410, 160, 201, 31))
        self.admin_username_label_6.setFont(font1)
        self.admin_password_label_15 = QLabel(self.body_admins_5)
        self.admin_password_label_15.setObjectName(u"admin_password_label_15")
        self.admin_password_label_15.setGeometry(QRect(410, 260, 201, 31))
        self.admin_password_label_15.setFont(font1)
        self.admin_id_text_6 = QLineEdit(self.body_admins_5)
        self.admin_id_text_6.setObjectName(u"admin_id_text_6")
        self.admin_id_text_6.setEnabled(False)
        self.admin_id_text_6.setGeometry(QRect(400, 100, 351, 31))
        self.admin_id_text_6.setFont(font7)
        self.admin_id_text_6.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.admin_password_text_15 = QLineEdit(self.body_admins_5)
        self.admin_password_text_15.setObjectName(u"admin_password_text_15")
        self.admin_password_text_15.setGeometry(QRect(400, 300, 351, 31))
        self.admin_password_text_15.setFont(font7)
        self.admin_password_text_15.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_14.addWidget(self.body_admins_5)

        self.popupPages.addWidget(self.reports_popup)
        self.reports_list_popup = QWidget()
        self.reports_list_popup.setObjectName(u"reports_list_popup")
        self.verticalLayout_15 = QVBoxLayout(self.reports_list_popup)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.head_admins_6 = QWidget(self.reports_list_popup)
        self.head_admins_6.setObjectName(u"head_admins_6")
        self.head_admins_6.setMaximumSize(QSize(16777215, 35))
        self.head_admins_6.setStyleSheet(u"")
        self.horizontalLayout_8 = QHBoxLayout(self.head_admins_6)
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(5, 0, 5, 0)
        self.admin_label_6 = QLabel(self.head_admins_6)
        self.admin_label_6.setObjectName(u"admin_label_6")
        self.admin_label_6.setFont(font1)

        self.horizontalLayout_8.addWidget(self.admin_label_6)

        self.horizontalSpacer_7 = QSpacerItem(484, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_7)

        self.pushButton_6 = QPushButton(self.head_admins_6)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMaximumSize(QSize(30, 30))
        self.pushButton_6.setIcon(icon2)
        self.pushButton_6.setIconSize(QSize(30, 30))

        self.horizontalLayout_8.addWidget(self.pushButton_6)


        self.verticalLayout_15.addWidget(self.head_admins_6)

        self.body_admins_6 = QWidget(self.reports_list_popup)
        self.body_admins_6.setObjectName(u"body_admins_6")
        self.body_admins_6.setStyleSheet(u"")
        self.admin_id_text_7 = QLineEdit(self.body_admins_6)
        self.admin_id_text_7.setObjectName(u"admin_id_text_7")
        self.admin_id_text_7.setEnabled(False)
        self.admin_id_text_7.setGeometry(QRect(20, 140, 350, 30))
        self.admin_id_text_7.setFont(font7)
        self.admin_id_text_7.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.admin_username_text_7 = QLineEdit(self.body_admins_6)
        self.admin_username_text_7.setObjectName(u"admin_username_text_7")
        self.admin_username_text_7.setGeometry(QRect(390, 140, 350, 30))
        self.admin_username_text_7.setFont(font7)
        self.admin_username_text_7.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.admin_id_label_7 = QLabel(self.body_admins_6)
        self.admin_id_label_7.setObjectName(u"admin_id_label_7")
        self.admin_id_label_7.setGeometry(QRect(30, 100, 240, 30))
        self.admin_id_label_7.setFont(font1)
        self.admin_username_label_7 = QLabel(self.body_admins_6)
        self.admin_username_label_7.setObjectName(u"admin_username_label_7")
        self.admin_username_label_7.setGeometry(QRect(400, 100, 200, 30))
        self.admin_username_label_7.setFont(font1)
        self.admin_save_btn_6 = QPushButton(self.body_admins_6)
        self.admin_save_btn_6.setObjectName(u"admin_save_btn_6")
        self.admin_save_btn_6.setGeometry(QRect(520, 390, 93, 28))
        self.admin_save_btn_6.setFont(font8)
        self.admin_save_btn_6.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.admin_refesh_btn_6 = QPushButton(self.body_admins_6)
        self.admin_refesh_btn_6.setObjectName(u"admin_refesh_btn_6")
        self.admin_refesh_btn_6.setGeometry(QRect(650, 390, 93, 28))
        self.admin_refesh_btn_6.setFont(font8)
        self.admin_refesh_btn_6.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.admin_username_text_8 = QLineEdit(self.body_admins_6)
        self.admin_username_text_8.setObjectName(u"admin_username_text_8")
        self.admin_username_text_8.setGeometry(QRect(390, 240, 350, 30))
        self.admin_username_text_8.setFont(font7)
        self.admin_username_text_8.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.admin_id_label_8 = QLabel(self.body_admins_6)
        self.admin_id_label_8.setObjectName(u"admin_id_label_8")
        self.admin_id_label_8.setGeometry(QRect(30, 200, 200, 30))
        self.admin_id_label_8.setFont(font1)
        self.admin_username_label_8 = QLabel(self.body_admins_6)
        self.admin_username_label_8.setObjectName(u"admin_username_label_8")
        self.admin_username_label_8.setGeometry(QRect(400, 200, 200, 30))
        self.admin_username_label_8.setFont(font1)
        self.admin_id_text_8 = QLineEdit(self.body_admins_6)
        self.admin_id_text_8.setObjectName(u"admin_id_text_8")
        self.admin_id_text_8.setEnabled(False)
        self.admin_id_text_8.setGeometry(QRect(20, 240, 350, 30))
        self.admin_id_text_8.setFont(font7)
        self.admin_id_text_8.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_15.addWidget(self.body_admins_6)

        self.popupPages.addWidget(self.reports_list_popup)

        self.verticalLayout_8.addWidget(self.popupPages)


        self.verticalLayout_16.addWidget(self.popupWidget)

        Admin.setCentralWidget(self.adminWidget)

        self.retranslateUi(Admin)

        self.main_pages.setCurrentIndex(4)
        self.popupPages.setCurrentIndex(5)


        QMetaObject.connectSlotsByName(Admin)
    # setupUi

    def retranslateUi(self, Admin):
        self.icon_admin.setText("")
        self.name_admin.setText(QCoreApplication.translate("Admin", u"\u0110i\u1ec3m danh sinh vi\u00ean", None))
        self.admin_minimize_btn.setText("")
        self.admin_expand_btn.setText("")
        self.admin_exit_btn.setText("")
        self.menu_btn.setText("")
        self.admins_btn.setText("")
        self.teachers_btn.setText("")
        self.students_btn.setText("")
        self.rooms_btn.setText("")
        self.reports_btn.setText("")
        self.reports_list_btn.setText("")
        self.logout_btn.setText("")
        self.admins_label.setText(QCoreApplication.translate("Admin", u"QU\u1ea2N TR\u1eca VI\u00caN", None))
        self.admins_input.setInputMask("")
        self.admins_input.setText("")
        self.admins_search_btn.setText(QCoreApplication.translate("Admin", u"T\u00ecm ki\u1ebfm", None))
        self.admins_add_btn.setText(QCoreApplication.translate("Admin", u"Th\u00eam", None))
        self.admins_edit_btn.setText(QCoreApplication.translate("Admin", u"S\u1eeda", None))
        self.admins_del_btn.setText(QCoreApplication.translate("Admin", u"X\u00f3a", None))
        self.teachers_name_label.setText(QCoreApplication.translate("Admin", u"GI\u1ea2NG VI\u00caN", None))
        self.teachers_input.setInputMask("")
        self.teachers_input.setText("")
        self.teachers_search_btn.setText(QCoreApplication.translate("Admin", u"T\u00ecm ki\u1ebfm", None))
        self.teachers_add_btn.setText(QCoreApplication.translate("Admin", u"Th\u00eam", None))
        self.teachers_edit_btn.setText(QCoreApplication.translate("Admin", u"S\u1eeda", None))
        self.teachers_del_btn.setText(QCoreApplication.translate("Admin", u"X\u00f3a", None))
        self.students_name_label.setText(QCoreApplication.translate("Admin", u"SINH VI\u00caN", None))
        self.students_input.setInputMask("")
        self.students_input.setText("")
        self.students_search_btn.setText(QCoreApplication.translate("Admin", u"T\u00ecm ki\u1ebfm", None))
        self.students_add_btn.setText(QCoreApplication.translate("Admin", u"Th\u00eam", None))
        self.students_edit_btn.setText(QCoreApplication.translate("Admin", u"S\u1eeda", None))
        self.students_del_btn.setText(QCoreApplication.translate("Admin", u"X\u00f3a", None))
        self.reports_list_name_label_5.setText(QCoreApplication.translate("Admin", u"L\u1edaP H\u1eccC", None))
        self.reports_list_input_5.setInputMask("")
        self.reports_list_input_5.setText("")
        self.reports_list_search_btn_5.setText(QCoreApplication.translate("Admin", u"T\u00ecm ki\u1ebfm", None))
        self.reports_list_add_btn_5.setText(QCoreApplication.translate("Admin", u"Th\u00eam", None))
        self.reports_list_edit_btn_5.setText(QCoreApplication.translate("Admin", u"S\u1eeda", None))
        self.reports_list_del_btn_5.setText(QCoreApplication.translate("Admin", u"X\u00f3a", None))
        self.reports_list_name_label_6.setText(QCoreApplication.translate("Admin", u"B\u00c1O C\u00c1O SINH VI\u00caN", None))
        self.reports_list_input_6.setInputMask("")
        self.reports_list_input_6.setText("")
        self.reports_list_search_btn_6.setText(QCoreApplication.translate("Admin", u"T\u00ecm ki\u1ebfm", None))
        self.reports_list_add_btn_6.setText(QCoreApplication.translate("Admin", u"Th\u00eam", None))
        self.reports_list_edit_btn_6.setText(QCoreApplication.translate("Admin", u"S\u1eeda", None))
        self.reports_list_del_btn_6.setText(QCoreApplication.translate("Admin", u"X\u00f3a", None))
        self.reports_list_name_label.setText(QCoreApplication.translate("Admin", u"DANH S\u00c1CH B\u00c1O C\u00c1O \u0110I\u1ec2M DANH", None))
        self.reports_list_input.setInputMask("")
        self.reports_list_input.setText("")
        self.reports_list_search_btn.setText(QCoreApplication.translate("Admin", u"T\u00ecm ki\u1ebfm", None))
        self.reports_list_add_btn.setText(QCoreApplication.translate("Admin", u"Th\u00eam", None))
        self.reports_list_edit_btn.setText(QCoreApplication.translate("Admin", u"S\u1eeda", None))
        self.reports_list_del_btn.setText(QCoreApplication.translate("Admin", u"X\u00f3a", None))
        self.admin_label.setText(QCoreApplication.translate("Admin", u"TH\u00d4NG TIN QU\u1ea2N TR\u1eca VI\u00caN", None))
        self.pushButton.setText("")
        self.admin_id_label.setText(QCoreApplication.translate("Admin", u"M\u00e3 Qu\u1ea3n tr\u1ecb vi\u00ean", None))
        self.admin_username_label.setText(QCoreApplication.translate("Admin", u"T\u00e0i kho\u1ea3n", None))
        self.admin_password_label.setText(QCoreApplication.translate("Admin", u"M\u1eadt kh\u1ea9u", None))
        self.admin_save_btn.setText(QCoreApplication.translate("Admin", u"L\u01b0u", None))
        self.admin_refesh_btn.setText(QCoreApplication.translate("Admin", u"L\u00e0m m\u1edbi", None))
        self.admin_label_2.setText(QCoreApplication.translate("Admin", u"TH\u00d4NG TIN GI\u1ea2NG VI\u00caN", None))
        self.pushButton_2.setText("")
        self.admin_id_label_2.setText(QCoreApplication.translate("Admin", u"M\u00e3 gi\u1ea3ng vi\u00ean", None))
        self.admin_username_label_2.setText(QCoreApplication.translate("Admin", u"T\u00ean gi\u1ea3ng vi\u00ean", None))
        self.admin_password_label_2.setText(QCoreApplication.translate("Admin", u"\u0110\u1ecba ch\u1ec9", None))
        self.admin_save_btn_2.setText(QCoreApplication.translate("Admin", u"L\u01b0u", None))
        self.admin_refesh_btn_2.setText(QCoreApplication.translate("Admin", u"L\u00e0m m\u1edbi", None))
        self.admin_password_label_3.setText(QCoreApplication.translate("Admin", u"M\u1eadt kh\u1ea9u", None))
        self.admin_password_label_4.setText(QCoreApplication.translate("Admin", u"S\u1ed1 \u0111i\u1ec7n tho\u1ea1i", None))
        self.admin_password_text_4.setText("")
        self.admin_label_3.setText(QCoreApplication.translate("Admin", u"TH\u00d4NG TIN SINH VI\u00caN", None))
        self.pushButton_3.setText("")
        self.admin_id_label_3.setText(QCoreApplication.translate("Admin", u"M\u00e3 sinh vi\u00ean", None))
        self.admin_username_label_3.setText(QCoreApplication.translate("Admin", u"T\u00ean sinh vi\u00ean", None))
        self.admin_password_label_5.setText(QCoreApplication.translate("Admin", u"L\u1edbp qu\u1ea3n l\u00fd", None))
        self.admin_save_btn_3.setText(QCoreApplication.translate("Admin", u"L\u01b0u", None))
        self.admin_refesh_btn_3.setText(QCoreApplication.translate("Admin", u"L\u00e0m m\u1edbi", None))
        self.admin_password_label_6.setText(QCoreApplication.translate("Admin", u"S\u1ed1 \u0111i\u1ec7n tho\u1ea1i", None))
        self.admin_password_label_7.setText(QCoreApplication.translate("Admin", u"\u0110\u1ecba ch\u1ec9", None))
        self.admin_password_text_7.setText("")
        self.admin_password_label_8.setText(QCoreApplication.translate("Admin", u"URL \u1ea2nh", None))
        self.admin_label_4.setText(QCoreApplication.translate("Admin", u"TH\u00d4NG TIN L\u1edaP H\u1eccC", None))
        self.pushButton_4.setText("")
        self.admin_id_label_4.setText(QCoreApplication.translate("Admin", u"M\u00e3 l\u1edbp", None))
        self.admin_username_label_4.setText(QCoreApplication.translate("Admin", u"M\u00e3 gi\u00e1o vi\u00ean", None))
        self.admin_password_label_9.setText(QCoreApplication.translate("Admin", u"L\u1ecbch h\u1ecdc", None))
        self.admin_save_btn_4.setText(QCoreApplication.translate("Admin", u"L\u01b0u", None))
        self.admin_refesh_btn_4.setText(QCoreApplication.translate("Admin", u"L\u00e0m m\u1edbi", None))
        self.admin_password_label_10.setText(QCoreApplication.translate("Admin", u"Ph\u00f2ng h\u1ecdc", None))
        self.admin_password_label_11.setText(QCoreApplication.translate("Admin", u"S\u1ed1 l\u01b0\u1ee3ng sinh vi\u00ean", None))
        self.admin_password_text_11.setText("")
        self.admin_password_label_12.setText(QCoreApplication.translate("Admin", u"S\u1ed1 bu\u1ed5i", None))
        self.admin_password_label_13.setText(QCoreApplication.translate("Admin", u"T\u00ean m\u00f4n h\u1ecdc", None))
        self.admin_label_5.setText(QCoreApplication.translate("Admin", u"TH\u00d4NG TIN \u0110I\u1ec2M DANH", None))
        self.pushButton_5.setText("")
        self.admin_id_label_5.setText(QCoreApplication.translate("Admin", u"M\u00e3 B\u00e1o c\u00e1o", None))
        self.admin_username_label_5.setText(QCoreApplication.translate("Admin", u"M\u00e3 sinh vi\u00ean", None))
        self.admin_password_label_14.setText(QCoreApplication.translate("Admin", u"\u0110i\u1ec3m danh", None))
        self.admin_save_btn_5.setText(QCoreApplication.translate("Admin", u"L\u01b0u", None))
        self.admin_refesh_btn_5.setText(QCoreApplication.translate("Admin", u"L\u00e0m m\u1edbi", None))
        self.admin_id_label_6.setText(QCoreApplication.translate("Admin", u"Ng\u00e0y B\u00e1o c\u00e1o", None))
        self.admin_username_label_6.setText(QCoreApplication.translate("Admin", u"M\u00e3 l\u1edbp", None))
        self.admin_password_label_15.setText(QCoreApplication.translate("Admin", u"Ghi chu", None))
        self.admin_label_6.setText(QCoreApplication.translate("Admin", u"TH\u00d4NG TIN B\u00c1O C\u00c1O \u0110I\u1ec2M DANH", None))
        self.pushButton_6.setText("")
        self.admin_id_label_7.setText(QCoreApplication.translate("Admin", u"M\u00e3 b\u00e1o c\u00e1o \u0111i\u1ec3m danh", None))
        self.admin_username_label_7.setText(QCoreApplication.translate("Admin", u"M\u00e3 l\u1edbp", None))
        self.admin_save_btn_6.setText(QCoreApplication.translate("Admin", u"L\u01b0u", None))
        self.admin_refesh_btn_6.setText(QCoreApplication.translate("Admin", u"L\u00e0m m\u1edbi", None))
        self.admin_id_label_8.setText(QCoreApplication.translate("Admin", u"S\u1ed1 l\u1ea7n \u0111i\u1ec3m danh", None))
        self.admin_username_label_8.setText(QCoreApplication.translate("Admin", u"M\u00e3 sinh vi\u00ean", None))
        pass
    # retranslateUi

