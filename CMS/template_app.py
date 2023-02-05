#Import Libraries
import streamlit as st
import streamlit.components.v1 as stc
import librosa
import numpy as np
import pandas as pd
import os
import time
import plotly.express as px
import requests
import json
from PIL import Image


def init():
    """Initialize the variable
    """
    global use_ploty, backend, print_time, recog_text, speech2text
    use_ploty = True 
    print_time = False
    speech2text = False
    backend = "http://localhost:8000"

    st.set_page_config(layout="wide")
    
    
def load_image(img_path:str):
    """load the image using PIL
    Args:
        img_path: Image path
    Returns:
        image: PIL Image object
    """
    image = Image.open(img_path)
    return image

class NumpyEncoder(json.JSONEncoder):
    """Encodes the numpy array into list
    """
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)

def create_request(uploaded_file,col1):
    """post request to predictions
    """
 
    url = f"{backend}/get_predictions"

    if not os.path.exists("tmp"):
        os.makedirs("tmp")

    if uploaded_file.name.split(".")[-1]!="wav":
        with open(os.path.join("tmp","file.wav"), "wb") as f:
            f.write(uploaded_file.getvalue())
            f.close()
        #load the audio file
        y, sr = librosa.load(os.path.join("tmp","file.wav"))
        print(y.shape,sr,uploaded_file.name)
         #payload
        files = {"name":uploaded_file.name.split(".")[0]+".wav","y":y,"sr":sr}
        # delete the intermedite file
        os.remove(os.path.join("tmp","file.wav"))
    else:
        #load the audio file
        y, sr = librosa.load(uploaded_file)
        print(y.shape,sr,uploaded_file.name)
        #payload
        files = {"name":uploaded_file.name,"y":y,"sr":sr}

    #post request
    response = requests.post(url, data=json.dumps(files,cls=NumpyEncoder))

    if speech2text:
        url1 = f"{backend}/speech_to_text"
        #post request
        response_text = requests.post(url1, data=json.dumps(files,cls=NumpyEncoder))
        print(response_text.json())

        if response_text.json()['text']!=' ':
            recog_text = response_text.json()['text']
            col1.markdown('<center><h3 style="color: black;">Recognized Text:'+recog_text+'</h3></center>',
                                    unsafe_allow_html=True)

    return response.json()
    


def main():
    """Main start of program
    """
    
    output_dic = {}
    #Header Image
    header = load_image(os.path.join("assets","header.png"))
    st.image(header,use_column_width=True)
    
    #Project Title
    st.markdown('<center><h1 style="color: black;">Audio Emotion Detection</h1></center>',
                            unsafe_allow_html=True)

    #layout
    au = st.empty()
    audio_container = au.container()
    start,col1, mid, col2 = au.columns([0.1,0.4,0.1,0.4])


    with col1:
        col1.markdown('<center><h3 style="color: black;">Input Audio</h3></center>',
                                unsafe_allow_html=True)

        uploaded_file = col1.file_uploader("Choose an Audio", type=["wav","mp3"])

        if uploaded_file is not None:
            col1.markdown('<center><h3 style="color: black;">Uploaded Audio</h3></center>',
                                unsafe_allow_html=True)
            col1.audio(uploaded_file)

                

    with col2:
        col2.markdown('<center><h3 style="color: black;">Prediction</h3></center>',
                                        unsafe_allow_html=True)
        if uploaded_file is not None:
            gif_path = os.path.join("assets","load.gif")
            gif_runner = col2.image(gif_path,use_column_width=True,width=10)
            
            output_dic = create_request(uploaded_file,col1)
            
            gif_runner.empty()
            if output_dic['status']==200:
                if use_ploty:
                    df = pd.DataFrame.from_dict(output_dic['probabilities'],orient='index').reset_index().rename(columns={'index':'Labels',0:'Probability'})
                    df = df.sort_values(by=["Probability"], ascending=False)
                    df['Probability'] = df['Probability'].apply(lambda x: x*100)
                    colors = ['lightsalmon'] * 7
                    colors[0] = 'lightgreen'
                    fig = px.bar(df,x="Labels",y="Probability",orientation='v')
                    fig.update_traces(marker_color=colors)
                    col2.plotly_chart(fig, use_container_width=True)
                else:
                    df = pd.DataFrame.from_dict(output_dic['probabilities'],orient='index').rename(columns={'index':'Labels',0:'Probability'})
                    col2.bar_chart(df,use_container_width=True)
                col2.markdown('<center><h3 style="color: black;">Predicted Emotion: '+output_dic["Emotion"]+'</h3></center>',
                                unsafe_allow_html=True)

                col2.markdown('<center><h3 style="color: green;">Confidence Score: '+str(output_dic["Confidence"])+'%</h3></center>',
                                unsafe_allow_html=True)
                if print_time:
                    col2.markdown('<center><h3 style="color: green;">Execution Time: '+str(output_dic['execution_time'])+'sec</h3></center>',
                                unsafe_allow_html=True)
                    
            else:
                col2.markdown('<center><h3 style="color: red;">Error! Try other Audio</h3></center>',
                                unsafe_allow_html=True)
        

if __name__=='__main__':
    init()
    main()