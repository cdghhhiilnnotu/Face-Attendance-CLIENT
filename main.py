from main_importer import *

from main_attendance import AttendanceWindow
from main_login import LoginWindow
from main_admin import AdminWindow
# import resources.resources

app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
loginWin = LoginWindow(widget)
attendanceWin = AttendanceWindow(widget)
adminWin = AdminWindow(widget)

widget.addWidget(loginWin)
widget.addWidget(attendanceWin)
widget.addWidget(adminWin)
widget.showFullScreen()
# widget.setWindowTitle(widget.currentWidget().objectName())
widget.setWindowFlag(Qt.FramelessWindowHint)
widget.setAttribute(Qt.WA_TranslucentBackground)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("Exiting")