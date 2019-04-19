from tkinter import Tk
from PIL import Image
from PIL import ImageTk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
import numpy as np
import cv2

def selectImage():
    Tk().withdraw()
    filename = askopenfilename(filetypes=(("jpeg","*.jpg"),("bmp","*.bmp"),("png","*.png"))) #lets you open jpg, bmp, or png images
    return(cv2.imread(filename))

def cv2ToPIL(cv2Image):#Converts a cv2 np.array into PIL format
    image = cv2.cvtColor(cv2Image, cv2.COLOR_BGR2RGB) #CV2 uses BGR format instead of RGB so you have to put them in the write order
    return(Image.fromarray(image))

def PILToCv2(pilImage):#Converts a PIL into cv2 np array
    image = np.array(pilImage)
    return cv2.cvtColor(image, cv2.COLOR_RGB2BGR) 
     

def saveImage(image):
    if type(image) is np.ndarray:   #checks to see if the image is an np array
        image = cv2ToPIL(image)
    file = asksaveasfilename(defaultextension=".jpg", filetypes=(("jpeg","*.jpg"),("bmp","*.bmp"),("png","*.png"))) #lets you save images as jpg, bmp, or png
    if file:
        image.save(file)
