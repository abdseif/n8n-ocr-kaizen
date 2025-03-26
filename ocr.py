from PIL import Image, ImageEnhance, ImageOps
import pytesseract
import cv2
import numpy as np

def preprocess_image(image):
    # Convert to grayscale
    image = image.convert('L')

    # Increase contrast
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(2.0)

    # Binarize (thresholding)
    image = ImageOps.invert(image)
    threshold = 150
    image = image.point(lambda x: 0 if x < threshold else 255, '1')
    image = ImageOps.invert(image)

    # Convert to NumPy and denoise using OpenCV
    image_np = np.array(image)
    denoised = cv2.fastNlMeansDenoising(image_np, None, 30, 7, 21)
    return Image.fromarray(denoised)

def extract_text_from_image(image):
    processed_image = preprocess_image(image)
    custom_config = r'--oem 1 --psm 11'
    return pytesseract.image_to_string(processed_image, config=custom_config)
