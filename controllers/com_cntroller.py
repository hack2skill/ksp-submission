# Copyright © DarkSide Assasins. All rights reserved.

from user.user import User,db
from main import app
from flask import json, jsonify, request
import bcrypt

from.sendSignupEmail import SignUpEmail

@app.route('/',methods=['GET'])
def home():
    return "Hello world"

@app.route('/login',methods=["POST"])
def login():

    db.session.query(User).delete()
    db.session.commit()
    
    admin = User.create_admin(User)
    User.addNewRecord(admin)

    all = User.query.all()
    print(all)
    
    email = request.json['email']
    password = request.json['password']

    login = User.query.filter_by(email = email).first()

    if login is not None:

        if(bcrypt.checkpw(password=password.encode('utf-8'),hashed_password=login.password.encode('utf-8'))):
            print("User success")
            resp = jsonify({
                'id':login.id,
                'email':login.email,
                'name':login.name,
                'password':str(login.password),
                'phone':login.phone,
                'role':login.role,
                'resp':"Logged in"
            })
            return resp
        else:
            print("Unsuccessfull")
            return jsonify({"res":"Password incorrect"})
    else:
        print("User doesn't exists")
        return jsonify({"res":"Username doesn't exist, please contact the admin"})