Tesseract OCR API Project
Overview
This project uses Tesseract OCR to extract text from images and PDFs. It includes scripts for OCR processing, PDF conversion, and an API for integration with n8n.

Folder Structure
ocr.py: Script for performing OCR on images.
pdf_to_images.py: Converts PDF pages into images.
api.py: Flask API to expose OCR functionality.
requirements.txt: Lists dependencies.
README.md: Project documentation.
Setup Instructions
Install Python 3.6 or higher.
Install dependencies:
Run the API:
Use the /ocr endpoint to upload files for text extraction.
Example Usage
Send a POST request to /ocr with a file (image or PDF) to extract text.
