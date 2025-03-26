import os
import tempfile
from flask import Flask, request, jsonify
from pdf2image import convert_from_path
from ocr import extract_text_from_image

app = Flask(__name__)

def convert_pdf_to_images(pdf_path):
    return convert_from_path(pdf_path, dpi=300, fmt='jpeg')  # High resolution

@app.route('/ocr', methods=['POST'])
def ocr():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']

    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(file.filename)[1]) as tmp:
        file.save(tmp.name)

        text = ""
        try:
            if file.filename.lower().endswith('.pdf'):
                for image in convert_pdf_to_images(tmp.name):
                    text += extract_text_from_image(image) + "\n"
            else:
                from PIL import Image
                image = Image.open(tmp.name)
                text = extract_text_from_image(image)

        except Exception as e:
            return jsonify({'error': str(e)}), 500
        finally:
            os.remove(tmp.name)

        return jsonify({'text': text})
