from .main_importer import *
from hau_ui.ui_login import *
from Custom_Widgets.Widgets import * 

class LoginWindow(QMainWindow):
    def __init__(self, widget):
        self.widget = widget
        super(LoginWindow, self).__init__()
        self.passwordIsHide = True
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui, jsonFiles={'hau_ui\\style-client.json'})
        self.isAdmin = True
        
        self.ui.signin_btn.clicked.connect(self.signin_func)
        self.ui.hide_password_btn.clicked.connect(self.hiding_password)
        self.ui.signin_exit_btn.clicked.connect(lambda: QApplication.quit())
        self.ui.admin_btn.clicked.connect(self.switch_admin)
        self.login_init()
    
    def hiding_password(self):
        self.passwordIsHide = not self.passwordIsHide
        if self.passwordIsHide:
            self.ui.signin_password_input.setEchoMode(QLineEdit.Password)
        else:
            self.ui.signin_password_input.setEchoMode(QLineEdit.Normal)

    def login_init(self):
        self.widget.setWindowFlag(Qt.FramelessWindowHint)
        self.setFixedWidth(590)
        self.setFixedHeight(410)
        self.passwordIsHide = False
        self.isAdmin = True
        self.ui.admin_btn.setText("Quản trị viên")
        self.hiding_password()
        self.ui.signin_username_input.setText("")
        self.ui.signin_password_input.setText("")
        self.ui.wrong_pass_label.hide()

    def switch_admin(self):
        if self.isAdmin:
            self.isAdmin = False
            self.ui.admin_btn.setText("Giảng viên")
        else:
            self.isAdmin = True
            self.ui.admin_btn.setText("Quản trị viên")

    def signin_func(self):
        if not self.isAdmin:
            if CollectData.check_user(self.ui.signin_username_input.text(),self.ui.signin_password_input.text()):
                self.signin_user_success()
            else:
                self.signin_fail()
        else:
            if CollectData.check_admin(self.ui.signin_username_input.text(),self.ui.signin_password_input.text()):
                self.signin_admin_success()
            else:
                self.signin_fail()
        
    def signin_user_success(self):
        self.widget.setCurrentIndex(1)
        self.widget.currentWidget().collector = CollectData.check_user(self.ui.signin_username_input.text(),self.ui.signin_password_input.text())
        self.widget.currentWidget().init_attendance()

    def signin_admin_success(self):
        self.widget.setCurrentIndex(2)
        self.widget.currentWidget().init_admin()

    def signin_fail(self):
        self.login_init()
        self.ui.wrong_pass_label.show()