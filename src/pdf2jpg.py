import fitz

def pdf2jpg(pdf:bytes) -> list:
    images = []
    with fitz.open(stream=pdf, filetype = 'pdf') as pdf_file:
        for page in pdf_file:
            pix = page.get_pixmap(matrix = fitz.Matrix(4,4))
            images.append(pix.pil_tobytes("JPEG"))
    return images
