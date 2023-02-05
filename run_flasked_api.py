"""
Import all necessary packages
"""

# import API level modules
from flask import Flask
import flask_compress
from flask_cors import CORS
import __root__

# import project files
from Scripts.xfactor_main import app_main
from Scripts.Utility import utils



app_wsgi = Flask(__name__)

# Compressing all response:
flask_compress.Compress(app_wsgi)

# Connecting all services via blueprint
app_wsgi.register_blueprint(app_main)

CORS(app_wsgi, resources={r'/*': {'origin': '*'}})
# Setting configs
app_wsgi.config["UPLOAD_FOLDER"] = __root__.path() + "/static/img"
app_wsgi.config["MAX_CONTENT_LENGTH"] = 5*1024*1024 # 5 MB
app_wsgi.config["ALLOWED_EXTENSION"] = [".jpg", ".jpeg", ".png", ".gif"]
# Declaring Apps:

if __name__ == "__main__":
    app_wsgi.run(host=utils.configuration["settings"]["ip"], port=utils.configuration["settings"]["port"], debug=True, threaded=True, use_reloader=False)