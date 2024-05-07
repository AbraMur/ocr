import pytesseract
import regex as re
from PIL import Image


if __name__ == '__main__':
    image = Image.open("")
    string = pytesseract.image_to_string(image, lang='eng+rus')
    result = re.findall(r'+7 /d/d/d /d/d/d-/d/d-/d/d', string)
    print(result)
