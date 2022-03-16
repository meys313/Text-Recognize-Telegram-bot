from data.config import BASE_DIR, pytesseract_way

import pytesseract
try:
    from PIL import Image
except ImportError:
    import Image

def recognize():
    pytesseract.pytesseract.tesseract_cmd = pytesseract_way

    img = Image.open(f'{BASE_DIR}/image.jpg')
    text = pytesseract.image_to_string(img, lang='rus')

    return text





