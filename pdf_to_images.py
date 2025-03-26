from pdf2image import convert_from_path

def convert_pdf(path):
    images = convert_from_path(path)
    for i, img in enumerate(images):
        img.save(f"page_{i+1}.jpg", "JPEG")

if __name__ == "__main__":
    convert_pdf("sample.pdf")
