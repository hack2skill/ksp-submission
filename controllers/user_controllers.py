# Copyright © DarkSide Assasins. All rights reserved.
from user.user import User, db
from routes.user_bp import user_bp

from flask import request, json,jsonify,render_template

@user_bp.route('/confirm/<token>',methods = ["GET","POST"])      
def signup_user(token):
    url = "/user/confirm/"+token
    return render_template("confrimUrl.html",route = url)

    if request.method == "GET":
        return jsonify({"resp":"launch url","token":token})
    
    if request.method == "POST":
        try:
            email = confirm_token(token)
        except:
            return jsonify({"resp":"Email expired, contact admin"})
        
        em = request.body["email"]
        na = request.body["name"]
        pa = request.body["password"]
        phone = request.body["phone"]
        desig = request.body["designation"]
        emVer = True

        if(email == em):
            signupUser = User.query.filter_by(email = em)

            if signupUser.emVerified == False:
                User.updateUserOnSignup(signupUser,email=em,name=na,password=pa,phone=phone,designation=desig,emVerified=emVer)
                return jsonify({"resp":"Signed up successfully, please login"})
            else:
                return jsonify({"resp" : "User already verified, please login"})
        else:
            print("Something went wrong")

            return jsonify({"resp":"Something went wrong"})
