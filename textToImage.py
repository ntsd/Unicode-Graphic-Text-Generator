from PIL import ImageFont, Image, ImageDraw
import textwrap

def textToImageExample():#Only Ascii
    # Source text, and wrap it.
    userinput = "5555"
    text = textwrap.fill(userinput, 50)

    # Font size, color and type.
    fontcolor = (255, 255, 255)
    fontsize = 40
    font = ImageFont.load_default().font #ImageFont.truetype('myfont.ttf', 11))

    # Determine text size using a scratch image.
    img = Image.new("RGBA", (1,1))
    draw = ImageDraw.Draw(img)
    textsize = draw.textsize(text, font)

    # Now that we know how big it should be, create
    # the final image and put the text on it.
    background = (0, 0, 0)
    img = Image.new("RGBA", textsize, background)
    draw = ImageDraw.Draw(img)
    draw.text((0, 0), text, fontcolor, font)

    img.show()
    #img.save("seesharp.png")



if __name__ == '__main__':
    textToImageExample()
