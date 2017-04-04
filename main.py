from tkinter.filedialog import askopenfilename

import numpy as np
import cv2

import time

import io

from CodeSet import CodeSet

import textToImage

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
def slicer(a, chunk_i, chunk_j, twoD=False):
    """
    :return Array of Arrays Rows of Array cols of Arrays of shape data will be nan if division != 0  y * x
    
    """
    n = cover_multiple(a.shape[0], chunk_i)
    m = cover_multiple(a.shape[1], chunk_j)
    c = np.empty((n, m))
    c.fill(255)#np.nan)
    c[:a.shape[0], :a.shape[1]] = a
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
    cv2.imshow("show gray scale", image)
    height, width = image.shape
    lineSize = width//3 #28 for Facebook
    scaleWidth = width//lineSize
    scaleHeight = scaleWidth*2
    print("size = ", width, "x",  height, " scale width = ", scaleWidth, " scale Height = ", scaleHeight)

    #speed test
    splitImage = slicer(image, scaleHeight, scaleWidth)


    # cv2.imshow("splitImage[0]", splitImage[1])
    # cv2.waitKey(0)

    charSet = [chr(i) for i in [0x2591, 0x2588, 0x2592, 0x2593]]#range(0x2591, 0x2593)]
    codeset = CodeSet("block", charSet, 'fonts/unifont.ttf')

    codeSetImageArrays = textToImage.codeSetToImageGenerate(codeset, scaleWidth, scaleHeight)

    print(len(splitImage), len(splitImage[0]), len(splitImage[0][0]))
    print(len(codeSetImageArrays), len(codeSetImageArrays[0]), len(codeSetImageArrays[0][0]))

    out = ""
    for index, imageBlock in enumerate(splitImage):#780
        minDifference = 99999
        minCode = 0

        for i, codeBlock in enumerate(codeSetImageArrays):#30
            difference = 0
            for row in range(scaleHeight):
                for col in range(scaleWidth):
                    difference += abs(imageBlock[row][col] - codeBlock[row][col])

            if difference < minDifference:
                minDifference = difference
                minCode = i

        if index % lineSize == 0:
            out += "\n"
        out += charSet[minCode]

    with io.open("output.txt", 'w', encoding='utf-8') as file:
        file.write(out)

    cv2.waitKey(0)
    # print(len(l2[0]), len(l2[0][0]))
    # print(len(codeSetImageArrays[0]), len(codeSetImageArrays[0][0]))


