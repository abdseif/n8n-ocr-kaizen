from PIL import Image, ImageEnhance
import pytesseract
import cv2
import numpy as np

def preprocess_image(image):
    # Convert to grayscale
    image = image.convert('L')

    # Increase contrast
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(2.0)

    # Convert to NumPy array
    image_np = np.array(image)

    # Binarize (thresholding)
    _, binary = cv2.threshold(image_np, 127, 255, cv2.THRESH_BINARY)

    # Ensure proper dtype
    binary = binary.astype(np.uint8)

    # Denoise image
    denoised = cv2.fastNlMeansDenoising(binary, None, 30, 7, 21)

    return Image.fromarray(denoised)

def extract_text_from_image(image):
    try:
        processed_image = preprocess_image(image)
        custom_config = r'--oem 1 --psm 11'
        return pytesseract.image_to_string(processed_image, config=custom_config)
    except Exception as e:
        return f"[OCR Error] {str(e)}"
