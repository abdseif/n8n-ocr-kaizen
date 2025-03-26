import pytesseract
from PIL import Image, ImageEnhance, ImageOps

def perform_ocr_on_images(images):
    text = ''
    for image in images:
        # Convert to grayscale
        image = image.convert('L')

        # Optional: Increase contrast
        enhancer = ImageEnhance.Contrast(image)
        image = enhancer.enhance(2.0)  # 2.0 = double contrast

        # Optional: Binarize image (convert to black and white)
        image = image.point(lambda x: 0 if x < 180 else 255, '1')

        # Apply OCR with custom config
        custom_config = r'--oem 1 --psm 6'
        text += pytesseract.image_to_string(image, config=custom_config)
    return text
