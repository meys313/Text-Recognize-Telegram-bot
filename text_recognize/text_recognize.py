from data.config import BASE_DIR, pytesseract_way
from aiogram.dispatcher import FSMContext

import pytesseract
try:
    from PIL import Image
except ImportError:
    import Image

def recognize(lang):

    print(lang)
    pytesseract.pytesseract.tesseract_cmd = pytesseract_way

    img = Image.open(f'{BASE_DIR}/image.jpg')
    text = pytesseract.image_to_string(img, lang=lang)

    return text






