from pathlib import Path
from subprocess import run

from PIL import Image
from htmlmin import minify
from weasyprint import (
    HTML,
    CSS,
)

from .src import cv


__all__ = (
    'build',
)


#------------------------------------------------------------------------------#
def build():
    base = Path('cv')

    png = base/'img'/'header.png'
    scss = base/'style'/'_constants.scss'
    with Image.open(png) as image, \
         scss.open('w') as scss:
            width, height = image.size
            ideal_width = min(width, 900)
            ratio = ideal_width/width
            ideal_height = round(height*ratio)
            scss.write(f'$WIDTH: {ideal_width}px;\n')
            scss.write(f'$HEIGHT: {ideal_height}px;\n')

    run(('npx', 'sass', str(base/'style'/'index.scss'),
                        str(base/'style'/'index.css'),
                        '--no-source-map',
                        '--style', 'compressed'),
        check=True,
        capture_output=True)

    html = base/'cv.html'
    with html.open('w') as target:
        target.write(minify(cv()))

    offline_css = CSS(string='@page { size: 255mm 935mm; margin: 0; }')
    HTML(html).write_pdf(base/'peter_varo_cv.pdf', stylesheets=[offline_css])
