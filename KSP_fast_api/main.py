import os
import pdfkit
from fastapi import FastAPI,Request,Form,UploadFile,File,Path
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import psycopg2
from sqlalchemy import create_engine
import sqlalchemy as sa
from starlette import schemas
from fastapi.responses import FileResponse
from PyPDF2 import PdfMerger
app = FastAPI()
from deepface import DeepFace
import threading
import io
origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.post("/finger-recognize")
async def getFingerData(assignment_file: UploadFile = File(...)):
    file_path = "uploads/" + assignment_file.filename
    with open(file_path, "wb") as f:
        f.write(await assignment_file.read())
    os_imgs_listed = os.listdir("finger_print_dataset")
    models = ["VGG-Face", "Facenet", "OpenFace", "DeepFace", "DeepID", "Dlib", "ArcFace"]
    listed = []
    def threaded():
        for vls in os_imgs_listed:
            print(vls)
            verification = DeepFace.verify(img1_path=file_path, img2_path="finger_print_dataset/"+vls, model_name =
            models[4], enforce_detection=False)
            if verification["verified"]:
                listed.append(vls)
    threaded()
    alchemy_engine = create_engine('postgresql+psycopg2://octavian:Cradle123#@kspmain2.postgres.database.azure.com:5432/postgres')
    db_connection = alchemy_engine.connect()
    dataFrame = pd.read_sql_table("finger_print_dataset", db_connection)
    all_df_set = list(dataFrame.columns.values.tolist())

    filter_vals=None
    for (index,vls) in enumerate(listed):
        if index==0:
            filter_vals=(dataFrame["FingerPrint_data"]==vls)
            continue
        filter_vals |= (dataFrame["FingerPrint_data"]==vls)

    filtered_val_reply = []
    for idx_tab in range(0,len(dataFrame[filter_vals].index)):
        to_apned_val = dict(dataFrame[filter_vals].iloc[idx_tab].to_dict())
        to_apned_val["id"] = idx_tab
        filtered_val_reply.append(to_apned_val)

    return {
        "responses": filtered_val_reply
    }

@app.post("/image-recognize")
async def getInformatin(assignment_file: UploadFile = File(...)):
    file_path = "uploads/" + assignment_file.filename
    with open(file_path, "wb") as f:
        f.write(await assignment_file.read())
    os_imgs_listed = os.listdir("imgs")
    models = ["VGG-Face", "Facenet", "OpenFace", "DeepFace", "DeepID", "Dlib", "ArcFace"]
    listed = []
    def threaded():
        for vls in os_imgs_listed:
            print(vls)
            verification = DeepFace.verify(img1_path=file_path, img2_path="imgs/"+vls, model_name = models[4],
                                                                 enforce_detection=False)
            if verification["verified"]:
                if len(listed)>5:
                    break
                listed.append(vls)
    # t1 = threading.Thread(target=threaded)
    # t1.start()

    threaded()

    alchemy_engine = create_engine('postgresql+psycopg2://octavian:Cradle123#@kspmain2.postgres.database.azure.com:5432/postgres')
    db_connection = alchemy_engine.connect()
    dataFrame = pd.read_sql_table("arrest_data_main", db_connection)
    all_df_set = list(dataFrame.columns.values.tolist())

    filter_vals=None
    for (index,vls) in enumerate(listed):
        if index==0:
            filter_vals=(dataFrame["Photo_Full_front"]==vls)
            continue
        filter_vals |= (dataFrame["Photo_Full_front"]==vls)

    filtered_val_reply = []
    for idx_tab in range(0,len(dataFrame[filter_vals].index)):
        to_apned_val = dict(dataFrame[filter_vals].iloc[idx_tab].to_dict())
        to_apned_val["id"] = idx_tab
        filtered_val_reply.append(to_apned_val)

    return {"responses": filtered_val_reply }

@app.post("/search/{key}")
def search(key: str):
    alchemy_engine = create_engine('postgresql+psycopg2://octavian:Cradle123#@kspmain2.postgres.database.azure.com:5432/postgres')
    db_connection = alchemy_engine.connect()
    dataFrame = pd.read_sql_table("cleaned_KSP_hackathondata(1)", db_connection)
    all_df_set = list(dataFrame.columns.values.tolist())

    alchemy_engine_2 = create_engine('postgresql+psycopg2://octavian:Cradle123#@kspmain2.postgres.database.azure.com:5432/postgres')
    db_connection_2 = alchemy_engine.connect()
    dataFrame_2 = pd.read_sql_table("icjs_main_data", db_connection)

    frames = [dataFrame, dataFrame_2]
    dataFrame = pd.concat(frames)

    search = key
    datatype_complete = {
        'State':"string",
        'District_Name':"string",
        'PS_Name':"string",
        'FIRNo':"string",
        'FIR_Date':"date",
        'Person_No':"string",
        'Arrest_Date':"date",
        'Person_Name':"string",
        'Father_Name':"string",
        'Gender':"string",
        'AgeWhileOpening':"range",
        'Age': "range",
        'Pres_Address1':"string",
        'Perm_Address1':"string",
        'PersonStatus':"string",
        'Name':"string",
        'Major_Head':"string",
        'Minor_Head':"string",
        'Crime_No':"string",
        'Arr_ID':"string",
        'Unit_ID':"string",
        'fir_id':"string",
        'dedt':"string"
    }
    filter_vals = None
    for index,vls in enumerate(dict(dataFrame.dtypes)):
        if index==0:
            if dataFrame.dtypes[vls]==int or dataFrame.dtypes[vls]==float:
                if search.isnumeric():
                    filter_vals = (dataFrame[vls]==int(search))
                continue
            filter_vals = (dataFrame[vls].str.contains(search, case=False))
            continue
        if dataFrame.dtypes[vls]==int or dataFrame.dtypes[vls]==float:
            if search.isnumeric():
                filter_vals |= (dataFrame[vls]==int(search))
            continue
        print(dataFrame[vls].dtypes)
        filter_vals |= (dataFrame[vls].str.contains(search, case=False))
    filtered_val_reply = []
    for idx_tab in range(0,len(dataFrame[filter_vals].index)):
        to_apned_val = dict(dataFrame[filter_vals].iloc[idx_tab].to_dict())
        to_apned_val["id"] = idx_tab
        filtered_val_reply.append(to_apned_val)
    return {
        "message": filtered_val_reply
    }

@app.post("/pdf/")
def generate_pdf(requests: dict):
    # merger = PdfMerger()
    html_content = generate_html(requests["message"][0])
    pdf = pdfkit.from_string(html_content,'out.pdf')
    buffer = io.BytesIO(pdf)
    buffer.seek(0)
    return FileResponse(pdf)

def generate_html(request: dict):
    html_content = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <style>
                *{
                    margin: 0;
                    padding: 0;
                    text-align: center;
                }
                .data > *{
                    margin: 0.5em;
                }
            </style>
        </head>
        <body>
            <div>
                <img src="./ksp.png" width="100" height="100">
                <h1 style = "padding-bottom: 1em;">Karnataka State Police</h1>
            </div>
            <div>
                <div style="float: left; font-size:24px;" class = 'data'>
                    <hr style = "width: 100%;"
        """
    html_content += "<p><strong>Name:</strong>" + request["Person_Name"] + "</p>"
    html_content +='<hr style = "width: 100%;">'
    html_content += "<p><strong>Age:</strong>" + str(request["Age"])+"</p>"
    html_content += '<hr style = "width: 100%;">'
    html_content += "<p><strong>Gender:</strong>" + request["Gender"]+ "</p>"
    html_content +='<hr style = "width: 100%;">'
    html_content +="<p><strong>FIR No:</strong>" + request["FIRNo"]+"</p>"
    html_content +='<hr style = "width: 100%;"> </div>'
    # if requestimage == None:
    #     html_content += "<h1 style = 'width: 250px; height: 250px;'>NO IMAGE </h1>"
    #  <img src="./President_Barack_Obama.jpg" width = "250" height = "250" style = "float: right; border: 1px solid #000;">
    html_content += "<div style = 'width: 100%; margin-top: 1em; display: flex; justify-content: center; font-size: 24px;' class='data'>"
    html_content +='<hr style = "width: 100%;">'
    html_content += '<p><strong>Date of Arrest:</strong>'+ request["Arrest_Date"]+'</p>'
    html_content +='<hr style = "width: 100%;">'
    html_content +='<p><strong>Reason for Arrest:</strong>' + request["Major_Head"] + '</p>'
    html_content +='<hr style = "width: 100%;">'
    html_content +='<p><strong>Police Station Name:</strong>' + request["PS_Name"] + '</p>'
    html_content +='<hr style = "width: 100%;">'
    html_content +='<p><strong>District:</strong>' + request["District_Name"] + '</p>'
    html_content +='<hr style = "width: 100%;">'
    html_content += 'p><strong>State:</strong>' + request["State"] + '</p>'
    # html_content += """
    #             </div>
    #             <div style = 'padding-top: 3em;'>
    #                 <h1>Fingerprint:</h1>
    #             """
    # if request["fingerprint"] == None:
    #     html_content += "<h1 style = 'width: 250px; height: 250px;'>NO FINGERPRINT </h1>"
    # <img src="./fingerprint.jpg" style="margin-top: 1em;" width = "250" height="250">
    html_content += """
                </div>
            </div>
        </body>
        </html>
        """
    return html_content
