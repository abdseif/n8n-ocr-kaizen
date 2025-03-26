from PIL import Image
import pytesseract

# Specify the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def perform_ocr(image_path):
    try:
        # Open the image file
        image = Image.open(image_path)
        # Perform OCR on the image
        text = pytesseract.image_to_string(image)
        return text
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    # Example usage
    image_path = "test.png"
    extracted_text = perform_ocr(image_path)
    print("Extracted Text:")
    print(extracted_text)
