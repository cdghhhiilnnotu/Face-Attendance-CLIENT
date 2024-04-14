from .hau_importer import *

class HauSettings():
    BASE_DIR = "http://127.0.0.1:5000/"
    API_SOURCE = "api_user.json"

    OPEN_CAM = True
    UNKNOWN_IMAGE_PATH = "resources\\apps\\no_data_found.png"
    MODEL_FILE_EXTENSION = ".keras"
    MODEL_HAAR = "haarcascade_frontalface_alt.xml"
    IMGS_DIR = "imgs"

    def check_cam():
        global OPEN_CAM
        OPEN_CAM = True if not OPEN_CAM else False
        return OPEN_CAM
    
    def display_image_func(this_label, this_img_path):
        if this_img_path == "" or not os.path.exists(this_img_path):
            this_img_path = HauSettings.UNKNOWN_IMAGE_PATH
        pixmap = QPixmap(f"{this_img_path}")
        this_label.setPixmap(pixmap)

    def menu_btns_style(
                    border_top_right_radius=0,
                    border_top_left_radius=0,
                    border_bottom_right_radius=0,
                    border_bottom_left_radius=0,
                    margin_top=0,
                    margin_right=0,
                    margin_bottom=0,
                    margin_left=0
                    ):
        return f"""
        color: rgb(0,0,0);
        background-color: rgb(188,203,234);
        border: 2px solid #000;
        font-weight: bold;
        font-size: 12pt;
        border-top-right-radius: {border_top_right_radius}px;
        border-top-left-radius: {border_top_left_radius}px;
        border-bottom-right-radius: {border_bottom_right_radius}px;
        border-bottom-left-radius: {border_bottom_left_radius}px;
        margin: {margin_top}px {margin_right}px {margin_bottom}px {margin_left}px;
        """

