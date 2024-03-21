import os
import sys
sys.path.append('hau_packages')

from get_data_module import *
from prepare_module import *
from preprocess_module import *
from training_module import *
from predict_module import *
from model_module import *
from logging_module import *


# CONST
DATASETS_PATH = 'hau_datasets'
RESULTS_PATH = 'hau_results'
STATISTIC_PATH = 'hau_statistics'
UNKNOWN_IMAGE_PATH = "resources\\apps\\no_data_found.png"
MODEL_FILE_EXTENSION = ".keras"
MODEL_DIR = "hau_models"
MODEL_HAAR = "haarcascade_frontalface_default.xml"
IMGS_DIR = "imgs"

ABOUT_US_TEXT = """
TRƯỜNG ĐẠI HỌC KIẾN TRÚC HÀ NỘI 
KHOA CÔNG NGHỆ THÔNG TIN 

NHÓM 9 - NGHIÊN CỨU KHOA HỌC

GIÁO VIÊN HƯỚNG DẪN:
TS. NGUYỄN THỊ HUỆ

THÀNH VIÊN: 
NGUYỄN THÀNH DƯƠNG - 2055010051 (NHÓM TRƯỞNG)
DƯƠNG KHÁNH LINH - 2055010153
PHÙNG DUY MẠNH - 2055010165
NGUYỄN THÁI NAM - 2055010183
ĐINH QUỐC TIẾN - 2055010231
"""

if not os.path.exists(DATASETS_PATH):
    os.makedirs(DATASETS_PATH)

if not os.path.exists(MODEL_DIR):
    os.makedirs(MODEL_DIR)


