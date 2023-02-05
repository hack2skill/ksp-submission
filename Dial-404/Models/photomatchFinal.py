import os
import cv2
import tkinter as tk
from tkinter import filedialog

def matcher(img1,img2):
    #img1 = cv2.imread('ArrestpersonsRename/scan0040#_1f2e6adc-f0f1-4780-a950-d2efb44622e3259.jpg')
    #cv2.imshow('Face1', img1)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    #img2 = cv2.imread('ArrestpersonsRename/scan0040#_1f2e6adc-f0f1-4780-a950-d2efb44622e3259.jpg')
    #cv2.imshow('Face2', img2)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

# Convert the images to grayscale
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# Create a SIFT object
    sift = cv2.SIFT_create()

# Detect the keypoints and descriptors in both images
    keypoints1, descriptors1 = sift.detectAndCompute(gray1, None)
    keypoints2, descriptors2 = sift.detectAndCompute(gray2, None)

# Create a brute-force matcher
    bf = cv2.BFMatcher()

# Match the descriptors using knn matching
    matches = bf.knnMatch(descriptors1, descriptors2, k=2)

# Filter the matches using the Lowe's ratio test
    good_matches = []
    for m, n in matches:
        if m.distance < 0.75 * n.distance:
            good_matches.append([m])

    # Draw the matches on the images
    result = cv2.drawMatchesKnn(img1, keypoints1, img2, keypoints2, good_matches, None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

    # Display the result
    #cv2.imshow('Matched Faces', result)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

    score = len(good_matches)/len(keypoints1)


    #print("SCORE: ",score)
    
    return result,score

def select_image():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path



def main():
    imgpath = select_image()
    image1 = cv2.imread(imgpath)
    cv2.imshow('Selected Image', image1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()    
    photoPath = "/home/krishnatejaswis/VSCode/ArrestpersonsRename"
    for filename in os.listdir(photoPath):
        if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
            #print(filename)
            image2 = cv2.imread(os.path.join(photoPath,filename))
            imgmatch,score = matcher(image1,image2)
            if score>0.9:
                # Display the result
                cv2.imshow('Matched Faces', imgmatch)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                score = round(score,4)
                print("Match percentage is: ",score*100)
                break
        
                
    #print(imgpath,filename)
main()

