FROM python:3.9-slim

RUN apt update && apt install -y tesseract-ocr libtesseract-dev poppler-utils
RUN pip install flask pytesseract pillow

COPY . /app
WORKDIR /app

CMD ["python", "main.py"]
