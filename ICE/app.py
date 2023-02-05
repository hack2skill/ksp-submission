from curses.ascii import isdigit
from flask import Flask, make_response, jsonify, send_file
from components.name_component import getDetailsFromName
from components.twitter_component import getDetailsFromTwitterHandle
from utils.pdf import generate_pdf_from_html
from components.phone_number_component import getDetailsFromPhoneNumberForTwilio
from components.phone_number_component import getDetailsFromPhoneNumber
from flask import request
from flask_cors import CORS
from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask,request
from twilio.rest import Client
import json
twilio_client = Client(account_sid, auth_token)

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/ping')
def hello_name():
    return 'Healthy'

@app.route('/getDetails')
def get_details():
    channel = str(request.args.get('channel'))
    value = str(request.args.get('value'))

    if channel == "truecaller":
        data = getDetailsFromPhoneNumber("+91"+value)
        return data
    elif channel == "twitter":
        data = getDetailsFromTwitterHandle(value)
        return data
    elif channel == "name":
        data = getDetailsFromName(value)
        return data

    print(value, channel)



@app.route('/reply',methods=["POST"])
def reply():
    message = request.values.get('Body', None)
    resp = MessagingResponse()
    if(len(str(message)) == 10):
        test = getDetailsFromPhoneNumberForTwilio(message)
        print(test)
        resp.message(test)
    elif(str(message) == "1"):
        resp.message("Thank you for replying. Please enter the mobile number of the person you want to search. Please don't include +91 in the number")
    else:
        resp.message("Welcome to Namma Sherlock.\n Press 1 to search using MobileNumber")
    return str(resp)

@app.route('/generateReport',methods = ['POST'])
def show_static_pdf():
    if request.method == "POST":
        # print(f"HI {request.data}")
        data = json.loads(request.get_data())
        # print(request.form)
        
        html_string = data["html_string"]
        
        status = generate_pdf_from_html(html_string)
        if status:
            # with open('GfG.pdf', 'rb') as static_file:
            return send_file('report.pdf', as_attachment=True)
        else:
            return {"response":"File not formed"}

if __name__ == '__main__':
    app.run(debug=True)
