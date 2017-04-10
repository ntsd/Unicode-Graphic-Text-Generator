from PIL import ImageFont, Image, ImageDraw
import textwrap

from CodeSet import CodeSet

from collections import Counter


def textToImageExample():  # Only Ascii
    # Source text, and wrap it.
    userinput = "0"
    text = textwrap.fill(userinput, 50)

    # Font size, color and type.
    fontcolor = (0, 0, 0)
    fontsize = 40
    # font = ImageFont.load_default().font
    font = ImageFont.truetype('fonts/arial-unicode-ms.ttf', 11, encoding="unicode")

    # Determine text size using a scratch image.
    img = Image.new("RGBA", (1, 1))
    draw = ImageDraw.Draw(img)
    textsize = draw.textsize(text, font)

    # Now that we know how big it should be, create
    # the final image and put the text on it.
    background = (255, 255, 255)
    img = Image.new("RGBA", textsize, background)
    draw = ImageDraw.Draw(img)
    draw.text((0, 0), userinput, fontcolor, font)

    img.show()
    # img.save("seesharp.png")


def codeSetToImageGenerate(codeSet, widthSize, heightSize):
    fontSize = widthSize
    codeImages = []
    font = ImageFont.truetype(codeSet.fontPATH, fontSize, encoding="unicode")
    fontColor = 0
    background = 255
    # maxH = 0
    # maxW = 0
    # minH = 99
    # minW = 99

    for i in codeSet.charSet:
        char = i
        img = Image.new('L', (1, 1))
        draw = ImageDraw.Draw(img)
        textSize = draw.textsize(char, font) #size w, h 10,5 in font unifont

        # if abs(textSize[0]-widthSize) > 3 or abs(textSize[1]-size) > 3:#to filter if size less than normal
        #     continue


        img = Image.new('L', (widthSize, heightSize), background)
        draw = ImageDraw.Draw(img)
        draw.text((0, 0), char, fontColor, font)

        # if textSize[0]>maxW: maxW = textSize[0]
        # if textSize[1]>maxH: maxH = textSize[1]
        # if textSize[0]<minW: minW = textSize[0]
        # if textSize[1]<minH: minH = textSize[1]

        imageArrays = list(img.getdata())


        #print(size//2, size)
        codeImages.append([imageArrays[widthSize*i:widthSize*i+widthSize] for i in range(heightSize)])

        #print(textSize, widthSize, size)

        #img.save("codeset/" + codeSet.name + "/" + char + ".png")

    #print("textSize=", textSize, "fontSize=", fontSize)
    # print(maxW, maxH,  minW ,minH )
    return codeImages

def getMostFontSize(charCodeSet, codeSet, fontSize):
    font = ImageFont.truetype(codeSet.fontPATH, fontSize, encoding="unicode")
    img = Image.new("RGBA", (1, 1))
    draw = ImageDraw.Draw(img)
    textSizeDict = {}
    for c in charCodeSet:
        textsize = draw.textsize(c*10, font)
        try:
            textSizeDict[textsize][0] += 1
            textSizeDict[textsize][1].append(c)
        except:
            textSizeDict[textsize] = [1, [c]]

    for i in textSizeDict:
        print(i, textSizeDict[i])

if __name__ == '__main__':

    charCodeSet = [chr(i)for i in [0x2591, 0x2588, 0x2592, 0x2593, 0x0020]]
    charCodeSet = [chr(i) for i in range(10000)]#[0x2591, 0x2588, 0x2592, 0x2593, 0x0020]]
    codeset = CodeSet("block", charCodeSet, 'fonts/arial.ttf')
    getMostFontSize(charCodeSet, codeset, 10)

