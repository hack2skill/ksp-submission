from flask import Flask, request, render_template
import pandas as pd
import re

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)
