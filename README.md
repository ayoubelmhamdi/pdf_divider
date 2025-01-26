# Divide/Split PDF pages into left and right halves.

### Usage

- Install requirements: `pip install -r requirements` or `pip install pdf2image pillow tqdm`
- Options:

- `-f`, `--file`: Input PDF file
- `-d`, `--dir`: Output directory

```bash
python3 main.py -f input.pdf -d output/
```


### INFO:
To know the `DPI` and `image colors`, we can use this options: `-f`, the first image is set to zero and the `-l`  set to the last image.

```bash
pdfimages -list ./foo.pdf -f 0 -l 13
```
