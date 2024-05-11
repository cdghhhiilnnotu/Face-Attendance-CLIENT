from hau_main.main_importer import *
from hau_main.main_attendance import AttendanceWindow
from hau_main.main_login import LoginWindow
from hau_main.main_admin import AdminWindow

app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
loginWin = LoginWindow(widget)
attendanceWin = AttendanceWindow(widget)
adminWin = AdminWindow(widget)

widget.addWidget(loginWin)
widget.addWidget(attendanceWin)
widget.addWidget(adminWin)
widget.showFullScreen()

widget.setWindowFlag(Qt.FramelessWindowHint)
widget.setAttribute(Qt.WA_TranslucentBackground)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("Exiting")