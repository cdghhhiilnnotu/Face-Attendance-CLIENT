import cv2
import matplotlib.pyplot as plt
from preprocess_module import *
import numpy as np
import random

def img_result(img_path, model):
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
    cv2.imwrite("test4.png", img)

    return "test4.png", colors, [np.argmax(guess) for guess in guesses]


