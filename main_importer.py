import os
import sys
import time
import threading

from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt, QPropertyAnimation
from PyQt5.QtGui import QIcon, QPixmap, QBrush, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QAbstractItemView, QFileDialog, QLineEdit

from hau_modules.hau_importer import *

# DATASETS_PATH = 'hau_datasets'
# RESULTS_PATH = 'hau_results'
# STATISTIC_PATH = 'hau_statistics'
# MODEL_DIR = "hau_models"
# UNKNOWN_IMAGE_PATH = "resources\\apps\\no_data_found.png"
# MODEL_FILE_EXTENSION = ".keras"
# MODEL_HAAR = "haarcascade_frontalface_default.xml"
# IMGS_DIR = "imgs"

# face_msv = []

# ABOUT_US_TEXT = """
# TRƯỜNG ĐẠI HỌC KIẾN TRÚC HÀ NỘI 
# KHOA CÔNG NGHỆ THÔNG TIN 

# NHÓM 9 - NGHIÊN CỨU KHOA HỌC

# GIÁO VIÊN HƯỚNG DẪN:
# TS. NGUYỄN THỊ HUỆ

# THÀNH VIÊN: 
# NGUYỄN THÀNH DƯƠNG - 2055010051 (NHÓM TRƯỞNG)
# DƯƠNG KHÁNH LINH - 2055010153
# PHÙNG DUY MẠNH - 2055010165
# NGUYỄN THÁI NAM - 2055010183
# ĐINH QUỐC TIẾN - 2055010231
# """

