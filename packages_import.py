import os
import sys
sys.path.append('hau_packages')

from get_data_module import *
from prepare_module import *
from preprocess_module import *
from training_module import *
from predict_module import *
from model_module import *

# CONST
UNKNOWN_IMAGE_PATH = "resources\\apps\\no_data_found.png"
MODEL_FILE_EXTENSION = ".keras"
MODEL_DIR = "models_dir"
MODEL_HAAR = "haarcascade_frontalface_default.xml"
IMGS_DIR = "imgs"



