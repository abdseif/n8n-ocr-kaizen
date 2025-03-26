from flask import Flask, request, jsonify
from pdf2image import convert_from_bytes
from PIL import Image
import pytesseract

app = Flask(__name__)

# Perform OCR on a single image
def perform_ocr(image):
    return pytesseract.image_to_string(image)

# OCR endpoint
@app.route('/ocr', methods=['POST'])
def ocr():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    try:
        if file.filename.lower().endswith('.pdf'):
            # Convert PDF bytes directly into image list
            images = convert_from_bytes(file.read())
        else:
            # Load standard image (jpg, png, etc.)
            image = Image.open(file.stream)
            images = [image]

        # Run OCR on all images
        text = ''
        for image in images:
            text += perform_ocr(image) + '\n'

        return jsonify({'text': text.strip()})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run()
