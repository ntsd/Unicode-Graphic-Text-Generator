
class CodeSet:

    def __init__(self, name, charSet, blockSizeRange, fontPATH='fonts/unifont.ttf'):
        """
        
        :param name : Name of Codeset
        :param charSet : List of Character Hex Code 
        :param fontPATH : PATH of font to use
        """
        self.name = name
        self.charSet = charSet
        self.fontPATH = fontPATH
        self.blockSizeRange = blockSizeRange

