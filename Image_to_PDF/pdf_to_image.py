import fitz  # PyMuPDF
from pathlib import Path

import Config

wdir = Config.wdir
pdf_path = Config.pdf_path
output_path = Config.output_path

def pdf_to_images(pdf_path, output_folder=None, fmt="png", dpi=200):
    """
    Convert each page of a PDF into an image.

    pdf_path:      path to the PDF file
    output_folder: folder to save images (defaults to a folder named after the PDF)
    fmt:           "png" or "jpg"
    dpi:           resolution (150-300 is typical; higher = bigger files)
    """
    pdf_path = Path(pdf_path)
    fmt = fmt.lower().replace("jpeg", "jpg")
    if fmt not in ("png", "jpg"):
        raise ValueError("fmt must be 'png' or 'jpg'")

    # Default folder: same name as the PDF, next to it
    out_dir = Path(output_folder) if output_folder else pdf_path.with_suffix("")
    out_dir.mkdir(parents=True, exist_ok=True)

    zoom = dpi / 72  # PDF base resolution is 72 DPI
    matrix = fitz.Matrix(zoom, zoom)

    saved_files = []
    with fitz.open(pdf_path) as doc:
        for page_number, page in enumerate(doc, start=1):
            pix = page.get_pixmap(matrix=matrix, alpha=False)
            out_file = out_dir / f"page_{page_number:03d}.{fmt}"
            pix.save(out_file)
            saved_files.append(out_file)
            print(f"Saved {out_file}")

    return saved_files


if __name__ == "__main__":
    pdf_to_images(pdf_path, output_folder=output_path, fmt="png", dpi=200)