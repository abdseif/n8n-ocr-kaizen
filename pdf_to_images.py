from pdf2image import convert_from_path

def convert_pdf_to_images(pdf_path, dpi=300, fmt='jpeg', grayscale=True, thread_count=2):
    try:
        images = convert_from_path(
            pdf_path,
            dpi=dpi,                  # High DPI for sharp OCR
            fmt=fmt,                  # JPEG is lighter than PNG
            grayscale=grayscale,      # Faster & improves contrast
            thread_count=thread_count,
            size=(1654, 2339),        # Resize to A4 @300DPI to reduce memory
            single_file=False         # Keeps multi-page output clean
        )
        return images
    except Exception as e:
        print(f"[PDF2IMAGE ERROR] {str(e)}")
        return []
