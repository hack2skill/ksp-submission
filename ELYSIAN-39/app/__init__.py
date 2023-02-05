from flask import Flask, url_for,render_template, request, session
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from importlib import import_module
from logging import basicConfig, DEBUG, getLogger, StreamHandler
from os import path
import os
import csv
from flask import Flask, request, render_template, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
from datetime import datetime

import pandas as pd
from werkzeug.utils import secure_filename

from PIL import Image
from pytesseract import pytesseract
from io import BytesIO
import base64
import re
from io import StringIO
from google_trans_new import google_translator
 






db = SQLAlchemy()
login_manager = LoginManager()

class BankForm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    field1 = db.Column(db.String(100), nullable=True)
    field2 = db.Column(db.String(100), nullable=True)


def register_extensions(app):
    db.init_app(app)
    login_manager.init_app(app)


def register_blueprints(app):
    for module_name in ('base', 'forms', 'ui', 'home', 'tables', 'data', 'additional'):
        module = import_module('app.{}.routes'.format(module_name))
        app.register_blueprint(module.blueprint)



def configure_database(app):

    @app.before_first_request
    def initialize_database():
        db.create_all()

    @app.teardown_request
    def shutdown_session(exception=None):
        db.session.remove()


def configure_logs(app):
    basicConfig(filename='error.log', level=DEBUG)
    logger = getLogger()
    logger.addHandler(StreamHandler())
    



def apply_themes(app):
    """
    Add support for themes.

    If DEFAULT_THEME is set then all calls to
      url_for('static', filename='')
      will modfify the url to include the theme name

    The theme parameter can be set directly in url_for as well:
      ex. url_for('static', filename='', theme='')

    If the file cannot be found in the /static/<theme>/ lcation then
      the url will not be modified and the file is expected to be
      in the default /static/ location
    """
    @app.context_processor
    def override_url_for():
        return dict(url_for=_generate_url_for_theme)

    def _generate_url_for_theme(endpoint, **values):
        if endpoint.endswith('static'):
            themename = values.get('theme', None) or \
                app.config.get('DEFAULT_THEME', None)
            if themename:
                theme_file = "{}/{}".format(themename, values.get('filename', ''))
                if path.isfile(path.join(app.static_folder, theme_file)):
                    values['filename'] = theme_file
        return url_for(endpoint, **values)


def create_app(config, selenium=False):
    app = Flask(__name__, static_folder='base/static')
    
    

 
#*** Flask configuration
 
# Define folder to save uploaded files to process further
    UPLOAD_FOLDER = os.path.join('staticFiles', 'uploads')
    
    # Define allowed files (for this example I want only csv file)

    # Configure upload file path flask
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    
    # Define secret key to enable session
    app.secret_key = 'This is your secret key to utilize session in Flask'
    
    
    @app.route('/upload')
    def index():
        return render_template('index_upload_and_show_data.html')
    
    @app.route('/upload',  methods=("POST", "GET"))
    def uploadFile():
        if request.method == 'POST':
            # upload file flask
            uploaded_df = request.files['uploaded-file']
    
            # Extracting uploaded data file name
            data_filename = secure_filename(uploaded_df.filename)
    
            # flask upload file to database (defined uploaded folder in static path)
            uploaded_df.save(os.path.join(app.config['UPLOAD_FOLDER'], data_filename))
    
            # Storing uploaded file path in flask session
            session['uploaded_data_file_path'] = os.path.join(app.config['UPLOAD_FOLDER'], data_filename)
    
            return render_template('index_upload_and_show_data_page2.html')
    
    
    @app.route('/show_data')
    def showDatap():
        # Retrieving uploaded file path from session
        data_file_path = session.get('uploaded_data_file_path', None)
        # from PDF_CSV import main
        # main(data_file_path)
        
        # f = open(data_file_path, "r")
        # print(f.read())
        # read csv file in python flask (reading uploaded csv file from uploaded server location)
        uploaded_df = pd.read_csv(data_file_path)
        uploaded_df.to_csv(r"C:\Users\siddh\flask_proj\app\home\s.csv",index=False)
        
        
        cols = uploaded_df.columns.values.tolist()
        for row in uploaded_df.itertuples(name='Pandas'):
            bank_form = BankForm(field1=row[2],field2=row[0])
            db.session.add(bank_form)
        db.session.commit()
        
        #pandas dataframe to html table flask
        uploaded_df_html = uploaded_df.to_html()
        return render_template('show_csv_data.html', data_var = uploaded_df_html)
    
     
    @app.route('/show_datap')
    def showData():
        # Retrieving uploaded file path from session
        data_file_path = session.get('uploaded_data_file_path', None)
        # import tabula
        # tabula.convert_into(data_file_path, "u.csv", output_format="csv", pages='1')
        # # from PDF_CSV import main
        # # main(data_file_path)
        
        # # f = open(data_file_path, "r")
        # # print(f.read())
        # # read csv file in python flask (reading uploaded csv file from uploaded server location)
        # uploaded_df = pd.read_csv("u.csv")
        # uploaded_df.to_csv(r"C:\Users\siddh\flask_proj\app\home\s.csv",index=False)
        
        import os
        print(data_file_path)
        os.system('camelot lattice -plot text '+str(data_file_path))
        
        # # cols = uploaded_df.columns.values.tolist()
        # # for row in uploaded_df.itertuples(name='Pandas'):
        # #     bank_form = BankForm(field1=row[1],field2=row[2])
        # #     db.session.add(bank_form)
        # # db.session.commit()
        
        # #pandas dataframe to html table flask
        # uploaded_df_html = uploaded_df.to_html()
        return render_template('show_csv_data.html')

        
    

    @app.route('/forms/form')
    def my_form():
        #text = request.form['srch']
        #processed_text = text.upper()
        
        #print(processed_text)
        #return str()
        return render_template('form.html')
    
    @app.route('/forms/form', methods=['POST'])
    def my_form_post():
        print("CHECKKK")
        text = request.form['srch']
        processed_text = text.upper()
        query = BankForm.query.filter_by(field2='27131').all()
        for b in query:
            print(b.field1)
        return render_template('form-db.html',data=query)
    
    @app.route('/forms/form_wizards')
    def my_form_wiz():
        return render_template('form_wizards.html')
    
    @app.route('/translate')
    def image():
        # path_to_tesseract = r'C:\Users\siddh\AppData\Local\Tesseract-OCR\tesseract.exe'
        # im = Image.open(r"C:\Users\siddh\flask_proj\staticFiles\uploads\cropped.png")
        # pytesseract.tesseract_cmd = path_to_tesseract
        # text = pytesseract.image_to_string(im,lang='eng')
        render_template('/forms/form_wizards')
        
    @app.route('/translate', methods=['POST'])
    def imagep():
        if request.method == 'POST':
            text = request.form['teamDropdown']
            path_to_tesseract = r'C:\Users\siddh\AppData\Local\Tesseract-OCR\tesseract.exe'
            im = Image.open(r"C:\Users\siddh\flask_proj\staticFiles\uploads\cropped.png")
            pytesseract.tesseract_cmd = path_to_tesseract
            text2 = pytesseract.image_to_string(im,lang='eng')
            if text in text2:
                val = 'True'
            else:
                val = 'False'
        return render_template('form_wizards2.html',val=val)
        
        

    @app.route('/forms/form_wizards', methods=['POST'])
    def my_form_wiz_post():
        if request.method == 'POST':
            print("CHECK")
            #upload file flask
            uploaded_df = request.files['uploaded-image']
            # Extracting uploaded data file name
            data_filename = "cropped.png"
            
            # flask upload file to database (defined uploaded folder in static path)
            uploaded_df.save(os.path.join(app.config['UPLOAD_FOLDER'], data_filename))
            #Storing uploaded file path in flask session
            session['uploaded_data_file_path'] = os.path.join(app.config['UPLOAD_FOLDER'], data_filename)
        return render_template('form_wizards.html')

    app.config.from_object(config)
    if selenium:
        app.config['LOGIN_DISABLED'] = True
    register_extensions(app)
    register_blueprints(app)
    configure_database(app)
    configure_logs(app)
    apply_themes(app)
    return app
