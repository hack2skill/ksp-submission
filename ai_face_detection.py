# Copyright © DarkSide Assasins. All rights reserved.

from deepface import DeepFace
from datetime import timedelta
import cv2
import numpy as np
import os
import pandas as pd

pd.set_option('display.max_columns', None)
csv_loc = 'Sample Missing Persons FIRS - Sheet1.csv'
df = pd.read_csv(csv_loc, sep=',', header=0)


def format_timedelta(td):
    """Utility function to format timedelta objects in a cool way (e.g 00:00:20.05)
    omitting microseconds and retaining milliseconds"""
    result = str(td)
    try:
        result, ms = result.split(".")
    except ValueError:
        return (result + ".00").replace(":", "-")
    ms = int(ms)
    ms = round(ms / 1e4)
    return f"{result}.{ms:02}".replace(":", "-")


def get_saving_frames_durations(cap, saving_fps):
    """A function that returns the list of durations where to save the frames"""
    s = []
    # get the clip duration by dividing number of frames by the number of frames per second
    clip_duration = cap.get(cv2.CAP_PROP_FRAME_COUNT) / cap.get(cv2.CAP_PROP_FPS)
    # use np.arange() to make floating-point steps
    for i in np.arange(0, clip_duration, 1 / saving_fps):
        s.append(i)
    return s


def video_to_frames(video_file):
    SAVING_FRAMES_PER_SECOND = 30
    filename, _ = os.path.splitext(video_file)
    filename += "-opencv"
    # make a folder by the name of the video file
    if not os.path.isdir(filename):
        os.mkdir(filename)
    # read the video file
    cap = cv2.VideoCapture(video_file)
    # get the FPS of the video
    fps = cap.get(cv2.CAP_PROP_FPS)
    # if the SAVING_FRAMES_PER_SECOND is above video FPS, then set it to FPS (as maximum)
    saving_frames_per_second = min(fps, SAVING_FRAMES_PER_SECOND)
    # get the list of duration spots to save
    saving_frames_durations = get_saving_frames_durations(cap, saving_frames_per_second)
    # start the loop
    count = 0
    while True:
        is_read, frame = cap.read()
        if not is_read:
            # break out of the loop if there are no frames to read
            break
        # get the duration by dividing the frame count by the FPS
        frame_duration = count / fps
        try:
            # get the earliest duration to save
            closest_duration = saving_frames_durations[0]
        except IndexError:
            # the list is empty, all duration frames were saved
            break
        if frame_duration >= closest_duration:
            # if closest duration is less than or equals the frame duration,
            # then save the frame
            frame_duration_formatted = format_timedelta(timedelta(seconds=frame_duration))
            cv2.imwrite(os.path.join(filename, f"frame{frame_duration_formatted}.jpg"), frame)
            # drop the duration spot from the list, since this duration spot is already saved
            try:
                saving_frames_durations.pop(0)
            except IndexError:
                pass
        # increment the frame count
        count += 1


def image_to_image_compare(img1_path, img2_path):
    result = DeepFace.verify(img1_path=img1_path, img2_path=img2_path, model_name='Facenet512', enforce_detection=False)
    if result.get("verified"):
        filename, _ = os.path.splitext(img1_path)
        filename += ".jpg"
        data = df[df['Photo_Full_front'] == filename]
        return {"Report": str(result), "Information": str(data)}
    return {"Report": str(result)}


def image_analyze(img_path):
    result = DeepFace.analyze(img_path=img_path)
    return {"Report": str(result)}


def find_image_in_db(img_path, db_path):
    result = DeepFace.find(img_path=img_path, db_path=db_path, enforce_detection=False)
    return {"Report": str(result)}


def find_image_in_video(img_path, video_path, db_path):
    video_to_frames(video_path)
    result = DeepFace.find(img_path=img_path, db_path=db_path, model_name='Facenet512', enforce_detection=False)
    return {"Report": str(result)}


def get_embeddings(img_path):
    embeddings = DeepFace.extract_faces(img_path=img_path)
    return {"Report": str(embeddings)}


if __name__ == '__main__':
    print(image_to_image_compare(
        img1_path="missing_FIR_images/02#_d6d26ac4-a989-494e-be57-674cda959d8079.jpg",
        img2_path="missing_FIR_images/6-000#_d11e623e-b8d2-4c24-886f-6b33c3c36d95424.jpg"))

    print(image_to_image_compare(
        img1_path="missing_FIR_images/01#_95a58ed8-63a3-4b38-b744-a3b0725ccce51535.jpg",
        img2_path="missing_FIR_images/01#_95a58ed8-63a3-4b38-b744-a3b0725ccce51535.jpg"))

    print(get_embeddings(img_path="images/20230205_004933.jpg"))

    print(image_to_image_compare(
        img1_path="images/20230205_004933.jpg",
        img2_path="images/20230205_004908.jpg" ))

    print(image_to_image_compare(
        img1_path="images/20230205_005906.jpg",
        img2_path="images/20230205_005906.jpg"))

    print(image_analyze(
        img_path="missing_FIR_images/02#_d6d26ac4-a989-494e-be57-674cda959d8079.jpg"))

    print(find_image_in_db(
        img_path='missing_FIR_images/01#_95a58ed8-63a3-4b38-b744-a3b0725ccce51535.jpg',
        db_path='missing_FIR_images'))

    print(find_image_in_video(
        img_path='images/Aamir_Khan_From_The_NDTV_Greenathon_at_Yash_Raj_Studios_(11).jpg',
        video_path='videos/video1.mp4',
        db_path='videos/video1-opencv'))
