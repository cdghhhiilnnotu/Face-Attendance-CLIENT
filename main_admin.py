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
        loadJsonStyle(self, self.ui, jsonFiles={'style-admin.json'})
        self.widget = widget
        self.admin_api = {}
        self.reset_api()
        self.admin_save_mode = ""
        self.teacher_save_mode = ""
        self.student_save_mode = ""
        self.room_save_mode = ""
        self.report_save_mode = ""
        self.report_list_save_mode = ""

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

        self.ui.admins_del_btn.clicked.connect(self.adp_delete_func)
        self.ui.teachers_del_btn.clicked.connect(self.tp_delete_func)
        self.ui.students_del_btn.clicked.connect(self.sp_delete_func)
        self.ui.rooms_del_btn.clicked.connect(self.roop_delete_func)
        self.ui.reports_del_btn.clicked.connect(self.repp_delete_func)
        self.ui.reports_list_del_btn.clicked.connect(self.relp_delete_func)
        
        self.init_admin()

    def reset_api(self):
        try:
            self.admin_api = requests.get(HauSettings.BASE_URL + f"/").json()
        except:
            print("No API or data found!")

    def logout_func(self):
        self.widget.setCurrentIndex(0)
        self.widget.currentWidget().login_init() 
        
    def swtich_page_func(self, index):
        self.ui.main_pages.setCurrentIndex(index)
        list_btns = [self.ui.admins_btn,self.ui.teachers_btn,self.ui.students_btn,self.ui.rooms_btn,self.ui.reports_btn,self.ui.reports_list_btn]
        for i in range(len(list_btns)):
            if i == index:
                list_btns[i].setStyleSheet(HauSettings.menu_btns_style(0,9,0,9,1,0,1,1))
            else:
                list_btns[i].setStyleSheet(HauSettings.menu_btns_style(9,9,9,9,1,1,1,1))

    def init_popup_buttons(self):
        self.ui.admins_add_btn.clicked.connect(lambda: self.adp_expand_popup('add'))
        self.ui.admins_edit_btn.clicked.connect(lambda: self.adp_expand_popup('edit'))
        self.ui.admins_exit_btn.clicked.connect(lambda: self.adp_collapse_popup('exit'))
        self.ui.admin_save_btn.clicked.connect(lambda: self.adp_collapse_popup('save'))

        self.ui.teachers_add_btn.clicked.connect(lambda: self.tp_expand_popup('add'))
        self.ui.teachers_edit_btn.clicked.connect(lambda: self.tp_expand_popup('edit'))
        self.ui.teachers_exit_btn.clicked.connect(lambda: self.tp_collapse_popup('exit'))
        self.ui.teacher_save_btn.clicked.connect(lambda: self.tp_collapse_popup('save'))

        self.ui.students_add_btn.clicked.connect(lambda: self.sp_expand_popup('add'))
        self.ui.students_edit_btn.clicked.connect(lambda: self.sp_expand_popup('edit'))
        self.ui.students_exit_btn.clicked.connect(lambda: self.sp_collapse_popup('exit'))
        self.ui.student_save_btn.clicked.connect(lambda: self.sp_collapse_popup('save'))
        
        self.ui.rooms_add_btn.clicked.connect(lambda: self.roop_expand_popup('add'))
        self.ui.rooms_edit_btn.clicked.connect(lambda: self.roop_expand_popup('edit'))
        self.ui.rooms_exit_btn.clicked.connect(lambda: self.roop_collapse_popup('exit'))
        self.ui.room_save_btn.clicked.connect(lambda: self.roop_collapse_popup('save'))

        self.ui.reports_add_btn.clicked.connect(lambda: self.repp_expand_popup('add'))
        self.ui.reports_edit_btn.clicked.connect(lambda: self.repp_expand_popup('edit'))
        self.ui.reports_exit_btn.clicked.connect(lambda: self.repp_collapse_popup('exit'))
        self.ui.reports_save_btn.clicked.connect(lambda: self.repp_collapse_popup('save'))

        self.ui.reports_list_add_btn.clicked.connect(lambda: self.relp_expand_popup('add'))
        self.ui.reports_list_edit_btn.clicked.connect(lambda: self.relp_expand_popup('edit'))
        self.ui.reports_list_exit_btn.clicked.connect(lambda: self.relp_collapse_popup('exit'))
        self.ui.reports_list_save_btn.clicked.connect(lambda: self.relp_collapse_popup('save'))

        self.ui.logout_btn.clicked.connect(self.logout_func)
        self.ui.admin_exit_btn.clicked.connect(self.exit_func)

    
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
        self.ui.menu.setMinimumWidth(50)
        list_btns = [self.ui.admins_btn,self.ui.teachers_btn,self.ui.students_btn,self.ui.rooms_btn,self.ui.reports_btn,self.ui.reports_list_btn,self.ui.menu_btn,self.ui.logout_btn]
        for i in range(len(list_btns)):
            list_btns[i].setStyleSheet(HauSettings.menu_btns_style(9,9,9,9,1,1,1,1))
            list_btns[i].setText("")
        
    def menu_func(self):
        if self.ui.menu.size().width() < 200:
            self.expand_menu()
        else:
            self.collapse_menu()
        self.sync_btn_page()

    def init_searching(self):
        giaovien_list = []
        for item in self.admin_api['giaovien']:
            giaovien_list.append(item['MaGV'])

        giaovien_completer = QCompleter(giaovien_list, self.ui.teachers_input)
        self.ui.teachers_input.setCompleter(giaovien_completer)

        sinhvien_list = []
        for item in self.admin_api['sinhvien']:
            sinhvien_list.append(item['MaSV'])

        sinhvien_completer = QCompleter(sinhvien_list, self.ui.students_input)
        self.ui.students_input.setCompleter(sinhvien_completer)

        lophoc_list = []
        for item in self.admin_api['lophoc']:
            lophoc_list.append(item['MaLop'])

        lophoc_completer = QCompleter(lophoc_list, self.ui.rooms_input)
        self.ui.rooms_input.setCompleter(lophoc_completer)

        baocao_list = []
        for item in self.admin_api['baocao']:
            baocao_list.append(item['MaSV'])

        baocao_completer = QCompleter(baocao_list, self.ui.reports_input)
        self.ui.reports_input.setCompleter(baocao_completer)

        dslop_list = []
        for item in self.admin_api['dslop']:
            dslop_list.append(item['MaLop'])

        dslop_completer = QCompleter(dslop_list, self.ui.reports_list_input)
        self.ui.teachers_input.setCompleter(dslop_completer)

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
        self.init_popup_buttons()
        self.sync_btn_page()
    
    def reset_popup(self):
        self.ui.admin_id_text.setText("")
        self.ui.admin_username_text.setText("")
        self.ui.admin_password_text.setText("")

        self.ui.teacher_id_text.setText("")
        self.ui.teacher_name_text.setText("")
        self.ui.teacher_password_text.setText("")
        self.ui.teacher_address_text.setText("")
        self.ui.teacher_password_text.setText("")
        self.ui.teacher_phone_text.setText("")

        self.ui.student_id_text.setText("")
        self.ui.student_name_text.setText("")
        self.ui.student_birth_text.setText("")
        self.ui.student_class_text.setText("")
        self.ui.student_address_text.setText("")
        self.ui.student_url_text.setText("")
        self.ui.student_phone_text.setText("")

        self.ui.room_id_text.setText("")
        self.ui.room_name_text.setText("")
        self.ui.room_teacher_text.setText("")
        self.ui.room_sche_text.setText("")
        self.ui.room_class_text.setText("")
        self.ui.room_student_num_text.setText("")
        self.ui.room_days_text.setText("")

        self.ui.reports_id_text.setText("")
        self.ui.reports_date_text.setText("")
        self.ui.reports_student_text.setText("")
        self.ui.reports_room_text.setText("")
        self.ui.reports_attend_text.setText("")
        self.ui.reports_note_text.setText("")

        self.ui.reports_list_id_text.setText("")
        self.ui.reports_list_class_text.setText("")
        self.ui.reports_list_student_text.setText("")
        self.ui.reports_list_count_text.setText("")

        self.admin_save_mode = ""
        self.teacher_save_mode = ""
        self.student_save_mode = ""
        self.room_save_mode = ""
        self.report_save_mode = ""
        self.report_list_save_mode = ""

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

    def adp_expand_popup(self, mode=""):
        self.ui.popupWidget.expandMenu()
        self.ui.popupPages.setCurrentIndex(0)
        if mode == 'edit':
            admin_idx = self.ui.admins_table.currentRow()
            admin_info = self.admin_api['admin'][admin_idx]
            self.ui.admin_id_text.setText(admin_info['MaAD'])
            self.ui.admin_username_text.setText(admin_info['TenDN'])
            self.ui.admin_password_text.setText(admin_info['MatKhau'])
            self.admin_save_mode = "edit"
        elif mode == 'add':
            self.ui.admin_id_text.setText("")
            self.ui.admin_username_text.setText("")
            self.ui.admin_password_text.setText("")
            self.admin_save_mode = "add"

    def adp_collapse_popup(self, mode=""):
        self.ui.popupWidget.collapseMenu()
        if mode == "save":
            self.adp_save_func()
        self.reset_popup()

    def adp_delete_func(self):
        admin_idx = self.ui.admins_table.currentRow()
        if admin_idx != -1:
            admin_info = self.admin_api['admin'][admin_idx]
            try:
                requests.delete(HauSettings.BASE_URL + f'admin/{admin_info["MaAD"]}')
                self.reset_api()
                self.init_admin()
            except:
                print("No Connect SERVER!")

    def adp_save_func(self):
        data_admin = {}
        data_admin['TenDN'] = self.ui.admin_username_text.text()
        data_admin['MatKhau'] = self.ui.admin_password_text.text()
        if self.admin_save_mode == "add":
            try:
                requests.post(HauSettings.BASE_URL + f'admin/post', data=data_admin)
                self.reset_api()
                self.init_admin()
            except:
                print("No Connect SERVER!")
        elif self.admin_save_mode == "edit":
            data_admin['MaAD'] = self.ui.admin_id_text.text()
            try:
                requests.put(HauSettings.BASE_URL + f'admin/put', data=data_admin)
                self.reset_api()
                self.init_admin()
            except:
                print("No Connect SERVER!")
            
        
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

    def tp_expand_popup(self, mode=""):
        self.ui.popupWidget.expandMenu()
        self.ui.popupPages.setCurrentIndex(1)
        if mode == 'edit':
            teacher_idx = self.ui.teachers_table.currentRow()
            if teacher_idx != -1:
                teacher_info = self.admin_api['giaovien'][teacher_idx]
                self.ui.teacher_id_text.setText(teacher_info['MaGV'])
                self.ui.teacher_name_text.setText(teacher_info['TenGV'])
                self.ui.teacher_birth_text.setText(teacher_info['NgSinh'])
                self.ui.teacher_address_text.setText(teacher_info['DiaChi'])
                self.ui.teacher_password_text.setText(teacher_info['MatKhau'])
                self.ui.teacher_phone_text.setText(teacher_info['SDT'])
                self.teacher_save_mode = "edit"
        elif mode == 'add':
            self.ui.teacher_id_text.setText("")
            self.ui.teacher_name_text.setText("")
            self.ui.teacher_password_text.setText("")
            self.ui.teacher_address_text.setText("")
            self.ui.teacher_password_text.setText("")
            self.ui.teacher_phone_text.setText("")
            self.teacher_save_mode = "add"

    def tp_collapse_popup(self, mode=""):
        self.ui.popupWidget.collapseMenu()
        # self.teacher_save_mode = mode
        if mode == "save":
            self.tp_save_func()
        self.reset_popup()


    def tp_delete_func(self):
        teacher_idx = self.ui.teachers_table.currentRow()
        if teacher_idx != -1:
            teacher_info = self.admin_api['giaovien'][teacher_idx]
            try:
                requests.delete(HauSettings.BASE_URL + f'giaovien/{teacher_info["MaGV"]}')
                self.reset_api()
                self.init_admin()
            except:
                print("No Connect SERVER!")

    def tp_save_func(self):
        data_teacher = {}
        data_teacher['MaGV'] = self.ui.teacher_id_text.text()
        data_teacher['NgSinh'] = self.ui.teacher_birth_text.text()
        data_teacher['DiaChi'] = self.ui.teacher_address_text.text()
        data_teacher['MatKhau'] = self.ui.teacher_password_text.text()
        data_teacher['TenGV'] = self.ui.teacher_name_text.text()
        data_teacher['SDT'] = self.ui.teacher_phone_text.text()
        print(self.teacher_save_mode)
        if self.teacher_save_mode == "add":
            try:
                requests.post(HauSettings.BASE_URL + f'teacher/post', data=data_teacher)
                self.reset_api()
                self.init_admin()
            except:
                print("No Connect SERVER!")
        elif self.teacher_save_mode == "edit":
            try:
                requests.put(HauSettings.BASE_URL + f'teacher/put', data=data_teacher)
                self.reset_api()
                self.init_admin()
            except:
                print("No Connect SERVER!")


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
            
    def sp_expand_popup(self, mode=""):
        self.ui.popupWidget.expandMenu()
        self.ui.popupPages.setCurrentIndex(2)
        if mode == 'edit':
            student_idx = self.ui.students_table.currentRow()
            student_info = self.admin_api['sinhvien'][student_idx]
            self.ui.student_id_text.setText(student_info['MaSV'])
            self.ui.student_name_text.setText(student_info['TenSV'])
            self.ui.student_birth_text.setText(student_info['NgSinh'])
            self.ui.student_class_text.setText(student_info['LopQL'])
            self.ui.student_address_text.setText(student_info['DiaChi'])
            self.ui.student_url_text.setText(student_info['LinkAnh'])
            self.ui.student_phone_text.setText(student_info['SDT'])
            self.student_save_mode = 'edit'
        elif mode == 'add':
            self.ui.student_id_text.setText("")
            self.ui.student_name_text.setText("")
            self.ui.student_birth_text.setText("")
            self.ui.student_class_text.setText("")
            self.ui.student_address_text.setText("")
            self.ui.student_url_text.setText("")
            self.ui.student_phone_text.setText("")
            self.student_save_mode = 'add'

    def sp_collapse_popup(self, mode=""):
        self.ui.popupWidget.collapseMenu()
        if mode == "save":
            self.sp_save_func()
        self.reset_popup()

    def sp_delete_func(self):
        student_idx = self.ui.students_table.currentRow()
        if student_idx != -1:
            student_info = self.admin_api['sinhvien'][student_idx]
            try:
                requests.delete(HauSettings.BASE_URL + f'sinhvien/{student_info["MaSV"]}')
                self.reset_api()
                self.init_admin()
            except:
                print("No Connect SERVER!")
    
    def sp_save_func(self):
        data_student = {}
        data_student['MaSV'] = self.ui.student_id_text.text()
        data_student['NgSinh'] = self.ui.student_birth_text.text()
        data_student['DiaChi'] = self.ui.student_address_text.text()
        data_student['LopQL'] = self.ui.student_class_text.text()
        data_student['LinkAnh'] = self.ui.student_url_text.text()
        data_student['TenSV'] = self.ui.student_name_text.text()
        data_student['SDT'] = self.ui.student_phone_text.text()
        print(self.student_save_mode)
        if self.student_save_mode == "add":
            try:
                requests.post(HauSettings.BASE_URL + f'student/post', data=data_student)
                self.reset_api()
                self.init_admin()
            except:
                print("No Connect SERVER!")
        elif self.student_save_mode == "edit":
            try:
                requests.put(HauSettings.BASE_URL + f'student/put', data=data_student)
                self.reset_api()
                self.init_admin()
            except:
                print("No Connect SERVER!")


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
                self.ui.rooms_table.setItem(row, 5, QTableWidgetItem(str(e['SoluongSV'])))
                self.ui.rooms_table.setItem(row, 6, QTableWidgetItem(str(e['SoNgay'])))
                row += 1
    
    def roop_expand_popup(self, mode=""):
        self.ui.popupWidget.expandMenu()
        self.ui.popupPages.setCurrentIndex(3)
        if mode == 'edit':
            room_idx = self.ui.rooms_table.currentRow()
            room_info = self.admin_api['lophoc'][room_idx]
            self.ui.room_id_text.setText(room_info['MaLop'])
            self.ui.room_name_text.setText(room_info['TenMon'])
            self.ui.room_teacher_text.setText(room_info['MaGV'])
            self.ui.room_sche_text.setText(room_info['LichHoc'])
            self.ui.room_class_text.setText(room_info['PhongHoc'])
            self.ui.room_student_num_text.setText(str(room_info['SoluongSV']))
            self.ui.room_days_text.setText(str(room_info['SoNgay']))
            self.room_save_mode = "edit"
        elif mode == 'add':
            self.ui.room_id_text.setText("")
            self.ui.room_name_text.setText("")
            self.ui.room_teacher_text.setText("")
            self.ui.room_sche_text.setText("")
            self.ui.room_class_text.setText("")
            self.ui.room_student_num_text.setText("")
            self.ui.room_days_text.setText("")
            self.room_save_mode = "add"

    def roop_collapse_popup(self, mode=""):
        self.ui.popupWidget.collapseMenu()
        if mode == "save":
            self.roop_save_func()
        self.reset_popup()

    def roop_delete_func(self):
        room_idx = self.ui.rooms_table.currentRow()
        if room_idx != -1:
            room_info = self.admin_api['lophoc'][room_idx]
            try:
                requests.delete(HauSettings.BASE_URL + f'lophoc/{room_info["MaLop"]}')
                self.reset_api()
                self.init_admin()
            except:
                print("No Connect SERVER!")

    def roop_save_func(self):
        data_room = {}
        data_room['MaLop'] = self.ui.room_id_text.text()
        data_room['TenMon'] = self.ui.room_name_text.text()
        data_room['MaGV'] = self.ui.room_teacher_text.text()
        data_room['LichHoc'] = self.ui.room_sche_text.text()
        data_room['PhongHoc'] = self.ui.room_class_text.text()
        data_room['SoluongSV'] = self.ui.room_student_num_text.text()
        data_room['SoNgay'] = self.ui.room_days_text.text()
        print(self.room_save_mode)
        if self.room_save_mode == "add":
            try:
                requests.post(HauSettings.BASE_URL + f'lophoc/post', data=data_room)
                self.reset_api()
                self.init_admin()
            except:
                print("No Connect SERVER!")
        elif self.room_save_mode == "edit":
            try:
                requests.put(HauSettings.BASE_URL + f'lophoc/put', data=data_room)
                self.reset_api()
                self.init_admin()
            except:
                print("No Connect SERVER!")


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

    def repp_expand_popup(self, mode=""):
        self.ui.popupWidget.expandMenu()
        self.ui.popupPages.setCurrentIndex(4)
        if mode == 'edit':
            reports_idx = self.ui.reports_table.currentRow()
            reports_info = self.admin_api['baocao'][reports_idx]
            self.ui.reports_id_text.setText(reports_info['MaBC'])
            self.ui.reports_date_text.setText(reports_info['NgayBC'])
            self.ui.reports_student_text.setText(reports_info['MaSV'])
            self.ui.reports_room_text.setText(reports_info['MaLop'])
            self.ui.reports_attend_text.setText(reports_info['DiemDanh'])
            self.ui.reports_note_text.setText(reports_info['GhiChu'])
            self.report_save_mode = 'edit'
        elif mode == 'add':
            self.ui.reports_id_text.setText("")
            self.ui.reports_date_text.setText("")
            self.ui.reports_student_text.setText("")
            self.ui.reports_room_text.setText("")
            self.ui.reports_attend_text.setText("")
            self.ui.reports_note_text.setText("")
            self.report_save_mode = 'add'

    def repp_collapse_popup(self, mode=""):
        self.ui.popupWidget.collapseMenu()
        if mode == "save":
            self.repp_save_func()
        self.reset_popup()

    def repp_delete_func(self):
        report_idx = self.ui.reports_table.currentRow()
        if report_idx != -1:
            report_info = self.admin_api['baocao'][report_idx]
            try:
                requests.delete(HauSettings.BASE_URL + f'baocao/{report_info["MaBC"]}')
                self.reset_api()
                self.init_admin()
            except:
                print("No Connect SERVER!")

    def repp_save_func(self):
        data_report = {}
        data_report['MaBC'] = self.ui.reports_id_text.text()
        data_report['NgayBC'] = self.ui.reports_date_text.text()
        data_report['MaSV'] = self.ui.reports_student_text.text()
        data_report['MaLop'] = self.ui.reports_room_text.text()
        data_report['DiemDanh'] = self.ui.reports_attend_text.text()
        data_report['GhiChu'] = self.ui.reports_note_text.text()
        print("report")
        if self.report_save_mode == "add":
            try:
                requests.post(HauSettings.BASE_URL + f'baocao/post', data=data_report)
                self.reset_api()
                self.init_admin()
            except:
                print("No Connect SERVER!")
        elif self.report_save_mode == "edit":
            try:
                requests.put(HauSettings.BASE_URL + f'baocao/put', data=data_report)
                self.reset_api()
                self.init_admin()
            except:
                print("No Connect SERVER!")


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

    def relp_expand_popup(self, mode=""):
        self.ui.popupWidget.expandMenu()
        self.ui.popupPages.setCurrentIndex(5)
        if mode == 'edit':
            reports_list_idx = self.ui.reports_list_table.currentRow()
            reports_list_info = self.admin_api['dslop'][reports_list_idx]
            self.ui.reports_list_id_text.setText(reports_list_info['MaDS'])
            self.ui.reports_list_class_text.setText(reports_list_info['MaLop'])
            self.ui.reports_list_student_text.setText(reports_list_info['MaSV'])
            self.ui.reports_list_count_text.setText(str(reports_list_info['SoDD']))
            self.report_list_save_mode = 'edit'
        elif mode == 'add':
            self.ui.reports_list_id_text.setText("")
            self.ui.reports_list_class_text.setText("")
            self.ui.reports_list_student_text.setText("")
            self.ui.reports_list_count_text.setText("")
            self.report_list_save_mode = 'add'

    def relp_collapse_popup(self, mode=""):
        self.ui.popupWidget.collapseMenu()
        if mode == "save":
            self.relp_save_func()
        self.reset_popup()

    def relp_delete_func(self):
        reports_list_idx = self.ui.reports_list_table.currentRow()
        if reports_list_idx != -1:
            reports_list_info = self.admin_api['dslop'][reports_list_idx]
            try:
                requests.delete(HauSettings.BASE_URL + f'dslop/{reports_list_info["MaDS"]}')
                self.reset_api()
                self.init_admin()
            except:
                print("No Connect SERVER!")

    def relp_save_func(self):
        data_reports_list = {}
        data_reports_list['MaDS'] = self.ui.reports_list_id_text.text()
        data_reports_list['MaLop'] = self.ui.reports_list_class_text.text()
        data_reports_list['MaSV'] = self.ui.reports_list_student_text.text()
        data_reports_list['SoDD'] = self.ui.reports_list_count_text.text()
        if self.report_list_save_mode == "add":
            try:
                requests.post(HauSettings.BASE_URL + f'dslop/post', data=data_reports_list)
                self.reset_api()
                self.init_admin()
            except:
                print("No Connect SERVER!")
        elif self.report_list_save_mode == "edit":
            try:
                requests.put(HauSettings.BASE_URL + f'dslop/put', data=data_reports_list)
                self.reset_api()
                self.init_admin()
            except:
                print("No Connect SERVER!")
        
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



