import pytesseract
from PIL import Image


if __name__ == '__main__':
    image = Image.open("filename")
    string = pytesseract.image_to_string(image, lang='eng+rus', config='--psm 6 -c tessedit_char_whitelist=+0123456789')
    print(string)
