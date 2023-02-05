# from keras.models import Sequential
# from keras.layers import Conv2D, ZeroPadding2D, Activation, Input, Concatenate
# from keras.models import Model
# from keras.layers.normalization import BatchNormalization
# from keras.layers.pooling import MaxPooling2D, AveragePooling2D
# from keras.layers.merge import Concatenate
# from keras.layers.core import Lambda, Flatten, Dense
# from keras.initializers import glorot_uniform
# from keras.engine.topology import Layer
# import random
# import shutil
# from numpy import genfromtxt


###################### ----------------------------------------ACTIVE LIBRARIES -----------------------------------###################################################################
import os
import warnings
warnings.filterwarnings("ignore")
import pickle
import numpy as np
import tensorflow as tf
from keras import backend as K
import keras

K.set_image_data_format("channels_first")
np.set_printoptions(threshold=2**31-1)

from Scripts.Services.ImageMatchingServices import fr_utils
from Scripts.Services.ImageMatchingServices import inception_blocks_v2
from Scripts.Services.ImageMatchingServices import preprocess
from Constants import const
from Scripts.Utility import utils
from Scripts.Services.MongoConnection.mongo_connection import MongoConn


from pprint import pprint

class Main:

    # Main function::
    def image_matching_main_service_method(self, case, user_data_json, server):
        try:
            # with graph.as_default():
            print("(a) Loading Face Recognition Model ...")
            # FRModel = inception_blocks_v2.faceRecoModel(input_shape=(3, 96, 96))
            # print("(b) Compiling Face Recognition Model ...")
            # FRModel.compile(optimizer='adam', loss=self.triplet_loss, metrics=['accuracy'])
            # print("(c) Loading Weights for Face Recognition Model ...")
            # fr_utils.load_weights_from_FaceNet(FRModel)

            K.clear_session()  # ValueError: Fetch argument <tf.Variable 'conv1/kernel:0' shape=(7, 7, 3, 64) dtype=float32_ref> cannot be interpreted as a Tensor. (Tensor Tensor("conv1/kernel:0", shape=(7, 7, 3, 64), dtype=float32_ref) is not an element of this graph.)
            g = tf.Graph()
            with g.as_default():
                FRModel = keras.models.load_model("./Assets/SavedModels/saved_FRmodel.hdf5", compile=False)
                # preprocess.preprocess_image_data(location=const.match_with_profile_images_folder)
                print("Generating Database of Available Images")
                mongo_conn_obj = MongoConn(server=server)


                if case == 'app1':

                    # Preprocessing the profile images uploaded to the size = (96,96)
                    preprocess.preprocess_image_data(img_file_path=user_data_json['profile_image_file_path'])

                    # To vectorize the image from image file path.
                    profile_image_embedding = self.get_img_embedding_from_image_location(img_file_path=user_data_json['profile_image_file_path'], model=FRModel)

                    return profile_image_embedding


                    # preference_img_embeddings_list = mongo_conn_obj.find_preferenceImageVector_from_table2(user_data_json=user_data_json)
                    #
                    # dist_dict_list1 = []
                    # for preference in preference_img_embeddings_list:
                    #     d = {}
                    #     dist = self.find_distance_from_img_embeddings(img_embedding1=preference["preference_img_embedding"], img_embedding2=profile_image_embedding, model=FRModel)
                    #     d['dist'] = float(dist)
                    #     d['preference_gender'] = preference['preference_gender']
                    #     d['preference_img_s3key'] = preference['preference_img_s3key']
                    #
                    #     dist_dict_list1.append(d)
                    #
                    # # To calculate Similarity score.
                    # for dic_i in dist_dict_list1:
                    #     similarity_score = 1.0 / (1.0 + dic_i['dist'])
                    #     dic_i['match_percentage'] = similarity_score * 100.0
                    #     dic_i['match_percentage'] = round(dic_i['match_percentage'], 2) # Rounding off the percentage decimal value (default=2)
                    #     dic_i['match_dist'] = float(dic_i['dist'])
                    #     dic_i.pop('dist', None)


                if case == 'app2':

                    # Getting all the profile images vectors (embeddings) from the Table#1.
                    profile_img_embeddings_list = mongo_conn_obj.find_profileImageVector_from_table1(user_data_json=user_data_json)

                    # Preprocessing the preference images uploaded to the size = (96,96)
                    preprocess.preprocess_image_data(img_file_path=user_data_json['preference_image_file_path'])

                    # # To vectorize the image from Numpy Array.
                    # preference_image_embedding = self.get_img_embedding_from_NumpyArray(img_array=user_data_json["preference_img_nparray"], model=FRModel)

                    # To vectorize the image from image file path.
                    preference_image_embedding = self.get_img_embedding_from_image_location(img_file_path=user_data_json['preference_image_file_path'], model=FRModel)

                    dist_dict_list2 = []
                    for profile in profile_img_embeddings_list:
                        d = {}
                        dist = self.find_distance_from_img_embeddings(img_embedding1=profile['profile_image_embedding'], img_embedding2=preference_image_embedding)
                        d['dist'] = float(dist)
                        d['match_user_id'] = profile['user_id']
                        d['match_gender'] = profile['gender']
                        # d['match_media_id'] = profile['media_id']
                        # d['profile_img_s3key'] = profile['profile_img_s3key']

                        dist_dict_list2.append(d)

                    # keys_tuple = self.key_with_max_and_min_val(dist_dict)
                    # max_dist = (max(dist_dict_list2, key=lambda x: x['dist']))['dist']
                    # min_dist = (min(dist_dict_list2, key=lambda x: x['dist']))['dist']


                    for dic_i in dist_dict_list2:
                        similarity_score = 1.0 / (1.0 + dic_i['dist'])
                        dic_i['match_percentage'] = similarity_score * 100.0
                        dic_i['match_percentage'] = round(dic_i['match_percentage'], 2) # Rounding off the percentage decimal value (default=2)
                        dic_i['match_dist'] = float(dic_i['dist'])
                        dic_i.pop('dist', None)

                    # pprint(dist_dict_list)
                    return dist_dict_list2, preference_image_embedding

        except Exception as e:
            utils.logger.exception("__ERROR__ ->" + str(e))



    # Geometrical Distance between Images
    def find_distance_from_img_embeddings(self, img_embedding1, img_embedding2):
        try:
            # encoding = fr_utils.image_to_encoding(image_path, model)
            dist = np.linalg.norm(img_embedding2 - img_embedding1)

            return dist
        except Exception as e:
            utils.logger.exception("--Error: Geometrical Distance between Images ->" + str(e))



    # Preprocess Images in a location/directory
    def get_img_embedding_from_NumpyArray(self, img_array, model):
        '''
        Input: numpy array.
        Output: image embedding
        '''
        try:

            img_embedding = fr_utils.image_to_encoding_from_numyArray(numpy_image=img_array, model=model)

            return img_embedding
        except Exception as e:
            utils.logger.exception("--Error: Preprocess Images in a location/directory ->" + str(e))


    def get_img_embedding_from_image_location(self, img_file_path, model):
        '''
        Input: file location/path
        Output: image embedding
        '''
        try:

            img_embedding = fr_utils.image_to_encoding_from_imagepath(image_path=img_file_path, model=model)

            return img_embedding
        except Exception as e:
            utils.logger.exception("--Error: Preprocess Images in a location/directory ->" + str(e))


    def key_with_max_and_min_val(self, dic):
        try:
            """ a) create a list of the dict's keys and values;
                b) return the key with the max value"""
            v = list(dic.values())
            k = list(dic.keys())

            return k[v.index(max(v))], k[v.index(min(v))]
        except Exception as e:
            utils.logger.exception("--Error: key_with_max_and_min_val ->" + str(e))


    # Triplet Loss Function
    def triplet_loss(self, y_true, y_pred, alpha=0.2):
        try:
            anchor = y_pred[0]
            positive = y_pred[1]
            negative = y_pred[2]
            pos_dist = tf.reduce_sum(tf.square(anchor - positive), axis=-1)
            neg_dist = tf.reduce_sum(tf.square(anchor - negative), axis=-1)
            basic_loss = pos_dist - neg_dist + alpha
            loss = tf.reduce_sum(tf.maximum(basic_loss, 0.0))

            return loss
        except Exception as e:
            utils.logger.exception("--ERROR: triple_loss " + str(e))






#-------------------------------- Having ImagePath as parameter for vectorizing images and finding distances---------------

    # Preprocess Images in a location/directory
    def create_datadict(self, database_location, model):
        try:
            data_dict = dict()

            for celeb in os.listdir(database_location):
                data_dict.update({celeb: fr_utils.image_to_encoding_from_imagepath(image_path=os.path.join(database_location, celeb), model=model)})

            return data_dict
        except Exception as e:
            utils.logger.exception("--Error: Preprocess Images in a location/directory ->" + str(e))


    def find_image_distances(self, image_location, database, model):
        try:
            dist_dict = {}
            for id in database.keys():
                dist = self.find_distance(image_path=image_location, identity=id, database=database, model=model)
                dist_dict.update({id: dist})

            return dist_dict
        except Exception as e:
            utils.logger.exception("--Error: Find Image Distances ->" + str(e))

    # Geometrical Distance between Images
    def find_distance(self, image_path, identity, database, model):
        try:
            encoding = fr_utils.image_to_encoding_from_imagepath(image_path, model)
            dist = np.linalg.norm(encoding - database[identity])

            return dist
        except Exception as e:
            utils.logger.exception("--Error: Geometrical Distance between Images ->" + str(e))



    # def display_image(self, image_loc, name):
    #     try:
    #         fig, axes = plt.subplots(1, 2, figsize=(18, 5))
    #         fig.subplots_adjust(hspace=0.5, wspace=0.5)
    #         for i, ax in enumerate(axes.flat):
    #             ax.imshow(cv2.cvtColor(cv2.imread(image_loc[i]), cv2.COLOR_BGR2RGB))
    #             ax.set_xlabel(name[i])
    #             ax.set_xticks([])
    #             ax.set_yticks([])
    #         plt.show()
    #     except Exception as e:
    #         utils.logger.exception("--Error: Display Images" + str(e))

