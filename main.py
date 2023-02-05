# Copyright © DarkSide Assasins. All rights reserved.
from flask import Flask, request, jsonify
from flask_migrate import Migrate
from flask_cors import CORS
from flask_mail import Mail

app = Flask(__name__)
app.config.from_object('config')
mail = Mail(app)
cors = CORS(app)

from routes.user_bp import user_bp
from routes.admin_bp import admin_bp
from controllers.com_cntroller import home,login
from user.user import User,db

db.init_app(app)
migrate = Migrate(app,db)

app.register_blueprint(user_bp, url_prefix = '/user')
app.register_blueprint(admin_bp, url_prefix = '/admin')


app.route('/',methods=['GET'])(home)
app.route('/login',methods=['POST'])(login)


if __name__=='__main__':
  app.run(debug=True,port=5000)
