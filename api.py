from flask import Flask, request, jsonify
from PIL import Image
import pytesseract
from pdf2image import convert_from_path

app = Flask(__name__)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

@app.route('/ocr', methods=['POST'])
def ocr():
    try:
        if 'file' not in request.files:
            return jsonify({"error": "No file uploaded"}), 400

        file = request.files['file']
        file.save('temp_file.pdf')

        if file.filename.endswith('.pdf'):
            images = convert_from_path('temp_file.pdf', dpi=300)
            extracted_text = ""
            for image in images:
                extracted_text += pytesseract.image_to_string(image) + "\n"
        else:
            image = Image.open('temp_file.pdf')
            extracted_text = pytesseract.image_to_string(image)

        return jsonify({"text": extracted_text}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
