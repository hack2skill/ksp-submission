import cv2
import face_recognition
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import time
import numpy as np
import os
import sys

faceProto="opencv_face_detector.pbtxt"
faceModel="opencv_face_detector_uint8.pb"
ageProto="age_deploy.prototxt"
ageModel="age_net.caffemodel"
genderProto="gender_deploy.prototxt"
genderModel="gender_net.caffemodel"

MODEL_MEAN_VALUES=(78.4263377603, 87.7689143744, 114.895847746)
ageList=['(0-2)', '(4-6)', '(8-12)', '(15-20)', '(25-32)', '(38-43)', '(48-53)', '(60-100)']
genderList=['Male','Female']

faceNet=cv2.dnn.readNet(faceModel,faceProto)
ageNet=cv2.dnn.readNet(ageModel,ageProto)
genderNet=cv2.dnn.readNet(genderModel,genderProto)

def highlightFace(net, frame, conf_threshold=0.7):
    frameOpencvDnn=frame.copy()
    frameHeight=frameOpencvDnn.shape[0]
    frameWidth=frameOpencvDnn.shape[1]
    blob=cv2.dnn.blobFromImage(frameOpencvDnn, 1.0, (300, 300), [104, 117, 123], True, False)

    net.setInput(blob)
    detections=net.forward()
    faceBoxes=[]
    for i in range(detections.shape[2]):
        confidence=detections[0,0,i,2]
        if confidence>conf_threshold:
            x1=int(detections[0,0,i,3]*frameWidth)
            y1=int(detections[0,0,i,4]*frameHeight)
            x2=int(detections[0,0,i,5]*frameWidth)
            y2=int(detections[0,0,i,6]*frameHeight)
            faceBoxes.append([x1,y1,x2,y2])
            cv2.rectangle(frameOpencvDnn, (x1,y1), (x2,y2), (0,255,0), int(round(frameHeight/150)), 8)
    return frameOpencvDnn,faceBoxes

if getattr(sys, 'frozen', False):
    # If the application is run as a bundle, the pyInstaller bootloader
    # extends the sys module by a flag frozen=True and sets the app
    # path into variable _MEIPASS'.
    application_path = sys._MEIPASS
else:
    application_path = os.path.dirname(os.path.abspath(__file__))

prototxt_path = os.path.join(application_path, "deploy.prototxt")
model_path = os.path.join(application_path, "res10_300x300_ssd_iter_140000_fp16.caffemodel")

# Load the model
net = cv2.dnn.readNetFromCaffe(prototxt_path, model_path)


width,height=(640,480)
padding=20
# modelFile = "res10_300x300_ssd_iter_140000_fp16.caffemodel"
# configFile = "deploy.prototxt"
# net = cv2.dnn.readNetFromCaffe(configFile, modelFile)

def face_detection_dnn(image,encodings):
    resultImg, faceBoxes = highlightFace(faceNet, image)
    if not faceBoxes:
        print("No face detected")

    for faceBox in faceBoxes:
        face = image[max(0, faceBox[1] - padding):
                     min(faceBox[3] + padding, image.shape[0] - 1), max(0, faceBox[0] - padding)
                                                                    :min(faceBox[2] + padding, image.shape[1] - 1)]

        blob = cv2.dnn.blobFromImage(face, 1.0, (227, 227), MODEL_MEAN_VALUES, swapRB=False)
        genderNet.setInput(blob)
        genderPreds = genderNet.forward()
        gender = genderList[genderPreds[0].argmax()]
        print(f'Gender: {gender}')

        ageNet.setInput(blob)
        agePreds = ageNet.forward()
        age = ageList[agePreds[0].argmax()]
        print(f'Age: {age[1:-1]} years')

        cv2.putText(image, f'{gender}, {age}', (faceBox[0], faceBox[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                    (0, 255, 255), 2, cv2.LINE_AA)
        # cv2.imshow("Detecting age and gender", resultImg)


    h, w = image.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 1.0,
                                 (300, 300), (104.0, 117.0, 123.0))
    net.setInput(blob)
    faces = net.forward()
    # print(faces)
    # to draw faces on image
    # print(faces.shape)
    face_names = []
    flag=False
    for i in range(faces.shape[2]):
        confidence = faces[0, 0, i, 2]
        if confidence > 0.5:
            box = faces[0, 0, i, 3:7] * np.array([w, h, w, h])
            (x, y, x1, y1) = box.astype("int")
            # print(x,y,x1,y1)
            face_locations=[(y,x1,y1,x)]
            face_encoding = face_recognition.face_encodings(image, face_locations)[0]
            # print(face_encodings)
            # face_recognition.encode
            matches=face_recognition.compare_faces(encodings,face_encoding)
            name = "Unknown"
            if True in matches:
                first_match_index = matches.index(True)
                # name = known_face_names[first_match_index]

                # Or instead, use the known face with the smallest distance to the new face
                face_distances = face_recognition.face_distance(encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                # if matches[best_match_index]:
                #     name = known_face_names[best_match_index]

                face_names.append(name)
                # cv2.rectangle(image, (x, y1 + 35), (x1, y1), (0, 0, 255), 0)
                font = cv2.FONT_HERSHEY_DUPLEX
                # cv2.putText(image, str(face_distances[best_match_index]), (x + 6, y - 6), font, 1.0, (255, 255, 255), 1)
                if face_distances[best_match_index]<5.25:
                    flag = True
                    cv2.putText(image, str(face_distances[best_match_index]), (x + 6, y - 6), font, 1.0,(255, 255, 255), 1)
                    cv2.rectangle(image, (x, y), (x1, y1), (0, 255, 0), 2)

            if not flag:
                cv2.rectangle(image, (x, y), (x1, y1), (255, 0, 0), 2)
    cv2.imshow('Video',image)





# Load the encodings from the image
def load_encodings_from_image(image_path):
    image = face_recognition.load_image_file(image_path)
    encoding = face_recognition.face_encodings(image)[0]
    print(encoding)
    print(type(encoding))
    return [encoding]

# # Recognize faces in a video
# def recognize_faces(video_path, encodings):
#     # Load the video
#     # video = cv2.VideoCapture(video_path)
#     video = cv2.VideoCapture(0)
#     # start_frame_number = 50
#     # video.set(cv2.CAP_PROP_POS_FRAMES, start_frame_number)
#
#     ctime, ptime = 0, 0
#     skip_frames = 10
#
#     while True:
#         # Read a frame from the video
#         ret, frame = video.read()
#         if not ret:
#             break
#
#         # Skip the frame if it's not the nth frame
#         if video.get(cv2.CAP_PROP_POS_FRAMES) % skip_frames != 0:
#             continue
#
#         original_frame = frame
#         # frame = cv2.resize(frame, (width, height))
#         ctime = time.time()
#         fps = 1 / (ctime - ptime)
#         ptime = ctime
#         fps = int(fps)
#         cv2.putText(frame, str(fps), (8, 80), cv2.FONT_HERSHEY_DUPLEX, 3, (0, 0, 255), 4)
#
#         # Convert the frame from BGR to RGB
#         # frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
#         rgb_frame = frame[:, :, ::-1]
#
#         # Find the face encodings in the frame
#         face_locations = face_recognition.face_locations(rgb_frame)
#         # print(len(face_locations))
#         face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
#
#         # Loop through each face in this frame of video
#         for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
#             # See if the face is a match for the known face(s)
#             cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
#             matches = face_recognition.compare_faces(encodings, face_encoding)
#             print(matches)
#             # If a match was found
#             if True in matches:
#                 # Draw a box around the face
#                 cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
#                 # font = cv2.FONT_HERSHEY_DUPLEX
#                 # cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
#
#         # Display the resulting image
#         cv2.imshow("Video", frame)
#         if cv2.waitKey(1) & 0xFF == ord("q"):
#             break
#
#     # Release the video
#     video.release()
#     cv2.destroyAllWindows()

# Upload a video file and an image file
def upload_video_and_image():
    video_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4")])
    if not video_path:
        return

    image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
    if not image_path:
        return

    encodings = load_encodings_from_image(image_path)
    # recognize_faces(video_path, encodings)

    url = "http://192.168.132.158:8080/video"
    # cap=cv2.VideoCapture(url)
    # cap=cv2.VideoCapture(video_path)
    cap = cv2.VideoCapture(0)
    ctime, ptime = 0, 0
    skip_frames = 20

    # Set the resolution
    width = 640
    height = 480
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    # Create a window with a fixed size
    cv2.namedWindow("Video", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Video", 640, 480)

    while True:
        ret, frame = cap.read()
        # frame=cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        if not ret:
            break

        # # Skip the frame if it's not the nth frame
        if cap.get(cv2.CAP_PROP_POS_FRAMES) % skip_frames != 0:
            continue

        ctime = time.time()
        fps = 1 / (ctime - ptime)
        ptime = ctime
        fps = int(fps)
        cv2.putText(frame, str(fps), (8, 80), cv2.FONT_HERSHEY_DUPLEX, 3, (0, 0, 255), 4)
        # frame=face_detection_mtcnn(frame)
        # frame=face_detection_hog(frame)
        # frame=face_detection_haarcascade(frame)
        # frame=face_detection_fr(frame)
        # face_locations = face_recognition.face_locations(frame)
        # print(face_locations)


        frame = face_detection_dnn(frame,encodings)

        # cv2.imshow('frame',frame)

        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q") or key == 27 or key == -1:
            break

    cap.release()
    cv2.destroyAllWindows()


# Create the GUI
root = tk.Tk()
root.title("Face Recognition")

upload_button = tk.Button(root, text="Upload Video and Image", command=upload_video_and_image)
upload_button.pack()

root.mainloop()
