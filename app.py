from flask import Flask,render_template,redirect,url_for
import os
app = Flask(__name__)
app.static_folder = 'static'

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    try:
        imagefile = app.request.files('imagefile', '')
    except Exception as err:
        pass
    


if __name__ == '__main__':
    app.run(debug=True)
