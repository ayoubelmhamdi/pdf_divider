# Divide/Split PDF pages into left and right halves.

### Usage

1. Install requirements: `pip install -r requirements` or `pip install pdf2image pillow tqdm`
2. Run: `python3 main.py -f input.pdf -d output/`

### Options

- `-f`, `--file`: Input PDF file
- `-d`, `--dir`: Output directory

### INFO:
to know the `DPI` and image `colors`, we can use
```
# -f first image is zero and -l is last image
pdfimages -list ./foo.pdf -f 0 -l 13
```
