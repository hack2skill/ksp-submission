from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from tensorflow.keras.models import Model
import numpy as np
from PIL import Image
import os

# All images given as a dataset
images = []
for file in os.listdir(os.path.abspath(".")+'/Altered/Altered-Easy/'):
    if not 'amlignore' in file:
        images.append(os.path.abspath(".")+'/Altered/Altered-Easy/'+file) 

for file in os.listdir(os.path.abspath(".")+'/Altered/Altered-Medium/'):
    if not 'amlignore' in file:
        images.append(os.path.abspath(".")+'/Altered/Altered-Medium/'+file) 

for file in os.listdir(os.path.abspath(".")+'/Altered/Altered-Hard/'):
    if not 'amlignore' in file:
        images.append(os.path.abspath(".")+'/Altered/Altered-Hard/'+file)         

for file in os.listdir(os.path.abspath(".")+'/Real/'):
    if not 'amlignore' in file:
        images.append(os.path.abspath(".")+'/Real/'+file)    


# This is for the generating the image names in order.
# Later scores will be calculate based on the same order and stored in finger_image_score.npy
for i in range(len(images)):
    result_file = open('finger_image_names.csv', 'a')
    result_file.write("{}{}".format(images[i], '\n'))


# model imagenet
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


all_features = np.zeros(shape=(len(images),4096))

for i in range(len(images)):
    print(images[i])
    feature = extract(img=Image.open(images[i]))
    all_features[i] = np.array(feature)

np.save(os.path.abspath(".")+'/finger_image_score.npy', all_features)

# Test image to check accuracy of a sample image
query = extract(img=Image.open("./Altered/Altered-Easy/100__M_Left_index_finger_CR.BMP")) # Extract its features
dists = np.linalg.norm(all_features - query, axis=1) # Calculate the similarity (distance) between images

ids = np.argsort(dists)[:5] # Extract 5 images that have lowest distance
# Match image
for id in ids:
    print(images[id].rsplit('/',1)[1], 100 - dists[id])
