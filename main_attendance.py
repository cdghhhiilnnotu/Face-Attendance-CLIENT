from main_importer import *

def background_func(func, args):
    th = threading.Thread(target=func, args=args)
    th.start()

class AttendanceWindow(QMainWindow):
    def __init__(self, widget):
        super(AttendanceWindow, self).__init__()
        loadUi("attendance.ui", self)
        self.widget = widget
        self.dataset_path = ""
        self.img_path = HauSettings.IMGS_DIR
        self.model_name_text = ""
        self.class_id_name = ""
        self.img_guess_name = ""
        self.list_model_trained = []
        self.collector = CollectData.check_user("","")
        
        self.menu_btn.clicked.connect(self.menu_func)
        self.logout_btn.clicked.connect(self.logout_func)
        self.home_btn.clicked.connect(lambda: self.swtich_page_func(0))
        self.recognize_btn.clicked.connect(lambda: self.swtich_page_func(1))
        self.report_btn.clicked.connect(lambda: self.swtich_page_func(2))
        self.chart_btn.clicked.connect(lambda: self.swtich_page_func(3))
        
        self.home_search_btn.clicked.connect(self.hp_search_func)
        # self.home_get_data_btn.clicked.connect(lambda: background_func(self.hp_get_data_func, ()))
        self.home_train_btn.clicked.connect(lambda: background_func(self.hp_training_func, ()))
        # self.recognize_guess_btn.clicked.connect(self.recp_show_guess_func)
        self.recognize_guess_btn.clicked.connect(self.start_capture_video)
        self.recognize_export_btn.clicked.connect(self.stop_capture_video)
        self.recognize_open_img_btn.clicked.connect(self.recp_open_image_to_guess_func)
        self.recognize_tab_1_btn.clicked.connect(lambda: self.recp_switch_subpage_func(0))
        self.recognize_tab_2_btn.clicked.connect(lambda: self.recp_switch_subpage_func(1))
        self.recognize_tab_3_btn.clicked.connect(lambda: self.recp_switch_subpage_func(2))
        self.report_search_btn.clicked.connect(self.repp_show_report_table_func)
        self.chart_show_btn.clicked.connect(self.chp_show_chart_func)
        self.attendance_exit_btn.clicked.connect(self.exit_func)
        self.thread = {}

    def logout_func(self):
        self.attendance_init()
        self.widget.setCurrentIndex(self.widget.currentIndex() - 1)
        self.widget.setWindowTitle(self.widget.currentWidget().objectName())
        self.widget.currentWidget().login_init() 
        
    def swtich_page_func(self, index):
        self.main_pages.setCurrentIndex(index)
        list_btns = [self.home_btn,self.recognize_btn,self.report_btn,self.chart_btn]
        for i in range(len(list_btns)):
            if i == index:
                list_btns[i].setStyleSheet(HauSettings.menu_btns_style(0,9,0,9,1,0,1,1))
            else:
                list_btns[i].setStyleSheet(HauSettings.menu_btns_style(9,9,9,9,1,1,1,1))

    def attendance_init(self):
        self.widget.move(109, 109)
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
        list_btns = [self.home_btn,self.recognize_btn,self.report_btn,self.chart_btn]
        list_pages = [self.home_page,self.recognize_page,self.report_page,self.chart_page]
        for i in range(len(list_btns)):
            if list_pages[i] == self.main_pages.currentWidget():
                list_btns[i].setStyleSheet(HauSettings.menu_btns_style(0,9,0,9,1,0,1,1))
            else:
                list_btns[i].setStyleSheet(HauSettings.menu_btns_style(9,9,9,9,1,1,1,1))

    def expand_menu(self):
        self.menu.setMinimumWidth(200)
        list_btns = [self.home_btn,self.recognize_btn,self.report_btn,self.chart_btn]
        list_btn_names = ["  Trang chủ","  Điểm danh","  Báo cáo","  Biểu đồ"]
        for i in range(len(list_btns)):
            list_btns[i].setStyleSheet(HauSettings.menu_btns_style(9,9,9,9,1,1,1,1))
            list_btns[i].setText(list_btn_names[i])
        self.menu_btn.setStyleSheet(HauSettings.menu_btns_style(9,9,0,0,1,1,1,1))
        self.menu_btn.setText("  MENU")
        self.logout_btn.setStyleSheet(HauSettings.menu_btns_style(0,0,9,9,1,1,1,1))
        self.logout_btn.setText("  ĐĂNG XUẤT")
        
    def collapse_menu(self):
        self.menu.setMinimumWidth(50)
        list_btns = [self.menu_btn,self.home_btn,self.recognize_btn,self.report_btn,self.chart_btn,self.logout_btn]
        for i in range(len(list_btns)):
            list_btns[i].setStyleSheet(HauSettings.menu_btns_style(9,9,9,9,1,1,1,1))
            list_btns[i].setText("")
        
    def menu_func(self):
        if self.menu.size().width() < 200:
            self.expand_menu()
        else:
            self.collapse_menu()
        self.sync_btn_page()
        

    # HOME PAGE
    def hp_init_func(self):
        self.hp_init_class_func("")
        self.home_class_input.setText("")
        self.home_table.setColumnWidth(0, 200)
        self.home_table.setColumnWidth(1, 400)
        self.home_table.setColumnWidth(2, 200)
        self.home_table.setColumnWidth(3, 200)
        self.home_table.setColumnWidth(4, 200)
        self.hp_show_table_func()
    
    def hp_init_class_func(self, name_of_class):
        self.class_id_name = name_of_class
        self.home_controllers.setStyleSheet("QWidget#home_controllers{background-image: url(./resources/apps/bg_header.png)}")
        self.model_name_label.setText(self.class_id_name + HauSettings.MODEL_FILE_EXTENSION)
        self.model_name_text = self.model_name_label.text()

    def hp_search_func(self):
        try:
            print("PRESS HOME SEARCH BUTTON")
            self.hp_init_class_func(self.home_class_input.text())
            self.hp_show_table_func()
        except:
            pass

    def hp_show_table_func(self):
        self.home_table.horizontalHeader().setVisible(True)
        datasv = self.collector.get_sv_by_class_id(self.class_id_name)
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
        self.dataset_path = os.path.join(self.collector.DATASETS_PATH,self.class_id_name)
        # self.home_get_data_btn.show()
        
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
            DatasetSupport.download_datasets_by_class_id(self.class_id_name, self.dataset_path, self.collector)
            self.model = HauModel(self.dataset_path, 1, self.class_id_name)
            self.model.training()
            self.model.evaluating()
            self.model.plot_train_history(os.path.join(self.collector.STATISTIC_PATH,self.class_id_name + ".png"))
            self.chp_show_chart_func()
            self.recp_init_func()
        except:
            pass


    # RECOGNITION PAGE
    def recp_init_func(self):
        self.recp_show_recognition_table_func([])
        self.recognize_img_path_input.setText("")
        if os.path.exists(self.collector.MODEL_DIR):
            self.recognize_models_box.addItems([m.split(".keras")[0] for m in os.listdir(self.collector.MODEL_DIR)])

        if self.recognize_models_box.count() > 0:
            self.recognize_guess_btn.show()
            self.recognize_tab_2_btn.show()
            self.recognize_tab_3_btn.show()
        else:
            self.recognize_guess_btn.hide()
            self.recognize_tab_2_btn.hide()
            self.recognize_tab_3_btn.hide()
        HauSettings.display_image_func(self.recognize_input_img_label, HauSettings.UNKNOWN_IMAGE_PATH)
        HauSettings.display_image_func(self.recognize_output_img_label, HauSettings.UNKNOWN_IMAGE_PATH)
        self.recp_switch_subpage_func(0)

    def recp_switch_subpage_func(self, index):
        print(f"PRESS RECOGNIZE PAGE {index} BUTTON")
        try:
            recognize_tab_btns = [self.recognize_tab_1_btn,self.recognize_tab_2_btn,self.recognize_tab_3_btn]
            for tab in recognize_tab_btns:
                tab.setStyleSheet(
                    "background-color: rgba(188, 188, 188, 100);border-radius: 5px;"
                )
            self.recognize_view.setCurrentIndex(index)
            recognize_tab_btns[index].setStyleSheet(
                "background-color: rgba(188, 188, 188, 255);border-radius: 5px;"
            )
        except:
            pass

    def recp_show_guess_func(self):
        print("PRESS RECOGNIZE GUESS BUTTON")
        try:
            self.dataset_path = os.path.join(self.collector.DATASETS_PATH,self.recognize_models_box.currentText())
            self.model = HauModel(self.dataset_path, 1, self.class_id_name) 
            self.model.load_model(self.recognize_models_box.currentText())
            if not HauSettings.check_cam():
                HauSettings.display_image_func(self.recognize_output_img_label, "")
                self.recp_switch_subpage_func(0)
            else:
                self.recp_switch_subpage_func(1)
                self.model.real_time_predict(os.listdir(self.dataset_path), self.model, self.recognize_models_box.currentText(), self.recognize_output_img_label)
        except:
            pass

    # BEGIN DISPLAY CAMERA SECTION
    def closeEvent(self, event):
        self.stop_capture_video()

    def stop_capture_video(self):
        self.thread[1].cam_enable = False
        face_guessed = list(dict.fromkeys(self.thread[1].face_guessed))
        self.recp_show_recognition_table_func(face_guessed)
        self.thread[1].stop()

    def start_capture_video(self):
        self.dataset_path = os.path.join(self.collector.DATASETS_PATH,self.recognize_models_box.currentText())
        self.model = HauModel(self.dataset_path, 1, self.class_id_name) 
        self.model.load_model(self.recognize_models_box.currentText())
        self.thread[1] = Thread_Video(1, os.listdir(self.dataset_path), self.model, self.recognize_output_img_label)
        self.thread[1].cam_enable = True
        self.thread[1].start()
        self.thread[1].signal.connect(self.show_wedcam)

    def show_wedcam(self, cv_img):
        """Updates the image_label with a new opencv image"""
        qt_img = self.convert_cv_qt(cv_img)
        self.recognize_output_img_label.setPixmap(qt_img)

    def convert_cv_qt(self, cv_img):
        """Convert from an opencv image to QPixmap"""
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(800, 600, Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)
    # END DISPLAY CAMERA SECTION

    def recp_show_recognition_table_func(self, guesses_indexes):
        try:
            self.recognize_table.horizontalHeader().setVisible(True)
            self.recognize_table.setRowCount(len(guesses_indexes))
            self.recognize_table.setSelectionBehavior(QAbstractItemView.SelectRows)
            self.recognize_table.setStyleSheet(
                "QTableView::item:selected { color:white; background:#000000; font-weight:900; }"
                "QHeaderView::section { color:white; background-color:#232326;}"
            )
            self.recognize_table.setColumnWidth(0, 200)
            for idx, guess in enumerate(guesses_indexes):
                itemColor = QTableWidgetItem()
                itemColor.setBackground(QBrush(QColor(255, 255, 255)))
                self.recognize_table.setItem(idx, 0, itemColor)
                # itemMSV = QTableWidgetItem(str(os.listdir(self.dataset_path)[guesses_indexes[idx]]))
                itemMSV = QTableWidgetItem(guess)
                
                itemMSV.setBackground(QBrush(QColor(255, 255, 255)))
                self.recognize_table.setItem(idx, 1, itemMSV)
        except:
            pass

    def recp_open_image_to_guess_func(self):
        print("PRESS RECOGNIZE OPEN FILE BUTTON")
        try:
            fname = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*)")
            if fname:
                self.img_guess_name = str(fname[0])
                self.recognize_img_path_input.setText(str(fname[0]))
                HauSettings.display_image_func(self.recognize_input_img_label, self.img_guess_name)
                self.recp_switch_subpage_func(0)
        except:
            pass


    # REPORT PAGE
    def repp_init_func(self):
        self.report_class_input.setText("")
        self.report_table.setColumnWidth(0, 200)
        self.report_table.setColumnWidth(1, 400)
        self.report_table.setColumnWidth(2, 200)
        self.report_table.setColumnWidth(3, 200)
        self.report_table.setColumnWidth(4, 200)
        self.repp_show_report_table_func()

    def repp_show_report_table_func(self):
        print("PRESS REPORT TABLE BUTTON")
        try:
            self.report_table.horizontalHeader().setVisible(True)
            datasv = self.collector.get_baocao_by_class_id(self.report_class_input.text())
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
        except:
            pass


    # CHART PAGE
    def chp_init_func(self):
        HauSettings.display_image_func(self.chart_result_img_label, HauSettings.UNKNOWN_IMAGE_PATH)

    def chp_show_chart_func(self):
        print("PRESS CHART MODEL BUTTON")
        try:
            HauSettings.display_image_func(self.chart_result_img_label, os.path.join(self.collector.STATISTIC_PATH, f"{self.chart_model_name_input.text()}.png"))
        except:
            HauSettings.display_image_func(self.chart_result_img_label, HauSettings.UNKNOWN_IMAGE_PATH)
        
        





