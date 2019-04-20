#import imageSelector
import gui
import filters
import color_model
import cip
import time
import numpy as np
import cv2
    
"""
test = imageSelector.image_selector
test.selectImage()
a = imageSelector.image_selector

cv2.imshow('image',a.cv2Image)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

#gui.app.window
gui.app.window.protocol("WM_DELETE_WINDOW", gui.app.window.quit)
gui.app.window.mainloop()

