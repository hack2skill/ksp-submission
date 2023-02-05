import cv2
import numpy as np

# Load the pre-trained deep learning model for face detection
face_detector = cv2.dnn.readNetFromCaffe('face_detector.prototxt', 'face_detector.caffemodel')

# Load the pre-trained deep learning models for age, gender and hair color classification
age_detector = cv2.dnn.readNetFromCaffe('age_classifier.prototxt', 'age_classifier.caffemodel')
gender_detector = cv2.dnn.readNetFromCaffe('gender_classifier.prototxt', 'gender_classifier.caffemodel')
hair_detector = cv2.dnn.readNetFromCaffe('hair_color_classifier.prototxt', 'hair_color_classifier.caffemodel')

# Load the input image
img = cv2.imread('input.jpg')

# Convert the image to a 4D blob
blob = cv2.dnn.blobFromImage(img, scalefactor=1.0, size=(300, 300), mean=(104, 177, 123))

# Pass the blob through the face detector
face_detector.setInput(blob)
faces = face_detector.forward()

# Loop through the faces
for i in range(faces.shape[2]):
    confidence = faces[0, 0, i, 2]

    # Filter out weak detections
    if confidence > 0.5:
        # Get the face bounding box
        x, y, w, h = int(faces[0, 0, i, 3]), int(faces[0, 0, i, 4]), int(faces[0, 0, i, 5]), int(faces[0, 0, i, 6])

        # Extract the face ROI
        face_roi = img[y:y+h, x:x+w]

        # Resize the face ROI to (224, 224)
        face_roi = cv2.resize(face_roi, (224, 224))

        # Convert the face ROI to a 4D blob
        blob = cv2.dnn.blobFromImage(face_roi, scalefactor=1.0, size=(224, 224), mean=(104, 117, 123))

        # Pass the blob through the age detector
        age_detector.setInput(blob)
        age_preds = age_detector.forward()

        # Get the age prediction from the output
        age = age_preds[0].argmax()

        # Pass the blob through the gender detector
        gender_detector.setInput(blob)
        gender_preds = gender_detector.forward()

        # Get the gender prediction from the output
        gender = "Male" if gender_preds[0][0] < 0.5 else "Female"

        # Pass the blob through the hair color detector
        hair_detector.setInput(blob)
        hair_preds = hair_detector.forward()

        # Get the hair
