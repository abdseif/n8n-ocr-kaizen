import os
import tempfile
from flask import Flask, request, jsonify
from pdf2image import convert_from_path
from ocr import extract_text_from_image
from PIL import Image

app = Flask(__name__)

# Limit pages and resolution to avoid Render OOM crash
def convert_pdf_to_images(pdf_path, max_pages=3):
    return convert_from_path(pdf_path, dpi=200, fmt='jpeg', first_page=1, last_page=max_pages)

@app.route("/")
def home():
    return "OCR API is live!"

@app.route("/ocr", methods=["POST"])
def ocr():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']

    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(file.filename)[1]) as tmp:
        file.save(tmp.name)
        temp_path = tmp.name

    text = ""

    try:
        if file.filename.lower().endswith('.pdf'):
            # Process only first 3 pages for stability
            for image in convert_pdf_to_images(temp_path):
                text += extract_text_from_image(image) + "\n"
        else:
            image = Image.open(temp_path)
            text = extract_text_from_image(image)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    finally:
        os.remove(temp_path)

    return jsonify({'text': text})
