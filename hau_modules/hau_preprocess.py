from .hau_importer import *

class PreprocessData():
    def standardized_image(datasets_path):
        for sub in os.listdir(datasets_path):
            sub_path = os.path.join(datasets_path,sub)
            for image in os.listdir(sub_path):
                image_path = os.path.join(sub_path, image)
                img = cv2.imread(image_path)
                img = cv2.resize(img, (224,224))
                cv2.imwrite(image_path, img)

    def augmentation_dataset(datasets_path, img_path):
        batch_size = 64
        img_height, img_width = 224,224
        datagen = ImageDataGenerator(
            rescale=1./255
        )
        DatasetSupport.reset_path(img_path)
        splitfolders.ratio(datasets_path, output=f'{img_path}', seed=123, ratio=(.7,.15,.15), group_prefix=None)

        
        train_ds = datagen.flow_from_directory(
            f'{img_path}/train',
            target_size = (img_height, img_width),
            batch_size = batch_size,
            subset = 'training',
            class_mode = 'categorical'
        )
        
        val_ds = datagen.flow_from_directory(
            f'{img_path}/val',
            target_size = (img_height, img_width),
            batch_size = batch_size,
            class_mode = 'categorical',
            shuffle = False
        )
        
        test_ds = datagen.flow_from_directory(
            f'{img_path}/test',
            target_size = (img_height, img_width),
            batch_size = batch_size,
            class_mode='categorical',
            shuffle=False)

        return train_ds, val_ds, test_ds

