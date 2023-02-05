https://stackoverflow.com/questions/43232813/convert-opencv-image-format-to-pil-image-format



Pillow and OpenCV use different formats of images. So you can't just read an image in Pillow and manipulate it into an OpenCV image. 
Pillow uses the RGB format as @ZdaR highlighted, and OpenCV uses the BGR format. So, you need a converter to convert from one format to another.

To convert from PIL image to OpenCV use:

import cv2
import numpy as np
from PIL import Image

pil_image=Image.open("demo2.jpg") # open image using PIL

# use numpy to convert the pil_image into a numpy array
numpy_image=numpy.array(pil_img)  

# convert to a openCV2 image, notice the COLOR_RGB2BGR which means that 
# the color is converted from RGB to BGR format
opencv_image=cv2.cvtColor(numpy_image, cv2.COLOR_RGB2BGR) 
To convert from OpenCV image to PIL image use:

import cv2
import numpy as np
from PIL import Image

opencv_image=cv2.imread("demo2.jpg") # open image using openCV2

# convert from openCV2 to PIL. Notice the COLOR_BGR2RGB which means that 
# the color is converted from BGR to RGB
color_coverted = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2RGB)
pil_image=Image.fromarray(color_coverted)