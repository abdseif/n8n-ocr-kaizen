from flask import Flask, request, jsonify
from pdf2image import convert_from_path
from PIL import Image
import pytesseract
import tempfile
import os

app = Flask(__name__)

def convert_pdf_to_images(pdf_path):
    # Generator that yields one image per page (JPEG to reduce memory)
    for page in convert_from_path(pdf_path, fmt='jpeg'):
        yield page

@app.route('/ocr', methods=['POST'])
def ocr():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']

    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        file.save(tmp.name)

    text_result = []

    try:
        if file.filename.endswith('.pdf'):
            for image in convert_pdf_to_images(tmp.name):
                text_result.append(pytesseract.image_to_string(image))
        else:
            image = Image.open(tmp.name)
            text_result.append(pytesseract.image_to_string(image))

        return jsonify({'text': '\n'.join(text_result)})

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        os.remove(tmp.name)
