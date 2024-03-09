import sys
import os
from PyQt5.QtCore import Qt

from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QAbstractItemView, QFileDialog
from PyQt5.QtGui import QIcon, QPixmap, QBrush, QColor
from packages_import import *

class AttendanceWindow(QMainWindow):
    def __init__(self, widget):
        self.dataset_path = "datasets"
        self.img_path = "imgs"
        self.model_name_path = ""
        self.widget = widget
        self.class_id_name = ""
        self.img_guess_name = ""
        self.list_model_trained = []
        super(AttendanceWindow, self).__init__()
        loadUi("attendance.ui", self)
        self.widget.setFixedWidth(800)
        self.widget.setFixedHeight(500)
        self.logout_btn.clicked.connect(self.logging_out)
        self.home_btn.clicked.connect(lambda: self.swtich_page(0))
        self.recog_btn.clicked.connect(lambda: self.swtich_page(1))
        self.report_btn.clicked.connect(lambda: self.swtich_page(2))
        self.chart_btn.clicked.connect(lambda: self.swtich_page(3))
        self.home_search_btn.clicked.connect(self.get_class_id)
        self.collect_btn.clicked.connect(self.get_data_func)
        self.train_btn.clicked.connect(self.training_func)
        self.guess_btn.clicked.connect(self.show_guess)
        self.open_btn.clicked.connect(self.open_image_to_guess)
        self.recog_tab_1.clicked.connect(lambda: self.switch_recog_page(0))
        self.recog_tab_2.clicked.connect(lambda: self.switch_recog_page(1))
        self.recog_tab_3.clicked.connect(lambda: self.switch_recog_page(2))
        self.report_search_btn.clicked.connect(self.show_report_table)
        self.train_btn.hide()
        self.collect_btn.hide()

    # HOME PAGE

    def logging_out(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() - 1)
        self.widget.setWindowTitle(self.widget.currentWidget().objectName())

    def switch_recog_page(self, index):
        self.recog_tab_1.setStyleSheet(
            "background-color: rgba(188, 188, 188, 100);border-radius: 5px;"
        )
        self.recog_tab_2.setStyleSheet(
            "background-color: rgba(188, 188, 188, 100);border-radius: 5px;"
        )
        self.recog_tab_3.setStyleSheet(
            "background-color: rgba(188, 188, 188, 100);border-radius: 5px;"
        )
        self.recog_subpage.setCurrentIndex(index)
        if index == 0:
            self.recog_tab_1.setStyleSheet(
                "background-color: rgba(188, 188, 188, 255);border-radius: 5px;"
            )
        elif index == 1:
            self.recog_tab_2.setStyleSheet(
                "background-color: rgba(188, 188, 188, 255);border-radius: 5px;"
            )
        else:
            self.recog_tab_3.setStyleSheet(
                "background-color: rgba(188, 188, 188, 255);border-radius: 5px;"
            )

    def swtich_page(self, index):
        self.pages.setCurrentIndex(index)

    def get_class_id(self):
        self.class_id_name = self.class_box.text()

        self.model_name.setText(self.class_id_name + ".keras")
        self.model_name_path = self.model_name.text()
        self.show_home_table()

    def show_home_table(self):
        datasv = get_sv_by_class(self.class_id_name)
        row = 0
        self.home_table.setRowCount(len(datasv))
        self.home_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.home_table.setStyleSheet(
            "QTableView::item:selected { color:white; background:#000000; font-weight:900; }"
            "QTableView::item { color:black; background:#fff;}"
            "QHeaderView::section { color:white; background-color:#232326;}"
        )
        for e in datasv:
            self.home_table.setItem(row, 0, QTableWidgetItem(e['MSV']))
            self.home_table.setItem(row, 1, QTableWidgetItem(e['TenSV']))
            self.home_table.setItem(row, 2, QTableWidgetItem(e['LopQL']))
            self.home_table.setItem(row, 3, QTableWidgetItem(e['NgSinh']))
            self.home_table.setItem(row, 4, QTableWidgetItem(e['SDT']))
            row += 1
        self.dataset_path = self.class_id_name
        self.collect_btn.show()
        
    def get_data_func(self):
        download_dataset_by_class(self.dataset_path,self.class_id_name)
        cleaning_dataset(self.dataset_path,'haarcascade_frontalface_default.xml')
        augmentation_dataset_main(self.dataset_path)
        standardized_image(self.dataset_path)
        split_folder(self.dataset_path, self.img_path)

        self.students, self.student_classes = data_classify(self.dataset_path, self.img_path)
        self.train_ds, self.val_ds, self.test_ds = augmentation_dataset_extra(self.img_path)
        self.train_btn.show()

    def training_func(self):
        self.model = compile_model(self.student_classes)
        self.model, self.history  = fit_model(self.model, self.train_ds, self.val_ds, self.model_name_path, 1)

        evaluate_model(self.model, self.model_name_path, self.test_ds)
        plot_train_history(self.history, f"{self.class_id_name}_acc_loss.png")
        self.show_chart_page()
        if self.class_id_name not in self.list_model_trained:
            self.list_model_trained.append(self.class_id_name)
            self.model_list.addItem(self.class_id_name) 


    # CHART PAGE
    def show_chart_page(self):
        pixmap = QPixmap(f"{self.class_id_name}_acc_loss.png")
        self.chart_pic.setPixmap(pixmap)

    def show_guess(self):
        # self.model = get_model_config(self.model_box_list.currentText())
        self.model = get_model_config("TH5216_20CN3")
        result_img, colors, guesses_indexes = img_result(self.img_guess_name, self.model)
        # print(colors)
        # print(guesses_indexes)
        pixmap = QPixmap(f"{result_img}")
        self.chart_pic.setPixmap(pixmap)
        self.show_recognition_table(colors, guesses_indexes)

    def show_recognition_table(self, colors, guesses_indexes):
        self.recog_table.setRowCount(len(colors))
        for idx, color in enumerate(colors):
            itemColor = QTableWidgetItem()
            itemColor.setBackground(QBrush(QColor(color[2], color[1], color[0])) )
            self.recog_table.setItem(idx, 0, itemColor)
            self.recog_table.setItem(idx, 1, QTableWidgetItem(str(os.listdir(self.dataset_path)[guesses_indexes[idx]])))

    def open_image_to_guess(self):
        fname = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*);;Python Files (*.py)")

        if fname:
            self.img_guess_name = str(fname[0])
            self.image_name.setText(str(fname[0]))

    def show_report_table(self):
        datasv = get_sv_by_class(self.class_name.text())
        row = 0
        self.report_table.setRowCount(len(datasv))
        self.report_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.report_table.setStyleSheet(
            "QTableView::item:selected { color:white; background:#000000; font-weight:900; }"
            "QTableView::item { color:black; background:#fff;}"
            "QHeaderView::section { color:white; background-color:#232326;}"
        )
        for e in datasv:
            self.report_table.setItem(row, 0, QTableWidgetItem(e['MSV']))
            self.report_table.setItem(row, 1, QTableWidgetItem(e['TenSV']))
            self.report_table.setItem(row, 2, QTableWidgetItem(e['LopQL']))
            self.report_table.setItem(row, 3, QTableWidgetItem(e['NgSinh']))
            self.report_table.setItem(row, 4, QTableWidgetItem(e['SDT']))
            row += 1
        






