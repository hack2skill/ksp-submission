import cv2
import matplotlib.pyplot as plt
from deepface import DeepFace
import numpy as np
import os
from moviepy.editor import VideoFileClip
import pandas as pd
from keras.preprocessing.image import ImageDataGenerator
from keras.utils import load_img,img_to_array

path = r"Backend\\uploads"
path1= r"Backend\\thief"
storepath=r"Frontend\\src\\Components\\Images"
storepath1=r"Frontend\\src\\Components\\imagesThief"
dbpath=r"Backend\\intermediate"
dbpath1=r"Backend\\thief_data"
aug_in=r"Backend\\augmentation"
aug_out=r"Frontend\\src\\Components\\augmented"

def prediction_and_write(imgpath1):
    fps=imagegenerator()
    imgpath= r"Backend\\uploads\\" + imgpath1[0]
    dbpath2=dbpath
    storepath=r"Frontend\\src\\Components\\Images"
    remove(storepath)
    
    recognition = DeepFace.find(
        img_path=imgpath, db_path=r"Backend\\intermediate", enforce_detection=False)
    print(recognition)
    n = 1
    arr=[]
    for i in recognition[0].identity:
        print(i)
        pred_img = cv2.imread(i)
        x=i.replace(dbpath,'')
        x=x.replace(r".jpg",'')
        x=x.replace(r'/','')
        x=x.replace(r'\\','')
        
        num=0 #this will store the frame number , after extracting from name of file
        
        file_name_len=len(x)
        j=file_name_len-1
        
        while j>=0:
            if x[j]>='0' and x[j]<='9':
                num=(num*10)+int(x[j])
            j-=1
        
        #reversing the number
        
        x=int(str(num)[::-1])
        
        x=int(x/fps)
        
        arr.append(x)
        grayf = cv2.cvtColor(pred_img, cv2.COLOR_BGR2RGB)
        resizedf = cv2.resize(grayf, (100, 100))
        normalized = resizedf/255
        reshapedf = np.reshape(normalized, (100, 100, 3))
        img=imgpath1[0].replace(".jpg",'')
        name = storepath+"\\"+ img +"_"+str(x)+".jpg"
        plt.imsave(name, reshapedf)
    os.remove(imgpath)
    os.chdir(r"Frontend\\src\\Components\\Images")
    lst=os.listdir()
    i=0
    while i<len(lst)-5:
        os.remove(lst[i])
        i=i+1
    os.chdir(r"..\\..\\..\\..")
    remove(dbpath2)

def infinite_run():
    while (1):
        path = r"Backend\\uploads"
        if (len(os.listdir(path)) == 0 and len(os.listdir(path1))==0 and len(os.listdir(aug_in))==0):
            count=1
        elif (len(os.listdir(path)) != 0):
            r=os.listdir(path)
            remove(storepath)
            prediction_and_write(r)
        elif(len(os.listdir(path1))!=0):
            r=os.listdir(path1)
            remove(storepath1)
            prediction_and_write_thief(r)
        elif(len(os.listdir(aug_in))!=0):
            r=os.listdir(aug_in)
            remove(aug_out)
            # print(r)
            augmentation(r)
            
def remove(path):
    matter=os.listdir(path)
    for i in matter:
        if(i=="representations_vgg_face.pkl"):
            continue
        i=path+"\\"+i
        os.remove(i)


def imagegenerator():
    cam=VideoFileClip(r"Backend\\Video\\WhatsApp Video 2023-02-04 at 6.23.15 PM.mp4")
    dur=int(cam.duration)
    cam = cv2.VideoCapture(r"Backend\\Video\\WhatsApp Video 2023-02-04 at 6.23.15 PM.mp4")
    currentframe = 1
    while (True):
        ret, frame = cam.read()
        if ret:
            name = r"Backend\\intermediate\\" + str(currentframe) + '.jpg'
            plt.imsave(name, frame)
            currentframe += 1
        else:
            break
    cam.release()
    fps=int(currentframe/dur)
    cv2.destroyAllWindows()
    # print(dur)
    # print(currentframe)
    # print(fps)
    return fps

def textfilegen(recognition):
    df=pd.DataFrame(recognition[0])
    no=df.shape[0]
    text_file = open(r"Backend\\test.txt", "w")
    lis=[]
    for k in range(no):
        y=df['identity'][k]
        new_str = ""
        i=1
        
        for c in reversed(y):
            if c == '/':
                break
                i=i+1
            elif i>4:
                new_str= new_str+c
                i=i+1
            else:
                i=i+1
        txt = new_str[::-1]
        lis.append(txt)
        
    print(lis)
    lis1=[]
    for j in lis:
        res = ''.join([i for i in j if not i.isdigit()])
        lis1.append(res)

    indexes = np.unique(lis1, return_index=True)[1]
    lis1=[lis1[index] for index in sorted(indexes)]

    file1 = open(r"Backend\\test.txt","w")
    for i in lis1:
        file1.write(i +"\n")
        
        
        
    file1.close()

def prediction_and_write_thief(imagepath1):
    imgpath=path1 + "\\" + imagepath1[0]
    print(imgpath)
    dbpath=dbpath1
    print(dbpath)
    strpath=storepath1
    recognition = DeepFace.find(
        img_path= imgpath, db_path=dbpath, enforce_detection=False)
    print(recognition)
    n = 1
    for i in recognition[0].identity:
        pred_img = cv2.imread(i)
        grayf = cv2.cvtColor(pred_img, cv2.COLOR_BGR2RGB)
        resizedf = cv2.resize(grayf, (100, 100))
        normalized = resizedf/255
        reshapedf = np.reshape(normalized, (100, 100, 3))
        name = strpath+"\\" + str(n)+ ".jpg"
        n=n+1
        plt.imsave(name, reshapedf)
    os.remove(imgpath)
    textfilegen(recognition)
    
    
def augmentation(imgp):
    datagen=ImageDataGenerator(rotation_range=30,width_shift_range=0.2,height_shift_range=0.2,rescale=1./255,shear_range=0.2,zoom_range=0.2,horizontal_flip=True,fill_mode='nearest')
    img_path=aug_in + "\\" + imgp[0]
    # i=os.listdir(img_path)
    pic=load_img(img_path)
    data_path=aug_out
    pic.getpixel
    pic_array=img_to_array(pic)
    pic_array=cv2.resize(pic_array,(200,200))
    print(pic_array.shape)
    pic_array= pic_array.reshape(1,*pic_array.shape)
    count=0
    for batch in datagen.flow(pic_array,batch_size=5,save_to_dir=data_path,save_prefix='shas'): 
        count+=1
        if(count==10):
            break
    os.remove(img_path)


infinite_run()


