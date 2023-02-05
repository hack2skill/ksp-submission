# Copyright © DarkSide Assasins. All rights reserved.
import os

SECRET_KEY = os.urandom(32)
SECURITY_PASSWORD_SALT = 'my_precious_two'
BCRYPT_LOG_ROUNDS = 13
WTF_CSRF_ENABLED = True
DEBUG_TB_ENABLED = False
DEBUG_TB_INTERCEPT_REDIRECTS = False
SERVER_NAME = "127.0.0.1:5000"

MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True  

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
SQLALCHEMY_TRACK_MODIFICATIONS = False

CORS_HEADERS = 'Content-Type'

MAIL_USERNAME = ' '
MAIL_PASSWORD = ' '
MAIL_DEFAULT_SENDER = " "
