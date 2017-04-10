
def getClosetByDifferenceROI(codeSetImageArrays, charSet, splitImage, scaleHeight, scaleWidth, lineSize):
    #get Min Difference Of Block
    out = ""
    for index, imageBlock in enumerate(splitImage):#780
        minDifference = 99999
        minCode = 0

        for i, codeBlock in enumerate(codeSetImageArrays):#30
            # difference = 0
            sumImageBlock = 0
            sumCodeBlock = 0
            for row in range(scaleHeight):
                for col in range(scaleWidth):
                    # difference += abs(imageBlock[row][col] - codeBlock[row][col])
                    sumImageBlock += imageBlock[row][col]
                    sumCodeBlock += codeBlock[row][col]
            difference = abs(sumImageBlock - sumCodeBlock)
            if difference < minDifference:
                minDifference = difference
                minCode = i

        if index % lineSize == 0:
            out += "\n"
        out += charSet[minCode]
    return out

def getClosetByDifferencePixel(codeSetImageArrays, charSet, splitImage, scaleHeight, scaleWidth, lineSize):
    #get Min Difference Of Block
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
    return out

def getClosetScaleByAvg(codeSetImageArrays, charSet, splitImage, scaleHeight, scaleWidth, lineSize):##Not Done
    scaleArray = []
    scaleArrayAvg = []
    for codeBlock in codeSetImageArrays:
        sumColor = 0
        for row in range(scaleHeight):
            for col in range(scaleWidth):
                sumColor += codeBlock[row][col]
        scaleArrayAvg.append(sumColor)

    out = ""