from flask import Flask, request
from flask_cors import CORS, cross_origin
import cv2
import numpy as np
import os

app = Flask(__name__)
cors = CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/", methods=['GET', 'POST'])
@cross_origin()
def func():

    if request.method == "POST":
        img = request.files['image']
        img.save('info.jpg')

        fingerprint_test = cv2.imread('info.jpg')

        for file in [file for file in os.listdir("Test")]:
            fingerprint_database_image = cv2.imread("./Test/" + file)
            sift = cv2.xfeatures2d.SIFT_create()
            keypoints_1, descriptors_1 = sift.detectAndCompute(
                fingerprint_test, None)
            keypoints_2, descriptors_2 = sift.detectAndCompute(
                fingerprint_database_image, None)

            matches = cv2.FlannBasedMatcher(dict(algorithm=1, trees=10), dict()).knnMatch(
                descriptors_1, descriptors_2, k=2
            )
            match_points = []

            for p, q in matches:
                if p.distance < 0.1 * q.distance:
                    match_points.append(p)

                    keypoints = 0

                    if len(keypoints_1) <= len(keypoints_2):
                        keypoints = len(keypoints_1)
                    else:
                        keypoints = len(keypoints_2)

                    print((len(match_points) / keypoints))

                    if (len(match_points) / keypoints) > 0.80:
                        # print("% match: ", len(match_points) / keypoints * 100)
                        # print("Figerprint ID: " + str(file))
                        # result = cv2.drawMatches(
                        #     fingerprint_test,
                        #     keypoints_1,
                        #     fingerprint_database_image,
                        #     keypoints_2,
                        #     match_points,
                        #     None,
                        # )
                        # result = cv2.resize(result, None, fx=2.5, fy=2.5)
                        # cv2.imwrite("result.jpg", result)
                        # cv2.waitKey(0)
                        # cv2.destroyAllWindows()
                        # return f"% match: ", len(match_points) / keypoints * 100, "Figerprint ID: " + str(file)
                        return str((len(match_points) / keypoints * 100))

        return "0"


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
