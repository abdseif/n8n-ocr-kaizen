from pdf2image import convert_from_path

def convert_pdf_to_images(pdf_path):
    return convert_from_path(
        pdf_path,
        dpi=300,                # High resolution for better OCR accuracy
        fmt='jpeg',             # JPEG has better compression
        grayscale=True,         # Reduce noise, improve OCR contrast
        thread_count=2          # Speed up multi-page conversion
    )
