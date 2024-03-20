import sys
import os
from PyQt5.QtCore import Qt
import threading

from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QAbstractItemView, QFileDialog
from PyQt5.QtGui import QIcon, QPixmap, QBrush, QColor
from packages_import import *

def background_func(func, args):
    th = threading.Thread(target=func, args=args)
    th.start()

class AttendanceWindow(QMainWindow):
    def __init__(self, widget):
        self.dataset_path = ""
        self.img_path = IMGS_DIR
        self.model_name_text = ""
        self.widget = widget
        self.class_id_name = ""
        self.img_guess_name = ""
        self.list_model_trained = []
        super(AttendanceWindow, self).__init__()
        loadUi("attendance.ui", self)
        
        self.logout_btn.clicked.connect(self.logging_out_func)
        self.home_btn.clicked.connect(lambda: self.swtich_page_func(0))
        self.recognize_btn.clicked.connect(lambda: self.swtich_page_func(1))
        self.report_btn.clicked.connect(lambda: self.swtich_page_func(2))
        self.chart_btn.clicked.connect(lambda: self.swtich_page_func(3))
        
        self.home_search_btn.clicked.connect(self.hp_search_func)
        self.home_get_data_btn.clicked.connect(lambda: background_func(self.hp_get_data_func, ()))
        self.home_train_btn.clicked.connect(lambda: background_func(self.hp_training_func, ()))
        self.recognize_guess_btn.clicked.connect(self.recp_show_guess_func)
        self.recognize_open_img_btn.clicked.connect(self.recp_open_image_to_guess_func)
        self.recognize_tab_1_btn.clicked.connect(lambda: self.recp_switch_subpage_func(0))
        self.recognize_tab_2_btn.clicked.connect(lambda: self.recp_switch_subpage_func(1))
        self.recognize_tab_3_btn.clicked.connect(lambda: self.recp_switch_subpage_func(2))
        self.report_search_btn.clicked.connect(self.repp_show_report_table_func)


    def logging_in_func(self):
        self.hp_init_func()
        self.recp_init_func()
        self.repp_init_func()
        self.chp_init_func()
        self.swtich_page_func(0)

    def logging_out_func(self):
        self.hp_init_func()
        self.recp_init_func()
        self.repp_init_func()
        self.chp_init_func()
        self.swtich_page_func(0)
        self.widget.setCurrentIndex(self.widget.currentIndex() - 1)
        self.widget.setWindowTitle(self.widget.currentWidget().objectName())
        self.widget.currentWidget().init_login() 

    def swtich_page_func(self, index):
        self.main_pages.setCurrentIndex(index)

    def display_image_func(self, this_label, this_img_path):
        if this_img_path == "" or not os.path.exists(this_img_path):
            this_img_path = UNKNOWN_IMAGE_PATH
        pixmap = QPixmap(f"{this_img_path}")
        this_label.setPixmap(pixmap)


    # HOME PAGE
    def hp_init_func(self):
        self.hp_init_class_func("")
        self.home_train_btn.hide()
        self.home_get_data_btn.hide()
        self.home_class_input.setText("")

        self.hp_show_table_func()
    
    def hp_init_class_func(self, name_of_class):
        self.class_id_name = name_of_class

        self.model_name_label.setText(self.class_id_name + MODEL_FILE_EXTENSION)
        self.model_name_text = self.model_name_label.text()

    def hp_search_func(self):
        self.hp_init_class_func(self.home_class_input.text())
        self.hp_show_table_func()
        self.chp_show_chart_func()

    def hp_show_table_func(self):
        self.home_table.horizontalHeader().setVisible(True)
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
            self.home_table.setItem(row, 0, QTableWidgetItem(e['MaSV']))
            self.home_table.setItem(row, 1, QTableWidgetItem(e['TenSV']))
            self.home_table.setItem(row, 2, QTableWidgetItem(e['LopQL']))
            self.home_table.setItem(row, 3, QTableWidgetItem(e['NgSinh']))
            self.home_table.setItem(row, 4, QTableWidgetItem(e['SDT']))
            row += 1
        self.dataset_path = os.path.join(DATASETS_PATH,self.class_id_name)
        self.home_get_data_btn.show()
        
    def hp_get_data_func(self):
        try:
            download_dataset_by_class(self.dataset_path,self.class_id_name)
            cleaning_dataset(self.dataset_path, MODEL_HAAR)
            augmentation_dataset_main(self.dataset_path)
            standardized_image(self.dataset_path)
            split_folder(self.dataset_path, self.img_path)

            self.students, self.student_classes = data_classify(self.dataset_path, self.img_path)
            self.train_ds, self.val_ds, self.test_ds = augmentation_dataset_extra(self.img_path)
            self.home_train_btn.show()
        except:
            pass

    def hp_training_func(self):
        self.model = compile_model(self.student_classes)
        self.model, self.history  = fit_model(self.model, self.train_ds, self.val_ds, self.model_name_text, 10)

        evaluate_model(self.model, self.model_name_text, self.test_ds)
        plot_train_history(self.history, f"{self.class_id_name}_acc_loss.png")
        self.chp_show_chart_func()
        self.recp_init_func()


    # RECOGNITION PAGE
    def recp_init_func(self):
        self.recp_show_recognition_table_func([], [])
        self.recognize_img_path_input.setText("")
        if os.path.exists(MODEL_DIR):
            self.recognize_models_box.addItems([m.split(".")[0] for m in os.listdir(MODEL_DIR)])

        if self.recognize_models_box.count() > 0:
            self.recognize_guess_btn.show()
        else:
            self.recognize_guess_btn.hide()
            self.recognize_tab_2_btn.hide()
            self.recognize_tab_3_btn.hide()
        self.display_image_func(self.recognize_input_img_label, UNKNOWN_IMAGE_PATH)
        self.display_image_func(self.recognize_output_img_label, UNKNOWN_IMAGE_PATH)
        self.recp_switch_subpage_func(0)

    def recp_switch_subpage_func(self, index):
        recognize_tab_btns = [self.recognize_tab_1_btn,self.recognize_tab_2_btn,self.recognize_tab_3_btn]
        for tab in recognize_tab_btns:
            tab.setStyleSheet(
                "background-color: rgba(188, 188, 188, 100);border-radius: 5px;"
            )
        self.recognize_view.setCurrentIndex(index)
        recognize_tab_btns[index].setStyleSheet(
            "background-color: rgba(188, 188, 188, 255);border-radius: 5px;"
        )

    def recp_show_guess_func(self):
        try:
            self.model = get_model_config(self.recognize_models_box.currentText())
            self.dataset_path = os.path.join(DATASETS_PATH,self.recognize_models_box.currentText())
            result_img_path, colors, guesses_indexes = guessing_img(self.dataset_path, self.img_guess_name, self.model)
            self.display_image_func(self.recognize_output_img_label, result_img_path)
            self.recp_show_recognition_table_func(colors, guesses_indexes)
        except:
            pass

    def recp_show_recognition_table_func(self, colors, guesses_indexes):
        self.recognize_table.horizontalHeader().setVisible(True)
        self.recognize_table.setRowCount(len(colors))
        self.recognize_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.recognize_table.setStyleSheet(
            "QTableView::item:selected { color:white; background:#000000; font-weight:900; }"
            "QHeaderView::section { color:white; background-color:#232326;}"
        )
        self.recognize_table.setColumnWidth(0, 200)
        for idx, color in enumerate(colors):
            itemColor = QTableWidgetItem()
            itemColor.setBackground(QBrush(QColor(color[2], color[1], color[0])))
            self.recognize_table.setItem(idx, 0, itemColor)
            itemMSV = QTableWidgetItem(str(os.listdir(self.dataset_path)[guesses_indexes[idx]]))
            itemMSV.setBackground(QBrush(QColor(255, 255, 255)))
            self.recognize_table.setItem(idx, 1, itemMSV)

    def recp_open_image_to_guess_func(self):
        fname = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*)")

        if fname:
            self.img_guess_name = str(fname[0])
            self.recognize_img_path_input.setText(str(fname[0]))
            self.display_image_func(self.recognize_input_img_label, self.img_guess_name)
            self.recp_switch_subpage_func(0)


    # REPORT PAGE
    def repp_init_func(self):
        self.report_class_input.setText("")
        self.repp_show_report_table_func()

    def repp_show_report_table_func(self):
        self.report_table.horizontalHeader().setVisible(True)
        datasv = get_baocao_all_class(self.report_class_input.text())
        row = 0
        self.report_table.setRowCount(len(datasv))
        self.report_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.report_table.setStyleSheet(
            "QTableView::item:selected { color:white; background:#000000; font-weight:900; }"
            "QTableView::item { color:black; background:#fff; }"
            "QHeaderView::section { color:white; background-color:#232326; }"
        )
        for e in datasv:
            self.report_table.setItem(row, 0, QTableWidgetItem(e['MaSV']))
            self.report_table.setItem(row, 1, QTableWidgetItem(e['TenSV']))
            self.report_table.setItem(row, 2, QTableWidgetItem(e['LopQL']))
            self.report_table.setItem(row, 3, QTableWidgetItem(e['MaLop']))
            self.report_table.setItem(row, 4, QTableWidgetItem(str(e['DiemDanh'])))
            row += 1


    # CHART PAGE
    def chp_init_func(self):
        if self.recognize_models_box.count() < 0:
            self.display_image_func(self.chart_result_img_label, UNKNOWN_IMAGE_PATH)
        else:
            self.chp_show_chart_func()

    def chp_show_chart_func(self):
        self.display_image_func(self.chart_result_img_label, f"{self.class_id_name}_acc_loss.png")

        





