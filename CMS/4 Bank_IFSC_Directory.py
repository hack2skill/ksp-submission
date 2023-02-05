import os
import time  # to simulate a real time data, time loop
import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import plotly.express as px  # interactive charts
import streamlit as st  # 🎈 data web app development
from PIL import Image
import random
from st_aggrid import AgGrid

def load_image(img_path:str):
    """load the image using PIL
    Args:
        img_path: Image path
    Returns:
        image: PIL Image object
    """
    image = Image.open(img_path)
    return image

dataset_url = "../data/bank_ifsc_data.csv"

# read csv from a URL
def get_data() -> pd.DataFrame:
    return pd.read_csv(dataset_url)

#Header Image
header = load_image(os.path.join("assets","logo.png"))

col1, col2, col3 = st.columns([0.4,0.4,0.2])
col2.image(header, width=200)

#Project Title
st.markdown('<center><h1 style="color: black;">Bank IFSC Directory</h1></center>',
                        unsafe_allow_html=True)

# CSS to inject contained in a string
hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """

# Inject CSS with Markdown
st.markdown(hide_table_row_index, unsafe_allow_html=True)

df = get_data()
banks = st.multiselect(
    "Choose Bank", list(df['BANK'].unique()[0:5])
)
if not banks:
    st.error("Please select at least one bank.")
else:
    data = df[df['BANK'].isin(banks)]
    # st.markdown(data.to_html(render_links=True),unsafe_allow_html=True)
