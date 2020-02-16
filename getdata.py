import os
import cv2 as cv
import numpy as np
import pickle as pc
def preprocessing(image):
    image= cv.resize(image,(200,200))
    image= cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    return image
data_dir= os.path.join(os.getcwd(),'clean_data')
img_dir= os.path.join(os.getcwd(),'Images')
data=[]
label=[]
for i in os.listdir(img_dir):
    image= cv.imread(os.path.join(img_dir,i))
    image= preprocessing(image)
    data.append(image)
    label.append(i.split('_')[0])
data= np.array(data)
label= np.array(label)   
with open(os.path.join(data_dir,'Images.p'),'wb') as f:
    pc.dump(data,f)
with open(os.path.join(data_dir,'Label.p'),'wb') as f:
    pc.dump(data,f)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    