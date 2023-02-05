# Copyright © DarkSide Assasins. All rights reserved.

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import bcrypt

db = SQLAlchemy()
ma = Marshmallow()

# User Table Model
class User(db.Model):

  __tablename__ = "user"

  id = db.Column(db.Integer,primary_key = True,autoincrement = True)
  email=db.Column(db.String, unique = True)
  name = db.Column(db.String(100))
  phone = db.Column(db.String(10))
  role = db.Column(db.Boolean,default=False)
  password = db.Column(db.String(100))
  designation = db.Column(db.String(25))
  emVerified = db.Column(db.Boolean,default = False)
  phVerified = db.Column(db.Boolean,default = False)

  def __init__(self,email,name,role,phone = "",password="",designation=""):

    self.email = email
    self.name = name
    self.role = role
    self.phone = phone
    self.password = bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt()).decode('utf-8')
    self.designation = designation
    
  @classmethod
  def admin(cls):
    email = "abc@gmail.com"
    name = "ABC"
    phone = "1234567809"
    role = True
    password = "!Sporthi1234"
    designation = "Student"
    return cls(email=email,name=name,role=role,phone=phone,password=password,designation=designation)


  @classmethod
  def addUser(cls,email,name,role) :
    email = email
    name = name
    role = role
    return cls(email=email,name=name,role=role)

  
  def create_admin(self):
    return self.admin()
    

  def updateUserOnSignup(record,email,name,phone,password,designation,emVerified) :

    record.email = email
    record.name = name
    record.phone = phone
    record.password = bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt()).decode('utf-8')
    record.emVerified = emVerified
    record.designation = designation

    db.session.commit()

  def get_id(self):
    return self.id
  
  def addNewRecord(record):
    db.session.add(record)
    db.session.commit()

  def removeUser(record):
    db.session.delete(record)
    db.session.commit()

class UserSchema(ma.Schema):
  class Meta:
    fields = ('id','email','name','password','phone','role','designation','emVerified','phVerified')

user_schema = UserSchema()
users_schema=UserSchema(many=True)