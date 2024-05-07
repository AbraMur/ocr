import pytesseract
from PIL import Image

if __name__ == '__main__':
    image = Image.open("image_2.jpg")
    string = pytesseract.image_to_string(image, lang='eng+rus')
    print(string)
