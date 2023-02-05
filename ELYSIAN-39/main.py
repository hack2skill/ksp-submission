from flask import Flask, render_template, request, redirect, url_for
import os
from os.path import join, dirname, realpath

import pandas as pd
import mysql.connector

app = Flask(__name__)


app.config["DEBUG"] = True

UPLOAD_FOLDER = 'static/files'
app.config['UPLOAD_FOLDER'] =  UPLOAD_FOLDER


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="csvdata"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")


for x in mycursor:
  print(x)






@app.route('/')
def index():
     
    return render_template('index.html')



@app.route("/", methods=['POST'])
def uploadFiles():
    
      uploaded_file = request.files['file']
      if uploaded_file.filename != '':
           file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
           uploaded_file.save(file_path)
           parseCSV(file_path)
      return redirect(url_for('index'))

def parseCSV(filePath):
      col_names = ['first_name','last_name','address', 'street', 'state' , 'zip']
      csvData = pd.read_csv(filePath,names=col_names, header=None)
      for i,row in csvData.iterrows():
             sql = "INSERT INTO addresses (first_name, last_name, address, street, state, zip) VALUES (%s, %s, %s, %s, %s, %s)"
             value = (row['first_name'],row['last_name'],row['address'],row['street'],row['state'],str(row['zip']))
             mycursor.execute(sql, value, if_exists='append')
             mydb.commit()
             print(i,row['first_name'],row['last_name'],row['address'],row['street'],row['state'],row['zip'])

if (__name__ == "__main__"):
     app.run(port = 5000)
