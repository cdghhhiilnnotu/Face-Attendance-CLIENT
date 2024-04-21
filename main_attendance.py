from main_importer import *
from ui_attendance import *
from Custom_Widgets.Widgets import * 
from PyQt5 import QtWidgets

def background_func(func, args):
    th = threading.Thread(target=func, args=args)
    th.start()

class AttendanceWindow(QMainWindow):
    def __init__(self, widget):
        super(AttendanceWindow, self).__init__()
        # loadUi("attendance.ui", self)
        self.ui = Ui_Attendance()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui)
        self.widget = widget
        self.dataset_path = ""
        self.img_path = HauSettings.IMGS_DIR
        self.model_name_text = ""
        self.class_id_name = ""
        self.img_guess_name = ""
        self.list_model_trained = []
        self.collector = CollectData.check_user("","")
        self.isRecording = False
        self.isTraining = False

        self.ui.menu_btn.clicked.connect(self.menu_func)
        self.ui.logout_btn.clicked.connect(self.logout_func)
        self.ui.home_btn.clicked.connect(lambda: self.swtich_page_func(0))
        self.ui.recognize_btn.clicked.connect(lambda: self.swtich_page_func(1))
        self.ui.report_btn.clicked.connect(lambda: self.swtich_page_func(2))
        self.ui.chart_btn.clicked.connect(lambda: self.swtich_page_func(3))
        
        self.ui.home_search_btn.clicked.connect(self.hp_search_func)
        # self.ui.home_get_data_btn.clicked.connect(lambda: background_func(self.ui.hp_get_data_func, ()))
        self.ui.home_train_btn.clicked.connect(lambda: background_func(self.hp_training_func, ()))
        # self.ui.recognize_guess_btn.clicked.connect(self.ui.recp_show_guess_func)
        self.ui.recognize_guess_btn.clicked.connect(self.start_capture_video)
        self.ui.recognize_export_btn.clicked.connect(self.stop_capture_video)
        self.ui.recognize_open_img_btn.clicked.connect(self.recp_open_image_to_guess_func)
        self.ui.recognize_tab_1_btn.clicked.connect(lambda: self.recp_switch_subpage_func(0))
        self.ui.recognize_tab_2_btn.clicked.connect(lambda: self.recp_switch_subpage_func(1))
        self.ui.recognize_tab_3_btn.clicked.connect(lambda: self.recp_switch_subpage_func(2))
        self.ui.report_search_btn.clicked.connect(self.repp_show_report_table_func)
        self.ui.chart_show_btn.clicked.connect(self.chp_show_chart_func)
        self.ui.attendance_exit_btn.clicked.connect(self.exit_func)
        self.ui.recognize_keep_btn.clicked.connect(self.recp_save_results)
        self.ui.recognize_refresh_btn.clicked.connect(self.recp_refresh_results)
        self.thread = {}

    def logout_func(self):
        self.attendance_init()
        self.widget.setCurrentIndex(self.widget.currentIndex() - 1)
        self.widget.setWindowTitle(self.widget.currentWidget().objectName())
        self.widget.currentWidget().login_init() 
        
    def swtich_page_func(self, index):
        self.ui.main_pages.setCurrentIndex(index)
        list_btns = [self.ui.home_btn,self.ui.recognize_btn,self.ui.report_btn,self.ui.chart_btn]
        for i in range(len(list_btns)):
            if i == index:
                list_btns[i].setStyleSheet(HauSettings.menu_btns_style(0,9,0,9,1,0,1,1))
            else:
                list_btns[i].setStyleSheet(HauSettings.menu_btns_style(9,9,9,9,1,1,1,1))

    def attendance_init(self):
        # self.ui.widget.setWindowFlag(Qt.Window)
        # self.ui.widget.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.attendance_expand_btn.hide()
        self.ui.attendance_minimize_btn.hide()
        self.setFixedWidth(1280)
        self.setFixedHeight(720)
        # self.widget.move(109, 109)
        self.widget.setWindowTitle(self.widget.currentWidget().objectName())
        self.hp_init_func()
        self.recp_init_func()
        self.repp_init_func()
        self.chp_init_func()
        self.swtich_page_func(0)
        self.collapse_menu()
        self.sync_btn_page()
    

    # TITLE ATTENDANCE
    def exit_func(self):
        QApplication.quit()


    # MAIN ATTENDANCE
    def sync_btn_page(self):
        list_btns = [self.ui.home_btn,self.ui.recognize_btn,self.ui.report_btn,self.ui.chart_btn]
        list_pages = [self.ui.home_page,self.ui.recognize_page,self.ui.report_page,self.ui.chart_page]
        for i in range(len(list_btns)):
            if list_pages[i] == self.ui.main_pages.currentWidget():
                list_btns[i].setStyleSheet(HauSettings.menu_btns_style(0,9,0,9,1,0,1,1))
            else:
                list_btns[i].setStyleSheet(HauSettings.menu_btns_style(9,9,9,9,1,1,1,1))

    def expand_menu(self):
        self.ui.menu.setMinimumWidth(200)
        list_btns = [self.ui.home_btn,self.ui.recognize_btn,self.ui.report_btn,self.ui.chart_btn]
        list_btn_names = ["  Trang chủ","  Điểm danh","  Báo cáo","  Biểu đồ"]
        for i in range(len(list_btns)):
            list_btns[i].setStyleSheet(HauSettings.menu_btns_style(9,9,9,9,1,1,1,1))
            list_btns[i].setText(list_btn_names[i])
        self.ui.menu_btn.setStyleSheet(HauSettings.menu_btns_style(9,9,0,0,1,1,1,1))
        self.ui.menu_btn.setText("  MENU")
        self.ui.logout_btn.setStyleSheet(HauSettings.menu_btns_style(0,0,9,9,1,1,1,1))
        self.ui.logout_btn.setText("  ĐĂNG XUẤT")
        
    def collapse_menu(self):
        self.ui.menu.setMinimumWidth(50)
        list_btns = [self.ui.menu_btn,self.ui.home_btn,self.ui.recognize_btn,self.ui.report_btn,self.ui.chart_btn,self.ui.logout_btn]
        for i in range(len(list_btns)):
            list_btns[i].setStyleSheet(HauSettings.menu_btns_style(9,9,9,9,1,1,1,1))
            list_btns[i].setText("")
        
    def menu_func(self):
        if self.ui.menu.size().width() < 200:
            self.expand_menu()
        else:
            self.collapse_menu()
        self.sync_btn_page()
        

    # HOME PAGE
    def hp_init_func(self):
        self.hp_init_class_func("")
        self.ui.home_class_input.setText("")
        self.ui.home_table.setColumnWidth(0, 200)
        self.ui.home_table.setColumnWidth(1, 400)
        self.ui.home_table.setColumnWidth(2, 200)
        self.ui.home_table.setColumnWidth(3, 200)
        self.ui.home_table.setColumnWidth(4, 200)
        self.hp_show_table_func()
    
    def hp_init_class_func(self, name_of_class):
        self.class_id_name = name_of_class
        # self.ui.home_controllers.setStyleSheet("QWidget#home_controllers{background-image: url(./resources/apps/bg_header.png)}")
        # self.ui.recognize_controllers.setStyleSheet("QWidget#recognize_controllers{background-image: url(./resources/apps/bg_header.png)}")
        # self.ui.report_controllers.setStyleSheet("QWidget#report_controllers{background-image: url(./resources/apps/bg_header.png)}")
        # self.ui.chart_controllers.setStyleSheet("QWidget#chart_controllers{background-image: url(./resources/apps/bg_header.png)}")
        self.ui.model_name_label.setText(self.class_id_name + HauSettings.MODEL_FILE_EXTENSION)
        self.model_name_text = self.ui.model_name_label.text()

    def hp_search_func(self):
        try:
            print("PRESS HOME SEARCH BUTTON")
            self.hp_init_class_func(self.ui.home_class_input.text())
            self.hp_show_table_func()
        except:
            pass

    def hp_show_table_func(self):
        self.ui.home_table.horizontalHeader().setVisible(True)
        datasv = self.collector.get_sv_by_class_id(self.class_id_name)
        row = 0
        self.ui.home_table.setRowCount(len(datasv))
        self.ui.home_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.home_table.setStyleSheet(
            "QTableView::item:selected { color:white; background:#000000; font-weight:900; }"
            "QTableView::item { color:black; background:#fff;}"
            "QHeaderView::section { color:white; background-color:#232326;}"
        )
        for e in datasv:
            self.ui.home_table.setItem(row, 0, QTableWidgetItem(e['MaSV']))
            self.ui.home_table.setItem(row, 1, QTableWidgetItem(e['TenSV']))
            self.ui.home_table.setItem(row, 2, QTableWidgetItem(e['LopQL']))
            self.ui.home_table.setItem(row, 3, QTableWidgetItem(e['NgSinh']))
            self.ui.home_table.setItem(row, 4, QTableWidgetItem(e['SDT']))
            row += 1
        self.dataset_path = os.path.join(self.collector.DATASETS_PATH,self.class_id_name)
        # self.ui.home_get_data_btn.show()
        
    def hp_get_data_func(self):
        print("PRESS HOME GET DATA BUTTON")
        try:
            DatasetSupport.download_datasets_by_class_id(self.class_id_name, self.dataset_path, self.collector)
            # self.home_train_btn.show()
        except:
            pass

    def hp_training_func(self):
        print("PRESS HOME TRAIN BUTTON")
        try:
            if not self.isTraining:
                self.isTraining = True
                DatasetSupport.download_datasets_by_class_id(self.class_id_name, self.dataset_path, self.collector)
                self.model = HauModel(self.dataset_path, 1, self.class_id_name, model_dir=self.collector.MODEL_DIR)
                self.model.training()
                self.model.evaluating()
                self.model.plot_train_history(os.path.join(self.collector.STATISTIC_PATH,self.class_id_name + ".png"))
                # self.chp_show_chart_func()
                self.recp_init_func()
                self.isTraining = False
        except:
            pass


    # RECOGNITION PAGE
    def recp_init_func(self):
        self.recp_show_recognition_table_func1([])
        self.ui.recognize_img_path_input.setText("")
        if os.path.exists(self.collector.MODEL_DIR):
            self.ui.recognize_models_box.addItems([m.split(".keras")[0] for m in os.listdir(self.collector.MODEL_DIR)])

        if self.ui.recognize_models_box.count() > 0:
            self.ui.recognize_guess_btn.show()
            self.ui.recognize_tab_2_btn.show()
            self.ui.recognize_tab_3_btn.show()
        else:
            self.ui.recognize_guess_btn.hide()
            self.ui.recognize_tab_2_btn.hide()
            self.ui.recognize_tab_3_btn.hide()
        HauSettings.display_image_func(self.ui.recognize_input_img_label, HauSettings.UNKNOWN_IMAGE_PATH)
        HauSettings.display_image_func(self.ui.recognize_output_img_label, HauSettings.UNKNOWN_IMAGE_PATH)
        self.recp_switch_subpage_func(0)

    def recp_switch_subpage_func(self, index):
        print(f"PRESS RECOGNIZE PAGE {index} BUTTON")
        try:
            recognize_tab_btns = [self.ui.recognize_tab_1_btn,self.ui.recognize_tab_2_btn,self.ui.recognize_tab_3_btn]
            for tab in recognize_tab_btns:
                tab.setStyleSheet(
                    "background-color: rgba(188, 188, 188, 100);border-radius: 5px;"
                )
            self.ui.recognize_view.setCurrentIndex(index)
            recognize_tab_btns[index].setStyleSheet(
                "background-color: rgba(188, 188, 188, 255);border-radius: 5px;"
            )
        except:
            pass

    def recp_save_results(self):
        for face_masv in self.face_guessed:
            data = {}
            data['masv'] = face_masv
            data['malop'] = self.ui.recognize_models_box.currentText()
            data['ghichu'] = ""
            requests.post(HauSettings.BASE_URL + "/giaovien/baocao", data)
        self.collector.user_api(self.collector.username_MGV)
        self.collector.update_api(data['malop'])

    def recp_refresh_results(self):
        self.recp_show_recognition_table_func1([])
        self.ui.recognize_img_path_input.setText("")
        HauSettings.display_image_func(self.ui.recognize_output_img_label, HauSettings.UNKNOWN_IMAGE_PATH)

    # BEGIN DISPLAY CAMERA SECTION
    def closeEvent(self, event):
        self.stop_capture_video()

    def stop_capture_video(self):
        try:
            self.thread[1].cam_enable = False
            self.face_guessed = list(dict.fromkeys(self.thread[1].face_guessed))
            self.recp_show_recognition_table_func1(self.face_guessed)
            self.thread[1].stop()
            self.recp_switch_subpage_func(2)
        except:
            pass

    def start_capture_video(self):
        if self.ui.recognize_img_path_input.text() == "":
            if not self.isRecording:
                self.isRecording = True
                self.dataset_path = os.path.join(self.collector.DATASETS_PATH,self.ui.recognize_models_box.currentText())
                self.model = HauModel(self.dataset_path, 1, self.class_id_name, model_dir=self.collector.MODEL_DIR) 
                self.model.load_model(self.ui.recognize_models_box.currentText())
                self.thread[1] = Thread_Video(1, os.listdir(self.dataset_path), self.model, self.ui.recognize_output_img_label)
                self.thread[1].cam_enable = True
                self.thread[1].start()
                self.thread[1].signal.connect(self.show_wedcam)
                self.recp_switch_subpage_func(1)
        else:
            self.dataset_path = os.path.join(self.collector.DATASETS_PATH,self.ui.recognize_models_box.currentText())
            self.model = HauModel(self.dataset_path, 1, self.class_id_name, model_dir=self.collector.MODEL_DIR) 
            self.model.load_model(self.ui.recognize_models_box.currentText())
            file_name, colors, guessed = self.model.guessing_img(self.dataset_path, self.ui.recognize_img_path_input.text(), self.model, self.ui.recognize_models_box.currentText(), self.collector)
            self.recp_show_recognition_table_func2(colors, guessed)
            self.face_guessed = list(dict.fromkeys(guessed))
            HauSettings.display_image_func(self.ui.recognize_output_img_label, file_name)


    def show_wedcam(self, cv_img):
        """Updates the image_label with a new opencv image"""
        qt_img = self.convert_cv_qt(cv_img)
        self.ui.recognize_output_img_label.setPixmap(qt_img)

    def convert_cv_qt(self, cv_img):
        """Convert from an opencv image to QPixmap"""
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(800, 600, Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)
    # END DISPLAY CAMERA SECTION

    def recp_show_recognition_table_func2(self, colors, guesses_indexes):
        self.ui.recognize_table.horizontalHeader().setVisible(True)
        self.ui.recognize_table.setRowCount(len(colors))
        self.ui.recognize_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.recognize_table.setStyleSheet(
            "QTableView::item:selected { color:white; background:#000000; font-weight:900; }"
            "QHeaderView::section { color:white; background-color:#232326;}"
        )
        self.ui.recognize_table.setColumnWidth(0, 200)
        for idx, color in enumerate(colors):
            itemColor = QTableWidgetItem()
            itemColor.setBackground(QBrush(QColor(color[2], color[1], color[0])))
            self.ui.recognize_table.setItem(idx, 0, itemColor)
            itemMSV = QTableWidgetItem(str(os.listdir(self.dataset_path)[guesses_indexes[idx]]))
            itemMSV.setBackground(QBrush(QColor(255, 255, 255)))
            self.ui.recognize_table.setItem(idx, 1, itemMSV)

    def recp_show_recognition_table_func1(self, guessed):
        try:
            self.ui.recognize_table.horizontalHeader().setVisible(True)
            self.ui.recognize_table.setRowCount(len(guessed))
            self.ui.recognize_table.setSelectionBehavior(QAbstractItemView.SelectRows)
            self.ui.recognize_table.setStyleSheet(
                "QTableView::item:selected { color:white; background:#000000; font-weight:900; }"
                "QHeaderView::section { color:white; background-color:#232326;}"
            )
            self.ui.recognize_table.setColumnWidth(0, 200)
            for idx, guess in enumerate(guessed):
                itemColor = QTableWidgetItem()
                itemColor.setBackground(QBrush(QColor(255, 255, 255)))
                self.ui.recognize_table.setItem(idx, 0, itemColor)
                # itemMSV = QTableWidgetItem(str(os.listdir(self.ui.dataset_path)[self.face_guessed[idx]]))
                itemMSV = QTableWidgetItem(guess)
                
                itemMSV.setBackground(QBrush(QColor(255, 255, 255)))
                self.ui.recognize_table.setItem(idx, 1, itemMSV)
        except:
            pass

    def recp_open_image_to_guess_func(self):
        print("PRESS RECOGNIZE OPEN FILE BUTTON")
        try:
            fname = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*)")
            if fname:
                self.img_guess_name = str(fname[0])
                self.ui.recognize_img_path_input.setText(str(fname[0]))
                HauSettings.display_image_func(self.ui.recognize_input_img_label, self.img_guess_name)
                self.recp_switch_subpage_func(0)
        except:
            pass


    # REPORT PAGE
    def repp_init_func(self):
        self.ui.report_class_input.setText("")
        self.ui.report_table.setColumnWidth(0, 200)
        self.ui.report_table.setColumnWidth(1, 400)
        self.ui.report_table.setColumnWidth(2, 200)
        self.ui.report_table.setColumnWidth(3, 200)
        self.ui.report_table.setColumnWidth(4, 200)
        self.repp_show_report_table_func()

    def repp_show_report_table_func(self):
        print("PRESS REPORT TABLE BUTTON")
        try:
            self.ui.report_table.horizontalHeader().setVisible(True)
            datasv = self.collector.get_baocao_by_class_id(self.ui.report_class_input.text())
            row = 0
            self.ui.report_table.setRowCount(len(datasv))
            self.ui.report_table.setSelectionBehavior(QAbstractItemView.SelectRows)
            self.ui.report_table.setStyleSheet(
                "QTableView::item:selected { color:white; background:#000000; font-weight:900; }"
                "QTableView::item { color:black; background:#fff; }"
                "QHeaderView::section { color:white; background-color:#232326; }"
            )
            for e in datasv:
                self.ui.report_table.setItem(row, 0, QTableWidgetItem(e['MaSV']))
                self.ui.report_table.setItem(row, 1, QTableWidgetItem(e['TenSV']))
                self.ui.report_table.setItem(row, 2, QTableWidgetItem(e['LopQL']))
                self.ui.report_table.setItem(row, 3, QTableWidgetItem(e['MaLop']))
                self.ui.report_table.setItem(row, 4, QTableWidgetItem(str(e['DiemDanh'])))
                row += 1
        except:
            pass


    # CHART PAGE
    def chp_init_func(self):
        self.ui.chart_model_name_input.setText("")
        HauSettings.display_image_func(self.ui.chart_result_img_label, HauSettings.UNKNOWN_IMAGE_PATH)

    def chp_show_chart_func(self):
        print("PRESS CHART MODEL BUTTON")
        try:
            HauSettings.display_image_func(self.ui.chart_result_img_label, os.path.join(self.collector.STATISTIC_PATH, f"{self.ui.chart_model_name_input.text()}.png"))
        except:
            HauSettings.display_image_func(self.ui.chart_result_img_label, HauSettings.UNKNOWN_IMAGE_PATH)
        
        





