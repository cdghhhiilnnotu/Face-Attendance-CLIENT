from main_importer import *
from ui_admin import *
from Custom_Widgets.Widgets import * 
from PyQt5 import QtWidgets

class AdminWindow(QMainWindow):
    def __init__(self, widget):
        super(AdminWindow, self).__init__()
        # loadUi("attendance.ui", self)
        self.ui = Ui_Admin()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui)
        self.widget = widget
        self.admin_api = {}
        try:
            self.admin_api = requests.get(HauSettings.BASE_URL + f"/").json()
        except:
            print("No API or data found!")

        self.ui.menu_btn.clicked.connect(self.menu_func)
        self.ui.admins_btn.clicked.connect(lambda: self.swtich_page_func(0))
        self.ui.teachers_btn.clicked.connect(lambda: self.swtich_page_func(1))
        self.ui.students_btn.clicked.connect(lambda: self.swtich_page_func(2))
        self.ui.rooms_btn.clicked.connect(lambda: self.swtich_page_func(3))
        self.ui.reports_btn.clicked.connect(lambda: self.swtich_page_func(4))
        self.ui.reports_list_btn.clicked.connect(lambda: self.swtich_page_func(5))
        self.ui.admins_search_btn.clicked.connect(lambda: self.adp_show_table(self.ui.admins_input.text()))
        self.ui.teachers_search_btn.clicked.connect(lambda: self.tp_show_table(self.ui.teachers_input.text()))
        self.ui.students_search_btn.clicked.connect(lambda: self.sp_show_table(self.ui.students_input.text()))
        self.ui.rooms_search_btn.clicked.connect(lambda: self.roop_show_table(self.ui.rooms_input.text()))
        self.ui.reports_search_btn.clicked.connect(lambda: self.repp_show_table(self.ui.reports_input.text()))
        self.ui.reports_list_search_btn.clicked.connect(lambda: self.relp_show_table(self.ui.reports_list_input.text()))
        
        self.init_admin()

    def logout_func(self):
        pass
        
    def swtich_page_func(self, index):
        self.ui.main_pages.setCurrentIndex(index)
        list_btns = [self.ui.admins_btn,self.ui.teachers_btn,self.ui.students_btn,self.ui.rooms_btn,self.ui.reports_btn,self.ui.reports_list_btn]
        for i in range(len(list_btns)):
            if i == index:
                list_btns[i].setStyleSheet(HauSettings.menu_btns_style(0,9,0,9,1,0,1,1))
            else:
                list_btns[i].setStyleSheet(HauSettings.menu_btns_style(9,9,9,9,1,1,1,1))

    def init_buttons(self):
        self.ui.admins_add_btn.clicked.connect(self.adp_expand_popup)
        self.ui.admins_edit_btn.clicked.connect(self.adp_expand_popup)
        self.ui.admins_exit_btn.clicked.connect(self.adp_collapse_popup)
        self.ui.teachers_add_btn.clicked.connect(self.tp_expand_popup)
        self.ui.teachers_edit_btn.clicked.connect(self.tp_expand_popup)
        self.ui.teachers_exit_btn.clicked.connect(self.tp_collapse_popup)
        self.ui.students_add_btn.clicked.connect(self.sp_expand_popup)
        self.ui.students_edit_btn.clicked.connect(self.sp_expand_popup)
        self.ui.students_exit_btn.clicked.connect(self.sp_collapse_popup)
        self.ui.rooms_add_btn.clicked.connect(self.roop_expand_popup)
        self.ui.rooms_edit_btn.clicked.connect(self.roop_expand_popup)
        self.ui.rooms_exit_btn.clicked.connect(self.roop_collapse_popup)
        self.ui.reports_add_btn.clicked.connect(self.repp_expand_popup)
        self.ui.reports_edit_btn.clicked.connect(self.repp_expand_popup)
        self.ui.reports_exit_btn.clicked.connect(self.repp_collapse_popup)
        self.ui.reports_list_add_btn.clicked.connect(self.relp_expand_popup)
        self.ui.reports_list_edit_btn.clicked.connect(self.relp_expand_popup)
        self.ui.reports_list_exit_btn.clicked.connect(self.relp_collapse_popup)

    

    # TITLE ADMIN
    def exit_func(self):
        QApplication.quit()


    # MAIN ADMIN
    def sync_btn_page(self):
        list_btns = [self.ui.admins_btn,self.ui.teachers_btn,self.ui.students_btn,self.ui.rooms_btn,self.ui.reports_btn,self.ui.reports_list_btn]
        list_pages = [self.ui.admins_page,self.ui.teachers_page,self.ui.students_page,self.ui.rooms_page,self.ui.reports_page,self.ui.reports_list_page]
        for i in range(len(list_btns)):
            if list_pages[i] == self.ui.main_pages.currentWidget():
                list_btns[i].setStyleSheet(HauSettings.menu_btns_style(0,9,0,9,1,0,1,1))
            else:
                list_btns[i].setStyleSheet(HauSettings.menu_btns_style(9,9,9,9,1,1,1,1))

    def expand_menu(self):
        # print("EXPAND")
        self.ui.menu.setMinimumWidth(200)
        list_btns = [self.ui.admins_btn,self.ui.teachers_btn,self.ui.students_btn,self.ui.rooms_btn,self.ui.reports_btn,self.ui.reports_list_btn]
        list_btn_names = [" Quản trị viên"," Giảng viên"," Sinh viên"," Lớp học", " Báo cáo SV", " DS báo cáo"]
        for i in range(len(list_btns)):
            list_btns[i].setStyleSheet(HauSettings.menu_btns_style(9,9,9,9,1,1,1,1))
            list_btns[i].setText(list_btn_names[i])
        self.ui.menu_btn.setStyleSheet(HauSettings.menu_btns_style(9,9,0,0,1,1,1,1))
        self.ui.menu_btn.setText(" MENU")
        self.ui.logout_btn.setStyleSheet(HauSettings.menu_btns_style(0,0,9,9,1,1,1,1))
        self.ui.logout_btn.setText(" ĐĂNG XUẤT")
        pass
        
    def collapse_menu(self):
        # print("COLLAPSE")
        self.ui.menu.setMinimumWidth(50)
        list_btns = [self.ui.admins_btn,self.ui.teachers_btn,self.ui.students_btn,self.ui.rooms_btn,self.ui.reports_btn,self.ui.reports_list_btn,self.ui.menu_btn,self.ui.logout_btn]
        for i in range(len(list_btns)):
            list_btns[i].setStyleSheet(HauSettings.menu_btns_style(9,9,9,9,1,1,1,1))
            list_btns[i].setText("")
        # pass
        
    def menu_func(self):
        if self.ui.menu.size().width() < 200:
            self.expand_menu()
        else:
            self.collapse_menu()
        # print("MENU")
        self.sync_btn_page()

    def init_searching(self):
        suggestion_list = ["apple", "banana", "cherry", "grape", "orange", "pear", "pineapple"]

        completer = QCompleter(suggestion_list, self.ui.admins_input)
        self.ui.admins_input.setCompleter(completer)

    def init_admin(self):
        self.ui.popupWidget.collapseMenu()
        self.setFixedWidth(1280)
        self.setFixedHeight(720)
        self.collapse_menu()
        self.init_searching()
        self.adp_init()
        self.tp_init()
        self.sp_init()
        self.roop_init()
        self.repp_init()
        self.relp_init()
        self.init_buttons()
    
    # ADMIN PAGE
    def adp_init(self):
        self.adp_init_table()
        self.adp_show_table("")
        
    def adp_init_table(self):
        self.ui.admins_table.setColumnWidth(0, 400)
        self.ui.admins_table.setColumnWidth(1, 400)
        self.ui.admins_table.setColumnWidth(2, 400)
        self.ui.admins_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.admins_table.setStyleSheet(
            "QTableView::item:selected { color:white; background:#000000; font-weight:900; }"
            "QTableView::item { color:black; background:#fff;}"
            "QHeaderView::section { color:white; background-color:#232326;}"
        )

    def adp_show_table(self, search_str):
        data_admin = self.admin_api['admin']
        if search_str != "":
            specific_data = [admin for admin in data_admin if admin['MaAD'] == search_str]
            self.ui.admins_table.setRowCount(len(specific_data))
            row = 0
            for e in specific_data:
                self.ui.admins_table.setItem(row, 0, QTableWidgetItem(e['MaAD']))
                self.ui.admins_table.setItem(row, 1, QTableWidgetItem(e['TenDN']))
                self.ui.admins_table.setItem(row, 2, QTableWidgetItem(e['MatKhau']))
                row += 1
        else:
            self.ui.admins_table.setRowCount(len(data_admin))
            row = 0
            for e in data_admin:
                self.ui.admins_table.setItem(row, 0, QTableWidgetItem(e['MaAD']))
                self.ui.admins_table.setItem(row, 1, QTableWidgetItem(e['TenDN']))
                self.ui.admins_table.setItem(row, 2, QTableWidgetItem(e['MatKhau']))
                row += 1

    def adp_expand_popup(self):
        self.ui.popupWidget.expandMenu()
        self.ui.popupPages.setCurrentIndex(0)

    def adp_collapse_popup(self):
        self.ui.popupWidget.collapseMenu()



    # TEACHER PAGE
    def tp_init(self):
        self.tp_init_table()
        self.tp_show_table("")
        
    def tp_init_table(self):
        self.ui.teachers_table.setColumnWidth(0, 400)
        self.ui.teachers_table.setColumnWidth(1, 600)
        self.ui.teachers_table.setColumnWidth(2, 300)
        self.ui.teachers_table.setColumnWidth(3, 400)
        self.ui.teachers_table.setColumnWidth(4, 400)
        self.ui.teachers_table.setColumnWidth(5, 400)
        self.ui.teachers_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.teachers_table.setStyleSheet(
            "QTableView::item:selected { color:white; background:#000000; font-weight:900; }"
            "QTableView::item { color:black; background:#fff;}"
            "QHeaderView::section { color:white; background-color:#232326;}"
        )

    def tp_show_table(self, search_str):
        data_teacher = self.admin_api['giaovien']
        if search_str != "":
            specific_data = [teacher for teacher in data_teacher if teacher['MaGV'] == search_str]
            self.ui.teachers_table.setRowCount(len(specific_data))
            
        else:
            specific_data = data_teacher
            self.ui.teachers_table.setRowCount(len(data_teacher))
        row = 0
        for e in specific_data:
                self.ui.teachers_table.setItem(row, 0, QTableWidgetItem(e['MaGV']))
                self.ui.teachers_table.setItem(row, 1, QTableWidgetItem(e['TenGV']))
                self.ui.teachers_table.setItem(row, 2, QTableWidgetItem(e['NgSinh']))
                self.ui.teachers_table.setItem(row, 3, QTableWidgetItem(e['DiaChi']))
                self.ui.teachers_table.setItem(row, 4, QTableWidgetItem(e['MatKhau']))
                self.ui.teachers_table.setItem(row, 5, QTableWidgetItem(e['SDT']))
                row += 1

    def tp_expand_popup(self):
        self.ui.popupWidget.expandMenu()
        self.ui.popupPages.setCurrentIndex(1)

    def tp_collapse_popup(self):
        self.ui.popupWidget.collapseMenu()


    # STUDENT PAGE
    def sp_init(self):
        self.sp_init_table()
        self.sp_show_table("")
        
    def sp_init_table(self):
        self.ui.students_table.setColumnWidth(0, 400)
        self.ui.students_table.setColumnWidth(1, 600)
        self.ui.students_table.setColumnWidth(2, 300)
        self.ui.students_table.setColumnWidth(3, 300)
        self.ui.students_table.setColumnWidth(4, 400)
        self.ui.students_table.setColumnWidth(5, 400)
        self.ui.students_table.setColumnWidth(6, 400)
        self.ui.students_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.students_table.setStyleSheet(
            "QTableView::item:selected { color:white; background:#000000; font-weight:900; }"
            "QTableView::item { color:black; background:#fff;}"
            "QHeaderView::section { color:white; background-color:#232326;}"
        )

    def sp_show_table(self, search_str):
        data_student = self.admin_api['sinhvien']
        if search_str != "":
            specific_data = [student for student in data_student if student['MaSV'] == search_str]
            self.ui.students_table.setRowCount(len(specific_data))
            
        else:
            specific_data = data_student
            self.ui.students_table.setRowCount(len(data_student))
        row = 0
        for e in specific_data:
                self.ui.students_table.setItem(row, 0, QTableWidgetItem(e['MaSV']))
                self.ui.students_table.setItem(row, 1, QTableWidgetItem(e['TenSV']))
                self.ui.students_table.setItem(row, 2, QTableWidgetItem(e['NgSinh']))
                self.ui.students_table.setItem(row, 3, QTableWidgetItem(e['LopQL']))
                self.ui.students_table.setItem(row, 4, QTableWidgetItem(e['DiaChi']))
                self.ui.students_table.setItem(row, 5, QTableWidgetItem(e['LinkAnh']))
                self.ui.students_table.setItem(row, 6, QTableWidgetItem(e['SDT']))
                row += 1
            
    def sp_expand_popup(self):
        self.ui.popupWidget.expandMenu()
        self.ui.popupPages.setCurrentIndex(2)

    def sp_collapse_popup(self):
        self.ui.popupWidget.collapseMenu()
    

    # ROOM PAGE
    def roop_init(self):
        self.roop_init_table()
        self.roop_show_table("")
    
    def roop_init_table(self):
        self.ui.rooms_table.setColumnWidth(0, 400)
        self.ui.rooms_table.setColumnWidth(1, 700)
        self.ui.rooms_table.setColumnWidth(2, 400)
        self.ui.rooms_table.setColumnWidth(3, 600)
        self.ui.rooms_table.setColumnWidth(4, 300)
        self.ui.rooms_table.setColumnWidth(5, 200)
        self.ui.rooms_table.setColumnWidth(6, 200)
        self.ui.rooms_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.rooms_table.setStyleSheet(
            "QTableView::item:selected { color:white; background:#000000; font-weight:900; }"
            "QTableView::item { color:black; background:#fff;}"
            "QHeaderView::section { color:white; background-color:#232326;}"
        )

    def roop_show_table(self, search_str):
        data_room = self.admin_api['lophoc']
        if search_str != "":
            specific_data = [room for room in data_room if room['MaLop'] == search_str]
            self.ui.rooms_table.setRowCount(len(specific_data))
            
        else:
            specific_data = data_room
            self.ui.rooms_table.setRowCount(len(data_room))
        row = 0
        for e in specific_data:
                self.ui.rooms_table.setItem(row, 0, QTableWidgetItem(e['MaLop']))
                self.ui.rooms_table.setItem(row, 1, QTableWidgetItem(e['TenMon']))
                self.ui.rooms_table.setItem(row, 2, QTableWidgetItem(e['MaGV']))
                self.ui.rooms_table.setItem(row, 3, QTableWidgetItem(e['LichHoc']))
                self.ui.rooms_table.setItem(row, 4, QTableWidgetItem(e['PhongHoc']))
                self.ui.rooms_table.setItem(row, 5, QTableWidgetItem(e['SoluongSV']))
                self.ui.rooms_table.setItem(row, 6, QTableWidgetItem(e['SoNgay']))
                row += 1
    
    def roop_expand_popup(self):
        self.ui.popupWidget.expandMenu()
        self.ui.popupPages.setCurrentIndex(3)

    def roop_collapse_popup(self):
        self.ui.popupWidget.collapseMenu()


    # REPORT PAGE
    def repp_init(self):
        self.repp_init_table()
        self.repp_show_table("")

    def repp_init_table(self):
        self.ui.reports_table.setColumnWidth(0, 400)
        self.ui.reports_table.setColumnWidth(1, 400)
        self.ui.reports_table.setColumnWidth(2, 400)
        self.ui.reports_table.setColumnWidth(3, 400)
        self.ui.reports_table.setColumnWidth(4, 400)
        self.ui.reports_table.setColumnWidth(5, 500)
        self.ui.reports_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.reports_table.setStyleSheet(
            "QTableView::item:selected { color:white; background:#000000; font-weight:900; }"
            "QTableView::item { color:black; background:#fff;}"
            "QHeaderView::section { color:white; background-color:#232326;}"
        )

    def repp_show_table(self, search_str):
        data_report = self.admin_api['baocao']
        if search_str != "":
            specific_data = [report for report in data_report if report['MaLop'] == search_str or report['MaSV'] == search_str]
            self.ui.reports_table.setRowCount(len(specific_data))
            
        else:
            specific_data = data_report
            self.ui.reports_table.setRowCount(len(data_report))
        row = 0
        for e in specific_data:
                self.ui.reports_table.setItem(row, 0, QTableWidgetItem(e['MaBC']))
                self.ui.reports_table.setItem(row, 1, QTableWidgetItem(e['NgayBC']))
                self.ui.reports_table.setItem(row, 2, QTableWidgetItem(e['MaSV']))
                self.ui.reports_table.setItem(row, 3, QTableWidgetItem(e['MaLop']))
                self.ui.reports_table.setItem(row, 4, QTableWidgetItem(e['DiemDanh']))
                self.ui.reports_table.setItem(row, 5, QTableWidgetItem(e['GhiChu']))
                row += 1

    def repp_expand_popup(self):
        self.ui.popupWidget.expandMenu()
        self.ui.popupPages.setCurrentIndex(4)

    def repp_collapse_popup(self):
        self.ui.popupWidget.collapseMenu()


    # REPORT LIST PAGE
    def relp_init(self):
        self.relp_init_table()
        self.relp_show_table("")
        
    def relp_init_table(self):
        self.ui.reports_list_table.setColumnWidth(0, 400)
        self.ui.reports_list_table.setColumnWidth(1, 400)
        self.ui.reports_list_table.setColumnWidth(2, 400)
        self.ui.reports_list_table.setColumnWidth(3, 200)
        self.ui.reports_list_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.reports_list_table.setStyleSheet(
            "QTableView::item:selected { color:white; background:#000000; font-weight:900; }"
            "QTableView::item { color:black; background:#fff;}"
            "QHeaderView::section { color:white; background-color:#232326;}"
        )

    def relp_show_table(self, search_str):
        data_reports_list = self.admin_api['dslop']
        if search_str != "":
            specific_data = [reports_list for reports_list in data_reports_list if reports_list['MaLop'] == search_str or reports_list['MaSV'] == search_str]
            self.ui.reports_list_table.setRowCount(len(specific_data))
            
        else:
            specific_data = data_reports_list
            self.ui.reports_list_table.setRowCount(len(data_reports_list))
        row = 0
        for e in specific_data:
                self.ui.reports_list_table.setItem(row, 0, QTableWidgetItem(e['MaDS']))
                self.ui.reports_list_table.setItem(row, 1, QTableWidgetItem(e['MaLop']))
                self.ui.reports_list_table.setItem(row, 2, QTableWidgetItem(e['MaSV']))
                self.ui.reports_list_table.setItem(row, 3, QTableWidgetItem(e['SoDD']))
                row += 1

    def relp_expand_popup(self):
        self.ui.popupWidget.expandMenu()
        self.ui.popupPages.setCurrentIndex(5)

    def relp_collapse_popup(self):
        self.ui.popupWidget.collapseMenu()
        

    # HOME PAGE
    def hp_init_func(self):
        # self.hp_init_class_func("")
        # self.ui.home_class_input.setText("")
        # self.ui.home_table.setColumnWidth(0, 200)
        # self.ui.home_table.setColumnWidth(1, 400)
        # self.ui.home_table.setColumnWidth(2, 200)
        # self.ui.home_table.setColumnWidth(3, 200)
        # self.ui.home_table.setColumnWidth(4, 200)
        # self.hp_show_table_func()
        pass
    
    def hp_init_class_func(self, name_of_class):
        # self.class_id_name = name_of_class
        # # self.ui.home_controllers.setStyleSheet("QWidget#home_controllers{background-image: url(./resources/apps/bg_header.png)}")
        # # self.ui.recognize_controllers.setStyleSheet("QWidget#recognize_controllers{background-image: url(./resources/apps/bg_header.png)}")
        # # self.ui.report_controllers.setStyleSheet("QWidget#report_controllers{background-image: url(./resources/apps/bg_header.png)}")
        # # self.ui.chart_controllers.setStyleSheet("QWidget#chart_controllers{background-image: url(./resources/apps/bg_header.png)}")
        # self.ui.model_name_label.setText(self.class_id_name + HauSettings.MODEL_FILE_EXTENSION)
        # self.model_name_text = self.ui.model_name_label.text()
        pass

    def hp_search_func(self):
        # try:
        #     print("PRESS HOME SEARCH BUTTON")
        #     self.hp_init_class_func(self.ui.home_class_input.text())
        #     self.hp_show_table_func()
        # except:
        #     pass
        pass

    def hp_show_table_func(self):
        # self.ui.home_table.horizontalHeader().setVisible(True)
        # datasv = self.collector.get_sv_by_class_id(self.class_id_name)
        # row = 0
        # self.ui.home_table.setRowCount(len(datasv))
        # self.ui.home_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        # self.ui.home_table.setStyleSheet(
        #     "QTableView::item:selected { color:white; background:#000000; font-weight:900; }"
        #     "QTableView::item { color:black; background:#fff;}"
        #     "QHeaderView::section { color:white; background-color:#232326;}"
        # )
        # for e in datasv:
        #     self.ui.home_table.setItem(row, 0, QTableWidgetItem(e['MaSV']))
        #     self.ui.home_table.setItem(row, 1, QTableWidgetItem(e['TenSV']))
        #     self.ui.home_table.setItem(row, 2, QTableWidgetItem(e['LopQL']))
        #     self.ui.home_table.setItem(row, 3, QTableWidgetItem(e['NgSinh']))
        #     self.ui.home_table.setItem(row, 4, QTableWidgetItem(e['SDT']))
        #     row += 1
        # self.dataset_path = os.path.join(self.collector.DATASETS_PATH,self.class_id_name)
        # # self.ui.home_get_data_btn.show()
        pass
        
    def hp_get_data_func(self):
        # print("PRESS HOME GET DATA BUTTON")
        # try:
        #     DatasetSupport.download_datasets_by_class_id(self.class_id_name, self.dataset_path, self.collector)
        #     # self.home_train_btn.show()
        # except:
        #     pass
        pass

    def hp_training_func(self):
        # print("PRESS HOME TRAIN BUTTON")
        # try:
        #     if not self.isTraining:
        #         self.isTraining = True
        #         DatasetSupport.download_datasets_by_class_id(self.class_id_name, self.dataset_path, self.collector)
        #         self.model = HauModel(self.dataset_path, 1, self.class_id_name, model_dir=self.collector.MODEL_DIR)
        #         self.model.training()
        #         self.model.evaluating()
        #         self.model.plot_train_history(os.path.join(self.collector.STATISTIC_PATH,self.class_id_name + ".png"))
        #         # self.chp_show_chart_func()
        #         self.recp_init_func()
        #         self.isTraining = False
        # except:
        #     pass
        pass


    # RECOGNITION PAGE
    def recp_init_func(self):
        # self.recp_show_recognition_table_func1([])
        # self.ui.recognize_img_path_input.setText("")
        # self.ui.recognize_models_box.clear()
        # if os.path.exists(self.collector.MODEL_DIR):
        #     print(self.collector.MODEL_DIR)
        #     self.ui.recognize_models_box.addItems([m.split(".keras")[0] for m in os.listdir(self.collector.MODEL_DIR)])

        # if self.ui.recognize_models_box.count() > 0:
        #     self.ui.recognize_guess_btn.show()
        #     self.ui.recognize_tab_2_btn.show()
        #     self.ui.recognize_tab_3_btn.show()
        # else:
        #     self.ui.recognize_guess_btn.hide()
        #     self.ui.recognize_tab_2_btn.hide()
        #     self.ui.recognize_tab_3_btn.hide()
        # HauSettings.display_image_func(self.ui.recognize_input_img_label, HauSettings.UNKNOWN_IMAGE_PATH)
        # HauSettings.display_image_func(self.ui.recognize_output_img_label, HauSettings.UNKNOWN_IMAGE_PATH)
        # self.recp_switch_subpage_func(0)
        pass

    def recp_switch_subpage_func(self, index):
        # print(f"PRESS RECOGNIZE PAGE {index} BUTTON")
        # try:
        #     recognize_tab_btns = [self.ui.recognize_tab_1_btn,self.ui.recognize_tab_2_btn,self.ui.recognize_tab_3_btn]
        #     for tab in recognize_tab_btns:
        #         tab.setStyleSheet(
        #             "background-color: rgba(188, 188, 188, 100);border-radius: 5px;"
        #         )
        #     self.ui.recognize_view.setCurrentIndex(index)
        #     recognize_tab_btns[index].setStyleSheet(
        #         "background-color: rgba(188, 188, 188, 255);border-radius: 5px;"
        #     )
        # except:
        #     pass
        pass

    def recp_save_results(self):
        # for face_masv in self.face_guessed:
        #     data = {}
        #     data['masv'] = face_masv
        #     data['malop'] = self.ui.recognize_models_box.currentText()
        #     data['ghichu'] = "M"
        #     requests.post(HauSettings.BASE_URL + "/giaovien/baocao", data)
        # self.collector.user_api(self.collector.username_MGV)
        # self.collector.update_api(data['malop'])
        pass

    def recp_refresh_results(self):
        # self.recp_show_recognition_table_func1([])
        # self.ui.recognize_img_path_input.setText("")
        # HauSettings.display_image_func(self.ui.recognize_output_img_label, HauSettings.UNKNOWN_IMAGE_PATH)
        pass

    # BEGIN DISPLAY CAMERA SECTION
    def closeEvent(self, event):
        # self.stop_capture_video()
        pass

    def stop_capture_video(self):
        # try:
        #     self.thread[1].cam_enable = False
        #     self.face_guessed = list(dict.fromkeys(self.thread[1].face_guessed))
        #     self.recp_show_recognition_table_func1(self.face_guessed)
        #     self.thread[1].stop()
        #     self.recp_switch_subpage_func(2)
        # except:
        #     pass
        pass

    def start_capture_video(self):
        # if self.ui.recognize_img_path_input.text() == "":
        #     if not self.isRecording:
        #         self.isRecording = True
        #         self.dataset_path = os.path.join(self.collector.DATASETS_PATH,self.ui.recognize_models_box.currentText())
        #         self.model = HauModel(self.dataset_path, 1, self.class_id_name, model_dir=self.collector.MODEL_DIR) 
        #         self.model.load_model(self.ui.recognize_models_box.currentText())
        #         self.thread[1] = Thread_Video(1, os.listdir(self.dataset_path), self.model, self.ui.recognize_output_img_label)
        #         self.thread[1].cam_enable = True
        #         self.thread[1].start()
        #         self.thread[1].signal.connect(self.show_wedcam)
        #         self.recp_switch_subpage_func(1)
        # else:
        #     self.dataset_path = os.path.join(self.collector.DATASETS_PATH,self.ui.recognize_models_box.currentText())
        #     self.model = HauModel(self.dataset_path, 1, self.class_id_name, model_dir=self.collector.MODEL_DIR) 
        #     self.model.load_model(self.ui.recognize_models_box.currentText())
        #     file_name, colors, guessed = self.model.guessing_img(self.dataset_path, self.ui.recognize_img_path_input.text(), self.model, self.ui.recognize_models_box.currentText(), self.collector)
        #     self.recp_show_recognition_table_func2(colors, guessed)
        #     self.face_guessed = list(dict.fromkeys(guessed))
        #     HauSettings.display_image_func(self.ui.recognize_output_img_label, file_name)
        pass


    def show_wedcam(self, cv_img):
        # """Updates the image_label with a new opencv image"""
        # qt_img = self.convert_cv_qt(cv_img)
        # self.ui.recognize_output_img_label.setPixmap(qt_img)
        pass

    def convert_cv_qt(self, cv_img):
        # """Convert from an opencv image to QPixmap"""
        # rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        # h, w, ch = rgb_image.shape
        # bytes_per_line = ch * w
        # convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        # p = convert_to_Qt_format.scaled(800, 600, Qt.KeepAspectRatio)
        # return QPixmap.fromImage(p)
        pass
    # END DISPLAY CAMERA SECTION

    def recp_show_recognition_table_func2(self, colors, guesses_indexes):
        # self.ui.recognize_table.horizontalHeader().setVisible(True)
        # self.ui.recognize_table.setRowCount(len(colors))
        # self.ui.recognize_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        # self.ui.recognize_table.setStyleSheet(
        #     "QTableView::item:selected { color:white; background:#000000; font-weight:900; }"
        #     "QHeaderView::section { color:white; background-color:#232326;}"
        # )
        # self.ui.recognize_table.setColumnWidth(0, 200)
        # for idx, color in enumerate(colors):
        #     itemColor = QTableWidgetItem()
        #     itemColor.setBackground(QBrush(QColor(color[2], color[1], color[0])))
        #     self.ui.recognize_table.setItem(idx, 0, itemColor)
        #     itemMSV = QTableWidgetItem(str(os.listdir(self.dataset_path)[guesses_indexes[idx]]))
        #     itemMSV.setBackground(QBrush(QColor(255, 255, 255)))
        #     self.ui.recognize_table.setItem(idx, 1, itemMSV)
        pass

    def recp_show_recognition_table_func1(self, guessed):
        # try:
        #     self.ui.recognize_table.horizontalHeader().setVisible(True)
        #     self.ui.recognize_table.setRowCount(len(guessed))
        #     self.ui.recognize_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        #     self.ui.recognize_table.setStyleSheet(
        #         "QTableView::item:selected { color:white; background:#000000; font-weight:900; }"
        #         "QHeaderView::section { color:white; background-color:#232326;}"
        #     )
        #     self.ui.recognize_table.setColumnWidth(0, 200)
        #     for idx, guess in enumerate(guessed):
        #         itemColor = QTableWidgetItem()
        #         itemColor.setBackground(QBrush(QColor(255, 255, 255)))
        #         self.ui.recognize_table.setItem(idx, 0, itemColor)
        #         # itemMSV = QTableWidgetItem(str(os.listdir(self.ui.dataset_path)[self.face_guessed[idx]]))
        #         itemMSV = QTableWidgetItem(guess)
                
        #         itemMSV.setBackground(QBrush(QColor(255, 255, 255)))
        #         self.ui.recognize_table.setItem(idx, 1, itemMSV)
        # except:
        #     pass
        pass

    def recp_open_image_to_guess_func(self):
        # print("PRESS RECOGNIZE OPEN FILE BUTTON")
        # try:
        #     fname = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*)")
        #     if fname:
        #         self.img_guess_name = str(fname[0])
        #         self.ui.recognize_img_path_input.setText(str(fname[0]))
        #         HauSettings.display_image_func(self.ui.recognize_input_img_label, self.img_guess_name)
        #         self.recp_switch_subpage_func(0)
        # except:
        #     pass
        pass


    # REPORT PAGE
    def repp_init_func(self):
        # self.ui.report_class_input.setText("")
        # self.ui.report_table.setColumnWidth(0, 200)
        # self.ui.report_table.setColumnWidth(1, 400)
        # self.ui.report_table.setColumnWidth(2, 200)
        # self.ui.report_table.setColumnWidth(3, 200)
        # self.ui.report_table.setColumnWidth(4, 200)
        # self.repp_show_report_table_func()
        pass

    def repp_show_report_table_func(self):
        # print("PRESS REPORT TABLE BUTTON")
        # try:
        #     self.ui.report_table.horizontalHeader().setVisible(True)
        #     datasv = self.collector.get_baocao_by_class_id(self.ui.report_class_input.text())
        #     row = 0
        #     self.ui.report_table.setRowCount(len(datasv))
        #     self.ui.report_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        #     self.ui.report_table.setStyleSheet(
        #         "QTableView::item:selected { color:white; background:#000000; font-weight:900; }"
        #         "QTableView::item { color:black; background:#fff; }"
        #         "QHeaderView::section { color:white; background-color:#232326; }"
        #     )
        #     for e in datasv:
        #         self.ui.report_table.setItem(row, 0, QTableWidgetItem(e['MaSV']))
        #         self.ui.report_table.setItem(row, 1, QTableWidgetItem(e['TenSV']))
        #         self.ui.report_table.setItem(row, 2, QTableWidgetItem(e['LopQL']))
        #         self.ui.report_table.setItem(row, 3, QTableWidgetItem(e['MaLop']))
        #         self.ui.report_table.setItem(row, 4, QTableWidgetItem(str(e['DiemDanh'])))
        #         row += 1
        # except:
        #     pass
        pass


    # CHART PAGE
    def chp_init_func(self):
        # self.ui.chart_model_name_input.setText("")
        # HauSettings.display_image_func(self.ui.chart_result_img_label, HauSettings.UNKNOWN_IMAGE_PATH)
        pass

    def chp_show_chart_func(self):
        # print("PRESS CHART MODEL BUTTON")
        # try:
        #     HauSettings.display_image_func(self.ui.chart_result_img_label, os.path.join(self.collector.STATISTIC_PATH, f"{self.ui.chart_model_name_input.text()}.png"))
        # except:
        #     HauSettings.display_image_func(self.ui.chart_result_img_label, HauSettings.UNKNOWN_IMAGE_PATH)
        pass
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    adminWin = AdminWindow(widget)

    widget.addWidget(adminWin)

    widget.show()
    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")



