import os
import time  # to simulate a real time data, time loop
import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import plotly.express as px  # interactive charts
import streamlit as st  # 🎈 data web app development
from PIL import Image
import random

def load_image(img_path:str):
    """load the image using PIL
    Args:
        img_path: Image path
    Returns:
        image: PIL Image object
    """
    image = Image.open(img_path)
    return image

dataset_url = "../data/cases_db.csv"

# read csv from a URL
def get_data() -> pd.DataFrame:
    return pd.read_csv(dataset_url)

df = get_data()

#Header Image
header = load_image(os.path.join("assets","logo.png"))

col1, col2, col3 = st.columns([0.4,0.4,0.2])
col2.image(header, width=200)

#Project Title
st.markdown('<center><h1 style="color: black;">Case Creation</h1></center>',
                        unsafe_allow_html=True)


st.markdown('<br>', unsafe_allow_html=True)
st.markdown('<br>', unsafe_allow_html=True)
st.markdown('<br>', unsafe_allow_html=True)


with st.form("my_form", clear_on_submit=True):
    case_id = st.text_input('Case ID')

    case_summary = st.text_area('''Case Description''')

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        with st.spinner('Creating Case'):
            time.sleep(2)
            df = get_data()
            df2 = {'Case ID': case_id, 'Case Description': case_summary}
            print(df2)
            print(df)
            df = df.append(df2, ignore_index = True)
            df.to_csv(dataset_url, index=False)
