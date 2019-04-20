from tkinter import Tk
from PIL import Image
from PIL import ImageTk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
import numpy as np
import gui
import cv2

def cv2ToPIL(cv2Image):#Converts a cv2 np.array into PIL format
    image = cv2.cvtColor(cv2Image, cv2.COLOR_BGR2RGB) #CV2 uses BGR format instead of RGB so you have to put them in the write order
    return Image.fromarray(image)


def PILToCv2(pilImage):#Converts a PIL into cv2 np array
    temp = np.array(pilImage)
    return cv2.cvtColor(temp, cv2.COLOR_RGB2BGR) 



class imageSelctor:
    def __init__(self):
        self.cv2Image = np.zeros((500,500,3),np.uint8)
        self.pilImage = cv2ToPIL(self.cv2Image)

    def selectImage(self):
        Tk().withdraw()
        filename = askopenfilename(filetypes=(("jpeg","*.jpg"),("bmp","*.bmp"),("png","*.png"))) #lets you open jpg, bmp, or png images
        self.cv2Image = cv2.imread(filename)
        self.pilImage = cv2ToPIL(self.cv2Image)
        gui.app.create_image_display()
        #gui.app.window.update_idletasks()
    
    def saveImage(self): 
        file = asksaveasfilename(defaultextension=".jpg", filetypes=(("jpeg","*.jpg"),("bmp","*.bmp"),("png","*.png"))) #lets you save images as jpg, bmp, or png
        if file:
            self.pilImage.save(file)
    
    def setImage(self, image):
        if type(image) is np.ndarray:   #checks to see if the image is an np array
            self.cv2Image = image
            self.pilImage = cv2ToPIL(image)
        else:
            self.pilImage = image
            self.cv2Image = PILToCv2(image)

    def prepForDisplay(self):
        yscale = 385
        xscale = 660
        y = self.cv2Image.shape[0]
        x = self.cv2Image.shape[1]
        scaler = 1 
        if (y/yscale) > (x/xscale):
            scaler = y/yscale
        else:
            scaler = x/xscale
        img = cv2.resize(self.cv2Image, (0,0), fx=1/scaler, fy=1/scaler)
        return ImageTk.PhotoImage(cv2ToPIL(img))

image_selector = imageSelctor()