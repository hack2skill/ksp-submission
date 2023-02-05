# Copyright © DarkSide Assasins. All rights reserved.

from user.user import User
from routes.admin_bp import admin_bp

from flask import request, json,jsonify,render_template,url_for

from .sendSignupEmail import SignUpEmail

import base64

import ai_face_detection

class Resp():
    def __init__(self,text):
        self.resp = text

@admin_bp.route("/addNewUser",methods = ['GET','POST'])
def add_user():

    token = ""

    if request.method == 'POST':
        all = User.query.all()
        print(all)

        em = request.json['email']
        na = request.json['name']
        ro = request.json['role']

        exists = User.query.filter_by(email = em).first()

        if exists is None:
            print("New user")

            newUser = User.addUser(email=em,name=na,role=ro)

            User.addNewRecord(newUser)

            all = User.query.all()
            print(all)

            if(User.query.filter_by(email = em) is not None):
                print("db updated with new email")
                emSent = SignUpEmail(em)
                emSent.sendEmail()

                token = emSent.token
                print(type(token))
                confirm_url = url_for('user_bp.signup_user',token = emSent.token,_external = True)
                print(confirm_url)
                html = render_template('activate.html',confirm_url = confirm_url)
                emSent.send_email(to=em,subject = "Please confirm your email",template=html)

                if(emSent.status):
                    print("Mail sent")
                    resp = "User added successfully. Check inbox to sign up"
                else:
                    resp = "Something went wrong"
        
        else:
            if exists.emVerified == True:
                resp = "User already exists, please login"
            else:
                resp = "Perfrom email verification from inbox"

        return jsonify({"resp" : resp})
    
    if request.method == "GET":
        resp = jsonify({"token" : token})
        return resp


@admin_bp.route("/search",methods=["GET","POST"])
def run_algorithm():

    res = {"Report":"Giaant blob of text"}
    if request.method == "POST":
        image_bytes = base64.b64decode(request.json["img_path"])

        with open(request.json["name"],"wb") as fl:
            fl.write(image_bytes)

        im_path = request.json["name"]
        db_path = "missing_FIR_images"
        video_db_path = "videos/video1-opencv"
        video_path='videos/video1.mp4'
        img2_path="missing_FIR_images/6-000#_d11e623e-b8d2-4c24-886f-6b33c3c36d95424.jpg"

        search = request.json["search_against"]
        if "Image" in search:
            print("Searching image to image")
            res = ai_face_detection.find_image_in_db(img_path=im_path,db_path= db_path)

        elif "Video" in search:
            print("Searching image to video")
            res = ai_face_detection.find_image_in_video(img_path = im_path,video_path= video_path,db_path=video_db_path)
        else:
            print("Snap filterss yayyy")
            res = ai_face_detection.image_to_image_compare(img1_path = im_path,img2_path= img2_path)
        print(res)
        return res
    if request.method == "GET":
        return res
