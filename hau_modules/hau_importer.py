import os
import json
import cv2
import keras
import random
import shutil
import requests
import numpy as np
import splitfolders
import tensorflow as tf
from PyQt5 import QtGui
from keras import layers
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.applications import DenseNet169
from PyQt5.QtCore import QThread, pyqtSignal, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon, QPixmap, QBrush, QColor
from keras.callbacks import ModelCheckpoint, EarlyStopping, ReduceLROnPlateau
from keras.regularizers import l2
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QAbstractItemView, QFileDialog, QLineEdit

from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

try:
    from .hau_settings import *
    print("hau_settings")
except:
    pass

try:
    from .hau_collector import *
    print("hau_collector")
except:
    pass

try:
    from .hau_data_supportor import *
    print("hau_data_supportor")
except:
    pass

try:
    from .hau_model import *
    print("hau_model")
except:
    pass

try:
    from .hau_thread import *
    print("hau_thread")
except:
    pass

# collector = CollectData.check_user("","")
