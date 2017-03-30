

def imageToText():   
    start = 0x2580#0x2500
    end = 0x259F#0x2570
    for i in range(start, end):
        print(chr(i), end="")

if __name__ == '__main__':
    imageToText()
