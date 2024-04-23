# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'adminQCfPjY.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import resources.resources

from Custom_Widgets.Widgets import QCustomSlideMenu

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
        self.adminWidget.setMinimumSize(QSize(0, 720))
        self.adminWidget.setMaximumSize(QSize(16777215, 2000))
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
        self.container.setMaximumSize(QSize(16777215, 16777215))
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
        self.remote_controllers.setMaximumSize(QSize(16777215, 305))
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

        self.verticalSpacer_2 = QSpacerItem(20, 300, QSizePolicy.Minimum, QSizePolicy.Preferred)

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
        if (self.admins_table.columnCount() < 3):
            self.admins_table.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem.setFont(font1);
        self.admins_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem1.setFont(font1);
        self.admins_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem2.setFont(font1);
        self.admins_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.admins_table.setObjectName(u"admins_table")
        self.admins_table.setFont(font6)
        self.admins_table.setStyleSheet(u"background-color: rgb(255, 255, 255);")
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
        if (self.teachers_table.columnCount() < 6):
            self.teachers_table.setColumnCount(6)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem3.setFont(font1);
        self.teachers_table.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem4.setFont(font1);
        self.teachers_table.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem5.setFont(font1);
        self.teachers_table.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem6.setFont(font1);
        self.teachers_table.setHorizontalHeaderItem(3, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem7.setFont(font1);
        self.teachers_table.setHorizontalHeaderItem(4, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem8.setFont(font1);
        self.teachers_table.setHorizontalHeaderItem(5, __qtablewidgetitem8)
        self.teachers_table.setObjectName(u"teachers_table")
        self.teachers_table.setFont(font6)
        self.teachers_table.setStyleSheet(u"background-color: rgb(255, 255, 255);")
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
        if (self.students_table.columnCount() < 7):
            self.students_table.setColumnCount(7)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem9.setFont(font1);
        self.students_table.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem10.setFont(font1);
        self.students_table.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem11.setFont(font1);
        self.students_table.setHorizontalHeaderItem(2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem12.setFont(font1);
        self.students_table.setHorizontalHeaderItem(3, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem13.setFont(font1);
        self.students_table.setHorizontalHeaderItem(4, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem14.setFont(font1);
        self.students_table.setHorizontalHeaderItem(5, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem15.setFont(font1);
        self.students_table.setHorizontalHeaderItem(6, __qtablewidgetitem15)
        self.students_table.setObjectName(u"students_table")
        self.students_table.setFont(font6)
        self.students_table.setStyleSheet(u"background-color: rgb(255, 255, 255);")
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
        self.rooms_controllers = QWidget(self.rooms_page)
        self.rooms_controllers.setObjectName(u"rooms_controllers")
        self.rooms_controllers.setMaximumSize(QSize(16777215, 200))
        self.rooms_controllers.setAutoFillBackground(False)
        self.verticalLayout_41 = QVBoxLayout(self.rooms_controllers)
        self.verticalLayout_41.setSpacing(0)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(-1, -1, -1, 0)
        self.rooms_name_label = QLabel(self.rooms_controllers)
        self.rooms_name_label.setObjectName(u"rooms_name_label")
        self.rooms_name_label.setMinimumSize(QSize(0, 30))
        self.rooms_name_label.setMaximumSize(QSize(16777215, 30))
        self.rooms_name_label.setFont(font4)
        self.rooms_name_label.setLayoutDirection(Qt.LeftToRight)
        self.rooms_name_label.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"padding-left: 10px;\n"
"font-weight: bold;\n"
"font-size: 15pt;")
        self.rooms_name_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_41.addWidget(self.rooms_name_label)

        self.widget_25 = QWidget(self.rooms_controllers)
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
        self.rooms_input = QLineEdit(self.widget_26)
        self.rooms_input.setObjectName(u"rooms_input")
        sizePolicy1.setHeightForWidth(self.rooms_input.sizePolicy().hasHeightForWidth())
        self.rooms_input.setSizePolicy(sizePolicy1)
        self.rooms_input.setMinimumSize(QSize(300, 30))
        self.rooms_input.setFont(font3)
        self.rooms_input.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 7px;\n"
"border: 2px solid #000;")

        self.verticalLayout_42.addWidget(self.rooms_input)

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
        self.rooms_search_btn = QPushButton(self.widget_27)
        self.rooms_search_btn.setObjectName(u"rooms_search_btn")
        self.rooms_search_btn.setMinimumSize(QSize(150, 30))
        self.rooms_search_btn.setMaximumSize(QSize(10, 30))
        self.rooms_search_btn.setFont(font5)
        self.rooms_search_btn.setStyleSheet(u"background-color: rgb(190,207,187);\n"
"color: rgb(0,0,0);\n"
"border-radius: 5px;\n"
"border: 2px solid #000;\n"
"font-weight: bold;\n"
"font-size: 12pt;")
        self.rooms_search_btn.setIconSize(QSize(25, 25))

        self.verticalLayout_43.addWidget(self.rooms_search_btn)

        self.rooms_add_btn = QPushButton(self.widget_27)
        self.rooms_add_btn.setObjectName(u"rooms_add_btn")
        self.rooms_add_btn.setMinimumSize(QSize(150, 30))
        self.rooms_add_btn.setMaximumSize(QSize(150, 30))
        self.rooms_add_btn.setFont(font5)
        self.rooms_add_btn.setStyleSheet(u"background-color: rgb(190,207,187);\n"
"color: rgb(0,0,0);\n"
"border-radius: 5px;\n"
"border: 2px solid #000;\n"
"font-weight: bold;\n"
"font-size: 12pt;")
        self.rooms_add_btn.setIcon(icon11)
        self.rooms_add_btn.setIconSize(QSize(25, 25))

        self.verticalLayout_43.addWidget(self.rooms_add_btn)

        self.rooms_edit_btn = QPushButton(self.widget_27)
        self.rooms_edit_btn.setObjectName(u"rooms_edit_btn")
        self.rooms_edit_btn.setMinimumSize(QSize(150, 30))
        self.rooms_edit_btn.setMaximumSize(QSize(150, 30))
        self.rooms_edit_btn.setFont(font5)
        self.rooms_edit_btn.setStyleSheet(u"background-color: rgb(190,207,187);\n"
"color: rgb(0,0,0);\n"
"border-radius: 5px;\n"
"border: 2px solid #000;\n"
"font-weight: bold;\n"
"font-size: 12pt;")
        self.rooms_edit_btn.setIcon(icon11)
        self.rooms_edit_btn.setIconSize(QSize(25, 25))

        self.verticalLayout_43.addWidget(self.rooms_edit_btn)

        self.rooms_del_btn = QPushButton(self.widget_27)
        self.rooms_del_btn.setObjectName(u"rooms_del_btn")
        self.rooms_del_btn.setMinimumSize(QSize(150, 30))
        self.rooms_del_btn.setMaximumSize(QSize(150, 30))
        self.rooms_del_btn.setFont(font5)
        self.rooms_del_btn.setStyleSheet(u"background-color: rgb(190,207,187);\n"
"color: rgb(0,0,0);\n"
"border-radius: 5px;\n"
"border: 2px solid #000;\n"
"font-weight: bold;\n"
"font-size: 12pt;")
        self.rooms_del_btn.setIcon(icon11)
        self.rooms_del_btn.setIconSize(QSize(25, 25))

        self.verticalLayout_43.addWidget(self.rooms_del_btn)

        self.verticalSpacer_17 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_43.addItem(self.verticalSpacer_17)


        self.horizontalLayout_16.addWidget(self.widget_27)


        self.verticalLayout_41.addWidget(self.widget_25)


        self.verticalLayout_6.addWidget(self.rooms_controllers)

        self.rooms_view = QWidget(self.rooms_page)
        self.rooms_view.setObjectName(u"rooms_view")
        self.rooms_view.setFont(font6)
        self.rooms_view.setStyleSheet(u"border-radius: 5px;\n"
"background-color:rgb(54, 71, 107); \n"
"border-radius: 5px;\n"
"border: 2px solid #000;\n"
"")
        self.verticalLayout_44 = QVBoxLayout(self.rooms_view)
        self.verticalLayout_44.setSpacing(0)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(11, 11, 11, 11)
        self.rooms_table = QTableWidget(self.rooms_view)
        if (self.rooms_table.columnCount() < 7):
            self.rooms_table.setColumnCount(7)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem16.setFont(font1);
        self.rooms_table.setHorizontalHeaderItem(0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem17.setFont(font1);
        self.rooms_table.setHorizontalHeaderItem(1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem18.setFont(font1);
        self.rooms_table.setHorizontalHeaderItem(2, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem19.setFont(font1);
        self.rooms_table.setHorizontalHeaderItem(3, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem20.setFont(font1);
        self.rooms_table.setHorizontalHeaderItem(4, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem21.setFont(font1);
        self.rooms_table.setHorizontalHeaderItem(5, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem22.setFont(font1);
        self.rooms_table.setHorizontalHeaderItem(6, __qtablewidgetitem22)
        self.rooms_table.setObjectName(u"rooms_table")
        self.rooms_table.setFont(font6)
        self.rooms_table.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.rooms_table.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.rooms_table.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)

        self.verticalLayout_44.addWidget(self.rooms_table)


        self.verticalLayout_6.addWidget(self.rooms_view)

        self.main_pages.addWidget(self.rooms_page)
        self.reports_page = QWidget()
        self.reports_page.setObjectName(u"reports_page")
        self.verticalLayout_7 = QVBoxLayout(self.reports_page)
        self.verticalLayout_7.setSpacing(3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(1, 1, 1, 1)
        self.reports_controllers = QWidget(self.reports_page)
        self.reports_controllers.setObjectName(u"reports_controllers")
        self.reports_controllers.setMaximumSize(QSize(16777215, 200))
        self.reports_controllers.setAutoFillBackground(False)
        self.verticalLayout_45 = QVBoxLayout(self.reports_controllers)
        self.verticalLayout_45.setSpacing(0)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(-1, -1, -1, 0)
        self.reports_name_label = QLabel(self.reports_controllers)
        self.reports_name_label.setObjectName(u"reports_name_label")
        self.reports_name_label.setMinimumSize(QSize(0, 30))
        self.reports_name_label.setMaximumSize(QSize(16777215, 30))
        self.reports_name_label.setFont(font4)
        self.reports_name_label.setLayoutDirection(Qt.LeftToRight)
        self.reports_name_label.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"padding-left: 10px;\n"
"font-weight: bold;\n"
"font-size: 15pt;")
        self.reports_name_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_45.addWidget(self.reports_name_label)

        self.widget_28 = QWidget(self.reports_controllers)
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
        self.reports_input = QLineEdit(self.widget_29)
        self.reports_input.setObjectName(u"reports_input")
        sizePolicy1.setHeightForWidth(self.reports_input.sizePolicy().hasHeightForWidth())
        self.reports_input.setSizePolicy(sizePolicy1)
        self.reports_input.setMinimumSize(QSize(300, 30))
        self.reports_input.setFont(font3)
        self.reports_input.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 7px;\n"
"border: 2px solid #000;")

        self.verticalLayout_46.addWidget(self.reports_input)

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
        self.reports_search_btn = QPushButton(self.widget_30)
        self.reports_search_btn.setObjectName(u"reports_search_btn")
        self.reports_search_btn.setMinimumSize(QSize(150, 30))
        self.reports_search_btn.setMaximumSize(QSize(10, 30))
        self.reports_search_btn.setFont(font5)
        self.reports_search_btn.setStyleSheet(u"background-color: rgb(190,207,187);\n"
"color: rgb(0,0,0);\n"
"border-radius: 5px;\n"
"border: 2px solid #000;\n"
"font-weight: bold;\n"
"font-size: 12pt;")
        self.reports_search_btn.setIconSize(QSize(25, 25))

        self.verticalLayout_47.addWidget(self.reports_search_btn)

        self.reports_add_btn = QPushButton(self.widget_30)
        self.reports_add_btn.setObjectName(u"reports_add_btn")
        self.reports_add_btn.setMinimumSize(QSize(150, 30))
        self.reports_add_btn.setMaximumSize(QSize(150, 30))
        self.reports_add_btn.setFont(font5)
        self.reports_add_btn.setStyleSheet(u"background-color: rgb(190,207,187);\n"
"color: rgb(0,0,0);\n"
"border-radius: 5px;\n"
"border: 2px solid #000;\n"
"font-weight: bold;\n"
"font-size: 12pt;")
        self.reports_add_btn.setIcon(icon11)
        self.reports_add_btn.setIconSize(QSize(25, 25))

        self.verticalLayout_47.addWidget(self.reports_add_btn)

        self.reports_edit_btn = QPushButton(self.widget_30)
        self.reports_edit_btn.setObjectName(u"reports_edit_btn")
        self.reports_edit_btn.setMinimumSize(QSize(150, 30))
        self.reports_edit_btn.setMaximumSize(QSize(150, 30))
        self.reports_edit_btn.setFont(font5)
        self.reports_edit_btn.setStyleSheet(u"background-color: rgb(190,207,187);\n"
"color: rgb(0,0,0);\n"
"border-radius: 5px;\n"
"border: 2px solid #000;\n"
"font-weight: bold;\n"
"font-size: 12pt;")
        self.reports_edit_btn.setIcon(icon11)
        self.reports_edit_btn.setIconSize(QSize(25, 25))

        self.verticalLayout_47.addWidget(self.reports_edit_btn)

        self.reports_del_btn = QPushButton(self.widget_30)
        self.reports_del_btn.setObjectName(u"reports_del_btn")
        self.reports_del_btn.setMinimumSize(QSize(150, 30))
        self.reports_del_btn.setMaximumSize(QSize(150, 30))
        self.reports_del_btn.setFont(font5)
        self.reports_del_btn.setStyleSheet(u"background-color: rgb(190,207,187);\n"
"color: rgb(0,0,0);\n"
"border-radius: 5px;\n"
"border: 2px solid #000;\n"
"font-weight: bold;\n"
"font-size: 12pt;")
        self.reports_del_btn.setIcon(icon11)
        self.reports_del_btn.setIconSize(QSize(25, 25))

        self.verticalLayout_47.addWidget(self.reports_del_btn)

        self.verticalSpacer_19 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_47.addItem(self.verticalSpacer_19)


        self.horizontalLayout_17.addWidget(self.widget_30)


        self.verticalLayout_45.addWidget(self.widget_28)


        self.verticalLayout_7.addWidget(self.reports_controllers)

        self.reports_view = QWidget(self.reports_page)
        self.reports_view.setObjectName(u"reports_view")
        self.reports_view.setFont(font6)
        self.reports_view.setStyleSheet(u"border-radius: 5px;\n"
"background-color:rgb(54, 71, 107); \n"
"border-radius: 5px;\n"
"border: 2px solid #000;\n"
"")
        self.verticalLayout_48 = QVBoxLayout(self.reports_view)
        self.verticalLayout_48.setSpacing(0)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(11, 11, 11, 11)
        self.reports_table = QTableWidget(self.reports_view)
        if (self.reports_table.columnCount() < 6):
            self.reports_table.setColumnCount(6)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem23.setFont(font1);
        self.reports_table.setHorizontalHeaderItem(0, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem24.setFont(font1);
        self.reports_table.setHorizontalHeaderItem(1, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem25.setFont(font1);
        self.reports_table.setHorizontalHeaderItem(2, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        __qtablewidgetitem26.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem26.setFont(font1);
        self.reports_table.setHorizontalHeaderItem(3, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        __qtablewidgetitem27.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem27.setFont(font1);
        self.reports_table.setHorizontalHeaderItem(4, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        __qtablewidgetitem28.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem28.setFont(font1);
        self.reports_table.setHorizontalHeaderItem(5, __qtablewidgetitem28)
        self.reports_table.setObjectName(u"reports_table")
        self.reports_table.setFont(font6)
        self.reports_table.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.reports_table.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.reports_table.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)

        self.verticalLayout_48.addWidget(self.reports_table)


        self.verticalLayout_7.addWidget(self.reports_view)

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
        if (self.reports_list_table.columnCount() < 4):
            self.reports_list_table.setColumnCount(4)
        __qtablewidgetitem29 = QTableWidgetItem()
        __qtablewidgetitem29.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem29.setFont(font1);
        self.reports_list_table.setHorizontalHeaderItem(0, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        __qtablewidgetitem30.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem30.setFont(font1);
        self.reports_list_table.setHorizontalHeaderItem(1, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        __qtablewidgetitem31.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem31.setFont(font1);
        self.reports_list_table.setHorizontalHeaderItem(2, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        __qtablewidgetitem32.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem32.setFont(font1);
        self.reports_list_table.setHorizontalHeaderItem(3, __qtablewidgetitem32)
        self.reports_list_table.setObjectName(u"reports_list_table")
        self.reports_list_table.setFont(font6)
        self.reports_list_table.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.reports_list_table.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.reports_list_table.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)

        self.verticalLayout_24.addWidget(self.reports_list_table)


        self.verticalLayout_29.addWidget(self.reports_list_view)

        self.main_pages.addWidget(self.reports_list_page)

        self.verticalLayout_2.addWidget(self.main_pages)


        self.horizontalLayout.addWidget(self.main)


        self.verticalLayout_16.addWidget(self.container)

        self.popupWidget = QCustomSlideMenu(self.adminWidget)
        self.popupWidget.setObjectName(u"popupWidget")
        self.popupWidget.setMinimumSize(QSize(800, 0))
        self.popupWidget.setMaximumSize(QSize(800, 500))
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
        self.verticalLayout_9.setContentsMargins(10, 10, 10, 10)
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

        self.admins_exit_btn = QPushButton(self.head_admins)
        self.admins_exit_btn.setObjectName(u"admins_exit_btn")
        self.admins_exit_btn.setMaximumSize(QSize(30, 30))
        self.admins_exit_btn.setIcon(icon2)
        self.admins_exit_btn.setIconSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.admins_exit_btn)


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
        self.verticalLayout_10.setSpacing(5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(10, 10, 10, 10)
        self.head_teachers = QWidget(self.teachers_popup)
        self.head_teachers.setObjectName(u"head_teachers")
        self.head_teachers.setMaximumSize(QSize(16777215, 35))
        self.head_teachers.setStyleSheet(u"")
        self.horizontalLayout_4 = QHBoxLayout(self.head_teachers)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(5, 0, 5, 0)
        self.teachers_label = QLabel(self.head_teachers)
        self.teachers_label.setObjectName(u"teachers_label")
        self.teachers_label.setFont(font1)

        self.horizontalLayout_4.addWidget(self.teachers_label)

        self.horizontalSpacer_3 = QSpacerItem(484, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.teachers_exit_btn = QPushButton(self.head_teachers)
        self.teachers_exit_btn.setObjectName(u"teachers_exit_btn")
        self.teachers_exit_btn.setMaximumSize(QSize(30, 30))
        self.teachers_exit_btn.setIcon(icon2)
        self.teachers_exit_btn.setIconSize(QSize(30, 30))

        self.horizontalLayout_4.addWidget(self.teachers_exit_btn)


        self.verticalLayout_10.addWidget(self.head_teachers)

        self.body_teachers = QWidget(self.teachers_popup)
        self.body_teachers.setObjectName(u"body_teachers")
        self.body_teachers.setStyleSheet(u"")
        self.teacher_id_text = QLineEdit(self.body_teachers)
        self.teacher_id_text.setObjectName(u"teacher_id_text")
        self.teacher_id_text.setEnabled(True)
        self.teacher_id_text.setGeometry(QRect(20, 100, 351, 31))
        self.teacher_id_text.setFont(font7)
        self.teacher_id_text.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.teacher_name_text = QLineEdit(self.body_teachers)
        self.teacher_name_text.setObjectName(u"teacher_name_text")
        self.teacher_name_text.setGeometry(QRect(20, 200, 351, 31))
        self.teacher_name_text.setFont(font7)
        self.teacher_name_text.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.teacher_address_text = QLineEdit(self.body_teachers)
        self.teacher_address_text.setObjectName(u"teacher_address_text")
        self.teacher_address_text.setGeometry(QRect(20, 300, 351, 31))
        self.teacher_address_text.setFont(font7)
        self.teacher_address_text.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.teacher_id_label = QLabel(self.body_teachers)
        self.teacher_id_label.setObjectName(u"teacher_id_label")
        self.teacher_id_label.setGeometry(QRect(30, 60, 201, 31))
        self.teacher_id_label.setFont(font1)
        self.teacher_name_label = QLabel(self.body_teachers)
        self.teacher_name_label.setObjectName(u"teacher_name_label")
        self.teacher_name_label.setGeometry(QRect(30, 160, 201, 31))
        self.teacher_name_label.setFont(font1)
        self.teacher_address_label = QLabel(self.body_teachers)
        self.teacher_address_label.setObjectName(u"teacher_address_label")
        self.teacher_address_label.setGeometry(QRect(30, 260, 201, 31))
        self.teacher_address_label.setFont(font1)
        self.teacher_save_btn = QPushButton(self.body_teachers)
        self.teacher_save_btn.setObjectName(u"teacher_save_btn")
        self.teacher_save_btn.setGeometry(QRect(520, 390, 93, 28))
        self.teacher_save_btn.setFont(font8)
        self.teacher_save_btn.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.teacher_refesh_btn = QPushButton(self.body_teachers)
        self.teacher_refesh_btn.setObjectName(u"teacher_refesh_btn")
        self.teacher_refesh_btn.setGeometry(QRect(650, 390, 93, 28))
        self.teacher_refesh_btn.setFont(font8)
        self.teacher_refesh_btn.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.teacher_password_label = QLabel(self.body_teachers)
        self.teacher_password_label.setObjectName(u"teacher_password_label")
        self.teacher_password_label.setGeometry(QRect(410, 60, 201, 31))
        self.teacher_password_label.setFont(font1)
        self.teacher_password_text = QLineEdit(self.body_teachers)
        self.teacher_password_text.setObjectName(u"teacher_password_text")
        self.teacher_password_text.setGeometry(QRect(400, 100, 351, 31))
        self.teacher_password_text.setFont(font7)
        self.teacher_password_text.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.teacher_birth_label = QLabel(self.body_teachers)
        self.teacher_birth_label.setObjectName(u"teacher_birth_label")
        self.teacher_birth_label.setGeometry(QRect(410, 160, 201, 31))
        self.teacher_birth_label.setFont(font1)
        self.teacher_birth_text = QLineEdit(self.body_teachers)
        self.teacher_birth_text.setObjectName(u"teacher_birth_text")
        self.teacher_birth_text.setGeometry(QRect(400, 200, 351, 31))
        self.teacher_birth_text.setFont(font7)
        self.teacher_birth_text.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.teacher_phone_label = QLabel(self.body_teachers)
        self.teacher_phone_label.setObjectName(u"teacher_phone_label")
        self.teacher_phone_label.setGeometry(QRect(410, 260, 201, 31))
        self.teacher_phone_label.setFont(font1)
        self.teacher_phone_text = QLineEdit(self.body_teachers)
        self.teacher_phone_text.setObjectName(u"teacher_phone_text")
        self.teacher_phone_text.setGeometry(QRect(400, 300, 351, 31))
        self.teacher_phone_text.setFont(font7)
        self.teacher_phone_text.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_10.addWidget(self.body_teachers)

        self.popupPages.addWidget(self.teachers_popup)
        self.students_popup = QWidget()
        self.students_popup.setObjectName(u"students_popup")
        self.verticalLayout_12 = QVBoxLayout(self.students_popup)
        self.verticalLayout_12.setSpacing(5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(10, 10, 10, 10)
        self.head_student = QWidget(self.students_popup)
        self.head_student.setObjectName(u"head_student")
        self.head_student.setMaximumSize(QSize(16777215, 35))
        self.head_student.setStyleSheet(u"")
        self.horizontalLayout_5 = QHBoxLayout(self.head_student)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(5, 0, 5, 0)
        self.students_label = QLabel(self.head_student)
        self.students_label.setObjectName(u"students_label")
        self.students_label.setFont(font1)

        self.horizontalLayout_5.addWidget(self.students_label)

        self.horizontalSpacer_4 = QSpacerItem(484, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.students_exit_btn = QPushButton(self.head_student)
        self.students_exit_btn.setObjectName(u"students_exit_btn")
        self.students_exit_btn.setMaximumSize(QSize(30, 30))
        self.students_exit_btn.setIcon(icon2)
        self.students_exit_btn.setIconSize(QSize(30, 30))

        self.horizontalLayout_5.addWidget(self.students_exit_btn)


        self.verticalLayout_12.addWidget(self.head_student)

        self.body_student = QWidget(self.students_popup)
        self.body_student.setObjectName(u"body_student")
        self.body_student.setStyleSheet(u"")
        self.student_id_text = QLineEdit(self.body_student)
        self.student_id_text.setObjectName(u"student_id_text")
        self.student_id_text.setEnabled(True)
        self.student_id_text.setGeometry(QRect(20, 60, 351, 31))
        self.student_id_text.setFont(font7)
        self.student_id_text.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.student_name_text = QLineEdit(self.body_student)
        self.student_name_text.setObjectName(u"student_name_text")
        self.student_name_text.setGeometry(QRect(20, 160, 351, 31))
        self.student_name_text.setFont(font7)
        self.student_name_text.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.student_class_text = QLineEdit(self.body_student)
        self.student_class_text.setObjectName(u"student_class_text")
        self.student_class_text.setGeometry(QRect(20, 360, 351, 31))
        self.student_class_text.setFont(font7)
        self.student_class_text.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.student_id_label = QLabel(self.body_student)
        self.student_id_label.setObjectName(u"student_id_label")
        self.student_id_label.setGeometry(QRect(30, 20, 201, 31))
        self.student_id_label.setFont(font1)
        self.student_name_label = QLabel(self.body_student)
        self.student_name_label.setObjectName(u"student_name_label")
        self.student_name_label.setGeometry(QRect(30, 120, 201, 31))
        self.student_name_label.setFont(font1)
        self.student_class_label = QLabel(self.body_student)
        self.student_class_label.setObjectName(u"student_class_label")
        self.student_class_label.setGeometry(QRect(30, 320, 201, 31))
        self.student_class_label.setFont(font1)
        self.student_save_btn = QPushButton(self.body_student)
        self.student_save_btn.setObjectName(u"student_save_btn")
        self.student_save_btn.setGeometry(QRect(520, 390, 93, 28))
        self.student_save_btn.setFont(font8)
        self.student_save_btn.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.student_refesh_btn = QPushButton(self.body_student)
        self.student_refesh_btn.setObjectName(u"student_refesh_btn")
        self.student_refesh_btn.setGeometry(QRect(650, 390, 93, 28))
        self.student_refesh_btn.setFont(font8)
        self.student_refesh_btn.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.student_phone_label = QLabel(self.body_student)
        self.student_phone_label.setObjectName(u"student_phone_label")
        self.student_phone_label.setGeometry(QRect(410, 20, 201, 31))
        self.student_phone_label.setFont(font1)
        self.student_phone_text = QLineEdit(self.body_student)
        self.student_phone_text.setObjectName(u"student_phone_text")
        self.student_phone_text.setGeometry(QRect(400, 60, 351, 31))
        self.student_phone_text.setFont(font7)
        self.student_phone_text.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.student_address_label = QLabel(self.body_student)
        self.student_address_label.setObjectName(u"student_address_label")
        self.student_address_label.setGeometry(QRect(410, 120, 201, 31))
        self.student_address_label.setFont(font1)
        self.student_address_text = QLineEdit(self.body_student)
        self.student_address_text.setObjectName(u"student_address_text")
        self.student_address_text.setGeometry(QRect(400, 160, 351, 31))
        self.student_address_text.setFont(font7)
        self.student_address_text.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.student_url_text = QLineEdit(self.body_student)
        self.student_url_text.setObjectName(u"student_url_text")
        self.student_url_text.setGeometry(QRect(400, 260, 351, 31))
        self.student_url_text.setFont(font7)
        self.student_url_text.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.student_url_label = QLabel(self.body_student)
        self.student_url_label.setObjectName(u"student_url_label")
        self.student_url_label.setGeometry(QRect(410, 220, 201, 31))
        self.student_url_label.setFont(font1)
        self.student_birth_label = QLabel(self.body_student)
        self.student_birth_label.setObjectName(u"student_birth_label")
        self.student_birth_label.setGeometry(QRect(30, 220, 201, 31))
        self.student_birth_label.setFont(font1)
        self.student_birth_text = QLineEdit(self.body_student)
        self.student_birth_text.setObjectName(u"student_birth_text")
        self.student_birth_text.setGeometry(QRect(20, 260, 351, 31))
        self.student_birth_text.setFont(font7)
        self.student_birth_text.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_12.addWidget(self.body_student)

        self.popupPages.addWidget(self.students_popup)
        self.rooms_popup = QWidget()
        self.rooms_popup.setObjectName(u"rooms_popup")
        self.verticalLayout_13 = QVBoxLayout(self.rooms_popup)
        self.verticalLayout_13.setSpacing(5)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(10, 10, 10, 10)
        self.head_rooms = QWidget(self.rooms_popup)
        self.head_rooms.setObjectName(u"head_rooms")
        self.head_rooms.setMaximumSize(QSize(16777215, 35))
        self.head_rooms.setStyleSheet(u"")
        self.horizontalLayout_6 = QHBoxLayout(self.head_rooms)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 0, 5, 0)
        self.rooms_label = QLabel(self.head_rooms)
        self.rooms_label.setObjectName(u"rooms_label")
        self.rooms_label.setFont(font1)

        self.horizontalLayout_6.addWidget(self.rooms_label)

        self.horizontalSpacer_5 = QSpacerItem(484, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)

        self.rooms_exit_btn = QPushButton(self.head_rooms)
        self.rooms_exit_btn.setObjectName(u"rooms_exit_btn")
        self.rooms_exit_btn.setMaximumSize(QSize(30, 30))
        self.rooms_exit_btn.setIcon(icon2)
        self.rooms_exit_btn.setIconSize(QSize(30, 30))

        self.horizontalLayout_6.addWidget(self.rooms_exit_btn)


        self.verticalLayout_13.addWidget(self.head_rooms)

        self.body_rooms = QWidget(self.rooms_popup)
        self.body_rooms.setObjectName(u"body_rooms")
        self.body_rooms.setStyleSheet(u"")
        self.room_id_text = QLineEdit(self.body_rooms)
        self.room_id_text.setObjectName(u"room_id_text")
        self.room_id_text.setEnabled(True)
        self.room_id_text.setGeometry(QRect(20, 40, 351, 31))
        self.room_id_text.setFont(font7)
        self.room_id_text.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.room_teacher_text = QLineEdit(self.body_rooms)
        self.room_teacher_text.setObjectName(u"room_teacher_text")
        self.room_teacher_text.setGeometry(QRect(20, 140, 351, 31))
        self.room_teacher_text.setFont(font7)
        self.room_teacher_text.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.room_sche_text = QLineEdit(self.body_rooms)
        self.room_sche_text.setObjectName(u"room_sche_text")
        self.room_sche_text.setGeometry(QRect(20, 240, 351, 131))
        self.room_sche_text.setFont(font7)
        self.room_sche_text.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.room_id_label = QLabel(self.body_rooms)
        self.room_id_label.setObjectName(u"room_id_label")
        self.room_id_label.setGeometry(QRect(30, 0, 201, 31))
        self.room_id_label.setFont(font1)
        self.room_teacher_label = QLabel(self.body_rooms)
        self.room_teacher_label.setObjectName(u"room_teacher_label")
        self.room_teacher_label.setGeometry(QRect(30, 100, 201, 31))
        self.room_teacher_label.setFont(font1)
        self.room_sche_label = QLabel(self.body_rooms)
        self.room_sche_label.setObjectName(u"room_sche_label")
        self.room_sche_label.setGeometry(QRect(30, 200, 201, 31))
        self.room_sche_label.setFont(font1)
        self.room_save_btn = QPushButton(self.body_rooms)
        self.room_save_btn.setObjectName(u"room_save_btn")
        self.room_save_btn.setGeometry(QRect(520, 390, 93, 28))
        self.room_save_btn.setFont(font8)
        self.room_save_btn.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.room_refesh_btn = QPushButton(self.body_rooms)
        self.room_refesh_btn.setObjectName(u"room_refesh_btn")
        self.room_refesh_btn.setGeometry(QRect(650, 390, 93, 28))
        self.room_refesh_btn.setFont(font8)
        self.room_refesh_btn.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.room_class_label = QLabel(self.body_rooms)
        self.room_class_label.setObjectName(u"room_class_label")
        self.room_class_label.setGeometry(QRect(410, 100, 201, 31))
        self.room_class_label.setFont(font1)
        self.room_class_text = QLineEdit(self.body_rooms)
        self.room_class_text.setObjectName(u"room_class_text")
        self.room_class_text.setGeometry(QRect(400, 140, 351, 31))
        self.room_class_text.setFont(font7)
        self.room_class_text.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.room_student_num_label = QLabel(self.body_rooms)
        self.room_student_num_label.setObjectName(u"room_student_num_label")
        self.room_student_num_label.setGeometry(QRect(410, 200, 201, 31))
        self.room_student_num_label.setFont(font1)
        self.room_student_num_text = QLineEdit(self.body_rooms)
        self.room_student_num_text.setObjectName(u"room_student_num_text")
        self.room_student_num_text.setGeometry(QRect(400, 240, 351, 31))
        self.room_student_num_text.setFont(font7)
        self.room_student_num_text.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.room_days_text = QLineEdit(self.body_rooms)
        self.room_days_text.setObjectName(u"room_days_text")
        self.room_days_text.setGeometry(QRect(400, 340, 351, 31))
        self.room_days_text.setFont(font7)
        self.room_days_text.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.room_days_label = QLabel(self.body_rooms)
        self.room_days_label.setObjectName(u"room_days_label")
        self.room_days_label.setGeometry(QRect(410, 300, 201, 31))
        self.room_days_label.setFont(font1)
        self.room_name_text = QLineEdit(self.body_rooms)
        self.room_name_text.setObjectName(u"room_name_text")
        self.room_name_text.setGeometry(QRect(400, 40, 351, 31))
        self.room_name_text.setFont(font7)
        self.room_name_text.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.room_name_label = QLabel(self.body_rooms)
        self.room_name_label.setObjectName(u"room_name_label")
        self.room_name_label.setGeometry(QRect(410, 0, 201, 31))
        self.room_name_label.setFont(font1)

        self.verticalLayout_13.addWidget(self.body_rooms)

        self.popupPages.addWidget(self.rooms_popup)
        self.reports_popup = QWidget()
        self.reports_popup.setObjectName(u"reports_popup")
        self.verticalLayout_14 = QVBoxLayout(self.reports_popup)
        self.verticalLayout_14.setSpacing(5)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(10, 10, 10, 10)
        self.head_reports = QWidget(self.reports_popup)
        self.head_reports.setObjectName(u"head_reports")
        self.head_reports.setMaximumSize(QSize(16777215, 35))
        self.head_reports.setStyleSheet(u"")
        self.horizontalLayout_7 = QHBoxLayout(self.head_reports)
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(5, 0, 5, 0)
        self.reports_label = QLabel(self.head_reports)
        self.reports_label.setObjectName(u"reports_label")
        self.reports_label.setFont(font1)

        self.horizontalLayout_7.addWidget(self.reports_label)

        self.horizontalSpacer_6 = QSpacerItem(484, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_6)

        self.reports_exit_btn = QPushButton(self.head_reports)
        self.reports_exit_btn.setObjectName(u"reports_exit_btn")
        self.reports_exit_btn.setMaximumSize(QSize(30, 30))
        self.reports_exit_btn.setIcon(icon2)
        self.reports_exit_btn.setIconSize(QSize(30, 30))

        self.horizontalLayout_7.addWidget(self.reports_exit_btn)


        self.verticalLayout_14.addWidget(self.head_reports)

        self.body_reports = QWidget(self.reports_popup)
        self.body_reports.setObjectName(u"body_reports")
        self.body_reports.setStyleSheet(u"")
        self.reports_id_text = QLineEdit(self.body_reports)
        self.reports_id_text.setObjectName(u"reports_id_text")
        self.reports_id_text.setEnabled(True)
        self.reports_id_text.setGeometry(QRect(30, 100, 351, 31))
        self.reports_id_text.setFont(font7)
        self.reports_id_text.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.reports_student_text = QLineEdit(self.body_reports)
        self.reports_student_text.setObjectName(u"reports_student_text")
        self.reports_student_text.setGeometry(QRect(30, 200, 351, 31))
        self.reports_student_text.setFont(font7)
        self.reports_student_text.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.reports_attend_text = QLineEdit(self.body_reports)
        self.reports_attend_text.setObjectName(u"reports_attend_text")
        self.reports_attend_text.setGeometry(QRect(30, 300, 351, 31))
        self.reports_attend_text.setFont(font7)
        self.reports_attend_text.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.reports_id_label = QLabel(self.body_reports)
        self.reports_id_label.setObjectName(u"reports_id_label")
        self.reports_id_label.setGeometry(QRect(40, 60, 201, 31))
        self.reports_id_label.setFont(font1)
        self.reports_student_label = QLabel(self.body_reports)
        self.reports_student_label.setObjectName(u"reports_student_label")
        self.reports_student_label.setGeometry(QRect(40, 160, 201, 31))
        self.reports_student_label.setFont(font1)
        self.reports_attend_label = QLabel(self.body_reports)
        self.reports_attend_label.setObjectName(u"reports_attend_label")
        self.reports_attend_label.setGeometry(QRect(40, 260, 201, 31))
        self.reports_attend_label.setFont(font1)
        self.reports_save_btn = QPushButton(self.body_reports)
        self.reports_save_btn.setObjectName(u"reports_save_btn")
        self.reports_save_btn.setGeometry(QRect(520, 390, 93, 28))
        self.reports_save_btn.setFont(font8)
        self.reports_save_btn.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.reports_refesh_btn = QPushButton(self.body_reports)
        self.reports_refesh_btn.setObjectName(u"reports_refesh_btn")
        self.reports_refesh_btn.setGeometry(QRect(650, 390, 93, 28))
        self.reports_refesh_btn.setFont(font8)
        self.reports_refesh_btn.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.reports_room_text = QLineEdit(self.body_reports)
        self.reports_room_text.setObjectName(u"reports_room_text")
        self.reports_room_text.setGeometry(QRect(400, 200, 351, 31))
        self.reports_room_text.setFont(font7)
        self.reports_room_text.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.reports_date_label = QLabel(self.body_reports)
        self.reports_date_label.setObjectName(u"reports_date_label")
        self.reports_date_label.setGeometry(QRect(410, 60, 201, 31))
        self.reports_date_label.setFont(font1)
        self.reports_room_label = QLabel(self.body_reports)
        self.reports_room_label.setObjectName(u"reports_room_label")
        self.reports_room_label.setGeometry(QRect(410, 160, 201, 31))
        self.reports_room_label.setFont(font1)
        self.reports_note_label = QLabel(self.body_reports)
        self.reports_note_label.setObjectName(u"reports_note_label")
        self.reports_note_label.setGeometry(QRect(410, 260, 201, 31))
        self.reports_note_label.setFont(font1)
        self.reports_date_text = QLineEdit(self.body_reports)
        self.reports_date_text.setObjectName(u"reports_date_text")
        self.reports_date_text.setEnabled(False)
        self.reports_date_text.setGeometry(QRect(400, 100, 351, 31))
        self.reports_date_text.setFont(font7)
        self.reports_date_text.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.reports_note_text = QLineEdit(self.body_reports)
        self.reports_note_text.setObjectName(u"reports_note_text")
        self.reports_note_text.setGeometry(QRect(400, 300, 351, 31))
        self.reports_note_text.setFont(font7)
        self.reports_note_text.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_14.addWidget(self.body_reports)

        self.popupPages.addWidget(self.reports_popup)
        self.reports_list_popup = QWidget()
        self.reports_list_popup.setObjectName(u"reports_list_popup")
        self.verticalLayout_15 = QVBoxLayout(self.reports_list_popup)
        self.verticalLayout_15.setSpacing(5)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.head_reports_list = QWidget(self.reports_list_popup)
        self.head_reports_list.setObjectName(u"head_reports_list")
        self.head_reports_list.setMaximumSize(QSize(16777215, 35))
        self.head_reports_list.setStyleSheet(u"")
        self.horizontalLayout_8 = QHBoxLayout(self.head_reports_list)
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(5, 0, 5, 0)
        self.reports_list_label = QLabel(self.head_reports_list)
        self.reports_list_label.setObjectName(u"reports_list_label")
        self.reports_list_label.setFont(font1)

        self.horizontalLayout_8.addWidget(self.reports_list_label)

        self.horizontalSpacer_7 = QSpacerItem(484, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_7)

        self.reports_list_exit_btn = QPushButton(self.head_reports_list)
        self.reports_list_exit_btn.setObjectName(u"reports_list_exit_btn")
        self.reports_list_exit_btn.setMaximumSize(QSize(30, 30))
        self.reports_list_exit_btn.setIcon(icon2)
        self.reports_list_exit_btn.setIconSize(QSize(30, 30))

        self.horizontalLayout_8.addWidget(self.reports_list_exit_btn)


        self.verticalLayout_15.addWidget(self.head_reports_list)

        self.body_reports_list = QWidget(self.reports_list_popup)
        self.body_reports_list.setObjectName(u"body_reports_list")
        self.body_reports_list.setStyleSheet(u"")
        self.reports_list_id_text = QLineEdit(self.body_reports_list)
        self.reports_list_id_text.setObjectName(u"reports_list_id_text")
        self.reports_list_id_text.setEnabled(True)
        self.reports_list_id_text.setGeometry(QRect(20, 140, 350, 30))
        self.reports_list_id_text.setFont(font7)
        self.reports_list_id_text.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.reports_list_class_text = QLineEdit(self.body_reports_list)
        self.reports_list_class_text.setObjectName(u"reports_list_class_text")
        self.reports_list_class_text.setGeometry(QRect(390, 140, 350, 30))
        self.reports_list_class_text.setFont(font7)
        self.reports_list_class_text.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.reports_list_id_label = QLabel(self.body_reports_list)
        self.reports_list_id_label.setObjectName(u"reports_list_id_label")
        self.reports_list_id_label.setGeometry(QRect(30, 100, 240, 30))
        self.reports_list_id_label.setFont(font1)
        self.reports_list_class_label = QLabel(self.body_reports_list)
        self.reports_list_class_label.setObjectName(u"reports_list_class_label")
        self.reports_list_class_label.setGeometry(QRect(400, 100, 200, 30))
        self.reports_list_class_label.setFont(font1)
        self.reports_list_save_btn = QPushButton(self.body_reports_list)
        self.reports_list_save_btn.setObjectName(u"reports_list_save_btn")
        self.reports_list_save_btn.setGeometry(QRect(520, 390, 93, 28))
        self.reports_list_save_btn.setFont(font8)
        self.reports_list_save_btn.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.reports_list_refesh_btn = QPushButton(self.body_reports_list)
        self.reports_list_refesh_btn.setObjectName(u"reports_list_refesh_btn")
        self.reports_list_refesh_btn.setGeometry(QRect(650, 390, 93, 28))
        self.reports_list_refesh_btn.setFont(font8)
        self.reports_list_refesh_btn.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.reports_list_student_text = QLineEdit(self.body_reports_list)
        self.reports_list_student_text.setObjectName(u"reports_list_student_text")
        self.reports_list_student_text.setGeometry(QRect(390, 240, 350, 30))
        self.reports_list_student_text.setFont(font7)
        self.reports_list_student_text.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.reports_list_count_label = QLabel(self.body_reports_list)
        self.reports_list_count_label.setObjectName(u"reports_list_count_label")
        self.reports_list_count_label.setGeometry(QRect(30, 200, 200, 30))
        self.reports_list_count_label.setFont(font1)
        self.reports_list_student_label = QLabel(self.body_reports_list)
        self.reports_list_student_label.setObjectName(u"reports_list_student_label")
        self.reports_list_student_label.setGeometry(QRect(400, 200, 200, 30))
        self.reports_list_student_label.setFont(font1)
        self.reports_list_count_text = QLineEdit(self.body_reports_list)
        self.reports_list_count_text.setObjectName(u"reports_list_count_text")
        self.reports_list_count_text.setEnabled(False)
        self.reports_list_count_text.setGeometry(QRect(20, 240, 350, 30))
        self.reports_list_count_text.setFont(font7)
        self.reports_list_count_text.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_15.addWidget(self.body_reports_list)

        self.popupPages.addWidget(self.reports_list_popup)

        self.verticalLayout_8.addWidget(self.popupPages)


        self.verticalLayout_16.addWidget(self.popupWidget)

        Admin.setCentralWidget(self.adminWidget)

        self.retranslateUi(Admin)

        self.main_pages.setCurrentIndex(0)
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
        ___qtablewidgetitem = self.admins_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Admin", u"M\u00e3 Qu\u1ea3n tr\u1ecb vi\u00ean", None));
        ___qtablewidgetitem1 = self.admins_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Admin", u"T\u00e0i kho\u1ea3n", None));
        ___qtablewidgetitem2 = self.admins_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Admin", u"M\u1eadt kh\u1ea9u", None));
        self.teachers_name_label.setText(QCoreApplication.translate("Admin", u"GI\u1ea2NG VI\u00caN", None))
        self.teachers_input.setInputMask("")
        self.teachers_input.setText("")
        self.teachers_search_btn.setText(QCoreApplication.translate("Admin", u"T\u00ecm ki\u1ebfm", None))
        self.teachers_add_btn.setText(QCoreApplication.translate("Admin", u"Th\u00eam", None))
        self.teachers_edit_btn.setText(QCoreApplication.translate("Admin", u"S\u1eeda", None))
        self.teachers_del_btn.setText(QCoreApplication.translate("Admin", u"X\u00f3a", None))
        ___qtablewidgetitem3 = self.teachers_table.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Admin", u"M\u00e3 Gi\u1ea3ng vi\u00ean", None));
        ___qtablewidgetitem4 = self.teachers_table.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Admin", u"T\u00ean Gi\u1ea3ng vi\u00ean", None));
        ___qtablewidgetitem5 = self.teachers_table.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Admin", u"Ng\u00e0y sinh", None));
        ___qtablewidgetitem6 = self.teachers_table.horizontalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Admin", u"\u0110\u1ecba ch\u1ec9", None));
        ___qtablewidgetitem7 = self.teachers_table.horizontalHeaderItem(4)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Admin", u"M\u1eadt kh\u1ea9u", None));
        ___qtablewidgetitem8 = self.teachers_table.horizontalHeaderItem(5)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Admin", u"S\u1ed1 \u0111i\u1ec7n tho\u1ea1i", None));
        self.students_name_label.setText(QCoreApplication.translate("Admin", u"SINH VI\u00caN", None))
        self.students_input.setInputMask("")
        self.students_input.setText("")
        self.students_search_btn.setText(QCoreApplication.translate("Admin", u"T\u00ecm ki\u1ebfm", None))
        self.students_add_btn.setText(QCoreApplication.translate("Admin", u"Th\u00eam", None))
        self.students_edit_btn.setText(QCoreApplication.translate("Admin", u"S\u1eeda", None))
        self.students_del_btn.setText(QCoreApplication.translate("Admin", u"X\u00f3a", None))
        ___qtablewidgetitem9 = self.students_table.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Admin", u"M\u00e3 Sinh vi\u00ean", None));
        ___qtablewidgetitem10 = self.students_table.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Admin", u"T\u00ean Sinh vi\u00ean", None));
        ___qtablewidgetitem11 = self.students_table.horizontalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Admin", u"Ng\u00e0y sinh", None));
        ___qtablewidgetitem12 = self.students_table.horizontalHeaderItem(3)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Admin", u"L\u1edbp qu\u1ea3n l\u00fd", None));
        ___qtablewidgetitem13 = self.students_table.horizontalHeaderItem(4)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Admin", u"\u0110\u1ecba ch\u1ec9", None));
        ___qtablewidgetitem14 = self.students_table.horizontalHeaderItem(5)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Admin", u"URL \u1ea3nh", None));
        ___qtablewidgetitem15 = self.students_table.horizontalHeaderItem(6)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("Admin", u"S\u1ed1 \u0111i\u1ec7n tho\u1ea1i", None));
        self.rooms_name_label.setText(QCoreApplication.translate("Admin", u"L\u1edaP H\u1eccC", None))
        self.rooms_input.setInputMask("")
        self.rooms_input.setText("")
        self.rooms_search_btn.setText(QCoreApplication.translate("Admin", u"T\u00ecm ki\u1ebfm", None))
        self.rooms_add_btn.setText(QCoreApplication.translate("Admin", u"Th\u00eam", None))
        self.rooms_edit_btn.setText(QCoreApplication.translate("Admin", u"S\u1eeda", None))
        self.rooms_del_btn.setText(QCoreApplication.translate("Admin", u"X\u00f3a", None))
        ___qtablewidgetitem16 = self.rooms_table.horizontalHeaderItem(0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("Admin", u"M\u00e3 L\u1edbp", None));
        ___qtablewidgetitem17 = self.rooms_table.horizontalHeaderItem(1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("Admin", u"T\u00ean H\u1ecdc ph\u1ea7n", None));
        ___qtablewidgetitem18 = self.rooms_table.horizontalHeaderItem(2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("Admin", u"M\u00e3 Gi\u00e1o vi\u00ean", None));
        ___qtablewidgetitem19 = self.rooms_table.horizontalHeaderItem(3)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("Admin", u"L\u1ecbch h\u1ecdc", None));
        ___qtablewidgetitem20 = self.rooms_table.horizontalHeaderItem(4)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("Admin", u"Ph\u00f2ng h\u1ecdc", None));
        ___qtablewidgetitem21 = self.rooms_table.horizontalHeaderItem(5)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("Admin", u"S\u1ed1 l\u01b0\u1ee3ng Sinh vi\u00ean", None));
        ___qtablewidgetitem22 = self.rooms_table.horizontalHeaderItem(6)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("Admin", u"S\u1ed1 bu\u1ed5i", None));
        self.reports_name_label.setText(QCoreApplication.translate("Admin", u"B\u00c1O C\u00c1O SINH VI\u00caN", None))
        self.reports_input.setInputMask("")
        self.reports_input.setText("")
        self.reports_search_btn.setText(QCoreApplication.translate("Admin", u"T\u00ecm ki\u1ebfm", None))
        self.reports_add_btn.setText(QCoreApplication.translate("Admin", u"Th\u00eam", None))
        self.reports_edit_btn.setText(QCoreApplication.translate("Admin", u"S\u1eeda", None))
        self.reports_del_btn.setText(QCoreApplication.translate("Admin", u"X\u00f3a", None))
        ___qtablewidgetitem23 = self.reports_table.horizontalHeaderItem(0)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("Admin", u"M\u00e3 B\u00e1o c\u00e1o", None));
        ___qtablewidgetitem24 = self.reports_table.horizontalHeaderItem(1)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("Admin", u"Ng\u00e0y B\u00e1o c\u00e1o", None));
        ___qtablewidgetitem25 = self.reports_table.horizontalHeaderItem(2)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("Admin", u"M\u00e3 Sinh vi\u00ean", None));
        ___qtablewidgetitem26 = self.reports_table.horizontalHeaderItem(3)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("Admin", u"M\u00e3 L\u1edbp", None));
        ___qtablewidgetitem27 = self.reports_table.horizontalHeaderItem(4)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("Admin", u"\u0110i\u1ec3m danh", None));
        ___qtablewidgetitem28 = self.reports_table.horizontalHeaderItem(5)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("Admin", u"Ghi ch\u00fa", None));
        self.reports_list_name_label.setText(QCoreApplication.translate("Admin", u"DANH S\u00c1CH B\u00c1O C\u00c1O \u0110I\u1ec2M DANH", None))
        self.reports_list_input.setInputMask("")
        self.reports_list_input.setText("")
        self.reports_list_search_btn.setText(QCoreApplication.translate("Admin", u"T\u00ecm ki\u1ebfm", None))
        self.reports_list_add_btn.setText(QCoreApplication.translate("Admin", u"Th\u00eam", None))
        self.reports_list_edit_btn.setText(QCoreApplication.translate("Admin", u"S\u1eeda", None))
        self.reports_list_del_btn.setText(QCoreApplication.translate("Admin", u"X\u00f3a", None))
        ___qtablewidgetitem29 = self.reports_list_table.horizontalHeaderItem(0)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("Admin", u"M\u00e3 Danh s\u00e1ch", None));
        ___qtablewidgetitem30 = self.reports_list_table.horizontalHeaderItem(1)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("Admin", u"M\u00e3 L\u1edbp", None));
        ___qtablewidgetitem31 = self.reports_list_table.horizontalHeaderItem(2)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("Admin", u"M\u00e3 Sinh vi\u00ean", None));
        ___qtablewidgetitem32 = self.reports_list_table.horizontalHeaderItem(3)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("Admin", u"T\u00ednh \u0111i\u1ec3m danh", None));
        self.admin_label.setText(QCoreApplication.translate("Admin", u"TH\u00d4NG TIN QU\u1ea2N TR\u1eca VI\u00caN", None))
        self.admins_exit_btn.setText("")
        self.admin_id_label.setText(QCoreApplication.translate("Admin", u"M\u00e3 Qu\u1ea3n tr\u1ecb vi\u00ean", None))
        self.admin_username_label.setText(QCoreApplication.translate("Admin", u"T\u00e0i kho\u1ea3n", None))
        self.admin_password_label.setText(QCoreApplication.translate("Admin", u"M\u1eadt kh\u1ea9u", None))
        self.admin_save_btn.setText(QCoreApplication.translate("Admin", u"L\u01b0u", None))
        self.admin_refesh_btn.setText(QCoreApplication.translate("Admin", u"L\u00e0m m\u1edbi", None))
        self.teachers_label.setText(QCoreApplication.translate("Admin", u"TH\u00d4NG TIN GI\u1ea2NG VI\u00caN", None))
        self.teachers_exit_btn.setText("")
        self.teacher_id_label.setText(QCoreApplication.translate("Admin", u"M\u00e3 gi\u1ea3ng vi\u00ean", None))
        self.teacher_name_label.setText(QCoreApplication.translate("Admin", u"T\u00ean gi\u1ea3ng vi\u00ean", None))
        self.teacher_address_label.setText(QCoreApplication.translate("Admin", u"\u0110\u1ecba ch\u1ec9", None))
        self.teacher_save_btn.setText(QCoreApplication.translate("Admin", u"L\u01b0u", None))
        self.teacher_refesh_btn.setText(QCoreApplication.translate("Admin", u"L\u00e0m m\u1edbi", None))
        self.teacher_password_label.setText(QCoreApplication.translate("Admin", u"M\u1eadt kh\u1ea9u", None))
        self.teacher_birth_label.setText(QCoreApplication.translate("Admin", u"Ng\u00e0y sinh", None))
        self.teacher_birth_text.setText("")
        self.teacher_phone_label.setText(QCoreApplication.translate("Admin", u"S\u1ed1 \u0111i\u1ec7n tho\u1ea1i", None))
        self.teacher_phone_text.setText("")
        self.students_label.setText(QCoreApplication.translate("Admin", u"TH\u00d4NG TIN SINH VI\u00caN", None))
        self.students_exit_btn.setText("")
        self.student_id_label.setText(QCoreApplication.translate("Admin", u"M\u00e3 sinh vi\u00ean", None))
        self.student_name_label.setText(QCoreApplication.translate("Admin", u"T\u00ean sinh vi\u00ean", None))
        self.student_class_label.setText(QCoreApplication.translate("Admin", u"L\u1edbp qu\u1ea3n l\u00fd", None))
        self.student_save_btn.setText(QCoreApplication.translate("Admin", u"L\u01b0u", None))
        self.student_refesh_btn.setText(QCoreApplication.translate("Admin", u"L\u00e0m m\u1edbi", None))
        self.student_phone_label.setText(QCoreApplication.translate("Admin", u"S\u1ed1 \u0111i\u1ec7n tho\u1ea1i", None))
        self.student_address_label.setText(QCoreApplication.translate("Admin", u"\u0110\u1ecba ch\u1ec9", None))
        self.student_address_text.setText("")
        self.student_url_label.setText(QCoreApplication.translate("Admin", u"URL \u1ea2nh", None))
        self.student_birth_label.setText(QCoreApplication.translate("Admin", u"Ng\u00e0y sinh", None))
        self.rooms_label.setText(QCoreApplication.translate("Admin", u"TH\u00d4NG TIN L\u1edaP H\u1eccC", None))
        self.rooms_exit_btn.setText("")
        self.room_id_label.setText(QCoreApplication.translate("Admin", u"M\u00e3 l\u1edbp", None))
        self.room_teacher_label.setText(QCoreApplication.translate("Admin", u"M\u00e3 gi\u00e1o vi\u00ean", None))
        self.room_sche_label.setText(QCoreApplication.translate("Admin", u"L\u1ecbch h\u1ecdc", None))
        self.room_save_btn.setText(QCoreApplication.translate("Admin", u"L\u01b0u", None))
        self.room_refesh_btn.setText(QCoreApplication.translate("Admin", u"L\u00e0m m\u1edbi", None))
        self.room_class_label.setText(QCoreApplication.translate("Admin", u"Ph\u00f2ng h\u1ecdc", None))
        self.room_student_num_label.setText(QCoreApplication.translate("Admin", u"S\u1ed1 l\u01b0\u1ee3ng sinh vi\u00ean", None))
        self.room_student_num_text.setText("")
        self.room_days_label.setText(QCoreApplication.translate("Admin", u"S\u1ed1 bu\u1ed5i", None))
        self.room_name_label.setText(QCoreApplication.translate("Admin", u"T\u00ean m\u00f4n h\u1ecdc", None))
        self.reports_label.setText(QCoreApplication.translate("Admin", u"TH\u00d4NG TIN \u0110I\u1ec2M DANH", None))
        self.reports_exit_btn.setText("")
        self.reports_id_label.setText(QCoreApplication.translate("Admin", u"M\u00e3 B\u00e1o c\u00e1o", None))
        self.reports_student_label.setText(QCoreApplication.translate("Admin", u"M\u00e3 sinh vi\u00ean", None))
        self.reports_attend_label.setText(QCoreApplication.translate("Admin", u"\u0110i\u1ec3m danh", None))
        self.reports_save_btn.setText(QCoreApplication.translate("Admin", u"L\u01b0u", None))
        self.reports_refesh_btn.setText(QCoreApplication.translate("Admin", u"L\u00e0m m\u1edbi", None))
        self.reports_date_label.setText(QCoreApplication.translate("Admin", u"Ng\u00e0y B\u00e1o c\u00e1o", None))
        self.reports_room_label.setText(QCoreApplication.translate("Admin", u"M\u00e3 l\u1edbp", None))
        self.reports_note_label.setText(QCoreApplication.translate("Admin", u"Ghi chu", None))
        self.reports_list_label.setText(QCoreApplication.translate("Admin", u"TH\u00d4NG TIN B\u00c1O C\u00c1O \u0110I\u1ec2M DANH", None))
        self.reports_list_exit_btn.setText("")
        self.reports_list_id_label.setText(QCoreApplication.translate("Admin", u"M\u00e3 b\u00e1o c\u00e1o \u0111i\u1ec3m danh", None))
        self.reports_list_class_label.setText(QCoreApplication.translate("Admin", u"M\u00e3 l\u1edbp", None))
        self.reports_list_save_btn.setText(QCoreApplication.translate("Admin", u"L\u01b0u", None))
        self.reports_list_refesh_btn.setText(QCoreApplication.translate("Admin", u"L\u00e0m m\u1edbi", None))
        self.reports_list_count_label.setText(QCoreApplication.translate("Admin", u"S\u1ed1 l\u1ea7n \u0111i\u1ec3m danh", None))
        self.reports_list_student_label.setText(QCoreApplication.translate("Admin", u"M\u00e3 sinh vi\u00ean", None))
        pass
    # retranslateUi

