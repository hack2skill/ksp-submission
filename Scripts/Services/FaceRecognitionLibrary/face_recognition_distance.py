import os
from Constants import const
from Scripts.Utility import utils
import face_recognition
import numpy as np


class FaceRecognition:

    def __init__(self):
        # from face_recognition import load_image_file, face_encodings, face_distance, compare_faces
        pass

    def face_enconding(self, img_file_path):
        try:
            load_img = face_recognition.load_image_file(img_file_path)
            img_encoding = face_recognition.face_encodings(load_img)

            if not len(img_encoding)==0:
                return img_encoding[0]

        except Exception as e:
            utils.logger.exception("__Error FaceRecognition: FaceEncoding__" + str(e))


    def face_distance(self, reference_img_file_path, test_img_file_path):

        try:
            reference_img_encoding = self.face_enconding(reference_img_file_path)
            test_img_encoding = self.face_enconding(test_img_file_path)

            if isinstance(reference_img_encoding, np.ndarray) and isinstance(test_img_encoding, np.ndarray):
                face_dist = face_recognition.face_distance([reference_img_encoding], test_img_encoding)
                is_comparable = face_recognition.compare_faces([reference_img_encoding], test_img_encoding)

                print(is_comparable[0])
                print(face_dist)

                return float(round(face_dist[0], 2)), is_comparable[0]

        except Exception as e:
            utils.logger.exception("__Error FaceRecognition: FaceDistance " + str(e))



    def face_comparison(self, reference_img_file_path, test_img_file_path):

        try:
            reference_img_encoding = self.face_enconding(reference_img_file_path)
            test_img_encoding = self.face_enconding(test_img_file_path)

            is_comparable = face_recognition.compare_faces([reference_img_encoding], test_img_encoding)
            print(is_comparable[0])

            return is_comparable[0]

        except Exception as e:
            utils.logger.exception("__Error FaceRecognition: FaceComparison__" + str(e))

    def face_comparison_encoding(self, list_ref_img_encoding, test_img_encoding):

        try:
            # reference_img_encoding = self.face_enconding(reference_img_file_path)
            # test_img_encoding = self.face_enconding(test_img_file_path)

            is_comparable_list = face_recognition.compare_faces(list_ref_img_encoding, test_img_encoding)
            face_dist_list = face_recognition.face_distance(list_ref_img_encoding, test_img_encoding)
            # print(is_comparable[0])

            return is_comparable_list, face_dist_list

        except Exception as e:
            utils.logger.exception("__Error FaceRecognition: FaceComparison__" + str(e))