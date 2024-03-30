import cv2
import matplotlib.pyplot as plt
from preprocess_module import *
import numpy as np
import random
from PyQt5.QtGui import QIcon, QPixmap, QBrush, QColor

UNKNOWN_IMAGE_PATH = "resources\\apps\\no_data_found.png"

OPEN_CAM = False

def guessing_img(dataset_img, img_path, model, name):
    colors = []
    img = cv2.imread(img_path)
    data_x, face_loc = tracking_face(img)

    for i in range(0,len(data_x)):
        data_x[i] = cv2.resize(data_x[i], (224,224), interpolation=cv2.INTER_AREA)

    data_x = np.array(data_x)
    data_x = data_x.astype(np.float32)
    guesses = model.predict(data_x)

    for i in range(len(face_loc)):
        x = face_loc[i][0]
        y = face_loc[i][0]
        w = face_loc[i][0]
        h = face_loc[i][0]
        if guesses[i][np.argmax(guesses[i])] > 0.9:
            color = (random.randint(0, 255), random.randint(0, 255), 0)
        elif guesses[i][np.argmax(guesses[i])] > 0.5 and guesses[i][np.argmax(guesses[i])] <= 0.9:
            color = (0, 255, 255)
        else:
            color = (0, 0, 255)
        cv2.rectangle(img, (x, y),(x+w, y+h), color, 3)
        colors.append(color)
    cv2.imwrite(os.path.join("hau_results", f"{name}_result.png"), img)

    return os.path.join("hau_results", f"{name}_result.png"), colors, [np.argmax(guess) for guess in guesses]

def display_image_func(this_label, this_img_path):
    if this_img_path == "" or not os.path.exists(this_img_path):
        this_img_path = UNKNOWN_IMAGE_PATH
    pixmap = QPixmap(f"{this_img_path}")
    this_label.setPixmap(pixmap)

def real_time_predict(dataset_img, model, name, label):
    haar_file = 'haarcascade_frontalface_default.xml'
    face_cascade = cv2.CascadeClassifier(haar_file)

    webcam = cv2.VideoCapture(0)
    while OPEN_CAM:
        (_, im) = webcam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            face = im[y:y + h, x:x + w]
            face_resize = cv2.resize(face, (224, 224))
            prediction = model.predict(np.expand_dims(face_resize, axis=0))
            cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), 3)
            # if (prediction[1] < 800):
            cv2.putText(im, '%s-%.0f' % (dataset_img[np.argmax(prediction)], np.max(prediction)), (x - 10, y - 10),
                        cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255))
            # print(students[np.argmax(prediction)])
        # cv2.imshow('frame', im)
        cv2.imwrite(os.path.join("hau_results", f"{name}_result.png"), im)
        display_image_func(label, os.path.join("hau_results", f"{name}_result.png"))
        # key = cv2.waitKey(10)
        # if key == 27:
        #     break
    webcam.release()
    cv2.destroyAllWindows()

def revert_cam():
    global OPEN_CAM
    OPEN_CAM = True if not OPEN_CAM else False
    return OPEN_CAM

