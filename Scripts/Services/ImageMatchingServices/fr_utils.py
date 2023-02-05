import warnings
warnings.filterwarnings("ignore")
import os
import pickle

import tensorflow as tf
# from tensorflow.python.keras.backend import _get_session #### New added

import cv2
import h5py
import numpy as np
from numpy import genfromtxt
from keras.layers import Conv2D, ZeroPadding2D, Activation, Input, concatenate
from keras.models import Model
from keras.layers.normalization import BatchNormalization
from keras.layers.pooling import MaxPooling2D, AveragePooling2D

from tqdm import tqdm

from Constants import const
from Scripts.Utility import utils

_FLOATX = "float32"


def variable(value, dtype=_FLOATX, name=None):
    # with graph.as_default():
    v = tf.Variable(np.asarray(value, dtype=dtype), name=name)
    _get_session().run(v.initializer)

    return v

def shape(x):
    return x.get_shape()

def square(x):
    return tf.square(x)

def zeros(shape, dtype=_FLOATX, name=None):
    return variable(np.zeros(shape=shape), dtype=dtype, name=name)

def concatenate(tensors, axis=-1):
    if axis < 0:
        axis = axis % len(tensors[0].get_shape())

    return tf.concat(axis, tensors)

def LRN2D(x):
    return tf.nn.lrn(x, alpha=1e-4, beta=0.75)


def conv2d_bn(x,
              layer=None,
              cv1_out=None,
              cv1_filter=(1, 1),
              cv1_strides=(1, 1),
              cv2_out=None,
              cv2_filter=(3, 3),
              cv2_strides=(1, 1),
              padding=None):

    num = "" if cv2_out == None else "1"
    tensor = Conv2D(cv1_out, cv1_filter, strides=cv1_strides, data_format="channels_first", name=layer + "_conv" + num)(x)
    tensor = BatchNormalization(axis=1, epsilon=1e-5, name=layer + "_bn" + num)(tensor)
    tensor = Activation("relu")(tensor)

    if padding == None:
        return tensor

    tensor = ZeroPadding2D(padding=padding, data_format="channels_first")(tensor)

    if cv2_out == None:
        return tensor

    tensor = Conv2D(cv2_out, cv2_filter, strides=cv2_strides, data_format="channels_first", name=layer + "_conv" + "2")(tensor)
    tensor = BatchNormalization(axis=1, epsilon=1e-5, name=layer + "_bn" + "2")(tensor)
    tensor = Activation("relu")(tensor)

    return tensor


def load_weights_from_FaceNet(FRmodel):
    """
    Load weights from csv files (which are exported from Openface torch model)
    :param FRmodel:
    :return:
    """
    try:
        weights = const.WEIGHTS

        if not os.path.exists("./Assets/saved_weights_dict.pkl"):
            weights_dict = load_weights()
            pickled_file = open("./Assets/saved_weights_dict.pkl", "wb")
            pickle.dump(weights_dict, pickled_file, protocol=pickle.HIGHEST_PROTOCOL)
            pickled_file.close()
        elif os.path.exists("./Assets/saved_weights_dict.pkl"):
            unpickled_file = open("./Assets/saved_weights_dict.pkl", "rb")
            weights_dict = pickle.load(unpickled_file)
        else:
            raise FileNotFoundError

        # Set layer weights of the model:
        for name in weights:
            if FRmodel.get_layer(name) != None:
                FRmodel.get_layer(name).set_weights(weights_dict[name])
            elif FRmodel.get_layer(name) != None:
                FRmodel.get_layer(name).set_weights(weights_dict[name])

    except Exception as e:
        utils.logger.exception("--ERROR-- : load_weights_from_FaceNet ->")


def load_weights():
    """
    Set weights path
    :return:
    """
    dir_path = "./Assets/weights"
    file_names = filter(lambda f: not f.startswith("."), os.listdir(dir_path))
    path = dict()
    weights_dict = dict()

    for n in file_names:
        path[n.replace(".csv", "")] = os.path.join(dir_path, n)

    for name in tqdm(const.WEIGHTS):
        if "conv" in name:
            conv_w = genfromtxt(path[name + "_w"], delimiter=",", dtype=None)
            conv_w = np.reshape(conv_w, const.conv_shape[name])
            conv_w = np.transpose(conv_w, (2, 3, 1, 0))
            conv_b = genfromtxt(path[name + "_b"], delimiter=",", dtype=None)

            weights_dict[name] = [conv_w, conv_b]

        elif "bn" in name:
            bn_w = genfromtxt(path[name + "_w"], delimiter=",", dtype=None)
            bn_b = genfromtxt(path[name + "_b"], delimiter=",", dtype=None)
            bn_m = genfromtxt(path[name + "_m"], delimiter=",", dtype=None)
            bn_v = genfromtxt(path[name + "_v"], delimiter=",", dtype=None)

            weights_dict[name] = [bn_w, bn_b, bn_m, bn_v]

        elif "dense" in name:
            dense_w = genfromtxt(dir_path + "/dense_w.csv", delimiter=",", dtype=None)
            dense_w = np.reshape(dense_w, (128, 736))
            dense_w = np.transpose(dense_w, (1, 0))
            dense_b = genfromtxt(dir_path + "/dense_b.csv", delimiter=",", dtype=None)

            weights_dict[name] = [dense_w, dense_b]

    return weights_dict



def load_dataset():
    #train_dataset = h5py.File("")
    pass

def image_to_encoding_from_imagepath(image_path, model):
    try:
        img1 = cv2.imread(image_path, 1)
        size = (96, 96)
        img = img1[..., ::-1]
        img = np.around(np.transpose(img, (2, 0, 1)) / 255.0, decimals=12)
        x_train = np.array([img])
        embedding = model.predict_on_batch(x_train)

        return embedding

    except Exception as e:
        utils.logger.exception("--ERROR-- : image_to_encoding ->" + str(e))

def image_to_encoding_from_numyArray(numpy_image, model):
    try:
        # img1 = cv2.imread(image_path, 1)
        size = (96, 96)
        opencv_image = cv2.cvtColor(numpy_image, cv2.COLOR_RGB2BGR)  # TODO: To convert from PIL image to OpenCV Pillow and OpenCV use different formats of images. So you can't just read an image in Pillow and manipulate it into an OpenCV image. Pillow uses the RGB format, and OpenCV uses the BGR format. So, you need a converter to convert from one format to another.
        opencv_image = cv2.resize(opencv_image, size)
        img = opencv_image[..., ::-1]
        img = np.around(np.transpose(img, (2, 0, 1)) / 255.0, decimals=12)
        x_train = np.array([img])
        embedding = model.predict_on_batch(x_train)

        return embedding
    except Exception as e:
        utils.logger.exception("--ERROR-- : image_to_encoding ->" + str(e))