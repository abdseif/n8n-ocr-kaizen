FROM python:3.11-slim

# Install required system packages
RUN apt-get update && \
    apt-get install -y \
    tesseract-ocr \
    poppler-utils \
    libglib2.0-0 \
    libsm6 \
    libxrender1 \
    libxext6 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Run the app
CMD ["gunicorn", "--workers=1", "--timeout=0", "--bind=0.0.0.0:10000", "api:app"]
