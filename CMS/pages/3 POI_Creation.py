import os
import time  # to simulate a real time data, time loop
import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import plotly.express as px  # interactive charts
import streamlit as st  # 🎈 data web app development
from PIL import Image
import random
import requests
import json
from datetime import datetime

def load_image(img_path:str):
    """load the image using PIL
    Args:
        img_path: Image path
    Returns:
        image: PIL Image object
    """
    image = Image.open(img_path)
    return image

dataset_url = "../data/pois_db.csv"

# read csv from a URL
def get_data() -> pd.DataFrame:
    return pd.read_csv(dataset_url)

df = get_data()
case_data = pd.read_csv("../data/cases_db.csv")

class NumpyEncoder(json.JSONEncoder):
    """Encodes the numpy array into list
    """
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)

def create_request(uploaded_file,poi_id,case_id):
    """post request to predictions
    """
    backend = "http://20.231.200.146:8000"

    url = f"{backend}/parse_bank_statement"

    if not os.path.exists("tmp"):
        os.makedirs("tmp")

    print(uploaded_file.name.split(".")[-1])

    with open(os.path.join("tmp",str(uploaded_file.name.split(".")[0]) + '.' + str(uploaded_file.name.split(".")[-1])), "wb") as f:
        f.write(uploaded_file.getvalue())
        f.close()

        file = {'file': (str(uploaded_file.name.split(".")[0]) + '.' + str(uploaded_file.name.split(".")[-1]), open(os.path.join("tmp",str(uploaded_file.name.split(".")[0]) + '.' + str(uploaded_file.name.split(".")[-1])), 'rb'))}

    #post request
    response = requests.post(url, files=file)
    data_path = str(case_id) + '_' + str(poi_id) + '_' + str(datetime.now().strftime("%Y-%m-%d-%H-%M-%S")) + '.csv'
    with open('../data/bank_statments/' + data_path, "wb") as f:
        f.write(response.content)
        f.close()
    # response.to_csv('../data/bank_statments/' + data_path, index=False)

    os.remove(os.path.join("tmp",str(uploaded_file.name.split(".")[0]) + '.' + str(uploaded_file.name.split(".")[-1])))

    return data_path

#Header Image
header = load_image(os.path.join("assets","logo.png"))

col1, col2, col3 = st.columns([0.4,0.4,0.2])
col2.image(header, width=200)

#Project Title
st.markdown('<center><h1 style="color: black;">POI Data Creation</h1></center>',
                        unsafe_allow_html=True)


st.markdown('<br>', unsafe_allow_html=True)
st.markdown('<br>', unsafe_allow_html=True)
st.markdown('<br>', unsafe_allow_html=True)

with st.form("my_form", clear_on_submit=True):
    case_id = st.selectbox("Case ID", options=list(case_data['Case ID'].unique()))

    poi_id = st.text_input('POI ID')
    poi_name = st.text_input('POI Name')

    poi_pan_card = st.text_input('POI PAN Card')
    poi_aadhaar = st.text_input('POI Aadhaar')

    uploaded_file = st.file_uploader("Upload Bank Statement")
            
    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        with st.spinner('Creating POI Data'):
            data_path = create_request(uploaded_file,poi_id,case_id)
            print(data_path)
            time.sleep(2)
            df = get_data()
            df2 = {'POI ID': poi_id, 'Case ID': case_id, 'POI Name': poi_name, 'POI PAN Card': poi_pan_card, 'POI Aadhaar': poi_aadhaar, 'POI Bank Statement': data_path}
            print(1)
            print(df2)
            print(2)
            print(df)
            df = df.append(df2, ignore_index = True)
            print(3)
            print(df)
            df.to_csv(dataset_url, index=False)
            case_data = pd.read_csv("../data/cases_db.csv")
            case_data = case_data.merge(df,on='Case ID',how='left')
            print(4)
            print(case_data)
            case_data.to_csv('../data/master_db.csv', index=False)
