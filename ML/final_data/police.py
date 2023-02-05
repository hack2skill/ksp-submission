from flask import Flask,jsonify,request
import numpy as np
import cv2
import os
import tensorflow as tf
import pandas as pd
train_df = pd.read_excel("Sample Missing Persons FIRS.xlsx")
ing = train_df["Photo_Full_front"].to_dict()


model = tf.keras.models.load_model("Model.h5")
app = Flask(__name__)

@app.route("/")
def home():
    return jsonify("Hello ur connected to the server")


@app.route("/image",methods=['POST'])
def pred():
    if request.method == 'POST':
        file=request.files["image"]
        file.save(file.filename)
        test_img = cv2.imread(file.filename)
        image=tf.image.resize(test_img,(224,224))
        image = np.expand_dims(image, axis=0)
        image_p=image/255.
       
        pre = model.predict(image_p)

          
       
    return jsonify(ing[pre.argmax()])