from .hau_importer import *
from packages_import import *
    
class HauSupportorA:
    def display_image_func(this_label, this_img_path):
        if this_img_path == "" or not os.path.exists(this_img_path):
            this_img_path = UNKNOWN_IMAGE_PATH
        pixmap = QPixmap(f"{this_img_path}")
        this_label.setPixmap(pixmap)
