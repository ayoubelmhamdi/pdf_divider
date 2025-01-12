#!/usr/bin/env python3

import os
import argparse

from pdf2image import convert_from_path
from PIL import Image
from tqdm import tqdm

def extract_half_from_pdf(pdf_path, output_dir):
    # pages = convert_from_path(pdf_path)
    pages = convert_from_path(pdf_path, dpi=300, fmt="pnm", thread_count=4)

    for i, page in tqdm(enumerate(pages)):
        width, height = page.size

        page.crop((width//8, 0, width//1.6, height)).save(f"{output_dir}/{i+1}_l.png")
        page.crop((width//2, 0, width, height)).save(f"{output_dir}/{i+1}_r.png")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Split PDF pages into left and right halves.')
    parser.add_argument('-f', '--file', required=True, help='Input PDF file path.')
    parser.add_argument('-d', '--dir', required=True, help='Output directory path.')
    args = parser.parse_args()

    os.makedirs(args.dir, exist_ok=True)
    extract_half_from_pdf(args.file, args.dir)
