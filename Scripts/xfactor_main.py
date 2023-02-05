import os
import random
import shutil
import json
import __root__
import numpy as np
from flask import Blueprint
from flask import request
from flask import *
from flask import jsonify
from flask import render_template
from werkzeug.utils import secure_filename
from pprint import pprint
from collections import OrderedDict


import io
import os
import shutil
from datetime import datetime
import json
import bson.json_util
import functools

import flask
from werkzeug.utils import secure_filename
from werkzeug.exceptions import RequestEntityTooLarge

from PIL import Image
# import pillow_avif
from io import BytesIO
import numpy as np


from Constants import const
from Scripts.Services.ImageMatchingServices.main_image_matching_service import Main
from Scripts.Services.AwsConnection.aws_s3_bucket_conn import AWS_S3BucketConnection
from Scripts.Services.FaceRecognitionLibrary.face_recognition_distance import FaceRecognition
from Scripts.Services.MongoConnection.mongo_connection import MongoConn
from Scripts.Utility import utils

exception_message = '{"status":False, "status":"Server error, please contact your administrator"}'
method_error_message = '{"status": False, "message": "Method not supported!"}'

app_main = Blueprint("app_main", __name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

server = "testing"

# server = "production"


@app_main.route("/index")
@app_main.route("/")
def index():
    target_folder = os.path.join(__root__.path(), "static/img")
    for root, dirs, files in os.walk(target_folder):
        for f in files:
            file_path = os.path.join(root, f)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
            except Exception as e:
                print("Failed to delete % s. Reason: %s" %(file_path, str(e)))


    return flask.render_template("home.html", file_path="img/image_here.jpg")

@app_main.route("/upload", methods=["POST"])
def upload():
    target = os.path.join(APP_ROOT, "static/img")
    if not os.path.isdir(target):
        # if os.name in ["nt", "posix"]:
        os.makedirs(target)

    for file in request.files.getlist("file"):
        if file.filename.endswith(tuple(current_app.config["ALLOWED_EXTENSION"])):
            file.save("static/img/" + const.img_now)
        elif file.filename.endswith("avif"):
            img = Image.open(file)
            img.save("static/img/" + const.img_now)

    shutil.copyfile("static/img/" + const.img_now, "static/img/" + const.img_normal)

    return flask.render_template("upload.html", file_path="img/img_now.jpg")

@app_main.route("/suspect_faces", methods=["GET", "POST"])
def suspect_faces():
    if request.method == "POST":
        try:
            top_matched_numbers = request.form.getlist('top_matched_numbers')[0]


            # for root, subdirs, files in os.walk("./Data/compare_profile_images"):
            #     for file in files:
            #         print("Deleting file : {}".format(file))
            #         os.remove(os.path.join(root, file))

            test_suspect_image_file = []
            for root, subdirs, files in os.walk(const.suspect_test_image):
                for file in files:
                    test_suspect_image_file.append(os.path.join(root, file))

            all_suspect_images = []
            for root, subdirs, files in os.walk(const.suspects_images_repo):
                for file in files:
                    all_suspect_images.append(os.path.join(root, file))


            compare_faces_obj = FaceRecognition()

            from collections import defaultdict

            response = {}

            ref_img_encodings = OrderedDict()
            list_ref_img_encodings = []
            list_ref_img_names = []

            for ref_img in all_suspect_images:
                if os.path.isfile(ref_img):
                    img_encoding = compare_faces_obj.face_enconding(ref_img)
                    if isinstance(img_encoding, np.ndarray):
                        ref_img_encodings[ref_img.split("/")[-1]] = img_encoding
                        list_ref_img_names.append(ref_img.split("/")[-1])
                        list_ref_img_encodings.append(img_encoding)

            if os.path.isfile(test_suspect_image_file[0]):
                test_img_encoding = compare_faces_obj.face_enconding(test_suspect_image_file[0])

                is_comparable_list, face_dist_list = compare_faces_obj.face_comparison_encoding(list_ref_img_encoding=list_ref_img_encodings, test_img_encoding=test_img_encoding)
                response2 = []
                for k, i, j in zip(ref_img_encodings.keys(), is_comparable_list, face_dist_list):
                    response[k] = {"is_comparable": i, "face_dist": j}
                    # response2.append([k, i, j])

                final_response = dict(OrderedDict(sorted(response.items(), key=lambda kv: kv[1]['face_dist'], reverse=False)[0:int(top_matched_numbers)]))
                # for k, v in final_response:
                #     # for k1, v1 in v.values():
                #     response2.append([k, list(v.values())])

                print("final_response........", response2)
                return json.dumps(str(final_response))
                # return render_template("matched.html", result=final_response)



        except Exception as e:
            utils.logger.exception("__Error__" + str(e))
