from PIL import Image
import pytesseract

def run_ocr(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

if __name__ == "__main__":
    path = "sample.jpg"  # Replace with your image path
    print(run_ocr(path))
