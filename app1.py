from flask import Flask, request, render_template
import pandas as pd
import re

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files["file"]
        df = pd.read_excel(file)
        return render_template("index.html")

    return render_template("index.html")


@app.route("/analysis", methods=['GET', 'POST'])
def analysis():
    return render_template("userDetails.html")


@app.route('/upi')
def upi():

    return render_template('upi.html')


@app.route('/neft')
def neft():

    return render_template('neft.html')


@app.route('/imps')
def imps():

    return render_template('imps.html')


@app.route('/userDetails')
def userDetails():
    return render_template('userDetails.html')


@app.route('/others')
def others():
    return render_template('others.html')


if __name__ == '__main__':
    app.run(debug=True)
