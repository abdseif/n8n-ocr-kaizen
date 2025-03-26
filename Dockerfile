FROM python:3.9-slim

RUN apt-get update && \
    apt-get install -y tesseract-ocr libtesseract-dev && \
    apt-get clean

COPY . /app
WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]
