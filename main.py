from tkinter.filedialog import askopenfilename

import numpy as np
import cv2

import time

import io

import CodeSet

import textToImage

import textImageMatching

import charSet

import math

def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print('%s function took %0.3f ms' % (f.__name__, (time2-time1)*1000.0))
        return ret
    return wrap

def cover_multiple(current_length, multiple):
    return ((current_length - 1) // multiple + 1) * multiple

@timing
def slicer(a, chunk_i, chunk_j, lineSize, twoD=False):
    """
    :return Array of Arrays Rows of Array cols of Arrays of shape data will be nan if division != 0  y * x
    
    """
    n = cover_multiple(a.shape[0], chunk_i)
    m = lineSize*chunk_j#cover_multiple(a.shape[1], chunk_j)
    print(n, m)
    c = np.empty((n, m))
    c.fill(255)#np.nan)
    c[:a.shape[0], :m] = a[:a.shape[0], :m]
    c = c.reshape(n // chunk_i, chunk_i, m // chunk_j, chunk_j)
    c = c.transpose(0, 2, 1, 3)
    if not twoD:
        c = c.reshape(-1, chunk_i, chunk_j)
    return c

@timing
def blockshaped(arr, nrows, ncols):
    """
    Return an array of shape (n, nrows, ncols) where
    n * nrows * ncols = arr.size

    If arr is a 2D array, the returned array should look like n subblocks with
    each subblock preserving the "physical" layout of arr.
    """
    h, w = arr.shape
    return (arr.reshape(h//nrows, nrows, -1, ncols)
            .swapaxes(1,2)
            .reshape(-1, nrows, ncols))

if __name__ == '__main__':
    filename = askopenfilename()
    image = cv2.imread(filename, 0)

    
    resize = 1
    lineSize = 48#defult = width//2 #39 for Facebook 70 for markdown 106 for steam
    
    if resize: # new method resize image more speed 
        height, width = image.shape
        scale = lineSize/width
        new_height = round(height*scale)
        new_width = lineSize
        print('new_width:{} new_height:{}'.format(new_width, new_height))
        thumbnail = cv2.resize(image, (new_width, new_height), interpolation = cv2.INTER_AREA)  #use for resize
        cv2.imshow("show gray scale", thumbnail)

        scaleWidth = 1 
        scaleHeight = 1 #1 for emoticon 2  for block font arial size hight is width*2 
        print("size = ", width, "x",  height, " scale width = ", scaleWidth, " scale Height = ", scaleHeight)

        splitImage = slicer(thumbnail, scaleHeight, scaleWidth, lineSize)

    if not resize:# old method no resize image
        cv2.imshow("show gray scale", image)
        height, width = image.shape
        scaleWidth = width//lineSize
        scaleHeight = scaleWidth*2 # 1 for emoticon  2 for font arial size hight is width*2 
        print("size = ", width, "x",  height, " scale width = ", scaleWidth, " scale Height = ", scaleHeight)

        #speed test
        splitImage = slicer(image, scaleHeight, scaleWidth, lineSize)


    print('splitImage.shape',splitImage.shape)
    #cv2.imshow("splitImage[0]", splitImage)
    # cv2.waitKey(0)

    charArray = [chr(i) for i in [0x2591, 0x2593]]#0x2591, 0x2588, 0x2592, 0x2593, 0x0020
    # charArray = [chr(i) for i in [0x2591, 0x2588, 0x2592, 0x2593, 0x0020]] # http://www.unicodemap.org/range/53/Block_Elements/ # 0x0020 is space

    # charArray = charSet.arail5x9

    codeset = CodeSet.CodeSet("block", charArray, 'fonts/arial-unicode-ms.ttf')#unifont.ttf')

    codeSetImageArrays = textToImage.codeSetToImageGenerate(codeset, scaleWidth, scaleHeight)

    print('codeSetImageArrays shape',len(codeSetImageArrays), len(codeSetImageArrays[0]), len(codeSetImageArrays[0][0]))

    out = textImageMatching.getClosetByDifferencePixel(codeSetImageArrays, charArray, splitImage, scaleHeight, scaleWidth, lineSize)

    print(len(out))

    with io.open("output.txt", 'w', encoding='utf-8') as file:
        # list of emoji unicode https://unicode.org/emoji/charts/full-emoji-list.html
        file.write(out.replace('▓','💗').replace('░','😸').replace(' ','░')) # for space not compress .replace('░','█') to reduce noise better
        #file.write(out) 

    print('Done put anykey to stop')
    cv2.waitKey(0)

    # print(len(l2[0]), len(l2[0][0]))
    # print(len(codeSetImageArrays[0]), len(codeSetImageArrays[0][0]))


