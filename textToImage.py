from PIL import ImageFont, Image, ImageDraw
import textwrap

from CodeSet import CodeSet


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


def codeSetToImageGenerate(codeSet, size):
    fontSize = size
    codeImages = []
    font = ImageFont.truetype(codeSet.fontPATH, fontSize, encoding="unicode")
    fontColor = 0
    background = 255
    widthSize = size//2
    # maxH = 0
    # maxW = 0
    # minH = 99
    # minW = 99

    for i in codeSet.charSet:
        char = i
        img = Image.new('L', (1, 1))
        draw = ImageDraw.Draw(img)
        textSize = draw.textsize(char, font) #size w, h 10,5 in font unifont

        if abs(textSize[0]-widthSize) > 3 or abs(textSize[1]-size) > 3:#to filter if size less than normal
            continue


        img = Image.new('L', (widthSize, size), background)
        draw = ImageDraw.Draw(img)
        draw.text((0, 0), char, fontColor, font)

        # if textSize[0]>maxW: maxW = textSize[0]
        # if textSize[1]>maxH: maxH = textSize[1]
        # if textSize[0]<minW: minW = textSize[0]
        # if textSize[1]<minH: minH = textSize[1]

        imageArrays = list(img.getdata())


        #print(size//2, size)
        codeImages.append([imageArrays[widthSize*i:widthSize*i+widthSize] for i in range(size)])

        #print(textSize, widthSize, size)

        #img.save("codeset/" + codeSet.name + "/" + char + ".png")

    #print("textSize=", textSize, "fontSize=", fontSize)
    # print(maxW, maxH,  minW ,minH )
    return codeImages

if __name__ == '__main__':
    codeset = CodeSet("block", [chr(i) for i in range(0x2580, 0x259F)], 'fonts/unifont.ttf')
    codeSetToImageGenerate(codeset, 10)
