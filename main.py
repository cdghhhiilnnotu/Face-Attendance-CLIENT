from main_importer import *

from main_attendance import AttendanceWindow
from main_login import LoginWindow
# import resources.resources

app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
loginWin = LoginWindow(widget)
attendanceWin = AttendanceWindow(widget)

widget.addWidget(loginWin)
widget.addWidget(attendanceWin)
widget.showFullScreen()
# widget.setWindowTitle(widget.currentWidget().objectName())
widget.setWindowFlag(Qt.FramelessWindowHint)
widget.setAttribute(Qt.WA_TranslucentBackground)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("Exiting")