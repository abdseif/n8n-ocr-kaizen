# main.py
from flask import Flask, request
import pytesseract
from PIL import Image
import io

app = Flask(__name__)

@app.route('/ocr', methods=['POST'])
def ocr():
    if 'file' not in request.files:
        return {"error": "No file provided"}, 400

    image = Image.open(request.files['file'].stream)
    text = pytesseract.image_to_string(image)
    return {"text": text}
  
