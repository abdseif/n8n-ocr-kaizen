from flask import Flask, request, jsonify
from ocr import perform_ocr  # assuming ocr.py has a function named perform_ocr
from pdf_to_images import convert_pdf_to_images  # if you support PDFs
import os
import tempfile

app = Flask(__name__)

@app.route('/ocr', methods=['POST'])
def ocr():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in request'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        file.save(tmp.name)

        if file.filename.endswith('.pdf'):
            images = convert_pdf_to_images(tmp.name)
            text = ''
            for img in images:
                text += perform_ocr(img) + '\n'
        else:
            text = perform_ocr(tmp.name)

        os.unlink(tmp.name)  # clean up

    return jsonify({'text': text})


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
