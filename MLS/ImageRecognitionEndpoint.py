from flask import Flask, request
from flask_cors import CORS, cross_origin
from PIL import Image
from io import BytesIO
import uuid
app = Flask(__name__)

from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from tensorflow.keras.models import Model
import numpy as np
from PIL import Image
import os
import json

images = tuple(open('faces_image_names.csv', 'r'))
fimages = tuple(open('finger_image_names.csv', 'r'))


base_model = VGG16(weights='imagenet')
model = Model(inputs=base_model.input, outputs=base_model.get_layer('fc1').output)

def extract(img):
   img = img.resize((224, 224)) # Resize the image
   img = img.convert('RGB') # Convert the image color space
   x = image.img_to_array(img) # Reformat the image
   x = np.expand_dims(x, axis=0)
   x = preprocess_input(x)
   feature = model.predict(x)[0] # Extract Features
   return feature / np.linalg.norm(feature)


def getNearestMatchingImageNames(input_path, type):
   result = []
   if type is 'finger':
      all_features = np.load(os.path.abspath(".")+'/finder_image_score.npy')
      query = extract(img=Image.open(input_path)) # Extract its features
      dists = np.linalg.norm(all_features - query, axis=1) # Calculate the similarity (distance) between images 
      ids = np.argsort(dists)[:5]
      for id in ids:
         if 100 - dists[id] > 99.9 :
            matched_finder = {}
            matched_finder['image_name'] = fimages[id].rsplit('/',1)[1]
            matched_finder['match_score'] = 100 - dists[id]
            result.append(matched_finder)
            return result
   else :
      all_features = np.load(os.path.abspath(".")+'/faces_image_score.npy')
      query = extract(img=Image.open(input_path)) # Extract its features
      dists = np.linalg.norm(all_features - query, axis=1) # Calculate the similarity (distance) between images 
      ids = np.argsort(dists)[:3]
      for id in ids:
         matched_finder = {}
         matched_finder['image_name'] = images[id].rsplit('/',1)[1]
         matched_finder['match_score'] = 100 - dists[id]
         result.append(matched_finder)
      return result



@app.route("/process_fingerprint", methods=["POST"])
@cross_origin()
def process_image2():
    # Get the binary data from the request body    
    image_data = request.files['file'] 
    # Open the binary data as an image    
    # image = Image.open(BytesIO(image_data))
    # Save the image to a file on local 
    filename = 'tmp_' + str(uuid.uuid4())
    image_data.save(filename)
    result = getNearestMatchingImageNames(filename, 'finger')
    
    return json.dumps(result)

@app.route("/process_faceimage", methods=["POST"])
@cross_origin()
def process_image():
    # Get the binary data from the request body    
    image_data = request.files['file'] 
    # Open the binary data as an image    
    # image = Image.open(BytesIO(image_data))
    # Save the image to a file on local 
    filename = 'tmp_' + str(uuid.uuid4())
    image_data.save(filename)
    result = getNearestMatchingImageNames(filename, 'face')
    
    return json.dumps(result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    cors = CORS(app)