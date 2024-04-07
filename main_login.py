from main_importer import *

class LoginWindow(QMainWindow):
    def __init__(self, widget):
        self.widget = widget
        super(LoginWindow, self).__init__()
        loadUi("login.ui", self)
        self.passwordIsHide = True
        
        self.signin_btn.clicked.connect(self.signin_func)
        self.hide_password_btn.clicked.connect(self.hiding_password)
        self.signin_exit_btn.clicked.connect(lambda: QApplication.quit())
        self.login_init()
    
    def hiding_password(self):
        self.passwordIsHide = not self.passwordIsHide
        if self.passwordIsHide:
            self.signin_password_input.setEchoMode(QLineEdit.Password)
        else:
            self.signin_password_input.setEchoMode(QLineEdit.Normal)

    def login_init(self):
        self.passwordIsHide = False
        self.hiding_password()
        self.signin_username_input.setText("")
        self.signin_password_input.setText("")
        self.wrong_pass_label.hide()

    def signin_func(self):
        if CollectData.check_user(self.signin_username_input.text(),self.signin_password_input.text()):
            self.signin_success()
        else:
            self.signin_fail()
        
    def signin_success(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)
        self.widget.currentWidget().collector = CollectData.check_user(self.signin_username_input.text(),self.signin_password_input.text())
        self.widget.currentWidget().attendance_init()

    def signin_fail(self):
        self.login_init()
        self.wrong_pass_label.show()