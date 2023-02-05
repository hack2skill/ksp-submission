import os
import cv2
import pathlib
from Constants import const

from Scripts.Utility import utils

def preprocess_image_data(img_file_path):
    try:
        # img_file_path = os.path.join(location, file)
        size = (96, 96)
        img = cv2.resize(cv2.imread(img_file_path), size)
        cv2.imwrite(img_file_path, img)

    except Exception as e:
        utils.logger.exception("--Preprocessing Error--" + str(e))





