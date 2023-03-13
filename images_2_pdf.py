from PIL import Image
import os
import sys
from pprint import pprint

path = 'files/'


def create_pdf(pdf_name):
    files = sorted([f for f in os.listdir(path) if not f.startswith('.')])
    pprint(files)
    pages = [Image.open(path + file).convert('RGB') for file in files]
    pages[0].save(pdf_name, 'PDF', resolution=100, optimize=True, save_all=True, append_images=pages[1:])


if __name__ == '__main__':
    pdf_name = 'out.pdf' if len(sys.argv) == 1 else sys.argv[1]
    if '.pdf' not in pdf_name:
        pdf_name += '.pdf'
    create_pdf(pdf_name)
