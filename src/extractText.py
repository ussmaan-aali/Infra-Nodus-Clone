import pytesseract
import io
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
tessdata_dir_config = '--tessdata-dir "C:\\Program Files\\Tesseract-OCR\\tessdata"'

def extractText(images:list):
    text = ""
    for idx, image in enumerate(images):
        try:
            img_text = pytesseract.image_to_string(Image.open(io.BytesIO(image)), config=tessdata_dir_config)
            text += img_text
        except Exception as e:
            text += ' '
            print(f"exception at page: {idx+1}")
    return text