import keras
import tensorflow as tf
from keras import layers
from keras.models import Sequential
from keras.applications import DenseNet169


def get_model_config(model_weight, class_num):
    densenet = DenseNet169(weights="imagenet", include_top=False, input_shape=(224,224,3))
    densenet.trainable = False
    inputs = tf.keras.Input((224,224,3))
    x = densenet(inputs, training=False)
    x = keras.layers.GlobalAveragePooling2D()(x)
    x = keras.layers.Dense(1024, activation='relu')(x)
    x = keras.layers.Dense(class_num, activation='softmax')(x)
    model = tf.keras.Model(inputs, x)

    model.load_weights(f'hau_models/{model_weight}.keras')
    return model

