#!/usr/bin/env python3

import os
import argparse
from pdf2image import convert_from_path
from PIL import Image

def extract_left_half_from_pdf(pdf_path, output_dir):
    pages = convert_from_path(pdf_path)

    for i, page in enumerate(pages):
        width, height = page.size

        page.crop((0, 0, width//1.75, height)).save(f"{output_dir}/{i+1}_l.png")
        page.crop((width*5//16, 0, width, height)).save(f"{output_dir}/{i+1}_r.png")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Split PDF pages into left and right halves.')
    parser.add_argument('-f', '--file', required=True, help='Input PDF file path.')
    parser.add_argument('-d', '--dir', required=True, help='Output directory path.')
    args = parser.parse_args()

    os.makedirs(args.dir, exist_ok=True)
    extract_left_half_from_pdf(args.file, args.dir)
