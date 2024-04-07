from .hau_importer import *

class HauModel():
    def __init__(self, datasets='datasets', epoch=1, name='', imgs='imgs', model_dir='models'):
        self.datasets_path = datasets
        self.img_height, self.img_width = 224,224
        self.input_shape = (self.img_height, self.img_width, 3)
        self.imgs_path = imgs
        self.epochs = epoch
        self.name = name
        self.model = self.init_model()
        self.model_path = model_dir
        self.guessed_students = []

    def training(self):
        self.standardized_image()
        self.augmentation_dataset_main()
        self.augmentation_dataset()
        self.data_classify()
        self.compile_model()
        self.fit_model()

    def evaluating(self):
        self.evaluate_model()
        # self.plot_train_history('result.png')

    def standardized_image(self):
        for sub in os.listdir(self.datasets_path):
            sub_path = os.path.join(self.datasets_path,sub)
            for image in os.listdir(sub_path):
                image_path = os.path.join(sub_path, image)
                img = cv2.imread(image_path)
                img = cv2.resize(img, (224,224))
                cv2.imwrite(image_path, img)

    def augmentation_dataset_main(self):
        datagen = ImageDataGenerator(
            rotation_range=40,
            width_shift_range=0.1,
            height_shift_range=0.1,
            shear_range=0.1,
            zoom_range=0.2,
            fill_mode='constant',
            horizontal_flip=True
        )
        
        for className in os.listdir(self.datasets_path):
            classPATH = os.path.join(self.datasets_path, className)
            len_IMG = len(os.listdir(classPATH))
            for imgName in os.listdir(classPATH):
                imgPATH = os.path.join(classPATH, imgName)
                img = load_img(imgPATH)
                x = img_to_array(img)
                x = x.reshape((1,) + x.shape)
        
                i = 0
                for batch in datagen.flow(x, batch_size=1, save_to_dir=classPATH, save_prefix=className, save_format='png'):
                    i += 1
                    if i > 10:
                        break

    def augmentation_dataset(self):
        batch_size = 64
        
        datagen = ImageDataGenerator(
            rescale=1./255
        )
        DatasetSupport.reset_path(self.imgs_path)
        splitfolders.ratio(self.datasets_path, output=f'{self.imgs_path}', seed=123, ratio=(.7,.15,.15), group_prefix=None)

        
        self.train_ds = datagen.flow_from_directory(
            f'{self.imgs_path}/train',
            target_size = (self.img_height, self.img_width),
            batch_size = batch_size,
            subset = 'training',
            class_mode = 'categorical'
        )
        
        self.val_ds = datagen.flow_from_directory(
            f'{self.imgs_path}/val',
            target_size = (self.img_height, self.img_width),
            batch_size = batch_size,
            class_mode = 'categorical',
            shuffle = False
        )
        
        self.test_ds = datagen.flow_from_directory(
            f'{self.imgs_path}/test',
            target_size = (self.img_height, self.img_width),
            batch_size = batch_size,
            class_mode='categorical',
            shuffle=False)

    def init_model(self):
        densenet = DenseNet169(weights="imagenet", include_top=False, input_shape=self.input_shape)
        densenet.trainable = False
        inputs = keras.Input(self.input_shape)
        x = densenet(inputs, training=False)
        x = keras.layers.GlobalAveragePooling2D()(x)
        x = keras.layers.Dense(1024, activation='relu')(x)
        x = keras.layers.Dense(len(os.listdir(self.datasets_path)), activation='softmax')(x)
        model = keras.Model(inputs, x)

        return model
    
    def data_classify(self):
        self.students = []
        for student in os.listdir(self.datasets_path):
            self.students.append([fn for fn in os.listdir(f'{self.datasets_path}/{student}')])
        
        self.student_classes = []
        for i in os.listdir(f'{self.imgs_path}/train'):
            self.student_classes+=[i]
        self.student_classes.sort()

        return self.students, self.student_classes

    def compile_model(self):        
        self.model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])
        
        self.model.summary()

    def fit_model(self):
        checkpointer = ModelCheckpoint(filepath=f'{self.model_path}/{self.name}.keras',
                                    monitor='accuracy', mode='max',
                                    verbose=1, save_best_only=True)
        early_stopping = EarlyStopping(monitor='loss', mode='min', verbose=1, patience=3)
        reduce_lr = ReduceLROnPlateau(monitor='loss', factor=0.2, patience=2, min_lr=0.001)
        callbacks=[early_stopping, reduce_lr, checkpointer]

        self.history = self.model.fit(self.train_ds, epochs = self.epochs, validation_data = self.val_ds, callbacks=callbacks)

    def evaluate_model(self):
        # self.model.load_weights(f'{self.model_path}/{self.name}.keras')
        self.score = self.model.evaluate(self.test_ds, verbose=1)

    def load_model(self, model_name):
        self.model.load_weights(f'{self.model_path}/{model_name}.keras')
    
    def real_time_predict(dataset_img, model, name, label):
        haar_file = HauSettings.MODEL_HAAR
        face_cascade = cv2.CascadeClassifier(haar_file)

        webcam = cv2.VideoCapture(0)
        while HauSettings.OPEN_CAM:
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
            HauSupportorA.display_image_func(label, os.path.join("hau_results", f"{name}_result.png"))
            # key = cv2.waitKey(10)
            # if key == 27:
            #     break
        webcam.release()
        cv2.destroyAllWindows()

    def plot_train_history(self, file_name_fig):
        plt.figure(figsize=(15,5))
        plt.subplot(1,2,1)
        plt.plot(self.history.history['accuracy'])
        plt.plot(self.history.history['val_accuracy'])
        plt.title('Model accuracy')
        plt.ylabel('accuracy')
        plt.xlabel('epoch')
        plt.legend(['train', 'validation'], loc='upper left')

        plt.subplot(1,2,2)
        plt.plot(self.history.history['loss'])
        plt.plot(self.history.history['val_loss'])
        plt.title('Model loss')
        plt.ylabel('loss')
        plt.xlabel('epoch')
        plt.legend(['train', 'validation'], loc='upper left')
        print(file_name_fig)
        plt.savefig(file_name_fig)
    


