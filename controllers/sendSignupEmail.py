# Copyright © DarkSide Assasins. All rights reserved.
from itsdangerous import URLSafeTimedSerializer
from main import app,mail
from flask_mail import Message
from user.user import User
import os,subprocess

class SignUpEmail():
    status = False
    email = ""
    token = ""
    def __init__(self,email):
        self.email = email
        self.status = False
    
    def generate_confirmation_token(self,em):
        serializer = URLSafeTimedSerializer(app.config["SECRET_KEY"])
        self.token  = serializer.dumps(em,salt = app.config["SECURITY_PASSWORD_SALT"])       

    def confirm_token(self,exp = 3600):
        serializer = URLSafeTimedSerializer(app.config["SECRET_KEY"])
        try:
            email = serializer.loads(
                self.token,
                salt = app.config["SECRET_KEY"],
                max_age = exp                
            )
        except:
            userToRemove = User.query.filter_by(email = self.email)
            User.removeUser(record=userToRemove)
            return False
        return email

    def send_email(self,to,subject,template):
        msg = Message(
            subject = subject,
            recipients = [to],
            html = template,
            sender = app.config["MAIL_DEFAULT_SENDER"]
        )
        try:
            st = mail.send(msg)
            self.status = True
        except Exception as e:
            print(e)
            print("mail not sent")
            self.status = False
            
    def sendEmail(self):
        self.generate_confirmation_token(self.email)
        