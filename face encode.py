import argparse
import pickle
import os
from os import listdir
from numpy import asarray
from numpy import expand_dims
from keras_facenet import FaceNet
from PIL import Image as Img
from utils import *


parser = argparse.ArgumentParser()

parser.add_argument('--model-cfg', type=str, default='./cfg/yolov3-face.cfg',
                    help='path to config file')
parser.add_argument('--model-weights', type=str,
                    default='./model-weights/yolov3-wider_16000.weights',
                    help='path to weights of model')
parser.add_argument('--image', type=str, default='',
                    help='path to image file')
parser.add_argument('--video', type=str, default='',
                    help='path to video file')
parser.add_argument('--src', type=int, default=0,
                    help='source of the camera')
parser.add_argument('--output-dir', type=str, default='outputs/',
                    help='path to the output directory')
args = parser.parse_args()

MyFaceNet =FaceNet()
net = cv2.dnn.readNetFromDarknet(args.model_cfg, args.model_weights)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)


folder='C:/Users/sanjai/KSP face recognition api/missing'
database={}
def face_encode(folder):
    for filename in listdir(folder):
        path = folder + filename
        frame = cv2.imread(folder + filename)
        print(path)
        # Stop the program if reached end of video

        # Create a 4D blob from a frame.
        blob = cv2.dnn.blobFromImage(frame, 1 / 255, (IMG_WIDTH, IMG_HEIGHT),
                                     [0, 0, 0], 1, crop=False)

        # Sets the input to the network
        net.setInput(blob)

        # Runs the forward pass to get output of the output layers
        outs = net.forward(get_outputs_names(net))

        # Remove the bounding boxes with low confidence
        faces = post_process(frame, outs, CONF_THRESHOLD, NMS_THRESHOLD)
        print('[i] ==> # detected faces: {}'.format(len(faces)))
        print('#' * 60)

        # initialize the set of information we'll displaying on the frame
        info = [
            ('number of faces detected', '{}'.format(len(faces)))

        ]
        print(faces)
        if len(faces) > 0:
            x1, y1, width, height = faces[0]
        else:
            x1, y1, width, height = 1, 1, 10, 10

        print(x1, y1, width, height)
        x1, y1 = abs(x1), abs(y1)
        x2, y2 = x1 + width, y1 + height

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = Img.fromarray(frame)  # konversi dari OpenCV ke PIL
        gbr_array = asarray(frame)
        face = gbr_array[y1:y2, x1:x2]

        face = Img.fromarray(face)
        face = face.resize((160, 160))
        face = asarray(face)

        face = expand_dims(face, axis=0)
        print(face)
        print(faces)
        signature = MyFaceNet.embeddings(face)
        print(signature)
        database[os.path.splitext(filename)[0]] = signature

    myfile = open("data.pkl", "wb")
    pickle.dump(database, myfile)
    myfile.close()


