from tkinter.filedialog import askopenfilename

import cv2

if __name__ == '__main__':
    filename = askopenfilename()
    lineSize = 28
    img = cv2.imread(filename,0)
    #cv2.imshow('image',img)
