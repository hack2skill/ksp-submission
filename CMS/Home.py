import os
import time  # to simulate a real time data, time loop
import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import plotly.express as px  # interactive charts
import streamlit as st  # 🎈 data web app development
from PIL import Image

st.set_page_config(
    page_title="CMS",
    page_icon="🗄️",
    layout="wide",
)

def load_image(img_path:str):
    """load the image using PIL
    Args:
        img_path: Image path
    Returns:
        image: PIL Image object
    """
    image = Image.open(img_path)
    return image

dataset_url = "../data/master_db.csv"

# read csv from a URL
def get_data() -> pd.DataFrame:
    return pd.read_csv(dataset_url)

df = get_data()

#Header Image
header = load_image(os.path.join("assets","logo.png"))

col1, col2, col3 = st.columns([0.4,0.4,0.2])
col2.image(header, width=200)

#Project Title
st.markdown('<center><h1 style="color: black;">Case Managment System</h1></center>',
                        unsafe_allow_html=True)


st.markdown('<br>', unsafe_allow_html=True)
st.markdown('<br>', unsafe_allow_html=True)
st.markdown('<br>', unsafe_allow_html=True)

# create three columns
start, col1, mid, col2 = st.columns([0.1,0.4,0.1,0.4])

with col1:
    col1.markdown('<h3 style="color: black;">Total Cases 📂</h3>',
                        unsafe_allow_html=True)

    col1.subheader((df['Case ID'].nunique()))

with col2:
    col2.markdown('<h3 style="color: black;">Total POIs 🧑</h3>',
                        unsafe_allow_html=True)

    col2.subheader((df['POI ID'].nunique()))
