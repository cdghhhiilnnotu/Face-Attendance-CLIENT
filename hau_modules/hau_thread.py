from .hau_importer import *

class Thread_Video(QThread):
    signal = pyqtSignal(np.ndarray)
    def __init__(self, index, dataset_img, model, label):
        self.index = index
        self.dataset_img, self.model, self.label = dataset_img, model, label
        print("start threading", self.index)
        self.face_guessed = []
        self.cam_enable = False
        super(Thread_Video, self).__init__()

    def run(self):
        haar_file = HauSettings.MODEL_HAAR
        face_cascade = cv2.CascadeClassifier(haar_file)
        webcam = cv2.VideoCapture(0)
        while self.cam_enable:
            try:
                ret, im = webcam.read()
                gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in faces:
                    face = im[y:y + h, x:x + w]
                    face_resize = cv2.resize(face, (224, 224))
                    prediction = self.model.model.predict(np.expand_dims(face_resize, axis=0))
                    cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), 3)
                    # if (prediction[1] < 800):
                    cv2.putText(im, '%s-%.0f' % (self.dataset_img[np.argmax(prediction)], np.max(prediction)), (x - 10, y - 10),
                                cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255))
                    self.face_guessed.append(self.dataset_img[np.argmax(prediction)])
            except:
                pass
            if ret:
                self.signal.emit(im)

    # def run(self):
    #     cap = cv2.VideoCapture(0)  # 'D:/8.Record video/My Video.mp4'
    #     while True:
    #         ret, cv_img = cap.read()
    #         if ret:
    #             self.signal.emit(cv_img)
    
    def stop(self):
        print("stop threading", self.index)
        self.exit()
        # return self.face_guessed