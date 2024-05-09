from main_importer import *
from ui_attendance import *
from Custom_Widgets.Widgets import * 
import time


gv_name, gv_pass = "",""
def background_func(func, args):
    th = threading.Thread(target=func, args=args)
    th.start()

class AttendanceWindow(QMainWindow):
    def __init__(self, widget):
        self.widget = widget
        super(AttendanceWindow, self).__init__()
        self.ui = Ui_Attendance()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui, jsonFiles={'style-client.json'})
        self.isRecording = False

        # ATTEDANCE ATTRIBUTE
        self.class_id = ""
        self.collector = CollectData.check_user(gv_name, gv_pass)
        self.thread = {}
        # self.ui.trainning_popup.expandMenu()
        
        # self.init_attendance()

    # COMMONS
    def init_attendance(self):
        self.setFixedWidth(1280)
        self.setFixedHeight(720)
        self.hp_init_page()
        self.repp_init_page()
        self.recp_init_page()
        self.swtich_page_func(0)
        self.init_suggesting_search()
        self.init_buttons()

    def init_buttons(self):
        self.ui.menu_btn.clicked.connect(self.menu_func)
        self.ui.logout_btn.clicked.connect(self.logout_func)
        self.ui.attendance_exit_btn.clicked.connect(QApplication.quit)
        self.ui.home_btn.clicked.connect(lambda: self.swtich_page_func(0))
        self.ui.recognize_btn.clicked.connect(lambda: self.swtich_page_func(1))
        self.ui.report_btn.clicked.connect(lambda: self.swtich_page_func(2))
        self.ui.home_search_btn.clicked.connect(self.hp_search_func)
        self.ui.home_train_btn.clicked.connect(lambda: background_func(self.hp_train_func, ()))
        self.ui.recognize_guess_btn.clicked.connect(self.start_capture_video)
        self.ui.recognize_export_btn.clicked.connect(self.stop_capture_video)
        self.ui.recognize_open_img_btn.clicked.connect(self.recp_open_image_to_guess_func)
        self.ui.recognize_delete_btn.clicked.connect(self.recp_delete_guess_func)
        self.ui.recognize_tab_1_btn.clicked.connect(lambda: self.recp_switch_subpage_func(0))
        self.ui.recognize_tab_2_btn.clicked.connect(lambda: self.recp_switch_subpage_func(1))
        self.ui.recognize_tab_3_btn.clicked.connect(lambda: self.recp_switch_subpage_func(2))
        self.ui.report_search_btn.clicked.connect(self.repp_init_table)
        self.ui.recognize_keep_btn.clicked.connect(self.recp_save_results)
        self.ui.recognize_refresh_btn.clicked.connect(self.recp_refresh_results)

    def logout_func(self):
        self.init_attendance()
        self.widget.setCurrentIndex(0)
        self.widget.currentWidget().login_init() 

    def init_suggesting_search(self):
        suggestion_list = self.collector.get_ds_malop()
        completer = QCompleter(suggestion_list, self.ui.home_class_input)
        self.ui.home_class_input.setCompleter(completer)

        completer = QCompleter(suggestion_list, self.ui.report_class_input)
        self.ui.report_class_input.setCompleter(completer)

        suggestion_list = self.collector.get_msv()
        completer = QCompleter(suggestion_list, self.ui.report_student_input)
        self.ui.report_student_input.setCompleter(completer)

    def swtich_page_func(self, index):
        self.ui.main_pages.setCurrentIndex(index)
        list_btns = [self.ui.home_btn,self.ui.recognize_btn,self.ui.report_btn]
        for i in range(len(list_btns)):
            if i == index:
                list_btns[i].setStyleSheet(HauSettings.menu_btns_style(0,9,0,9,1,0,1,1))
            else:
                list_btns[i].setStyleSheet(HauSettings.menu_btns_style(9,9,9,9,1,1,1,1))

    def sync_btn_page(self):
        list_btns = [self.ui.home_btn,self.ui.recognize_btn,self.ui.report_btn]
        list_pages = [self.ui.home_page,self.ui.recognize_page,self.ui.report_page]
        for i in range(len(list_btns)):
            if list_pages[i] == self.ui.main_pages.currentWidget():
                list_btns[i].setStyleSheet(HauSettings.menu_btns_style(0,9,0,9,1,0,1,1))
            else:
                list_btns[i].setStyleSheet(HauSettings.menu_btns_style(9,9,9,9,1,1,1,1))

    def expand_menu(self):
        self.ui.menu.setMinimumWidth(200)
        list_btns = [self.ui.home_btn,self.ui.recognize_btn,self.ui.report_btn]
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
        list_btns = [self.ui.menu_btn,self.ui.home_btn,self.ui.recognize_btn,self.ui.report_btn,self.ui.logout_btn]
        for i in range(len(list_btns)):
            list_btns[i].setStyleSheet(HauSettings.menu_btns_style(9,9,9,9,1,1,1,1))
            list_btns[i].setText("")
        
    def menu_func(self):
        if self.ui.menu.size().width() < 200:
            self.expand_menu()
        else:
            self.collapse_menu()
        self.sync_btn_page()


    # HOME
    def hp_init_page(self):
        self.ui.home_class_input.setText("")
        self.ui.model_model_label.setText(".keras")
        self.ui.home_class_input.textChanged.connect(lambda: self.ui.model_model_label.setText(self.ui.home_class_input.text() + ".keras"))
        self.hp_init_table()

    def hp_init_table(self, search=""):
        self.class_id = search
        self.ui.home_table.setColumnWidth(0, 200)
        self.ui.home_table.setColumnWidth(1, 400)
        self.ui.home_table.setColumnWidth(2, 200)
        self.ui.home_table.setColumnWidth(3, 200)
        self.ui.home_table.setColumnWidth(4, 200)
        self.ui.home_table.horizontalHeader().setVisible(True)
        datasv = self.collector.get_sv_by_class_id(search)
        row = 0
        HauSettings.custom_table(self.ui.home_table, len(datasv))
        for e in datasv:
            self.ui.home_table.setItem(row, 0, QTableWidgetItem(e['MaSV']))
            self.ui.home_table.setItem(row, 1, QTableWidgetItem(e['TenSV']))
            self.ui.home_table.setItem(row, 2, QTableWidgetItem(e['LopQL']))
            self.ui.home_table.setItem(row, 3, QTableWidgetItem(e['NgSinh']))
            self.ui.home_table.setItem(row, 4, QTableWidgetItem(e['SDT']))
            row += 1
        self.dataset_path = os.path.join(self.collector.DATASETS_PATH,search)

    def hp_search_func(self):
        self.hp_init_table(self.ui.home_class_input.text())
        self.ui.model_model_label.setText(self.class_id + ".keras")

    def hp_train_func(self):
        # print("hELO")
        # self.ui.trainning_popup.expandMenu()
        # return
        start = time.time()
        DatasetSupport.download_datasets_by_class_id(self.class_id, self.dataset_path, self.collector)
        self.model = HauModel(self.dataset_path, 100, self.class_id, model_dir=self.collector.MODEL_DIR)
        print(f"Download: {time.time() - start}")
        start = time.time()
        self.model.training()
        self.model.evaluating()
        self.recp_init_page()
        print(f"Training: {time.time() - start}")

        # dlg = QMessageBox(self)
        # dlg.setWindowTitle("I have a question!")
        # dlg.setText("This is a simple dialog")
        # button = dlg.exec()

        # if button == QMessageBox.Ok:
        #     print("OK!")


    # RECOGNIZE
    def recp_init_page(self):
        self.recp_show_recognition_table_func1([])
        self.ui.recognize_img_path_input.setText("")
        self.ui.recognize_models_box.clear()
        if os.path.exists(self.collector.MODEL_DIR):
            print(self.collector.MODEL_DIR)
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
            if self.ui.recognize_late_btn.isChecked():
                data['ghichu'] = "M"
            else:
                data['ghichu'] = ""

            requests.post(HauSettings.BASE_URL + "/giaovien/baocao", data)
        self.collector.user_api(self.collector.username_MGV)
        self.collector.update_api(data['malop'])
        self.recp_refresh_results()

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
            self.isRecording = False
        except:
            pass

    def start_capture_video(self):
        if self.ui.recognize_img_path_input.text() == "":
            if not self.isRecording:
                self.isRecording = True
                self.dataset_path = os.path.join(self.collector.DATASETS_PATH,self.ui.recognize_models_box.currentText())
                self.model = HauModel(self.dataset_path, 1, self.class_id, model_dir=self.collector.MODEL_DIR) 
                self.model.load_model(self.ui.recognize_models_box.currentText())
                self.thread[1] = Thread_Video(1, os.listdir(self.dataset_path), self.model, self.ui.recognize_output_img_label)
                self.thread[1].cam_enable = True
                self.thread[1].start()
                self.thread[1].signal.connect(self.show_wedcam)
                self.recp_switch_subpage_func(1)
        else:
            self.dataset_path = os.path.join(self.collector.DATASETS_PATH,self.ui.recognize_models_box.currentText())
            self.model = HauModel(self.dataset_path, 1, self.class_id, model_dir=self.collector.MODEL_DIR) 
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
        HauSettings.custom_table(self.ui.recognize_table, len(colors))
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
            HauSettings.custom_table(self.ui.recognize_table, len(guessed))
            self.ui.recognize_table.setColumnWidth(0, 200)
            for idx, guess in enumerate(guessed):
                itemColor = QTableWidgetItem()
                itemColor.setBackground(QBrush(QColor(255, 255, 255)))
                self.ui.recognize_table.setItem(idx, 0, itemColor)
                itemMSV = QTableWidgetItem(guess)
                
                itemMSV.setBackground(QBrush(QColor(255, 255, 255)))
                self.ui.recognize_table.setItem(idx, 1, itemMSV)
        except:
            pass

    def recp_delete_guess_func(self):
        del self.face_guessed[self.ui.recognize_table.currentRow()]
        self.recp_show_recognition_table_func1(self.face_guessed)

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


    # REPORT
    def repp_init_page(self):
        self.ui.report_class_input.setText("")
        self.ui.report_student_input.setText("")
        self.repp_init_table()
        self.ui.report_wrong_label.setText("")
    
    def repp_init_table(self, search_class="", search_student=""):
        search_class = self.ui.report_class_input.text()
        search_student = self.ui.report_student_input.text()
        self.ui.report_table.setColumnWidth(0, 200)
        self.ui.report_table.setColumnWidth(1, 400)
        self.ui.report_table.setColumnWidth(2, 200)
        self.ui.report_table.setColumnWidth(3, 200)
        self.ui.report_table.setColumnWidth(4, 200)
        self.ui.report_table.setColumnWidth(5, 200)
        
        datasv = []
        if search_student == "":
            datasv = self.collector.get_baocao_by_class_id(search_class)
        else:
            datasv = self.collector.get_baocao_detail(search_class,search_student)
        if len(datasv) == 0:
            self.ui.report_wrong_label.setText("Sai thông tin")
            self.ui.report_class_input.setText("")
            self.ui.report_student_input.setText("")
        else:
            self.ui.report_wrong_label.setText("")
            row = 0
            
            HauSettings.custom_table(self.ui.report_table, len(datasv))
            for e in datasv:
                self.ui.report_table.setItem(row, 0, QTableWidgetItem(e['MaSV']))
                self.ui.report_table.setItem(row, 1, QTableWidgetItem(e['TenSV']))
                self.ui.report_table.setItem(row, 2, QTableWidgetItem(e['LopQL']))
                self.ui.report_table.setItem(row, 3, QTableWidgetItem(e['MaLop']))
                self.ui.report_table.setItem(row, 4, QTableWidgetItem(str(e['DiemDanh'])))
                if search_student == "":
                    self.ui.report_table.setItem(row, 5, QTableWidgetItem(""))
                else:
                    self.ui.report_table.setItem(row, 5, QTableWidgetItem(str(e['GhiChu'])))
                row += 1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    attendanceWin = AttendanceWindow(widget)

    widget.addWidget(attendanceWin)

    widget.show()
    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")


