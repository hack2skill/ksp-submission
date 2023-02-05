from find_face import findFaces
import cv2






webcam = cv2.VideoCapture("C:/Users/sanjai/KSP face recognition api/videos/cctv3.mp4")
while True:
    ret, frame = webcam.read()

    if not ret:
        print("CAM NOT OPEND")
        break
    print(frame)

    frame = findFaces(frame)

    cv2.imshow('camera', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
