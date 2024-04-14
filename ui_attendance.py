# -*- coding: utf-8 -*-

################################################################################
<<<<<<< HEAD
## Form generated from reading UI file 'attendancezBMygb.ui'
=======
## Form generated from reading UI file 'attendanceDJFEEF.ui'
>>>>>>> 21d62066e8deaec4a75b5f673663c02766886afd
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import resources.resources

class Ui_Attendance(object):
    def setupUi(self, Attendance):
        if not Attendance.objectName():
            Attendance.setObjectName(u"Attendance")
        Attendance.resize(1333, 819)
        font = QFont()
        font.setFamily(u"Cambria")
        Attendance.setFont(font)
        Attendance.setWindowTitle(u"Attendance")
        self.attendanceWidget = QWidget(Attendance)
        self.attendanceWidget.setObjectName(u"attendanceWidget")
        self.verticalLayout_19 = QVBoxLayout(self.attendanceWidget)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.panel_window = QWidget(self.attendanceWidget)
        self.panel_window.setObjectName(u"panel_window")
        self.panel_window.setMinimumSize(QSize(0, 40))
        self.panel_window.setMaximumSize(QSize(16777215, 40))
        self.panel_window.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"border-top-right-radius: 5px;\n"
"border-top-left-radius: 5px;")
        self.horizontalLayout_2 = QHBoxLayout(self.panel_window)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.icon_attendance = QLabel(self.panel_window)
        self.icon_attendance.setObjectName(u"icon_attendance")
        self.icon_attendance.setMinimumSize(QSize(30, 30))
        self.icon_attendance.setMaximumSize(QSize(30, 30))
        self.icon_attendance.setPixmap(QPixmap(u":/apps/apps/logo_app.png"))
        self.icon_attendance.setScaledContents(True)
        self.icon_attendance.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.icon_attendance)

        self.name_attendance = QLabel(self.panel_window)
        self.name_attendance.setObjectName(u"name_attendance")
        font1 = QFont()
        font1.setFamily(u"Cascadia Code")
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setWeight(75)
        self.name_attendance.setFont(font1)
        self.name_attendance.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.name_attendance.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.name_attendance)

        self.horizontalSpacer_2 = QSpacerItem(1017, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.attendance_minimize_btn = QPushButton(self.panel_window)
        self.attendance_minimize_btn.setObjectName(u"attendance_minimize_btn")
        self.attendance_minimize_btn.setMinimumSize(QSize(25, 25))
        self.attendance_minimize_btn.setMaximumSize(QSize(25, 25))
        icon = QIcon()
        icon.addFile(u":/icon-EC8482/EC8482/minus-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.attendance_minimize_btn.setIcon(icon)
        self.attendance_minimize_btn.setIconSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.attendance_minimize_btn)

        self.attendance_expand_btn = QPushButton(self.panel_window)
        self.attendance_expand_btn.setObjectName(u"attendance_expand_btn")
        self.attendance_expand_btn.setMinimumSize(QSize(25, 25))
        self.attendance_expand_btn.setMaximumSize(QSize(25, 25))
        icon1 = QIcon()
        icon1.addFile(u":/icon-EC8482/EC8482/octagon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.attendance_expand_btn.setIcon(icon1)
        self.attendance_expand_btn.setIconSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.attendance_expand_btn)

        self.attendance_exit_btn = QPushButton(self.panel_window)
        self.attendance_exit_btn.setObjectName(u"attendance_exit_btn")
        self.attendance_exit_btn.setMinimumSize(QSize(25, 25))
        self.attendance_exit_btn.setMaximumSize(QSize(25, 25))
        icon2 = QIcon()
        icon2.addFile(u":/icon-EC8482/EC8482/x-octagon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.attendance_exit_btn.setIcon(icon2)
        self.attendance_exit_btn.setIconSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.attendance_exit_btn)


        self.verticalLayout_19.addWidget(self.panel_window)

        self.container = QWidget(self.attendanceWidget)
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
        self.menu.setMaximumSize(QSize(500, 16777215))
        self.menu.setStyleSheet(u"background-color:rgb(223,229,219);\n"
"border-radius: 9px;\n"
"")
        self.verticalLayout_11 = QVBoxLayout(self.menu)
        self.verticalLayout_11.setSpacing(1)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.menu_btn = QPushButton(self.menu)
        self.menu_btn.setObjectName(u"menu_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menu_btn.sizePolicy().hasHeightForWidth())
        self.menu_btn.setSizePolicy(sizePolicy)
        self.menu_btn.setMinimumSize(QSize(40, 50))
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
        self.menu_btn.setIconSize(QSize(30, 30))
        self.menu_btn.setAutoRepeatDelay(300)
        self.menu_btn.setAutoRepeatInterval(100)

        self.verticalLayout_11.addWidget(self.menu_btn)

        self.verticalSpacer = QSpacerItem(20, 160, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_11.addItem(self.verticalSpacer)

        self.remote_controllers = QWidget(self.menu)
        self.remote_controllers.setObjectName(u"remote_controllers")
        self.remote_controllers.setMinimumSize(QSize(0, 210))
        self.verticalLayout = QVBoxLayout(self.remote_controllers)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.home_btn = QPushButton(self.remote_controllers)
        self.home_btn.setObjectName(u"home_btn")
        self.home_btn.setMinimumSize(QSize(0, 50))
        self.home_btn.setFont(font2)
        self.home_btn.setStyleSheet(u"margin: 4px 4px 4px 4px;\n"
"background-color:rgb(188,203,234);\n"
"border-radius:9px;\n"
"border: 2px solid #000;\n"
"font-size: 12pt;\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/icon-dark/icon-dark/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.home_btn.setIcon(icon4)
        self.home_btn.setIconSize(QSize(30, 30))

        self.verticalLayout.addWidget(self.home_btn)

        self.recognize_btn = QPushButton(self.remote_controllers)
        self.recognize_btn.setObjectName(u"recognize_btn")
        self.recognize_btn.setMinimumSize(QSize(0, 50))
        self.recognize_btn.setFont(font2)
        self.recognize_btn.setStyleSheet(u"margin: 4px 4px 4px 4px;\n"
"background-color:rgb(188,203,234);\n"
"border-radius:9px;\n"
"border: 2px solid #000;\n"
"font-size: 12pt;\n"
"")
        icon5 = QIcon()
        icon5.addFile(u":/icon-dark/icon-dark/user-check.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.recognize_btn.setIcon(icon5)
        self.recognize_btn.setIconSize(QSize(30, 30))

        self.verticalLayout.addWidget(self.recognize_btn)

        self.report_btn = QPushButton(self.remote_controllers)
        self.report_btn.setObjectName(u"report_btn")
        self.report_btn.setMinimumSize(QSize(0, 50))
        self.report_btn.setFont(font2)
        self.report_btn.setStyleSheet(u"margin: 4px 4px 4px 4px;\n"
"background-color:rgb(188,203,234);\n"
"border-radius:9px;\n"
"border: 2px solid #000;\n"
"font-size: 12pt;\n"
"")
        icon6 = QIcon()
        icon6.addFile(u":/icon-dark/icon-dark/file-text.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.report_btn.setIcon(icon6)
        self.report_btn.setIconSize(QSize(30, 30))

        self.verticalLayout.addWidget(self.report_btn)

        self.chart_btn = QPushButton(self.remote_controllers)
        self.chart_btn.setObjectName(u"chart_btn")
        self.chart_btn.setMinimumSize(QSize(0, 50))
        self.chart_btn.setFont(font2)
        self.chart_btn.setStyleSheet(u"margin: 4px 4px 4px 4px;\n"
"background-color:rgb(188,203,234);\n"
"border-radius:9px;\n"
"border: 2px solid #000;\n"
"font-size: 12pt;\n"
"")
        icon7 = QIcon()
        icon7.addFile(u":/icon-dark/icon-dark/pie-chart.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.chart_btn.setIcon(icon7)
        self.chart_btn.setIconSize(QSize(30, 30))

        self.verticalLayout.addWidget(self.chart_btn)


        self.verticalLayout_11.addWidget(self.remote_controllers)

        self.verticalSpacer_2 = QSpacerItem(20, 294, QSizePolicy.Minimum, QSizePolicy.Expanding)

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
        icon8 = QIcon()
        icon8.addFile(u":/icon-dark/icon-dark/log-out.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.logout_btn.setIcon(icon8)
        self.logout_btn.setIconSize(QSize(30, 30))

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
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.verticalLayout_4 = QVBoxLayout(self.home_page)
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(1, 1, 1, 1)
        self.home_controllers = QWidget(self.home_page)
        self.home_controllers.setObjectName(u"home_controllers")
        self.home_controllers.setAutoFillBackground(False)
        self.verticalLayout_12 = QVBoxLayout(self.home_controllers)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.home_name_label = QLabel(self.home_controllers)
        self.home_name_label.setObjectName(u"home_name_label")
        self.home_name_label.setMinimumSize(QSize(0, 30))
        self.home_name_label.setMaximumSize(QSize(16777215, 30))
        font3 = QFont()
        font3.setFamily(u"Cascadia Mono SemiBold")
        font3.setPointSize(20)
        font3.setBold(True)
        font3.setUnderline(False)
        font3.setWeight(75)
        font3.setStrikeOut(False)
        self.home_name_label.setFont(font3)
        self.home_name_label.setLayoutDirection(Qt.LeftToRight)
        self.home_name_label.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"padding-left: 10px;\n"
"font-weight: bold;\n"
"font-size: 20pt;")
        self.home_name_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_12.addWidget(self.home_name_label)

        self.widget_3 = QWidget(self.home_controllers)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(0, 150))
        self.horizontalLayout_4 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.widget_2 = QWidget(self.widget_3)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_13 = QVBoxLayout(self.widget_2)
        self.verticalLayout_13.setSpacing(5)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(7, 7, 7, 7)
        self.home_class_input = QLineEdit(self.widget_2)
        self.home_class_input.setObjectName(u"home_class_input")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.home_class_input.sizePolicy().hasHeightForWidth())
        self.home_class_input.setSizePolicy(sizePolicy1)
        self.home_class_input.setMinimumSize(QSize(300, 30))
        font4 = QFont()
        font4.setFamily(u"Cascadia Code")
        font4.setPointSize(10)
        self.home_class_input.setFont(font4)
        self.home_class_input.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 7px;\n"
"border: 2px solid #000;")

        self.verticalLayout_13.addWidget(self.home_class_input)

        self.verticalSpacer_3 = QSpacerItem(20, 46, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_3)


        self.horizontalLayout_4.addWidget(self.widget_2)

        self.widget = QWidget(self.widget_3)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(150, 0))
        self.verticalLayout_14 = QVBoxLayout(self.widget)
        self.verticalLayout_14.setSpacing(5)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(1, 1, 1, 1)
        self.home_search_btn = QPushButton(self.widget)
        self.home_search_btn.setObjectName(u"home_search_btn")
        self.home_search_btn.setMinimumSize(QSize(150, 30))
        self.home_search_btn.setMaximumSize(QSize(10, 30))
        font5 = QFont()
        font5.setFamily(u"Cascadia Code")
        font5.setPointSize(12)
        font5.setBold(True)
        font5.setWeight(75)
        self.home_search_btn.setFont(font5)
        self.home_search_btn.setStyleSheet(u"background-color: rgb(190,207,187);\n"
"color: rgb(0,0,0);\n"
"border-radius: 5px;\n"
"border: 2px solid #000;\n"
"font-weight: bold;\n"
"font-size: 12pt;")
        self.home_search_btn.setIconSize(QSize(25, 25))

        self.verticalLayout_14.addWidget(self.home_search_btn)

        self.home_train_btn = QPushButton(self.widget)
        self.home_train_btn.setObjectName(u"home_train_btn")
        self.home_train_btn.setMinimumSize(QSize(150, 30))
        self.home_train_btn.setMaximumSize(QSize(150, 30))
        self.home_train_btn.setFont(font5)
        self.home_train_btn.setStyleSheet(u"background-color: rgb(190,207,187);\n"
"color: rgb(0,0,0);\n"
"border-radius: 5px;\n"
"border: 2px solid #000;\n"
"font-weight: bold;\n"
"font-size: 12pt;")
        icon9 = QIcon()
        icon9.addFile(u":/icons/zap.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.home_train_btn.setIcon(icon9)
        self.home_train_btn.setIconSize(QSize(25, 25))

        self.verticalLayout_14.addWidget(self.home_train_btn)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_5)


        self.horizontalLayout_4.addWidget(self.widget)


        self.verticalLayout_12.addWidget(self.widget_3)


        self.verticalLayout_4.addWidget(self.home_controllers)

        self.home_view = QWidget(self.home_page)
        self.home_view.setObjectName(u"home_view")
        font6 = QFont()
        font6.setFamily(u"Cascadia Code")
        self.home_view.setFont(font6)
        self.home_view.setStyleSheet(u"border-radius: 5px;\n"
"background-color:rgb(54, 71, 107); \n"
"border-radius: 5px;\n"
"border: 2px solid #000;\n"
"")
        self.verticalLayout_3 = QVBoxLayout(self.home_view)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.home_table = QTableWidget(self.home_view)
        if (self.home_table.columnCount() < 5):
            self.home_table.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem.setFont(font1);
        __qtablewidgetitem.setBackground(QColor(0, 0, 0));
        self.home_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem1.setFont(font1);
        self.home_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem2.setFont(font1);
        self.home_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem3.setFont(font1);
        self.home_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem4.setFont(font1);
        self.home_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.home_table.setObjectName(u"home_table")
        self.home_table.setFont(font6)
        self.home_table.setStyleSheet(u"border-radius: 5px;\n"
"border: 0px;\n"
"background-color: rgb(255, 255, 255);")
        self.home_table.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.home_table.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)

        self.verticalLayout_3.addWidget(self.home_table)

        self.model_name_label = QLabel(self.home_view)
        self.model_name_label.setObjectName(u"model_name_label")
        self.model_name_label.setMinimumSize(QSize(0, 30))
        font7 = QFont()
        font7.setFamily(u"Cascadia Code")
        font7.setPointSize(11)
        font7.setUnderline(True)
        self.model_name_label.setFont(font7)
        self.model_name_label.setLayoutDirection(Qt.LeftToRight)
        self.model_name_label.setStyleSheet(u"color: rgb(255,255,255);\n"
"\n"
"border-radius: 5px;\n"
"border: 0px solid ;")
        self.model_name_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.model_name_label)


        self.verticalLayout_4.addWidget(self.home_view)

        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 3)
        self.main_pages.addWidget(self.home_page)
        self.recognize_page = QWidget()
        self.recognize_page.setObjectName(u"recognize_page")
        self.verticalLayout_5 = QVBoxLayout(self.recognize_page)
        self.verticalLayout_5.setSpacing(2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(1, 1, 1, 1)
        self.recognize_controllers = QWidget(self.recognize_page)
        self.recognize_controllers.setObjectName(u"recognize_controllers")
        self.verticalLayout_15 = QVBoxLayout(self.recognize_controllers)
        self.verticalLayout_15.setSpacing(5)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(11, 11, 11, 11)
        self.recognize_name_label = QLabel(self.recognize_controllers)
        self.recognize_name_label.setObjectName(u"recognize_name_label")
        self.recognize_name_label.setMinimumSize(QSize(0, 30))
        self.recognize_name_label.setMaximumSize(QSize(16777215, 30))
        self.recognize_name_label.setFont(font3)
        self.recognize_name_label.setLayoutDirection(Qt.LeftToRight)
        self.recognize_name_label.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"padding-left: 10px;\n"
"font-weight: bold;\n"
"font-size: 20pt;")
        self.recognize_name_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_15.addWidget(self.recognize_name_label)

        self.widget_7 = QWidget(self.recognize_controllers)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(1, 1, 1, 1)
        self.widget_5 = QWidget(self.widget_7)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_17 = QVBoxLayout(self.widget_5)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.recognize_img_path_input = QLineEdit(self.widget_5)
        self.recognize_img_path_input.setObjectName(u"recognize_img_path_input")
        self.recognize_img_path_input.setEnabled(False)
        self.recognize_img_path_input.setMinimumSize(QSize(0, 30))
        self.recognize_img_path_input.setFont(font4)
        self.recognize_img_path_input.setStyleSheet(u"\n"
"border-radius: 5px;\n"
"padding-left: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 7px;\n"
"border: 2px solid #000;")
        self.recognize_img_path_input.setFrame(True)
        self.recognize_img_path_input.setEchoMode(QLineEdit.Normal)

        self.verticalLayout_17.addWidget(self.recognize_img_path_input)

        self.recognize_models_box = QComboBox(self.widget_5)
        self.recognize_models_box.setObjectName(u"recognize_models_box")
        self.recognize_models_box.setMinimumSize(QSize(0, 30))
        font8 = QFont()
        font8.setFamily(u"Cascadia Code")
        font8.setPointSize(9)
        self.recognize_models_box.setFont(font8)
        self.recognize_models_box.setLayoutDirection(Qt.LeftToRight)
        self.recognize_models_box.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"padding-right: 20px;")

        self.verticalLayout_17.addWidget(self.recognize_models_box)

        self.widget_4 = QWidget(self.widget_5)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.recognize_tab_1_btn = QPushButton(self.widget_4)
        self.recognize_tab_1_btn.setObjectName(u"recognize_tab_1_btn")
        self.recognize_tab_1_btn.setMaximumSize(QSize(50, 16777215))
        self.recognize_tab_1_btn.setFont(font)
        self.recognize_tab_1_btn.setStyleSheet(u"background-color: rgb(188, 188, 188);\n"
"border-radius: 5px;")

        self.horizontalLayout_6.addWidget(self.recognize_tab_1_btn)

        self.recognize_tab_2_btn = QPushButton(self.widget_4)
        self.recognize_tab_2_btn.setObjectName(u"recognize_tab_2_btn")
        self.recognize_tab_2_btn.setMaximumSize(QSize(50, 16777215))
        self.recognize_tab_2_btn.setFont(font)
        self.recognize_tab_2_btn.setStyleSheet(u"background-color: rgba(188, 188, 188, 100);\n"
"border-radius: 5px;")

        self.horizontalLayout_6.addWidget(self.recognize_tab_2_btn)

        self.recognize_tab_3_btn = QPushButton(self.widget_4)
        self.recognize_tab_3_btn.setObjectName(u"recognize_tab_3_btn")
        self.recognize_tab_3_btn.setMaximumSize(QSize(50, 16777215))
        self.recognize_tab_3_btn.setFont(font)
        self.recognize_tab_3_btn.setStyleSheet(u"background-color: rgba(188, 188, 188, 100);\n"
"border-radius: 5px;")

        self.horizontalLayout_6.addWidget(self.recognize_tab_3_btn)

        self.horizontalSpacer = QSpacerItem(800, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)


        self.verticalLayout_17.addWidget(self.widget_4)


        self.horizontalLayout_5.addWidget(self.widget_5)

        self.widget_6 = QWidget(self.widget_7)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_16 = QVBoxLayout(self.widget_6)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.recognize_open_img_btn = QPushButton(self.widget_6)
        self.recognize_open_img_btn.setObjectName(u"recognize_open_img_btn")
        self.recognize_open_img_btn.setMinimumSize(QSize(150, 30))
        self.recognize_open_img_btn.setFont(font5)
        self.recognize_open_img_btn.setStyleSheet(u"background-color: rgb(190,207,187);\n"
"color: rgb(0,0,0);\n"
"border-radius: 5px;\n"
"border: 2px solid #000;\n"
"font-weight: bold;\n"
"font-size: 12pt;")
        icon10 = QIcon()
        icon10.addFile(u":/icons/crosshair.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.recognize_open_img_btn.setIcon(icon10)
        self.recognize_open_img_btn.setIconSize(QSize(25, 25))

        self.verticalLayout_16.addWidget(self.recognize_open_img_btn)

        self.recognize_guess_btn = QPushButton(self.widget_6)
        self.recognize_guess_btn.setObjectName(u"recognize_guess_btn")
        self.recognize_guess_btn.setMinimumSize(QSize(150, 30))
        self.recognize_guess_btn.setFont(font5)
        self.recognize_guess_btn.setStyleSheet(u"background-color: rgb(190,207,187);\n"
"color: rgb(0,0,0);\n"
"border-radius: 5px;\n"
"border: 2px solid #000;\n"
"font-weight: bold;\n"
"font-size: 12pt;")
        icon11 = QIcon()
        icon11.addFile(u":/icons/smile.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.recognize_guess_btn.setIcon(icon11)
        self.recognize_guess_btn.setIconSize(QSize(25, 25))

        self.verticalLayout_16.addWidget(self.recognize_guess_btn)

        self.recognize_export_btn = QPushButton(self.widget_6)
        self.recognize_export_btn.setObjectName(u"recognize_export_btn")
        self.recognize_export_btn.setMinimumSize(QSize(150, 30))
        self.recognize_export_btn.setFont(font5)
        self.recognize_export_btn.setStyleSheet(u"background-color: rgb(190,207,187);\n"
"color: rgb(0,0,0);\n"
"border-radius: 5px;\n"
"border: 2px solid #000;\n"
"font-weight: bold;\n"
"font-size: 12pt;")
        icon12 = QIcon()
        icon12.addFile(u":/icons/user-check.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.recognize_export_btn.setIcon(icon12)
        self.recognize_export_btn.setIconSize(QSize(25, 25))

        self.verticalLayout_16.addWidget(self.recognize_export_btn)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_4)


        self.horizontalLayout_5.addWidget(self.widget_6)


        self.verticalLayout_15.addWidget(self.widget_7)


        self.verticalLayout_5.addWidget(self.recognize_controllers)

        self.recognize_view = QStackedWidget(self.recognize_page)
        self.recognize_view.setObjectName(u"recognize_view")
        self.recognize_view.setFont(font6)
        self.recognize_view.setStyleSheet(u"border-radius: 5px;\n"
"background-color:rgb(54, 71, 107); \n"
"border-radius: 5px;\n"
"border: 2px solid #000;\n"
"\n"
"")
        self.recognize_image = QWidget()
        self.recognize_image.setObjectName(u"recognize_image")
        self.recognize_image.setStyleSheet(u"border-radius: 5px;")
        self.horizontalLayout_9 = QHBoxLayout(self.recognize_image)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.recognize_input_img_label = QLabel(self.recognize_image)
        self.recognize_input_img_label.setObjectName(u"recognize_input_img_label")
        self.recognize_input_img_label.setFont(font6)
        self.recognize_input_img_label.setStyleSheet(u"background-color: rgb(238, 0, 255);")
        self.recognize_input_img_label.setPixmap(QPixmap(u"../../../Duong/.designer/backup/resources/apps/no_data_found.png"))
        self.recognize_input_img_label.setScaledContents(True)

        self.horizontalLayout_9.addWidget(self.recognize_input_img_label)

        self.recognize_view.addWidget(self.recognize_image)
        self.recognize_detect = QWidget()
        self.recognize_detect.setObjectName(u"recognize_detect")
        self.recognize_detect.setStyleSheet(u"border-radius: 5px;")
        self.horizontalLayout_8 = QHBoxLayout(self.recognize_detect)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.recognize_output_img_label = QLabel(self.recognize_detect)
        self.recognize_output_img_label.setObjectName(u"recognize_output_img_label")
        self.recognize_output_img_label.setFont(font6)
        self.recognize_output_img_label.setStyleSheet(u"background-color: rgb(127, 255, 29);")
        self.recognize_output_img_label.setPixmap(QPixmap(u"../../../Duong/.designer/backup/resources/apps/no_data_found.png"))
        self.recognize_output_img_label.setScaledContents(True)

        self.horizontalLayout_8.addWidget(self.recognize_output_img_label)

        self.recognize_view.addWidget(self.recognize_detect)
        self.recognize_report = QWidget()
        self.recognize_report.setObjectName(u"recognize_report")
        self.recognize_report.setStyleSheet(u"background-color: rgb(44, 49, 58);\n"
"border-radius: 5px;")
        self.verticalLayout_10 = QVBoxLayout(self.recognize_report)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.recognize_table = QTableWidget(self.recognize_report)
        if (self.recognize_table.columnCount() < 2):
            self.recognize_table.setColumnCount(2)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem5.setFont(font1);
        self.recognize_table.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem6.setFont(font1);
        self.recognize_table.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        self.recognize_table.setObjectName(u"recognize_table")
        self.recognize_table.setFont(font6)
        self.recognize_table.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(0, 170, 255);")
        self.recognize_table.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.recognize_table.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.recognize_table.setGridStyle(Qt.SolidLine)
        self.recognize_table.horizontalHeader().setVisible(False)
        self.recognize_table.horizontalHeader().setMinimumSectionSize(49)
        self.recognize_table.horizontalHeader().setProperty("showSortIndicator", False)
        self.recognize_table.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_10.addWidget(self.recognize_table)

        self.widget_9 = QWidget(self.recognize_report)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setMinimumSize(QSize(0, 70))
        self.widget_9.setStyleSheet(u"border: 0px")
        self.recognize_keep_btn = QPushButton(self.widget_9)
        self.recognize_keep_btn.setObjectName(u"recognize_keep_btn")
        self.recognize_keep_btn.setGeometry(QRect(1040, 20, 150, 30))
        self.recognize_keep_btn.setMinimumSize(QSize(150, 30))
        self.recognize_keep_btn.setFont(font5)
        self.recognize_keep_btn.setStyleSheet(u"background-color: rgb(190,207,187);\n"
"color: rgb(0,0,0);\n"
"border-radius: 5px;\n"
"border: 2px solid #000;\n"
"font-weight: bold;\n"
"font-size: 12pt;")
        self.recognize_keep_btn.setIcon(icon12)
        self.recognize_keep_btn.setIconSize(QSize(25, 25))

        self.verticalLayout_10.addWidget(self.widget_9)

        self.recognize_view.addWidget(self.recognize_report)

        self.verticalLayout_5.addWidget(self.recognize_view)

        self.verticalLayout_5.setStretch(0, 3)
        self.verticalLayout_5.setStretch(1, 7)
        self.main_pages.addWidget(self.recognize_page)
        self.report_page = QWidget()
        self.report_page.setObjectName(u"report_page")
        self.verticalLayout_7 = QVBoxLayout(self.report_page)
        self.verticalLayout_7.setSpacing(2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(1, 1, 1, 1)
        self.report_controllers = QWidget(self.report_page)
        self.report_controllers.setObjectName(u"report_controllers")
        self.verticalLayout_18 = QVBoxLayout(self.report_controllers)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.report_name_label = QLabel(self.report_controllers)
        self.report_name_label.setObjectName(u"report_name_label")
        self.report_name_label.setMaximumSize(QSize(16777215, 30))
        self.report_name_label.setFont(font3)
        self.report_name_label.setLayoutDirection(Qt.LeftToRight)
        self.report_name_label.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"padding-left: 10px;\n"
"font-weight: bold;\n"
"font-size: 20pt;")
        self.report_name_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_18.addWidget(self.report_name_label)

        self.widget_8 = QWidget(self.report_controllers)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.report_class_input = QLineEdit(self.widget_8)
        self.report_class_input.setObjectName(u"report_class_input")
        self.report_class_input.setMinimumSize(QSize(0, 30))
        self.report_class_input.setFont(font4)
        self.report_class_input.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 7px;\n"
"border: 2px solid #000;")

        self.horizontalLayout_7.addWidget(self.report_class_input)

        self.report_search_btn = QPushButton(self.widget_8)
        self.report_search_btn.setObjectName(u"report_search_btn")
        self.report_search_btn.setMinimumSize(QSize(150, 30))
        self.report_search_btn.setFont(font5)
        self.report_search_btn.setStyleSheet(u"background-color: rgb(190,207,187);\n"
"color: rgb(0,0,0);\n"
"border-radius: 5px;\n"
"border: 2px solid #000;\n"
"font-weight: bold;\n"
"font-size: 12pt;")
        icon13 = QIcon()
        icon13.addFile(u":/icons/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.report_search_btn.setIcon(icon13)
        self.report_search_btn.setIconSize(QSize(25, 25))

        self.horizontalLayout_7.addWidget(self.report_search_btn)


        self.verticalLayout_18.addWidget(self.widget_8)


        self.verticalLayout_7.addWidget(self.report_controllers)

        self.report_view = QWidget(self.report_page)
        self.report_view.setObjectName(u"report_view")
        self.report_view.setFont(font6)
        self.report_view.setStyleSheet(u"border-radius: 5px;\n"
"background-color:rgb(54, 71, 107); \n"
"border-radius: 5px;\n"
"border: 2px solid #000;")
        self.verticalLayout_6 = QVBoxLayout(self.report_view)
        self.verticalLayout_6.setSpacing(11)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(11, 11, 11, 11)
        self.report_table = QTableWidget(self.report_view)
        if (self.report_table.columnCount() < 5):
            self.report_table.setColumnCount(5)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem7.setFont(font1);
        __qtablewidgetitem7.setBackground(QColor(0, 0, 0, 0));
        self.report_table.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem8.setFont(font1);
        self.report_table.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem9.setFont(font1);
        self.report_table.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem10.setFont(font1);
        self.report_table.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem11.setFont(font1);
        self.report_table.setHorizontalHeaderItem(4, __qtablewidgetitem11)
        self.report_table.setObjectName(u"report_table")
        self.report_table.setFont(font6)
        self.report_table.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(0, 255, 64);")
        self.report_table.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.report_table.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)

        self.verticalLayout_6.addWidget(self.report_table)


        self.verticalLayout_7.addWidget(self.report_view)

        self.verticalLayout_7.setStretch(0, 3)
        self.verticalLayout_7.setStretch(1, 7)
        self.main_pages.addWidget(self.report_page)
        self.chart_page = QWidget()
        self.chart_page.setObjectName(u"chart_page")
        self.verticalLayout_9 = QVBoxLayout(self.chart_page)
        self.verticalLayout_9.setSpacing(2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(1, 1, 1, 1)
        self.chart_controllers = QWidget(self.chart_page)
        self.chart_controllers.setObjectName(u"chart_controllers")
        self.verticalLayout_8 = QVBoxLayout(self.chart_controllers)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.chart_name_label = QLabel(self.chart_controllers)
        self.chart_name_label.setObjectName(u"chart_name_label")
        self.chart_name_label.setFont(font3)
        self.chart_name_label.setLayoutDirection(Qt.LeftToRight)
        self.chart_name_label.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"padding-left: 10px;\n"
"font-weight: bold;\n"
"font-size: 20pt;")
        self.chart_name_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_8.addWidget(self.chart_name_label)

        self.search_panel = QWidget(self.chart_controllers)
        self.search_panel.setObjectName(u"search_panel")
        self.horizontalLayout_3 = QHBoxLayout(self.search_panel)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.chart_model_name_input = QLineEdit(self.search_panel)
        self.chart_model_name_input.setObjectName(u"chart_model_name_input")
        self.chart_model_name_input.setMinimumSize(QSize(30, 30))
        self.chart_model_name_input.setFont(font4)
        self.chart_model_name_input.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 7px;\n"
"border: 2px solid #000;")

        self.horizontalLayout_3.addWidget(self.chart_model_name_input)

        self.chart_show_btn = QPushButton(self.search_panel)
        self.chart_show_btn.setObjectName(u"chart_show_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.chart_show_btn.sizePolicy().hasHeightForWidth())
        self.chart_show_btn.setSizePolicy(sizePolicy2)
        self.chart_show_btn.setMinimumSize(QSize(150, 30))
        self.chart_show_btn.setFont(font5)
        self.chart_show_btn.setStyleSheet(u"background-color: rgb(190,207,187);\n"
"color: rgb(0,0,0);\n"
"border-radius: 5px;\n"
"border: 2px solid #000;\n"
"font-weight: bold;\n"
"font-size: 12pt;")
        icon14 = QIcon()
        icon14.addFile(u":/icons/codesandbox.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.chart_show_btn.setIcon(icon14)
        self.chart_show_btn.setIconSize(QSize(25, 25))

        self.horizontalLayout_3.addWidget(self.chart_show_btn)


        self.verticalLayout_8.addWidget(self.search_panel)

        self.chart_result_text_label = QLabel(self.chart_controllers)
        self.chart_result_text_label.setObjectName(u"chart_result_text_label")
        font9 = QFont()
        font9.setFamily(u"Cascadia Code")
        font9.setPointSize(11)
        font9.setUnderline(False)
        self.chart_result_text_label.setFont(font9)
        self.chart_result_text_label.setLayoutDirection(Qt.LeftToRight)
        self.chart_result_text_label.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"padding-left: 10px;")
        self.chart_result_text_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_8.addWidget(self.chart_result_text_label)

        self.verticalLayout_8.setStretch(0, 1)
        self.verticalLayout_8.setStretch(1, 1)
        self.verticalLayout_8.setStretch(2, 3)

        self.verticalLayout_9.addWidget(self.chart_controllers)

        self.chart_view = QWidget(self.chart_page)
        self.chart_view.setObjectName(u"chart_view")
        self.chart_view.setFont(font6)
        self.chart_view.setStyleSheet(u"border-radius: 5px;\n"
"background-color:rgb(54, 71, 107); \n"
"border-radius: 5px;\n"
"border: 2px solid #000;")
        self.horizontalLayout_10 = QHBoxLayout(self.chart_view)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.chart_result_img_label = QLabel(self.chart_view)
        self.chart_result_img_label.setObjectName(u"chart_result_img_label")
        self.chart_result_img_label.setMaximumSize(QSize(50000, 50000))
        self.chart_result_img_label.setFont(font6)
        self.chart_result_img_label.setLayoutDirection(Qt.RightToLeft)
        self.chart_result_img_label.setStyleSheet(u"background-color: rgb(0, 255, 204);")
        self.chart_result_img_label.setPixmap(QPixmap(u"../../../Duong/.designer/backup/resources/apps/no_data_found.png"))
        self.chart_result_img_label.setScaledContents(True)
        self.chart_result_img_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.chart_result_img_label)


        self.verticalLayout_9.addWidget(self.chart_view)

        self.verticalLayout_9.setStretch(0, 3)
        self.verticalLayout_9.setStretch(1, 7)
        self.main_pages.addWidget(self.chart_page)

        self.verticalLayout_2.addWidget(self.main_pages)


        self.horizontalLayout.addWidget(self.main)


        self.verticalLayout_19.addWidget(self.container)

        Attendance.setCentralWidget(self.attendanceWidget)

        self.retranslateUi(Attendance)

        self.main_pages.setCurrentIndex(0)
        self.recognize_view.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Attendance)
    # setupUi

    def retranslateUi(self, Attendance):
        self.icon_attendance.setText("")
        self.name_attendance.setText(QCoreApplication.translate("Attendance", u"\u0110i\u1ec3m danh sinh vi\u00ean", None))
        self.attendance_minimize_btn.setText("")
        self.attendance_expand_btn.setText("")
        self.attendance_exit_btn.setText("")
        self.menu_btn.setText("")
        self.home_btn.setText("")
        self.recognize_btn.setText("")
        self.report_btn.setText("")
        self.chart_btn.setText("")
        self.logout_btn.setText("")
        self.home_name_label.setText(QCoreApplication.translate("Attendance", u"TRANG CH\u1ee6", None))
        self.home_class_input.setInputMask("")
        self.home_class_input.setText("")
        self.home_search_btn.setText(QCoreApplication.translate("Attendance", u"T\u00ecm ki\u1ebfm", None))
        self.home_train_btn.setText(QCoreApplication.translate("Attendance", u"Hu\u1ea5n luy\u1ec7n", None))
        ___qtablewidgetitem = self.home_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Attendance", u"MSV", None));
        ___qtablewidgetitem1 = self.home_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Attendance", u"H\u1ecd v\u00e0 t\u00ean", None));
        ___qtablewidgetitem2 = self.home_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Attendance", u"L\u1edbp QL", None));
        ___qtablewidgetitem3 = self.home_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Attendance", u"Ng\u00e0y sinh", None));
        ___qtablewidgetitem4 = self.home_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Attendance", u"S\u1ed1 \u0111i\u1ec7n tho\u1ea1i", None));
        self.model_name_label.setText(QCoreApplication.translate("Attendance", u"model_name.keras", None))
        self.recognize_name_label.setText(QCoreApplication.translate("Attendance", u"\u0110I\u1ec2M DANH", None))
        self.recognize_img_path_input.setInputMask("")
        self.recognize_img_path_input.setText("")
        self.recognize_models_box.setCurrentText("")
        self.recognize_tab_1_btn.setText("")
        self.recognize_tab_2_btn.setText("")
        self.recognize_tab_3_btn.setText("")
        self.recognize_open_img_btn.setText(QCoreApplication.translate("Attendance", u"M\u1edf \u1ea3nh", None))
        self.recognize_guess_btn.setText(QCoreApplication.translate("Attendance", u"\u0110i\u1ec3m danh", None))
        self.recognize_export_btn.setText(QCoreApplication.translate("Attendance", u"K\u1ebft qu\u1ea3", None))
        self.recognize_input_img_label.setText("")
        self.recognize_output_img_label.setText("")
        ___qtablewidgetitem5 = self.recognize_table.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Attendance", u"Box Color", None));
        ___qtablewidgetitem6 = self.recognize_table.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Attendance", u"M\u00e3 sinh vi\u00ean", None));
        self.recognize_keep_btn.setText(QCoreApplication.translate("Attendance", u"L\u01b0u", None))
        self.report_name_label.setText(QCoreApplication.translate("Attendance", u"B\u00c1O C\u00c1O", None))
        self.report_class_input.setInputMask("")
        self.report_class_input.setText("")
        self.report_search_btn.setText(QCoreApplication.translate("Attendance", u"T\u00ecm ki\u1ebfm", None))
        ___qtablewidgetitem7 = self.report_table.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Attendance", u"MSV", None));
        ___qtablewidgetitem8 = self.report_table.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Attendance", u"H\u1ecd v\u00e0 t\u00ean", None));
        ___qtablewidgetitem9 = self.report_table.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Attendance", u"L\u1edbp QL", None));
        ___qtablewidgetitem10 = self.report_table.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Attendance", u"M\u00e3 l\u1edbp", None));
        ___qtablewidgetitem11 = self.report_table.horizontalHeaderItem(4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Attendance", u"\u0110i\u1ec3m danh", None));
        self.chart_name_label.setText(QCoreApplication.translate("Attendance", u"BI\u1ec2U \u0110\u1ed2 HU\u1ea4N LUY\u1ec6N M\u00d4 H\u00ccNH", None))
        self.chart_model_name_input.setInputMask("")
        self.chart_model_name_input.setText("")
        self.chart_show_btn.setText(QCoreApplication.translate("Attendance", u"M\u00f4 h\u00ecnh", None))
        self.chart_result_text_label.setText(QCoreApplication.translate("Attendance", u"Model: ...", None))
        self.chart_result_img_label.setText("")
        pass
    # retranslateUi

