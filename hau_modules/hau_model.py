from .hau_importer import *

class HauModel():
    def __init__(self, datasets='datasets', epoch=100, name='', imgs='imgs', model_dir='models'):
        self.datasets_path = datasets
        self.img_height, self.img_width = 224,224
        self.input_shape = (self.img_height, self.img_width, 3)
        self.imgs_path = imgs
        self.epochs = epoch
        self.name = name
        self.model = self.init_model_tl()
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

    def standardized_image(self):
        for sub in os.listdir(self.datasets_path):
            sub_path = os.path.join(self.datasets_path,sub)
            for image in os.listdir(sub_path):
                image_path = os.path.join(sub_path, image)
                try:
                    img = cv2.imread(image_path)
                    img = cv2.resize(img, (224,224))
                    cv2.imwrite(image_path, img)
                except:
                    pass

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
        gen_batch_size = 10
        
        datagen = ImageDataGenerator(
            rescale=1./255
        )
        DatasetSupport.reset_path(self.imgs_path)
        splitfolders.ratio(self.datasets_path, output=f'{self.imgs_path}', seed=123, ratio=(.7,.15,.15), group_prefix=None)

        
        self.train_ds = datagen.flow_from_directory(
            f'{self.imgs_path}/train',
            target_size = (self.img_height, self.img_width),
            batch_size = gen_batch_size,
            subset = 'training',
            class_mode = 'categorical'
        )
        
        self.val_ds = datagen.flow_from_directory(
            f'{self.imgs_path}/val',
            target_size = (self.img_height, self.img_width),
            batch_size = gen_batch_size,
            class_mode = 'categorical',
            shuffle = False
        )
        
        self.test_ds = datagen.flow_from_directory(
            f'{self.imgs_path}/test',
            target_size = (self.img_height, self.img_width),
            batch_size = gen_batch_size,
            class_mode='categorical',
            shuffle=False)

    def init_model_nor(self):
        self.epochs = 100
        inputs = keras.Input(self.input_shape)
        x = keras.layers.Conv2D(64,(5,5),activation='relu', kernel_regularizer=l2(0.001 * 4))(inputs)
        x = keras.layers.AveragePooling2D(pool_size=(3,3))(x)
        x = keras.layers.Conv2D(32,(5,5),activation='relu', kernel_regularizer=l2(0.001 * 1))(x)
        x = keras.layers.MaxPooling2D(pool_size=(3,3))(x)

        x = keras.layers.Flatten()(x)
        x = keras.layers.Dense(len(os.listdir(self.datasets_path)), activation='softmax')(x)
        model = keras.Model(inputs, x)

        return model

    def init_model_tl(self):
        self.epochs = 20
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
        self.score = self.model.evaluate(self.test_ds, verbose=1)

    def load_model(self, model_name):
        self.model.load_weights(f'{self.model_path}/{model_name}.keras')

    def tracking_face(self, img):
        face_locs = []
        img_faces = []
        img = cv2.resize(img, (int(img.shape[1]/(img.shape[0]/512)),512), interpolation=cv2.INTER_AREA)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        face_detector = cv2.CascadeClassifier(HauSettings.MODEL_HAAR)
        faces = []
        for scale in range(2, 9):
            for neighbor in range(2, 6):
                for face in face_detector.detectMultiScale(img_gray, 1 + 0.1 * scale, neighbor):
                    faces.append(face)

        for (x, y, w, h) in faces:
            img_faces.append(img[y:y+h, x:x+w])
            face_locs.append((x,y,w,h))
        return img_faces, face_locs
    
    def guessing_img(self, dataset_img, img_path, model, name, collector):
        colors = []
        img = cv2.imread(img_path)
        data_x, face_loc = self.tracking_face(img)

        for i in range(0,len(data_x)):
            data_x[i] = cv2.resize(data_x[i], (224,224), interpolation=cv2.INTER_AREA)

        data_x = np.array(data_x)
        data_x = data_x.astype(np.float32)
        guesses = model.model.predict(data_x)

        for i in range(len(face_loc)):
            x = face_loc[i][0]
            y = face_loc[i][0]
            w = face_loc[i][0]
            h = face_loc[i][0]
            if guesses[i][np.argmax(guesses[i])] > 0.9:
                color = (random.randint(0, 255), random.randint(0, 255), 0)
            elif guesses[i][np.argmax(guesses[i])] > 0.5 and guesses[i][np.argmax(guesses[i])] <= 0.9:
                color = (0, 255, 255)
            cv2.rectangle(img, (x, y),(x+w, y+h), color, 3)
            colors.append(color)
        cv2.imwrite(os.path.join(collector.RESULTS_PATH, f"{name}_result.png"), img)
        print(colors)
        return os.path.join(collector.RESULTS_PATH, f"{name}_result.png"), colors, [np.argmax(guess) for guess in guesses]    





