from pdf2image import convert_from_path

def convert_pdf_to_images(pdf_path, output_folder):
    try:
        # Convert PDF pages to images
        images = convert_from_path(pdf_path, dpi=300)
        for i, image in enumerate(images):
            image.save(f"{output_folder}/page_{i + 1}.jpg", "JPEG")
        return f"PDF converted successfully. Images saved in {output_folder}"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    # Example usage
    pdf_path = "test.pdf"
    output_folder = "output_images"
    result = convert_pdf_to_images(pdf_path, output_folder)
    print(result)
