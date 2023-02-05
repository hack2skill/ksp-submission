#identify faces and authenticate
import face_recognition
#computer vision
import cv2
import numpy as np
# webcam #0 
video_capture = cv2.VideoCapture(0)
# Loading sample pictures and learning
elon_image = face_recognition.load_image_file("ImagesBasic/Elon Musk.webp")
elon_face_encoding = face_recognition.face_encodings(elon_image)[0]
biden_image = face_recognition.load_image_file("ImagesBasic/Joe Biden.jpg")
biden_face_encoding = face_recognition.face_encodings(biden_image)[0]

#list of known face encodings and their names
known_face_encodings = [
    elon_face_encoding,
    biden_face_encoding
]
known_face_names = [
    "Elon Musk",
    "Joe Biden"
]

face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    # grbbing individual frame from the video
    ret, frame = video_capture.read()

    # processing every other frame to save time
    if process_this_frame:
        # resize frame to 1/4 size for processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        # convert the image from BGR color to RGB color (opencv uses the former,face_rec uses the latter)
        rgb_small_frame = small_frame[:, :, ::-1]
        
        # find all the faces and encodings in the current vid frame
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # check if the face is a match for the known face
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame


    # displaying results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # resulting image
    cv2.imshow('Video', frame)

    # q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()