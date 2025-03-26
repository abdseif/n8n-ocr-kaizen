import pytesseract
from PIL import Image

def extract_text_from_image(image: Image.Image) -> str:
    custom_config = r'--oem 3 --psm 6'
    return pytesseract.image_to_string(image, config=custom_config)
