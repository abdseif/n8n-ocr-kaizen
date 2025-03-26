import os
import tempfile
from flask import Flask, request, jsonify
from ocr import extract_text_from_image
from pdf2image import convert_from_path
from PIL import Image

app = Flask(__name__)

# Restrict to first few pages to avoid OOM crashes on Render
def convert_pdf_to_images(pdf_path, max_pages=3):
    return convert_from_path(
        pdf_path,
        dpi=200,
        fmt='jpeg',
        first_page=1,
        last_page=max_pages,
        grayscale=True,
        thread_count=2
    )

@app.route("/")
def home():
    return "✅ OCR API is Live"

@app.route("/ocr", methods=["POST"])
def ocr():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']

    # Save uploaded file to a temporary location
    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(file.filename)[1]) as tmp:
        file.save(tmp.name)
        temp_path = tmp.name

    try:
        text = ""
        if file.filename.lower().endswith('.pdf'):
            images = convert_pdf_to_images(temp_path)
            for image in images:
                text += extract_text_from_image(image) + "\n"
        else:
            image = Image.open(temp_path)
            text = extract_text_from_image(image)

        return jsonify({'text': text})

    except Exception as e:
        return jsonify({'error': f"OCR failed: {str(e)}"}), 500

    finally:
        # Always clean up temp file
        if os.path.exists(temp_path):
            os.remove(temp_path)
