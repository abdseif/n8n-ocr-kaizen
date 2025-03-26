from flask import Flask, request, jsonify
from pdf2image import convert_from_path
from PIL import Image
import pytesseract
import tempfile
import os

app = Flask(__name__)

def convert_pdf_to_images(pdf_path, output_folder):
    return convert_from_path(pdf_path, output_folder=output_folder)

def perform_ocr(image):
    return pytesseract.image_to_string(image)

@app.route('/ocr', methods=['POST'])
def ocr():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    with tempfile.TemporaryDirectory() as temp_dir:
        with tempfile.NamedTemporaryFile(delete=False, dir=temp_dir) as tmp:
            file.save(tmp.name)

            try:
                if file.filename.lower().endswith('.pdf'):
                    images = convert_pdf_to_images(tmp.name, temp_dir)
                else:
                    images = [Image.open(tmp.name)]

                text = ''
                for image in images:
                    text += perform_ocr(image) + '\n'

                return jsonify({'text': text.strip()})

            except Exception as e:
                return jsonify({'error': str(e)}), 500
