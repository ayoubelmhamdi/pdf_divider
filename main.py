#!/usr/bin/env python3

from pdf2image import convert_from_path
from PIL import Image

def extract_left_half_from_pdf(pdf_path, output_dir, output_suffix):
    pages = convert_from_path(pdf_path)
    
    for i, page in enumerate(pages):
        width, height = page.size
        page.crop((0, 0, width//1.5, height)).save(f"{output_dir}/{i+1}_l.png")

if __name__ == '__main__':
    pdf_path = "../main.pdf"
    extract_left_half_from_pdf(pdf_path, "output", "l")
