from flask import Flask, request, jsonify
import pytesseract
from pdf2image import convert_from_path
from werkzeug.utils import secure_filename
import os
import tempfile

app = Flask(__name__)

@app.route("/ocr", methods=["POST"])
def ocr():
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files['file']
    filename = secure_filename(file.filename)

    with tempfile.TemporaryDirectory() as temp_dir:
        pdf_path = os.path.join(temp_dir, filename)
        file.save(pdf_path)

        # Store all extracted text
        full_text = []

        # Convert PDF one page at a time
        for i, image in enumerate(convert_from_path(pdf_path)):
            text = pytesseract.image_to_string(image)
            full_text.append(f"--- Page {i+1} ---\n{text.strip()}")

        result = "\n\n".join(full_text)

    return jsonify({"text": result})
