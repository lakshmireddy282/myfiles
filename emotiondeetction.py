import cv2  #pip install 
from deepface import DeepFace #pip install deepface

im=cv2.imread('happy.jpg') #input the image 
predictions=DeepFace.analyze(img) #using deepface library analyze the image
print("The emotion in the image is :"+ predictions['dominant_emotion']) #out the emotion detected in the image using the deepface library.

